import os
import asyncio
from logger import LOGGER
from asyncio.subprocess import PIPE
from asyncio import create_subprocess_exec, wait_for
from time import time as get_time

from pyleaves import Leaves
from pyrogram.types import (
    InputMediaPhoto, InputMediaVideo, InputMediaDocument, InputMediaAudio
)
from helpers.files import fileSizeLimit, cleanup_download, get_download_path
from helpers.msg import get_parsed_msg

def progressArgs(action, progress_message, start_time):
    PROGRESS_BAR = """
    Percentage: {percentage:.2f}% | {current}/{total}
    Speed: {speed}/s
    Estimated Time Left: {est_time} seconds
    """
    return (action, progress_message, start_time, PROGRESS_BAR, "▓", "░")

async def cmd_exec(cmd):
    proc = await create_subprocess_exec(*cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = await proc.communicate()
    return stdout.decode().strip(), stderr.decode().strip(), proc.returncode

async def get_media_info(path):
    try:
        result = await cmd_exec([
            "ffprobe", "-hide_banner", "-loglevel", "error",
            "-print_format", "json", "-show_format", "-show_streams", path,
        ])
        if result[0] and result[2] == 0:
            import json
            data = json.loads(result[0])
            fields = data.get("format", {})
            duration = round(float(fields.get("duration", 0)))
            width = height = None
            for stream in data.get("streams", []):
                if stream.get("codec_type") == "video":
                    width = stream.get("width")
                    height = stream.get("height")
                    break
            return duration, width, height
    except Exception as e:
        LOGGER(__name__).warning(f"Could not extract media info: {e}")
    return 0, None, None

async def get_video_thumbnail(video_file, duration):
    os.makedirs("Assets", exist_ok=True)
    output = os.path.join("Assets", f"thumb_{int(get_time()*1000)}.jpg")
    if not duration: duration = 3
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", str(duration // 2), "-i", video_file, "-vframes", "1", "-q:v", "2", "-y", output]
    try:
        _, _, code = await wait_for(cmd_exec(cmd), timeout=60)
        if code == 0 and os.path.exists(output):
            return output
    except Exception as e:
        LOGGER(__name__).warning(f"Could not generate thumbnail: {e}")
    return None

async def send_media(bot, message, media_path, media_type, caption, progress_message=None, start_time=None, target_chat_id=None, is_premium=False):
    # 'bot' here is the selected worker
    file_size = os.path.getsize(media_path)
    if progress_message and not await fileSizeLimit(file_size, message, "upload", is_premium): return

    chat_id = target_chat_id if target_chat_id else message.chat.id
    
    send_kwargs = {
        "chat_id": chat_id,
        "caption": caption or ""
    }
    
    if progress_message and start_time:
        send_kwargs["progress"] = Leaves.progress_for_pyrogram
        send_kwargs["progress_args"] = progressArgs("📥 Uploading", progress_message, start_time)

    try:
        LOGGER(__name__).info(f"Uploading file via {bot.me.first_name}: {os.path.basename(media_path)}")
        if media_type == "photo":
            await bot.send_photo(photo=media_path, **send_kwargs)
        elif media_type == "video":
            dur, w, h = await get_media_info(media_path)
            thumb = await get_video_thumbnail(media_path, dur)
            try:
                await bot.send_video(video=media_path, duration=dur, width=w, height=h, thumb=thumb, supports_streaming=True, **send_kwargs)
            finally:
                if thumb and os.path.exists(thumb): os.remove(thumb)
        elif media_type == "audio":
            dur, _, _ = await get_media_info(media_path)
            await bot.send_audio(audio=media_path, duration=dur, **send_kwargs)
        elif media_type == "document":
            await bot.send_document(document=media_path, **send_kwargs)
            
    except Exception as e:
        LOGGER(__name__).error(f"Upload Failed: {e}")

async def processMediaGroup(chat_message, bot, message, target_chat_id=None):
    # FIX: Logic wrapped in try/finally for safer cleanup
    media_group = await chat_message.get_media_group()
    valid_media = []
    files_to_clean = []
    
    LOGGER(__name__).info(f"Processing Album ID {chat_message.media_group_id} ({len(media_group)} items)")
    
    try:
        for msg in media_group:
            if msg.media:
                try:
                    from helpers.msg import get_file_name
                    fname = get_file_name(msg.id, msg)
                    dpath = get_download_path(f"album_{chat_message.media_group_id}", fname)
                    path = await msg.download(file_name=dpath)
                    if path:
                        files_to_clean.append(path)
                        cap = await get_parsed_msg(msg.caption or "", msg.caption_entities)
                        if msg.photo: valid_media.append(InputMediaPhoto(path, caption=cap))
                        elif msg.video: valid_media.append(InputMediaVideo(path, caption=cap))
                        elif msg.document: valid_media.append(InputMediaDocument(path, caption=cap))
                        elif msg.audio: valid_media.append(InputMediaAudio(path, caption=cap))
                except Exception as e:
                    LOGGER(__name__).error(f"Album item download failed: {e}")

        if valid_media:
            dest = target_chat_id if target_chat_id else message.chat.id
            await bot.send_media_group(chat_id=dest, media=valid_media)
            LOGGER(__name__).info(f"Album Uploaded: {chat_message.media_group_id}")
            return True
            
    except Exception as e:
        LOGGER(__name__).error(f"Album Error: {e}")
    finally:
        # FIX: Ensure cleanup happens even if upload fails
        for f in files_to_clean: cleanup_download(f)
    
    return False

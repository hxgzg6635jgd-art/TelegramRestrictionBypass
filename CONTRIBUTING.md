# 🤝 Contributing to TelegramRestrictionBypass

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

---

## 📋 Table of Contents

- [Code of Conduct](#-code-of-conduct)
- [How Can I Contribute?](#-how-can-i-contribute)
- [Development Setup](#-development-setup)
- [Coding Standards](#-coding-standards)
- [Commit Guidelines](#-commit-guidelines)
- [Pull Request Process](#-pull-request-process)
- [Testing](#-testing)
- [Documentation](#-documentation)

---

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all.

### Our Standards

**Positive behavior includes:**
- ✅ Using welcoming and inclusive language
- ✅ Being respectful of differing viewpoints
- ✅ Gracefully accepting constructive criticism
- ✅ Focusing on what is best for the community
- ✅ Showing empathy towards other community members

**Unacceptable behavior includes:**
- ❌ Trolling, insulting/derogatory comments, and personal attacks
- ❌ Public or private harassment
- ❌ Publishing others' private information without permission
- ❌ Other conduct which could reasonably be considered inappropriate

---

## 🎯 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title** - Descriptive summary of the issue
- **Description** - Detailed explanation of the problem
- **Steps to reproduce** - How to trigger the bug
- **Expected behavior** - What should happen
- **Actual behavior** - What actually happens
- **Environment** - OS, Python version, dependencies
- **Logs** - Relevant error messages (remove sensitive info)

**Template:**
```markdown
**Description:**
Brief description of the bug

**Steps to Reproduce:**
1. Run command X
2. Open file Y
3. See error

**Expected Behavior:**
Should do X

**Actual Behavior:**
Does Y instead

**Environment:**
- OS: Ubuntu 22.04
- Python: 3.11.5
- Docker: Yes/No

**Logs:**
```
[paste relevant logs here]
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. Include:

- **Clear title** - Descriptive feature name
- **Use case** - Why is this feature needed?
- **Proposed solution** - How should it work?
- **Alternatives** - Other approaches considered
- **Examples** - Similar features in other projects

### Contributing Code

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Submit** a pull request

---

## 🛠️ Development Setup

### Prerequisites

- Python 3.11+
- Git
- FFmpeg
- Text editor (VS Code, PyCharm, etc.)

### Setup Steps

```bash
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/TelegramRestrictionBypass.git
cd TelegramRestrictionBypass

# 2. Create virtual environment
python3.11 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Install development dependencies
pip install pytest pytest-asyncio black flake8 mypy

# 5. Configure environment
cp config.env.example config.env
nano config.env  # Add your test credentials

# 6. Run the bot
python main.py
```

### Project Structure

```
TelegramRestrictionBypass/
├── main.py              # Entry point and handlers
├── config.py            # Configuration loading
├── logger.py            # Logging setup
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image
├── docker-compose.yml   # Docker Compose config
├── helpers/             # Utility modules
│   ├── files.py        # File operations
│   ├── msg.py          # Message parsing
│   ├── settings.py     # Persistent config
│   ├── state.py        # Batch state management
│   └── utils.py        # Media handling
├── docs/                # Documentation
│   ├── README.md       # Full documentation
│   ├── INSTALLATION.md # Setup guide
│   ├── SETUP.md        # Configuration
│   ├── QUICKSTART.md   # Quick start
│   ├── DEPENDENCIES.md # Package info
│   └── DOCKER.md       # Docker guide
└── .github/            # GitHub templates
    └── ISSUE_TEMPLATE/
```

---

## 📝 Coding Standards

### Python Style Guide

Follow **PEP 8** guidelines:

```python
# Good
def download_message(client, message_id):
    """Download a single Telegram message."""
    pass

# Bad
def downloadMessage(client,message_id):
    pass
```

### Code Formatting

Use **Black** formatter:

```bash
# Format all Python files
black .

# Check without modifying
black --check .

# Format specific file
black main.py
```

### Linting

Use **Flake8**:

```bash
# Check all files
flake8 .

# Check specific file
flake8 main.py

# Ignore specific errors
flake8 --ignore=E501,W503 .
```

### Type Hints

Add type hints where possible:

```python
# Good
def get_file_size(path: str) -> int:
    return os.path.getsize(path)

# Acceptable (complex types)
from typing import Optional, List, Dict

def process_messages(messages: List[Message]) -> Dict[int, str]:
    pass
```

### Docstrings

Use Google-style docstrings:

```python
def download_file(url: str, destination: str) -> bool:
    """Download a file from URL to destination.

    Args:
        url: The URL to download from
        destination: Local path to save file

    Returns:
        True if successful, False otherwise

    Raises:
        ValueError: If URL is invalid
        IOError: If cannot write to destination
    """
    pass
```

### Error Handling

Use specific exceptions:

```python
# Good
try:
    user_id = int(message.command[1])
except (ValueError, IndexError) as e:
    logger.error(f"Invalid user ID: {e}")
    return

# Bad
try:
    user_id = int(message.command[1])
except:
    pass
```

### Logging

Use the logger consistently:

```python
from logger import LOGGER

logger = LOGGER(__name__)

# Good
logger.info("Starting download")
logger.warning("FloodWait detected")
logger.error(f"Failed to upload: {e}")

# Bad
print("Starting download")
```

---

## 📝 Commit Guidelines

### Commit Messages

Follow conventional commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style (formatting, no logic change)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**

```bash
# Good commits
git commit -m "feat(download): add retry logic for failed downloads"
git commit -m "fix(worker): prevent crash when bot token is invalid"
git commit -m "docs(readme): update installation instructions"
git commit -m "refactor(utils): simplify media group processing"

# Bad commits
git commit -m "fixed stuff"
git commit -m "update"
git commit -m "asdf"
```

### Commit Best Practices

- ✅ Keep commits small and focused
- ✅ One logical change per commit
- ✅ Test before committing
- ✅ Write descriptive messages
- ❌ Don't commit incomplete features
- ❌ Don't mix unrelated changes

---

## 🔄 Pull Request Process

### Before Submitting

1. **Update** from main branch
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Test** your changes
   ```bash
   python main.py  # Manual testing
   black --check .
   flake8 .
   ```

3. **Document** your changes
   - Update README if needed
   - Add comments to complex code
   - Update relevant documentation

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe how you tested these changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-reviewed code
- [ ] Commented complex code
- [ ] Updated documentation
- [ ] No new warnings
- [ ] Tested locally

## Related Issues
Closes #123
```

### Review Process

1. Maintainers will review your PR
2. Address any requested changes
3. Once approved, PR will be merged
4. Your contribution will be credited

### After Merge

```bash
# Update your fork
git checkout main
git pull upstream main
git push origin main

# Delete feature branch
git branch -d feature/your-feature
git push origin --delete feature/your-feature
```

---

## 🧪 Testing

### Manual Testing

Test all affected features:

```bash
# Start bot
python main.py

# Test commands
/start
/dl <test_link>
/bdl <start> <end>
/connect <test_token>
```

### Automated Testing (Future)

When test suite is added:

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_download.py

# With coverage
pytest --cov=. --cov-report=html
```

### Test Checklist

- [ ] Bot starts without errors
- [ ] All commands work
- [ ] Error handling works
- [ ] Logs are written correctly
- [ ] No crashes during operation
- [ ] Docker build succeeds
- [ ] Documentation is accurate

---

## 📖 Documentation

### When to Update Docs

Update documentation when:
- Adding new features
- Changing commands
- Modifying configuration
- Fixing bugs that users should know about
- Improving setup process

### Documentation Files

| File | Purpose |
|------|---------|
| `README.md` | Project overview |
| `docs/INSTALLATION.md` | Setup instructions |
| `docs/SETUP.md` | Configuration guide |
| `docs/QUICKSTART.md` | Quick reference |
| `docs/DEPENDENCIES.md` | Package information |
| `docs/DOCKER.md` | Docker deployment |
| `CONTRIBUTING.md` | This file |

### Documentation Style

- Use clear, concise language
- Include code examples
- Add screenshots when helpful
- Keep formatting consistent
- Test all commands/steps

---

## 🎨 Code Review Checklist

Before submitting, review:

### Functionality
- [ ] Feature works as intended
- [ ] Edge cases handled
- [ ] Error handling present
- [ ] No breaking changes (or documented)

### Code Quality
- [ ] Follows PEP 8
- [ ] No unnecessary complexity
- [ ] DRY (Don't Repeat Yourself)
- [ ] Meaningful variable names
- [ ] Comments where needed

### Security
- [ ] No credentials in code
- [ ] Input validation present
- [ ] No SQL injection risks
- [ ] Secure file operations

### Performance
- [ ] No unnecessary loops
- [ ] Efficient algorithms
- [ ] Proper async/await usage
- [ ] Resource cleanup (files, connections)

---

## 🏆 Recognition

Contributors are credited in:
- Pull request merge commits
- Release notes
- README contributors section

### Hall of Fame

Top contributors will be featured in the README!

---

## 📞 Getting Help

### Resources
- 📖 [Documentation](docs/README.md)
- 🐛 [Issue Tracker](https://github.com/Paidguy/TelegramRestrictionBypass/issues)
- 💬 [Discussions](https://github.com/Paidguy/TelegramRestrictionBypass/discussions)

### Questions?

- Check existing issues and discussions
- Ask in GitHub Discussions
- Be patient and respectful

---

## 🙏 Thank You!

Thank you for contributing to TelegramRestrictionBypass! Every contribution, no matter how small, helps make this project better.

**Happy coding! 🚀**

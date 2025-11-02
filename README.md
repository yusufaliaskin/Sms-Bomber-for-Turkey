# SMS Bomber for Turkey

_Advanced SMS bombing tool for Turkish service providers_

[![GitHub Stars](https://img.shields.io/github/stars/yusufaliaskin/Sms-Bomber-for-Turkey?style=social)](https://github.com/yusufaliaskin/Sms-Bomber-for-Turkey)
[![GitHub Forks](https://img.shields.io/github/forks/yusufaliaskin/Sms-Bomber-for-Turkey?style=social)](https://github.com/yusufaliaskin/Sms-Bomber-for-Turkey)
[![License](https://img.shields.io/badge/license-Educational-blue.svg)](https://github.com/yusufaliaskin/Sms-Bomber-for-Turkey)

## 📋 Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Command Line Interface](#command-line-interface)
  - [Discord Bot](#discord-bot)
  - [Discord Selfbot](#discord-selfbot)
  - [Telegram Bot](#telegram-bot)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

## 📝 Description

Enough Reborn is a powerful SMS bombing tool with a modern, feature-rich interface. It supports multiple Turkish service providers and offers both standalone CLI and bot integrations for Discord and Telegram.

**⚠️ For educational purposes only. Misuse of this tool may violate laws and regulations.**

## ✨ Features

- 🎨 **Modern CLI Interface** - Rich terminal UI with progress bars, animations, and real-time statistics
- 🚀 **Turbo Mode** - Multi-threaded SMS sending for maximum speed
- 📊 **System Dashboard** - Real-time monitoring of CPU, RAM, and network status
- 🤖 **Bot Integration** - Discord and Telegram bot support
- 🔧 **Multiple Entry Points** - CLI, GUI (app.py), and bot modes
- 📱 **50+ Service Providers** - Supports major Turkish services including:
  - E-commerce: Trendyol, Hepsiburada, Getir
  - Food Delivery: Yemeksepeti, Dominos, KöfteciYusuf
  - Retail: BIM, Koton, English Home, WMF
  - And many more...

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Internet connection

### Step 1: Clone the Repository

```bash
git clone https://github.com/yusufaliaskin/Sms-Bomber-for-Turkey.git
cd Sms-Bomber-for-Turkey
```

### Step 2: Install Dependencies

```bash
pip3 install -r requirements.txt
```

**Note:** The main script (`enough.py`) includes automatic dependency checking and installation, so missing libraries will be installed automatically on first run.

### Step 3: Run the Application

```bash
python3 enough.py
```

## 💻 Usage

### Command Line Interface

#### Main Menu Options

1. **Normal SMS Mode** - Send SMS one by one with custom intervals
2. **Turbo SMS Mode** - High-speed multi-threaded SMS sending
3. **Show Services** - Display all available SMS services
4. **Exit** - Quit the application

#### Normal SMS Mode

1. Enter phone number (10 digits, without +90)
2. Optionally provide email address
3. Specify number of SMS to send (or press Enter for infinite)
4. Set interval between messages (in seconds)

#### Turbo SMS Mode

1. Provide a text file with phone numbers (one per line)
2. Configure:
   - Mail count
   - SMS count per number
   - Thread count (1-200, recommended: 10-50)
3. Confirm and start sending

### Discord Bot

#### Setup

1. Navigate to the bot directory:
```bash
cd bot
```

2. Install bot dependencies:
```bash
pip3 install -r requirements.txt
```

3. Edit `discord-enough.py` and add your bot token:
```python
TOKEN = "your-discord-bot-token"
```

4. Enable **Privileged Gateway Intents** in Discord Developer Portal:
   - Go to https://discord.com/developers/applications
   - Select your application
   - Navigate to "Bot" section
   - Enable all Privileged Gateway Intents

5. Run the bot:
```bash
python3 discord-enough.py
```

#### Bot Commands

- `*sms <phone_number>` - Send SMS to specified number
- `*help` - Display help message

### Discord Selfbot

#### Finding Your Token

1. Open Discord in your browser (use the account you want as a bot)
2. Open Developer Tools (F12)
3. Go to the Network tab
4. Keep the console open and click on a chat you haven't clicked during this session
5. Find a request ending with `messages?limit=50`
6. In the request Headers, find the `Authorization` value - this is your token
7. Add the token to `discord-selfbot-enough.py`:
```python
token = "your-token-here"  # as a string
```

#### Finding Chat ID

1. Send a message to the bot account from your real account
2. Open Discord in browser and log in to the bot account
3. Click on your real account's chat
4. The number after `@me/` in the URL is your chat ID
5. Add it to `discord-selfbot-enough.py`:
```python
chat_id = 123456789  # as an integer
```

**Note:** If using in a Discord server, the second number after `channels/` (separated by `/`) is the chat ID.

#### Selfbot Commands

- `.sms <phone_number>` - Send SMS to specified number
- `.help` - Display help message
- `.status` - Display custom status message

### Telegram Bot

#### Setup

1. Get a bot token from [@BotFather](https://t.me/BotFather)
2. Edit `telegram-enough.py`:
```python
TOKEN = "your-telegram-bot-token"
```

3. Run the bot:
```bash
cd bot
python3 telegram-enough.py
```

#### Bot Commands

- `/start` - Initialize bot
- `/sms` - Start SMS sending process
- `/config <count:interval>` - Configure SMS count and interval (e.g., `/config 50:3`)
- `/help` - Display help message

## 📁 Project Structure

```
Sms-Boomber/
├── bot/                          # Bot implementations
│   ├── discord-enough.py         # Discord bot
│   ├── discord-selfbot-enough.py # Discord selfbot
│   ├── telegram-enough.py        # Telegram bot (python-telegram-bot)
│   ├── telegram-enough(requests).py # Telegram bot (requests)
│   └── requirements.txt          # Bot-specific dependencies
├── enough.py                     # Main CLI application
├── sms.py                        # SMS service implementations
├── app.py                        # GUI application (TCKN validator)
├── int.py                        # Test file
├── requirements.txt              # Main dependencies
└── README.md                     # This file
```

## ⚙️ Configuration

### Main Application (`enough.py`)

The main application includes several configurable parameters:

- **Service List**: Edit `sms.py` to add/remove services
- **Default Settings**: Modify theme colors and animation speeds in `enough.py`

### Bot Configuration

#### Discord Bot (`discord-enough.py`)
```python
TOKEN = ""      # Your Discord bot token
adet = 52       # Number of SMS to send
saniye = 0      # Interval between messages (seconds)
```

#### Discord Selfbot (`discord-selfbot-enough.py`)
```python
token = ""      # Your Discord token
chat_id =       # Chat ID (integer)
adet = 55       # Number of SMS
saniye = 0      # Interval (seconds)
```

#### Telegram Bot (`telegram-enough.py`)
```python
TOKEN = ""      # Your Telegram bot token
```

Configuration is done via `/config` command.

## 📦 Requirements

### Core Dependencies

- `colorama>=0.4.6` - Terminal colors and styling
- `requests>=2.31.0` - HTTP requests
- `pyfiglet>=1.0.2` - ASCII art text
- `rich>=13.7.0` - Rich terminal formatting
- `psutil>=5.9.8` - System monitoring

### Bot Dependencies

- `discord.py>=2.3.2` - Discord bot framework
- `python-telegram-bot>=20.7` - Telegram bot framework

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository at https://github.com/yusufaliaskin/Sms-Bomber-for-Turkey
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request to https://github.com/yusufaliaskin/Sms-Bomber-for-Turkey

## ⚠️ Disclaimer

**IMPORTANT:** This tool is provided for educational purposes only. The developers are not responsible for any misuse or damage caused by this program. Use at your own risk.

- SMS bombing may be illegal in your country
- Unauthorized use may violate terms of service
- Always obtain proper authorization before testing
- Respect privacy and telecommunications laws

## 📄 License

This project is provided as-is without any warranty. Use responsibly.

## 📞 Contact & Support

- **Repository**: [github.com/yusufaliaskin/Sms-Bomber-for-Turkey](https://github.com/yusufaliaskin/Sms-Bomber-for-Turkey)
- **Issues**: [Report bugs or request features](https://github.com/yusufaliaskin/Sms-Bomber-for-Turkey/issues)
- **Discussions**: [Join the community](https://github.com/yusufaliaskin/Sms-Bomber-for-Turkey/discussions)

---

**⭐ Star this repository if you find it useful!**

**Made with ❤️ by [Yusuf Ali Aşkın](https://github.com/yusufaliaskin)**

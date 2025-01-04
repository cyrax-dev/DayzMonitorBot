![GitHub top language](https://img.shields.io/github/languages/top/cyrax-dev/crxsnake) ![PyPI - Python Version](https://img.shields.io/badge/python-3.10%2B-blue) ![GitHub License](https://img.shields.io/github/license/cyrax-dev/crxsnake)

### Discord bot for monitoring DayZ servers
> The bot takes information from the Dayz server through the Query port

### 🚀 Opportunities
- Running multiple bots simultaneously - suitable for monitoring several servers at once.
- Customisable text - the ability to change the text about the server state (online/offline).

### 📋 Requirements
| Software required | Installation link |
| ------ | ------ |
| Python | [Download the installer from the official website ↗](https://www.python.org/ftp/python/3.12.7/python-3.12.7-amd64.exe)|
| Python installation | [View instructions on YouTube ↗](https://www.youtube.com/watch?v=Gt8PcB_RD04)|
| Discord Token | [Create a Discord app ↗](https://discord.com/developers/applications/)|

### 💥 Installation
- **1. Download and install Python**
- **2. Take the IP address and Query port of the server**
- **3. Create a bot and get a token**
- **4. Download the bot source code / or the .exe build**

### ➕  Customisation
> **The bot settings are located in the `settings` folder in the `servers.json` file**
```json
[
  {
    "name": "ServerName",
    "token": "DiscordToken",
    "ip": "127.0.0.1",
    "port": 2305,
    "status_online": "🟢 Online {player}/{slot} | {emoji} {time}",
    "status_offline": "🔴 Server OFF"
  },
  {
    "name": "ServerName",
    "token": "DiscordToken",
    "ip": "127.0.0.1",
    "port": 2305,
    "status_online": "🟢 Online {player}/{slot} | {emoji} {time}",
    "status_offline": "🔴 Server OFF"
  }
]
```

### 🎉 Launch
To start the bot, run the `start.bat` or `.exe` file

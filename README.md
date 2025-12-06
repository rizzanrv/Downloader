# Downloader Bot

A Telegram bot for downloading media content from various platforms.  
Example: https://t.me/tiktokdownloadtoolbot

## 🎯 Features

- Download videos from YouTube, Instagram Reels, TikTok
- Download audio from SoundCloud and other sources
- Automatic conversion to optimal formats (MP3 for audio, MP4 for video)
- File size check before sending
- Error handling during download
- DRM and protected content detection (e.g., Spotify, Netflix)

## 📋 Requirements

- Python 3.8+
- FFmpeg (for audio/video conversion)

## 🚀 Installation and Running

### 1. Clone the repository
```bash
git clone https://github.com/rizzanrv/Downloader
cd Downloader
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file based on `.env.example`:
```bash
BOT_TOKEN=your_telegram_bot_token_here
DOWNLOAD_DIR=downloads
```
You can get `BOT_TOKEN` from [@BotFather](https://t.me/BotFather) on Telegram.

### 4. Run the bot
```bash
python3 bot.py
```

## 📝 Usage

1. Start the bot
2. Send a media link in the chat with the bot
3. The bot will download the file and send it back to you

### Supported Platforms:
- **🎵 SoundCloud** - downloads as MP3
- **▶️ YouTube** - downloads as MP4
- **📸 Instagram Reels** - downloads as MP4
- **🎬 TikTok** - downloads as MP4

### ⚠️ Limitations
- Maximum photo size: **5 MB**
- Maximum file size: **50 MB**
- Links must start with `http://` or `https://`
- DRM-protected or private content **cannot be downloaded** (e.g., Spotify, Apple Music, Netflix, private Instagram posts)
- Some Instagram posts may require cookies for downloading

### 🛠️ Libraries Used
- **aiogram** - asynchronous framework for Telegram API
- **yt-dlp** - media downloading from various platforms
- **python-dotenv** - environment variable management

### ⚡ Notes on DRM and Protected Content
- Spotify, Netflix, Apple Music, and other DRM-protected services are **not supported** due to legal restrictions.
- Private Instagram posts or Reels may require authentication cookies.
- The bot will notify the user if a URL points to DRM-protected content or cannot be downloaded.


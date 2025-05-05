# Master's degree Thesis

AI Telegram bot for analyzing historical events.

The bot is based on Telegram Messenger and uses GROQ AI for analyzing data.  
Information is taken from Wikipedia and sent to GROQ as a prompt.  
After processing, the result is returned to the user in the chat as an AI-generated explanation.

## Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#the-structure)
- [Author](#author)

## Features

- Recognizes events in user input  
- Explains reasons (social, economic, etc.)  
- Integration with Telegram  

## Installation

### Repository Cloning:

```bash
git clone https://github.com/NikolayKossov/Masters-s-Thesis.git
cd project
```

### Installation of requirements:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Keys:

Add the following to your `.env` file:

```
API_KEY=your_key (can be created via BotFather)  
GROQ_API_KEY=groq_key (https://console.groq.com/keys)
```

### Start:

```bash
python bot.py
```

## Usage

Open Telegram and activate the bot using `/start`.  
Type a historical event and wait 5–10 seconds.

## The Structure

```
project/
├── bot.py
├── event_analyzer.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Author

Nikolay Kossov  
https://github.com/NikolayKossov  
https://github.com/Nidvig

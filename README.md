# Chatbot AI

A lightweight conversational AI starter that demonstrates natural-language processing, intent detection, and a simple response engine.

## Features

- Intent-based conversation routing
- Basic NLP preprocessing and keyword extraction
- Conversation memory for contextual responses
- Interactive CLI for local testing
- Unit tests for core chatbot behavior

## Project structure

```text
chatbot-ai/
├── chatbot/
│   ├── __init__.py
│   ├── app.py
│   ├── core.py
│   ├── intents.py
│   ├── nlp.py
│   └── models/
│       └── __init__.py
├── docs/
│   ├── api.md
│   ├── customization.md
│   └── setup.md
├── tests/
│   └── test_chatbot.py
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

## Quick start

### Prerequisites

- Python 3.10+
- pip

### Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run the chatbot

```bash
python -m chatbot.app
```

### Example interaction

```text
You: hello
Bot: Hello! How can I help you today?

You: tell me about your features
Bot: This assistant can help with product questions, support, and general conversation.

You: bye
Bot: Goodbye! Come back anytime.
```

## How it works

1. User input is normalized and tokenized.
2. Keywords are extracted to infer the likely intent.
3. A router selects the correct response handler.
4. The bot returns a contextual answer and keeps recent conversation history.

## Testing

```bash
pytest
```

## License

MIT

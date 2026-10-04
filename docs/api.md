# API documentation

## ChatBot

The `ChatBot` class is the main interface for conversational logic.

### Methods

- `chat(user_message: str) -> str`: Process a message and return a matching bot response.
- `recent_history() -> list`: Return the last few messages in conversation memory.

### Example

```python
from chatbot import ChatBot

bot = ChatBot()
response = bot.chat("hello")
print(response)
```

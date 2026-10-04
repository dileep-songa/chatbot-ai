# Customization guide

## Add a new intent

1. Update the `detect_intent` method in `chatbot/nlp.py`.
2. Add a response handler in `chatbot/intents.py`.
3. Extend tests in `tests/test_chatbot.py`.

## Improve the NLP layer

You can replace the simple keyword matcher with:

- sentence embeddings
- transformer models
- external AI APIs
- database-backed knowledge retrieval

## Extend the app

Consider adding:

- REST API endpoints
- web frontend
- user authentication
- analytics and logging

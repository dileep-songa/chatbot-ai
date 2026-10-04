import pytest

from chatbot import ChatBot


@pytest.mark.parametrize(
    ("message", "expected_fragment"),
    [
        ("hello there", "Hello"),
        ("can you help me", "help"),
        ("bye for now", "Goodbye"),
        ("what features do you have", "This assistant"),
    ],
)
def test_chatbot_responses(message, expected_fragment):
    bot = ChatBot()
    response = bot.chat(message)
    assert expected_fragment in response


def test_empty_message_returns_prompt():
    bot = ChatBot()
    response = bot.chat("   ")
    assert "Please send a message" in response


def test_conversation_history_is_tracked():
    bot = ChatBot(max_history=3)
    bot.chat("hello")
    bot.chat("help")
    history = bot.recent_history()
    assert len(history) == 2
    assert history[0]["intent"] == "greeting"
    assert history[1]["intent"] == "help"


def test_session_memory_tracks_interactions():
    bot = ChatBot(session_id="session-001")
    bot.chat("hello", session_id="session-001")
    history = bot.get_session_history("session-001")
    assert len(history) == 1
    assert history[0]["intent"] == "greeting"
    assert "Hello" in history[0]["response"]

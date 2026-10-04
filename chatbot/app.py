from __future__ import annotations

import argparse

from chatbot.core import ChatBot


def _run_interactive_session() -> None:
    bot = ChatBot()
    print("Chatbot AI ready. Type 'exit' to quit.")
    while True:
        try:
            user_input = input("You: ").strip()
        except EOFError:
            print("\nSession ended.")
            break

        if user_input.lower() in {"exit", "quit", "bye"}:
            print("Bot: Goodbye! Come back anytime.")
            break

        response = bot.chat(user_input)
        print(f"Bot: {response}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the chatbot AI CLI")
    parser.add_argument("--demo", action="store_true", help="Run a short demo conversation")
    args = parser.parse_args()

    if args.demo:
        bot = ChatBot()
        for sample in ["hello", "tell me about your features", "help me", "bye"]:
            print(f"You: {sample}")
            print(f"Bot: {bot.chat(sample)}")
        return

    _run_interactive_session()


if __name__ == "__main__":
    main()

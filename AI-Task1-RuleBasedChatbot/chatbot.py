import random
import re
from datetime import datetime


BOT_NAME = "Nova"


RULES = [
    {
        "patterns": [r"\b(hi|hello|hey|good morning|good evening)\b"],
        "responses": [
            "Hello! How can I help you today?",
            "Hi there. What would you like to talk about?",
            "Hey! Ask me something simple and I will try to help.",
        ],
    },
    {
        "patterns": [r"\bhow are you\b", r"\bhow'?s it going\b"],
        "responses": [
            "I am doing well, thanks for asking. How are you?",
            "I am fine and ready to chat.",
        ],
    },
    {
        "patterns": [r"\b(your name|who are you)\b"],
        "responses": [
            f"My name is {BOT_NAME}. I am a small rule-based chatbot.",
            f"I am {BOT_NAME}, a chatbot built with simple pattern matching.",
        ],
    },
    {
        "patterns": [r"\bwhat can you do\b", r"\bhelp\b", r"\bcommands\b"],
        "responses": [
            "You can ask about my name, the time, Python, this project, jokes, or basic greetings.",
            "Try asking: 'what is your name', 'tell me a joke', 'what is python', or 'what time is it'.",
        ],
    },
    {
        "patterns": [r"\btime\b", r"\bcurrent time\b"],
        "responses": ["The current time is {time}."],
    },
    {
        "patterns": [r"\bdate\b", r"\btoday\b"],
        "responses": ["Today's date is {date}."],
    },
    {
        "patterns": [r"\bpython\b"],
        "responses": [
            "Python is a beginner-friendly programming language used for web apps, automation, data science, and AI.",
            "Python is popular because its syntax is clear and it has a huge collection of libraries.",
        ],
    },
    {
        "patterns": [r"\b(rule based|rule-based)\b", r"\bchatbot project\b"],
        "responses": [
            "A rule-based chatbot replies by checking the user's message against predefined rules.",
            "This project uses simple patterns to decide which response fits the user's input.",
        ],
    },
    {
        "patterns": [r"\bjoke\b", r"\bmake me laugh\b"],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "I told my computer I needed a break, and it said: no problem, I will go to sleep.",
        ],
    },
    {
        "patterns": [r"\bthank you\b", r"\bthanks\b"],
        "responses": [
            "You're welcome!",
            "No problem. Happy to help.",
        ],
    },
    {
        "patterns": [r"\bbye\b", r"\bgoodbye\b", r"\bexit\b", r"\bquit\b"],
        "responses": [
            "Goodbye! Have a great day.",
            "See you later!",
        ],
        "ends_chat": True,
    },
]


FALLBACK_RESPONSES = [
    "I am not sure about that yet. Try asking something simpler.",
    "I do not have a rule for that question, but I am still learning.",
    "Can you rephrase that? I understand greetings, time, date, Python, jokes, and project questions.",
]


def clean_text(text):
    """Make user input easier to match against rules."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s'-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def format_response(response):
    now = datetime.now()
    return response.format(
        time=now.strftime("%I:%M %p"),
        date=now.strftime("%B %d, %Y"),
    )


def find_response(user_message):
    cleaned_message = clean_text(user_message)

    for rule in RULES:
        for pattern in rule["patterns"]:
            if re.search(pattern, cleaned_message):
                response = random.choice(rule["responses"])
                return format_response(response), rule.get("ends_chat", False)

    return random.choice(FALLBACK_RESPONSES), False


def run_chat():
    print(f"{BOT_NAME}: Hello! I am {BOT_NAME}, your rule-based chatbot.")
    print(f"{BOT_NAME}: Type 'help' to see what I can answer, or 'bye' to exit.\n")

    while True:
        user_message = input("You: ")

        if not user_message.strip():
            print(f"{BOT_NAME}: Please type something so I can respond.")
            continue

        response, should_end = find_response(user_message)
        print(f"{BOT_NAME}: {response}")

        if should_end:
            break


if __name__ == "__main__":
    run_chat()

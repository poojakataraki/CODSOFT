# Rule-Based Chatbot

A simple command-line chatbot that gives responses using predefined rules and pattern matching. The project is built in Python and does not need any external libraries.

## Features

- Responds to greetings and basic conversation
- Answers simple questions about itself
- Gives current time and date
- Handles keywords like Python, project, help, jokes, thanks, and goodbye
- Uses regular expressions for pattern matching
- Includes a small test file

## Project Structure

```text
.
├── chatbot.py
├── test_chatbot.py
├── README.md
└── .gitignore
```

## How to Run

Make sure Python is installed, then run:

```bash
python chatbot.py
```

To exit the chatbot, type:

```text
bye
```

## Example Chat

```text
Nova: Hello! I am Nova, your rule-based chatbot.
Nova: Type 'help' to see what I can answer, or 'bye' to exit.

You: hello
Nova: Hi there. What would you like to talk about?

You: what can you do
Nova: Try asking: 'what is your name', 'tell me a joke', 'what is python', or 'what time is it'.

You: bye
Nova: See you later!
```

## Run Tests

```bash
python -m unittest
```

## How It Works

The chatbot first cleans the user's message by converting it to lowercase and removing unnecessary symbols. Then it checks the message against a list of rules. Each rule contains patterns and possible responses. When a pattern matches, the chatbot returns one response from that rule.

If no rule matches, the chatbot gives a fallback response.

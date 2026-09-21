

# 🤖 Basic Chatbot

## 📌 Project Overview

This project is a simple **rule-based chatbot** built using Python.

The chatbot takes input from the user and gives a predefined response based on what the user types.

## 🎯 Goal

The goal of this project is to practice:

* `if-elif-else`
* Functions
* `while` loops
* `input()` and `print()`
* Function calling
* Basic user interaction

## 💬 Supported Messages

| User Input    | Chatbot Response    |
| ------------- | ------------------- |
| `hello`       | `Hi!`               |
| `how are you` | `I'm fine, thanks!` |
| `bye`         | `Goodbye!`          |

If the chatbot doesn't recognize the input, it responds:

```text
Sorry, I don't understand.
```

## 🧠 How It Works

First, we define a function called `chatbot`:

```python
def chatbot():
```

The function contains the chatbot's logic.

At the end, we call the function:

```python
chatbot()
```

Calling `chatbot()` tells Python to **run the function**.

## 🛠️ Example

```text
You: hello
Bot: Hi!

You: how are you
Bot: I'm fine, thanks!

You: bye
Bot: Goodbye!
```

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python chatbot.py
```

## 📚 What I Learned

Through this project, I learned that:

* `def` is used to **define a function**.
* `chatbot()` is used to **call/run the function**.
* `input()` takes information from the user.
* `if`, `elif`, and `else` make decisions.
* `while` keeps the chatbot running.
* `break` stops the loop.

## 🚀 Future Improvements

The chatbot can later be improved by adding:

* More questions and answers
* A name for the chatbot
* A `help` command
* More flexible user input
* More natural conversations

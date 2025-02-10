# AI-CHATBOT-WITH-NLP

- **Company:** CODTECH IT SOLUTIONS  
- **Name:** Devyani Karade  
- **Intern ID:** CT08LTW  
- **Domain:** Python  
- **Batch Duration:** February 5th, 2025 - March 5th, 2025  
- **Mentor:** Neela Santhosh  

This repository contains a Python-based chatbot that uses the **NLTK Chat Module** to handle basic conversations. Additionally, the chatbot integrates **Wikipedia API** to fetch relevant information when user queries are beyond predefined responses. It also includes a **Streamlit web interface** for interactive chatbot conversations.

## Features

✅ Handles basic conversations using predefined responses  
✅ Fetches relevant information from Wikipedia  
✅ Supports both **terminal-based** and **web-based (Streamlit)** interaction  
✅ Simple and easy-to-use chatbot with regex-based pattern matching  

## 1. Terminal-Based ChatBot

The chatbot runs in the terminal and supports:

- Greeting the user
- Answering basic predefined queries (e.g., name, location, abilities, age, etc.)
- Fetching Wikipedia summaries for unknown queries
- Exiting with 'quit', 'bye', or 'see you'

## 2. Streamlit-Based ChatBot

The chatbot can also run on a web interface using **Streamlit**. The web-based chatbot allows users to interact using a simple UI with text input and chatbot responses.

### Running the Streamlit ChatBot

```sh
streamlit run task3.py
```

## Technologies Used

- **Python** - Core programming language  
- **NLTK** - Natural Language Processing for chatbot conversation  
- **Wikipedia API** - Fetching real-time information  
- **Streamlit** - Web-based chatbot UI  
- **Regular Expressions (re)** - Pattern matching for chatbot responses  

## Usage

1. **For Terminal ChatBot:**
   - Run `task_3.py` in the terminal.
   - Type queries and get responses.
   - Type 'quit', 'bye', or 'see you' to exit.

2. **For Streamlit ChatBot:**
   - Run `task3.py` using `streamlit run task_3.py`.
   - Enter queries in the input field.
   - Receive chatbot responses instantly.

## Example Interactions

**User:** Hi  
**ChatBot:** Hello! How can I help you?  

**User:** What is the meaning of Capitalism?  
**ChatBot:** ChatBot: The concept of late capitalism (in German: Spätkapitalismus) was first used by the German social scientist Werner Sombart (1863-1941) in 1928, to describe the new capitalist order emerging at that time - with the claim, that it was the beginning of a new stage in the history of capitalism. As a young man, Sombart was a socialist who associated with Marxist intellectuals and the German social-democratic party.

## OUTPUT of chatbot:
![Image](https://github.com/user-attachments/assets/b8621624-e795-4a2d-89b8-2f3867f3f7e0)



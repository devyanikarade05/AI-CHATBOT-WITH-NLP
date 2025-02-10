#Using streamlit
import streamlit as st
import re
import wikipedia
from nltk.chat.util import Chat, reflections

def get_wikipedia_summary(topic):
    try:
        return wikipedia.summary(topic, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Did you mean: {', '.join(e.options[:3])}?"
    except wikipedia.exceptions.PageError:
        return "Sorry, I don't have any knowledge about that."
    except:
        return "Sorry from me, Ask me after some time."

pairs = [
    [r"my name is (.*)", ["Hello %1, how can I help you today?"]],
    [r"what is your name ?", ["I am ChatBot."]],
    [r"how are you ?", ["I'm doing well, thank you!", "I'm great, thanks for asking."]],
    [r"quit|bye|see you", ["Bye! Take care."]],
    [r"sorry (.*)", ["It's alright.", "No problem."]],
    [r"hi|hey|hello", ["Hello!", "Hey there!"]],
    [r"(.*) (location|city) ?", ["I am a chatbot, so I don't have a physical location."]],
    [r"what can you do ?", ["I can answer your questions, have a simple conversation, and assist you with basic queries."]],
    [r"(.*) (weather|temperature) ?", ["I'm sorry, I don't have access to real-time weather data."]],
    [r"how old are you|what is your age", ["I am just a program, so I don't have an age."]],
    [r"thank you|thanks", ["You're welcome!", "No problem!"]],
    [r"okay|ok", ["Yes, do you have any other questions?", "Ask me anything..."]]
]

chatbot = Chat(pairs, reflections)

st.title("ChatBot")
st.write("Hi! I'm ChatBot. Type 'quit', 'bye', or 'see you' to exit.")

user_input = st.text_input("You:", "")

if user_input:
    if re.match(pairs[3][0], user_input.lower()):
        st.write("**ChatBot:** Bye! Take care.")
    else:
        response = chatbot.respond(user_input) or get_wikipedia_summary(user_input)
        st.write(f"**ChatBot:** {response}")


#terminal: streamlit run task3.py (command)
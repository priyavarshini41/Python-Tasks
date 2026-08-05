from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections
import nltk

nltk.download('punkt')

app = Flask(__name__)

pairs = [

    [r"hi|hello|hey|hii",
    ["Hello! How can I help you? 😊",
     "Hi there 👋",
     "Hey! Nice to meet you!"]],

    [r"how are you ?",
    ["I'm doing great 😊 How about you?"]],

    [r"what is your name ?",
    ["I am an AI chatbot built using Python and NLTK."]],

    [r"who created you ?",
    ["I was created as an NLP project."]],

    [r"what can you do ?",
    ["I can answer questions and chat with you."]],

    [r"what is python ?",
    ["Python is a programming language used in AI, web development and data science."]],

    [r"what is java ?",
    ["Java is widely used for application development."]],

    [r"what is ai ?",
    ["Artificial Intelligence enables machines to mimic human intelligence."]],

    [r"what is nlp ?",
    ["NLP stands for Natural Language Processing."]],

    [r"tell me a joke",
    ["Why do programmers prefer dark mode? Because light attracts bugs 😆"]],

    [r"good morning",
    ["Good morning ☀️"]],

    [r"good night",
    ["Good night 🌙 Sleep well!"]],

    [r"thanks|thank you",
    ["You're welcome 😊"]],

    [r"bye|quit|exit",
    ["Goodbye 👋 Have a nice day!"]],

    [r"(.*)",
    ["Sorry, I didn't understand that.",
     "Could you ask that differently?",
     "I'm still learning 😊"]]

]

chatbot = Chat(pairs, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    response = chatbot.respond(user_message)

    if response is None:
        response = "I don't understand."

    return jsonify({
        "reply": response
    })


if __name__ == "__main__":
    app.run(debug=True)
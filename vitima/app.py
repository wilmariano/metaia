from flask import Flask, render_template, request, session
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
chatbot = ChatBot("Friday")

app.secret_key = 'casadosbot'

#from chatterbot.trainers import ListTrainer
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
#trainer = ListTrainer(chatbot)
trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train(conversation)
trainer.train('chatterbot.corpus.portuguese')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
   "games"
)

chatbot = ChatBot(
    'Example Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.50
        }
    ]
)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if userText == "arvores":
        return str("são verdes em cima")
        session['assunto'] = 8267
    elif 'assunto' in session:
        if userText == "elas respiram?":
            return str("sim e soltam carbono")
    else:
        return str(chatbot.get_response(userText))
if __name__ == "__main__":
    app.run()


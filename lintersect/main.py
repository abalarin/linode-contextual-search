from flask import Flask, render_template, request

from snips_nlu.default_configs import CONFIG_EN
from snips_nlu import SnipsNLUEngine
import io
import json

app = Flask(__name__)


loaded_engine = SnipsNLUEngine.from_path("./models/engine")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/searchit', methods=["POST"])
def search():
    intents = loaded_engine.parse(request.json, top_n=2)

    nlu_intents = {}
    for intent in intents:
        if intent['intent']['intentName'] != None:
            nlu_intents[intent['intent']['intentName']] = intent['intent']['probability']


    return json.dumps(nlu_intents)

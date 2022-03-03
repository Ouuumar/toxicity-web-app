from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin

import torch
import json
import pandas as pd
from detoxify import Detoxify

COLUMNS = [
    "toxicity",
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]

model = torch.hub.load('unitaryai/detoxify','toxic_bert')


app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')

def web_page():
    return render_template("index.html")


@app.route("/toxicity", methods=['GET', 'POST'])

@cross_origin()

def toxic_analysis():
    print(request.args)
    text = request.args['text']

    results = Detoxify('original').predict(str(text))
    final_result = pd.DataFrame.from_dict(results, orient='index').round(5)

    return json.dumps(str(results))

if __name__ == '__main__':
    app.run(threaded=False, debug=True, host='0.0.0.0', port=7979)
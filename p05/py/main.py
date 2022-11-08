# Get path to my module
from flask import *
import json

app = Flask(__name__)

# Data Dictionary
jsonString = '{"0": "200px-Panini_SMTCC_156.jpg", "1": "200px-Panini_SMTCC_150.jpg", "2": "200px-Panini_SMTCC_151.jpg", "3": "200px-Panini_SMTCC_146.jpg", "4": "200px-Panini_SMTCC_160.jpg", "5": "200px-Panini_SMTCC_159.jpg", "6": "200px-Panini_SMTCC_155.jpg", "7": "200px-Panini_SMTCC_147.jpg", "8": "200px-Panini_SMTCC_157.jpg", "9": "200px-Panini_SMTCC_149.jpg"}'

# Load JSON string into a dictionary
data = json.loads(jsonString)


@app.route('/', methods=['GET'])
def request_page():
    id = str(request.args.get('card'))

    # Loop along dictionary keys
    for key in data:
        if (key == id):
            return data[key]


if __name__ == '__main__':
    app.run(port=5000)

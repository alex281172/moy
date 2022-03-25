import requests
import json
from flask import Flask


#контроль


text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text

currensies = json.loads(text)
# print(currensies['Valute'])
for currensy in currensies['Valute']:
    print(currensy)

app = Flask(__name__)

@app.route("/")
def hello():
    text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
    currensies = json.loads(text)
    result = ''
    for currensy in currensies['Valute']:
        result += str(currensy) + '<br>'
    return result

if __name__ == "__main__":
    app.run()
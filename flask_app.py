import json

from flask import Flask, render_template, request, g

app = Flask(__name__)


def get_data(file_name='result.json'):
    with open(file_name, 'r') as file:
        data = json.loads(file.read())
    return data


@app.route("/")
def home():
    data = get_data()
    return render_template("home.html",
                           year_days=data.get('year_days'),
                           peoples=data.get('peoples'),
                           day_range=data.get('day_range'),
                           result=data.get('result'))


if __name__ == "__main__":
    app.run()

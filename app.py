from flask import Flask, render_template
from random import choices

FRUITS = ["Apple", "Orange", "Banana"]
app = Flask(__name__)


def random_fruit():
    return choices(FRUITS)[0]


@app.route("/fruit")
def get_fruit():
    """Random Fruit"""
    fruit = random_fruit()
    return render_template("fruit.html", fruit=fruit)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

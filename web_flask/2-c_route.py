#!/usr/bin/python3
"""_summary_

Returns:
    _type_: _description_
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """_summary_

    Returns:
        _type_: _description_
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """_summary_"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """_summary_

    Args:
        text (_type_): _description_

    Returns:
        _type_: _description_
    """
    formatted_text = text.replace("_", " ")
    return f"C {formatted_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

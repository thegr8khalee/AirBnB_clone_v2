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


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """_summary_

    Args:
        text (str, optional): _description_. Defaults to "is cool".

    Returns:
        _type_: _description_
    """
    formatted_text = text.replace("_", " ")
    return f"Python {formatted_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number_template(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

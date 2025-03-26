"""
This module contains a simple Flask application that fetches a secret
from an environment variable and displays it.
"""

import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """
    This function returns a greeting message with the secret value
    fetched from the MY_SECRET environment variable.
    """
    secret_value = os.environ.get('MY_SECRET', 'Secret not found')
    return f'Hello!!, This value "{secret_value}" is fetched from the environment variable.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)

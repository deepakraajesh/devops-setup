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
    fetched from the APP_SECRET environment variable.
    """
    secret_value = os.environ.get('APP_SECRET', 'Secret not found')
    sops_secret_value = os.environ.get('SOPS_SECRET', 'SOPS secret not found')
    result = f'''Hello!!, This value "{secret_value}" is fetched from the Secrets Manager.\n
                 This value "{sops_secret_value}" is fetched from the SOPS Secret.'''
    formatted_result = result.replace('\n', '<br>')
    return formatted_result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)

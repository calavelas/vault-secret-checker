from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    pod_name = os.getenv("HOSTNAME")
    env_vars = os.environ
    html = f"<h1>Pod Name: {pod_name}</h1><h2>Environment Variables:</h2><ul>"
    for key, value in env_vars.items():
        html += f"<li>{key}: {value}</li>"
    html += "</ul>"
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

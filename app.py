from flask import Flask, render_template

app = Flask(__name__)

from controllers import user_controller, country_controller, memory_controller

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "welcome to the flask tutorials updated with Fluxcd and image automation"


if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 80, debug = True)

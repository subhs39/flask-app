from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Messi is the Greatest of All Time !"

if __name__ == "__main__":
    application.run()

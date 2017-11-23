from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    return render_template("main.html")

if __name__ == "__main__":
    application.run()

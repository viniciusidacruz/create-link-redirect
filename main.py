from flask import Flask, render_template, url_for

application = Flask(__name__)

@application.route("/")
def home_page():
    return render_template("homepage.html")
    

if __name__ == '__main__':
    application.run(debug=True)
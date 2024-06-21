from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")


@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard1.html")
    return "hy this is my dashboard page"



if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hello")
def hello():

    return render_template('2.html')
@app.route("/about")
def harry():
    name = "rohan das"
    return render_template('about.html', name2= name)
app.run(debug=True)

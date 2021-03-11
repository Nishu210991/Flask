from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/Nishu')
def me():
    #name = request.args.get("name", "World")
    return "Hello Beautiful!"

@app.route('/about')
def Nishu():
    name="Nishu"
    return render_template('about.html', name=name)

@app.route("/bootstrap")
def Boot():
    return render_template('bootstrap.html')

app.run(debug=True)
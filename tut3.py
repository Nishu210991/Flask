from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index1.html')

@app.route('/about')
def Nishu():
    name="Nishu"
    return render_template('about1.html', name=name)

@app.route("/bootstrap")
def Boot():
    return render_template('bootstrap.html')

if __name__=="__main__":
    app.run(host='127.0.0.1', port=5000 , debug=True)
    # automatically change show on broswer if debug=True.Don't need to reload the page.
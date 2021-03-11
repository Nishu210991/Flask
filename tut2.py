from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/about')
def Nishu():
    name="Nishu"
    return render_template('about.html', name=name)

if __name__=="__main__":
    #app.run(debug=True) # automatically change show on broswer if debug=True.Don't need to reload the page.
    app.run(host='127.0.0.1', port=4444, debug=True)

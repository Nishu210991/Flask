from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    #name = request.args.get("name", "World")
    return "Hello!"


@app.route('/Nishu')
def Nishu():
    #name = request.args.get("name", "World")
    return "Hello Beautiful!"

if __name__=="__main__":
    #app.run(debug=True) # automatically change show on broswer if debug=True.Don't need to reload the page.
    app.run(host='127.0.0.1', port=8000, debug=True)


from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return("Python Flask website started here!")
@app.route('/contacts')
def contacts():
    return("contacts page displayed here!")
@app.route('/services')
def services():
    return("services page started here")
if __name__ == "__main__":
    app.run(debug=True)




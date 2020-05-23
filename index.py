from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return("python flask website started here)")
@app.route('/contacts')
def contacts():
    return("contacts page here")

if __name__=="__main":
    app.run(Debug=True)




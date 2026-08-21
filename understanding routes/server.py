from flask import Flask , render_template
app= Flask(__name__)

@app.route("/")
def hello():
    return " Hello"

@app.route("/Champion")
def champion():
    return "champion"

@app.route("/hello/<name>")
def hello_name(name):
    print(name)
    return "hello" + name

@app.route("/repeat/<int:time>/<word>")
def repeat_word(time,word):
        return "<br>".join([word] * time)

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! No response. Try again.", 404

if __name__ == "__main__":
    app.run(debug=True)
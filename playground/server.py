from flask import Flask , render_template
app= Flask(__name__)

@app.route("/")
<<<<<<< HEAD

# @app.route("/play")
# def play():
#     return render_template("index.html")

@app.route("/play/<x>/<color>")
def play(x,color):
    return render_template("index.html",num=int(x),color=color)

=======
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
>>>>>>> a341f61d9d54334ee06420db9231cf0b7a1cbadd

if __name__ == "__main__":
    app.run(debug=True)
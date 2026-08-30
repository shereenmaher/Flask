from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/4')
def index2():
    return render_template("index2.html")

@app.route('/<rows>/<columns>')
def changeSquares(rows, columns):
    return render_template("change.html", rows=int(rows), columns=int(columns))

if __name__=="__main__":
    app.run(debug=True)


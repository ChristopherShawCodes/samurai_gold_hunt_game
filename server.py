from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

app.secret_key="Secret Shiznit Code"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process_money',methods=["POST"])
def process():
    print(request.form["building"])
    return redirect("/")



if __name__=="__main__":
    app.run(debug=True)
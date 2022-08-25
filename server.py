from flask import Flask, render_template, redirect, session, request
#import the randint functionality, this provides the ability to provide 2 values as a range and it will return a random value within that range
from random import randint
#import the date/time functionality
from datetime import datetime

app = Flask(__name__)

app.secret_key="Secret Shiznit Code"


@app.route('/')
def index():
    if "gold" not in session:
        session["gold"] = 0
        session["activities"] = []
    return render_template("index.html")


@app.route('/process_money', methods=["POST"])
def process():
    building = request.form["building"]
    if building == "farm":
        gold_to_add = randint(10,20)
    elif building == "cave":
        gold_to_add = randint(5,10)
    elif building == "house":
        gold_to_add = randint(2,5)
    else:
        #you can use randint and assign a -0 value to add a "take away" function
        gold_to_add = randint(-50,50)
        #prints which button was clicked in the terminal which is hidden to the user
        print(request.form["building"])
        #line 31 references line 15 on index.html
        #<h3>Your Gold: <span class="gold">{{session["gold"]}}</span></h3>
    session["gold"] += gold_to_add
    #the following will be displayed in the "activities" area on the UI
    session["activities"].append({
        "gold": gold_to_add,
        "building": building,
        "time": datetime.now()
    })
    print(session["activities"])
    return redirect("/")



if __name__=="__main__":
    app.run(debug=True)
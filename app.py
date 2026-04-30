from flask import Flask, render_template, request
import random
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/random-number-generator", methods=["GET", "POST"])
def rannum():
    number = None
    if request.method == "POST":
        number = random.randint(1, 100)
    return render_template("randomnumbergenerator.html", number=number)
        
if __name__ == "__main__":
    app.run()

from flask import Flask
@app.route("/")
def home():
    return "Hello, World"
if __name__ == "__main__":
    app.run()
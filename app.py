from flask import Flask, render_template, request

# create server object 
app = Flask(__name__)

# create routes 
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        pass
    if request.method == "POST":
        request.form.get("name")
        request.form.post("name")

    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
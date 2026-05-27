from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample admission data
data = {
    "fee":"B.Tech CSE fee is ₹1,20,000 per year.",
    "mba":"MBA eligibility requires graduation with 50%.",
    "hostel":"Hostel fee is ₹60,000 per year.",
    "date":"Admission last date is July 30."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():

    question = request.json["question"].lower()

    if "fee" in question:
        answer = data["fee"]

    elif "mba" in question:
        answer = data["mba"]

    elif "hostel" in question:
        answer = data["hostel"]

    elif "date" in question:
        answer = data["date"]

    else:
        answer = "Information not found."

    return jsonify({
        "answer":answer
    })

if __name__ == "__main__":
    app.run(debug=True)
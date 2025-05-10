from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    status = ""
    ratio = ""
    if request.method == "POST":
        income = float(request.form["income"])
        annuity = float(request.form["annuity"])
        loan_type = request.form["loan_type"]
        ratio = annuity / income

        if income >= 180_000_000 and ratio <= 0.25 and loan_type != "Cash Loans":
            status = "Disetujui ✅"
        else:
            status = "Ditolak ❌"

        ratio = f"{ratio * 100:.2f}%"

    return render_template("index.html", status=status, ratio=ratio)

if __name__ == "__main__":
    app.run(debug=True)

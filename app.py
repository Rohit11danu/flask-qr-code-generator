from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_path = None

    if request.method == "POST":
        data = request.form["data"]
        img = qrcode.make(data)
        qr_path = "static/qrcode.png"
        img.save(qr_path)

    return render_template("index.html", qr_path=qr_path)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import os
from infer_engine import run_full_analysis

app = Flask(__name__)
os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image = None
    if request.method == "POST":
        f = request.files["chart"]
        path = os.path.join("uploads", f.filename)
        f.save(path)
        decision, confidence, image, _ = run_full_analysis(path)
        result = {"decision": decision, "confidence": confidence}
    return render_template("index.html", result=result, image=image)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

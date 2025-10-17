from flask import Flask, render_template, request, redirect, url_for, session, flash
import joblib
import pymysql

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Needed for sessions

# Load model + vectorizer
model = joblib.load("rf_model_balanced.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# MySQL connection
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="2025",
    database="cyberbullying_db"
)

# Hardcoded admin credentials (you can later move to DB)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"

# -----------------------------
# Routes
# -----------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("text")
    if not text:
        return {"error": "Please enter text."}
    
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    
    # Save to MySQL
    cur = conn.cursor()
    cur.execute("INSERT INTO predictions (text, prediction) VALUES (%s, %s)", (text, str(pred)))
    conn.commit()
    
    return {"text": text, "prediction": str(pred)}


@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["admin_logged_in"] = True
            return redirect(url_for("admin_dashboard"))
        else:
            flash("Invalid credentials", "danger")
            return redirect(url_for("admin_login"))
    return render_template("admin_login.html")


@app.route("/admin")
def admin_dashboard():
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))

    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM predictions ORDER BY id ASC")
    predictions = cur.fetchall()
    return render_template("admin.html", predictions=predictions)


@app.route("/admin-logout")
def admin_logout():
    session.pop("admin_logged_in", None)
    return redirect(url_for("admin_login"))


if __name__ == "__main__":
    app.run(debug=True)
    
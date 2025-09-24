from flask import Flask, request, redirect, render_template_string, jsonify

app = Flask(__name__)

# In-memory storage for notes
notes = []

# HTML template (kept simple for demo)
TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Notes App</title>
</head>
<body>
    <h1>My Notes</h1>
    <form method="POST" action="/add">
        <input type="text" name="note" placeholder="Enter your note" required>
        <button type="submit">Add</button>
    </form>
    <ul>
        {% for note in notes %}
            <li>{{ note }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(TEMPLATE, notes=notes)

@app.route("/add", methods=["POST"])
def add_note():
    note = request.form.get("note")
    if note:
        notes.append(note)
    return redirect("/")

# ✅ Add a health-check route (for tests and CI/CD)
@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    # ✅ Bind to 0.0.0.0 so it works inside Docker/EC2
    app.run(host="0.0.0.0", port=5000, debug=True)

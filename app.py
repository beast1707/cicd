from flask import Flask, request, redirect, render_template_string, jsonify

app = Flask(__name__)

# In-memory storage for notes
notes = []

# HTML template with embedded CSS
TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Notes App</title>
    <style>
        /* Global styles */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(to bottom right, #f5f7fa, #c3cfe2);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
        }

        .container {
            width: 100%;
            max-width: 600px;
            margin: 60px auto;
            background: #ffffff;
            border-radius: 16px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            padding: 30px 40px;
            text-align: center;
            transition: all 0.3s ease;
        }

        .container:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 24px rgba(0, 0, 0, 0.15);
        }

        h1 {
            font-size: 2.2rem;
            color: #2c3e50;
            margin-bottom: 20px;
        }

        form {
            display: flex;
            gap: 10px;
            justify-content: center;
            margin-bottom: 25px;
        }

        input[type="text"] {
            flex: 1;
            padding: 12px 16px;
            border: 2px solid #3498db;
            border-radius: 8px;
            font-size: 1rem;
            outline: none;
            transition: all 0.2s ease;
        }

        input[type="text"]:focus {
            border-color: #2980b9;
            box-shadow: 0 0 6px rgba(41, 128, 185, 0.5);
        }

        button {
            background: #3498db;
            color: #ffffff;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        button:hover {
            background: #2980b9;
            transform: translateY(-1px);
            box-shadow: 0 4px 8px rgba(41, 128, 185, 0.3);
        }

        ul {
            list-style-type: none;
            padding: 0;
            margin-top: 20px;
            text-align: left;
        }

        li {
            background: #ecf0f1;
            margin-bottom: 10px;
            padding: 12px 16px;
            border-radius: 8px;
            font-size: 1rem;
            color: #2c3e50;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            transition: transform 0.2s ease;
        }

        li:hover {
            transform: scale(1.02);
            background: #dfe6e9;
        }

        footer {
            margin-top: 20px;
            font-size: 0.9rem;
            color: #95a5a6;
        }

        @media (max-width: 600px) {
            form {
                flex-direction: column;
            }
            button {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📒 My Notes</h1>
        <form method="POST" action="/add">
            <input type="text" name="note" placeholder="Write a note..." required>
            <button type="submit">Add</button>
        </form>
        <ul>
            {% for note in notes %}
                <li>{{ note }}</li>
            {% endfor %}
        </ul>
        <footer>✨ Simple Flask Notes App ✨</footer>
    </div>
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

# ✅ Health check for CI/CD
@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    # ✅ Bind to 0.0.0.0 so it works inside Docker/EC2
    app.run(host="0.0.0.0", port=5000, debug=True)

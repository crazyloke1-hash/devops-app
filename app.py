from flask import Flask, request, redirect, render_template_string
import sqlite3

app = Flask(__name__)

def get_conn():
    return sqlite3.connect("expenses.db")

# create table
conn = get_conn()
conn.execute("CREATE TABLE IF NOT EXISTS expenses(name TEXT, amount REAL)")
conn.close()

HTML = """
<h1>Expense Tracker</h1>

<form method="post" action="/add">
  Name: <input name="name"><br>
  Amount: <input name="amount" type="number"><br>
  <button type="submit">Add</button>
</form>

<h2>Expenses</h2>
<ul>
{% for e in data %}
  <li>{{e[0]}} - {{e[1]}}</li>
{% endfor %}
</ul>

<h2>Total: {{total}}</h2>
"""

@app.route("/")
def home():
    conn = get_conn()
    data = conn.execute("SELECT * FROM expenses").fetchall()
    total = conn.execute("SELECT SUM(amount) FROM expenses").fetchone()[0]
    conn.close()
    return render_template_string(HTML, data=data, total=total)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    amount = request.form["amount"]

    conn = get_conn()
    conn.execute("INSERT INTO expenses VALUES (?,?)", (name, amount))
    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
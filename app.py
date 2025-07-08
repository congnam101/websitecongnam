from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def index():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="mydb"
        )
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        return f"Connected to MySQL! Tables: {tables}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
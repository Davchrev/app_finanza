from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Ruta para mostrar los gastos
@app.route('/')
def home():
    conn = sqlite3.connect('finanzas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    conn.close()
    return render_template('index.html', expenses=expenses)

# Ruta para agregar un nuevo gasto
@app.route('/add_expense', methods=['POST'])
def add_expense():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        amount = request.form['amount']
        date = request.form['date']

        # Conectar a la base de datos y agregar el gasto
        conn = sqlite3.connect('finanzas.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (name, category, amount, date) VALUES (?, ?, ?, ?)",
                       (name, category, amount, date))
        conn.commit()
        conn.close()

        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

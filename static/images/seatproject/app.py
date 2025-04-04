from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Function to get a new database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="janhvi123",
        database="test"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book_seat', methods=['POST'])
def book_seat():
    seat_number = request.form['seat']
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Check if the seat is already booked
        cursor.execute("SELECT status FROM seat_table WHERE seatno = %s", (seat_number,))
        seat = cursor.fetchone()

        if seat:
            if seat[0] == 1:
                return jsonify({"message": f"Seat {seat_number} is already booked.", "status": "failed"})
            else:
                # Update the seat status to booked
                cursor.execute("UPDATE seat_table SET status=1 WHERE seatno = %s", (seat_number,))
                conn.commit()
                return jsonify({"message": f"Seat {seat_number} booked successfully!", "status": "success"})
        else:
            return jsonify({"message": f"Seat {seat_number} not found.", "status": "failed"})

    except mysql.connector.Error as err:
        return jsonify({"message": f"An error occurred: {err}", "status": "error"})

    finally:
        cursor.close()
        conn.close()

@app.route('/get_seat_status')
def get_seat_status():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT seatno, status FROM seat_table")
        seats = [{'seatno': seat[0], 'status': seat[1]} for seat in cursor.fetchall()]
        return jsonify(seats)

    except mysql.connector.Error as err:
        return jsonify({"message": f"An error occurred: {err}", "status": "error"})

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)

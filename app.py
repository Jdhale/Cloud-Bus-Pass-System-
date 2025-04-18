from flask import Flask, jsonify, request, render_template, redirect, session, send_file
from datetime import datetime
import mysql.connector
from mysql.connector import errorcode
import random
import qrcode
from io import BytesIO

from datetime import datetime
app = Flask(__name__)

app.secret_key = 'spymun'  

try:
    cnx = mysql.connector.connect(user='root', password='NewStrongPass123!',
                                  database='demose')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("Connection done")
    cnx.close()
db_config = {
    'user': 'root',
    'password': 'NewStrongPass123!',
    'host': 'localhost',
    'database': 'demoseat',
}

def validate_credentials(enrollmentno, password):
    try:
        cnx = mysql.connector.connect(user='root', password='NewStrongPass123!',
                                      database='demose')
        cursor = cnx.cursor()

        query = "SELECT * FROM userlogin WHERE enrollmentno = %s AND password = %s"
        cursor.execute(query, (enrollmentno, password))
        result = cursor.fetchone()

        cursor.close()
        cnx.close()

        return result is not None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False


def display_seat(seats,date):
    try:
        cnx = mysql.connector.connect(user='root', password='NewStrongPass123!', database='demoseat')
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor = cnx.cursor()
        
        for i in range(1, 35):  # Range should start from 1 and end at 34
            query = "SELECT status FROM {} WHERE seatno = %s".format(date)
            cursor.execute(query, (i,))
            x = cursor.fetchone()
            if x is not None:  # Check if a row was fetched
                seats.append(x[0])  # Append the status to the seats list
            else:
                seats.append(None)  # Append None if no row was fetched for that seatno
        cnx.close()

def update_status(seat_number,date):
    try:
        cnx = mysql.connector.connect(user='root', password='NewStrongPass123!', database='demoseat')
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor = cnx.cursor()
        query = "UPDATE {} SET status = 'seat booked' WHERE seatno = %s".format(date)
        cursor.execute(query, (seat_number,))
        query = "UPDATE {} SET enroll = %s WHERE seatno = %s".format(date)
        cursor.execute(query, (session['enrollmentno'],seat_number,))
        cnx.commit()
        cursor.close()
        cnx.close()

def fetch_booked_seats(enrollment):
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        # Assuming table names are table0, table1, table2, and table3
        tables = ['table0', 'table1', 'table2', 'table3']
        booked_seats = []

        for table in tables:
            query = f"SELECT seatno FROM {table} WHERE enroll = %s"
            cursor.execute(query, (enrollment,))
            results = cursor.fetchall()
            for result in results:
                ans='SeatNo : '
                ans=ans  + str(result[0])
                ans=ans+' for '
                if(table=='table0'):
                    ans=ans+'26th April 2024'
                elif (table=='table1'):
                    ans=ans+'27th April 2024'
                elif (table=='table2'):
                    ans=ans+'28th April 2024'
                elif (table=='table3'):
                    ans=ans+'29th April 2024'    
                booked_seats.append(ans)

        cursor.close()
        cnx.close()

        return booked_seats

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
def get_available_seats():
    try:
        cnx = mysql.connector.connect(user='root', password='NewStrongPass123!',
                                      host='localhost', database='demoseat')
        cursor = cnx.cursor()

        query = "SELECT seat_number FROM emer_table WHERE status = 'available' LIMIT 5"
        cursor.execute(query)
        available_seats = [row[0] for row in cursor.fetchall()]  # Fetch all rows and extract seat_number

        cursor.close()
        cnx.close()

        return available_seats
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
# Route for profile page
@app.route('/profile')
def profile():
    if 'enrollmentno' in session:
        enrollment = session['enrollmentno']
        booked_seats = fetch_booked_seats(enrollment)
        return render_template('profile.html', enrollment=enrollment, booked_seats=booked_seats)
    else:
        return 'Unauthorized access'
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/HomePage')
def HomePage():
    return render_template('HomePage.html')
@app.route('/TimePage')
def TimePage():
    return render_template('TimePage.html') 
@app.route('/bus_track')
def bus_track():
    return render_template('bus_track.html')
@app.route('/student_pass')
def student_pass():
    return render_template('student_pass.html')


@app.route('/login', methods=['POST'])
def login():
    enrollmentno = request.form.get('Enrollmentno')
    password = request.form.get('password')

    if validate_credentials(enrollmentno, password):
        # Credentials are valid, store enrollment number in session
        session['enrollmentno'] = enrollmentno
        return render_template('HomePage.html')
    else:
        # Invalid credentials, display an error message
        return render_template('index.html', error_message='Invalid credentials')


@app.route('/CommunityForum')
def CommunityForum():
    cnx = mysql.connector.connect(user='root', password='NewStrongPass123!',
                                  database='demose')
    cursor=cnx.cursor()
    cursor.execute('SELECT * FROM posts ORDER BY date DESC')
    posts = cursor.fetchall()
    return render_template('CommunityForum.html', posts=posts)


@app.route('/submit', methods=['POST'])
def submit_post():
    cnx = mysql.connector.connect(user='root', password='NewStrongPass123!',
                                  database='demose')
    cursor=cnx.cursor()
    title = request.form['postTitle']
    content = request.form['postContent']
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('INSERT INTO posts (title, content, date) VALUES (%s, %s, %s)', (title, content, date))
    cnx.commit()
    return redirect('/CommunityForum')


@app.route('/booking', methods=['POST'])
def booking():
    if 'enrollmentno' in session:
        session['date'] = request.form['date']
        seats = []
        table=['table0','table1','table2','table3']
        print(session['date'])
        display_seat(seats,table[int(session['date'])])
        return render_template('booking.html', seat1='{}'.format(seats[0]),seat2='{}'.format(seats[1]),seat3='{}'.format(seats[2]),seat4='{}'.format(seats[3]),seat5='{}'.format(seats[4]),seat6='{}'.format(seats[5]),seat7='{}'.format(seats[6]),seat8='{}'.format(seats[7]),seat9='{}'.format(seats[8]),seat10='{}'.format(seats[9]),seat11='{}'.format(seats[10]),seat12='{}'.format(seats[11]),seat13='{}'.format(seats[12]),seat14='{}'.format(seats[13]),seat15='{}'.format(seats[14]),seat16='{}'.format(seats[15]),seat17='{}'.format(seats[16]),seat18='{}'.format(seats[17]),seat19='{}'.format(seats[18]),seat20='{}'.format(seats[19]),seat21='{}'.format(seats[20]),seat22='{}'.format(seats[21]),seat23='{}'.format(seats[22]),seat24='{}'.format(seats[23]),seat25='{}'.format(seats[24]),seat26='{}'.format(seats[25]),seat27='{}'.format(seats[26]),seat28='{}'.format(seats[27]),seat29='{}'.format(seats[28]),seat30='{}'.format(seats[29]),seat31='{}'.format(seats[30]),seat32='{}'.format(seats[31]),seat33='{}'.format(seats[32]),seat34='{}'.format(seats[33]),)
    else:
        return redirect('/') 


@app.route('/selection', methods=['POST'])
def selection():
    if 'enrollmentno' in session:
        val = [x for x in request.form.values()]
        print(val)
        seat_number=val[0]
        table=['table0','table1','table2','table3']
        update_status(int(seat_number),table[int(session['date'])])
        return render_template('woho.html', seatno=seat_number,enroll=session['enrollmentno'])
    else:
        return redirect('/') 

    
@app.route('/emergency_booking')
def emergency_booking():
    available_seats = get_available_seats()  # Fetch available seats from the database
    return render_template('emergency_booking.html', available_seats=available_seats)

@app.route('/book_seat', methods=['POST'])
def book_seat():
    selected_seat = request.form['seat']
    try:
        cnx = mysql.connector.connect(user='root', password='NewStrongPass123!', host='localhost', database='demoseat')
        cursor = cnx.cursor()

        query = "UPDATE emer_table SET  status='Unavailable' WHERE seat_number = {}".format(selected_seat)
     

        cursor.close()
        cnx.close()

    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    return render_template('woho.html', seatno=selected_seat,enroll=session['enrollmentno'])

@app.route('/logout')
def logout():
    session.pop('enrollmentno', None)  
    return redirect('/')


# Simulating bus GPS locations
bus_locations = {
    1: {"lat": 19.0760, "lng": 72.8777},  # Example: Mumbai coordinates
    2: {"lat": 28.7041, "lng": 77.1025}   # Example: Delhi coordinates
}

@app.route('/get_bus_location/<int:bus_id>')
def get_bus_location(bus_id):
    if bus_id in bus_locations:
        # Simulate slight movement in coordinates
        bus_locations[bus_id]["lat"] += random.uniform(-0.001, 0.001)
        bus_locations[bus_id]["lng"] += random.uniform(-0.001, 0.001)
        return jsonify(bus_locations[bus_id])
    return jsonify({"error": "Bus not found"}), 404

# qr code

# Route to apply for a student bus pass

def connect_db():
    try:
        cnx = mysql.connector.connect(user='root', password='NewStrongPass123!', database='demose')
        return cnx
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Route to apply for a student bus pass (GET and POST methods)
@app.route('/apply_bus_pass', methods=['GET', 'POST'])
def apply_bus_pass():
    if 'enrollmentno' in session:
        student_id = session['enrollmentno']

        # Check if the student already has an active pass
        cnx = connect_db()
        if cnx:
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM bus_passes WHERE student_id = %s ORDER BY issued_on DESC LIMIT 1", (student_id,))
            existing_pass = cursor.fetchone()
            cursor.close()
            cnx.close()

            if existing_pass:
                # If there's an existing pass, inform the student that they can only have one pass
                return render_template('apply_bus_pass.html', error_message="You already have an active bus pass.")

        # If no existing pass is found, allow the student to apply for a new pass
        if request.method == 'POST':
            name = request.form.get('name')
            route = request.form.get('route')
            validity = request.form.get('validity')
            issued_on = datetime.now().strftime('%Y-%m-%d')
            
            cnx = connect_db()
            if cnx:
                cursor = cnx.cursor()
                cursor.execute("INSERT INTO bus_passes (student_id, name, route, validity, issued_on) VALUES (%s, %s, %s, %s, %s)",
                               (student_id, name, route, validity, issued_on))
                cnx.commit()
                cursor.close()
                cnx.close()
            
            return redirect('/view_bus_pass')  # Redirect to view bus pass page after applying
        return render_template('apply_bus_pass.html')  # If it's a GET request, show the form

    return redirect('/')  # Redirect to home page if no enrollment number in session


# Route to view active bus pass
@app.route('/view_bus_pass')
def view_bus_pass():
    if 'enrollmentno' in session:
        student_id = session['enrollmentno']
        cnx = connect_db()
        if cnx:
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM bus_passes WHERE student_id = %s ORDER BY issued_on DESC LIMIT 1", (student_id,))
            pass_data = cursor.fetchone()
            cursor.close()
            cnx.close()
            
            if pass_data:
                # Generate QR Code
                qr_data = f"Student ID: {pass_data[0]} | Name: {pass_data[2]} | Route: {pass_data[3]} | Validity: {pass_data[4]}  "
                qr = qrcode.make(qr_data)
                img_io = BytesIO()
                qr.save(img_io, 'PNG')
                img_io.seek(0)
                
                return send_file(img_io, mimetype='image/png')  # Send the QR code image as response
    return "No active pass found"  # If no pass data found

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


from flask import Flask, render_template, request

app = Flask(__name__)

patients = []
appointments = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    age = request.form['age']
    disease = request.form['disease']

    patients.append({
        'name': name,
        'age': age,
        'disease': disease
    })

    return render_template('index.html', message="Patient Registered Successfully!")

@app.route('/appointment', methods=['POST'])
def appointment():
    patient = request.form['patient']
    doctor = request.form['doctor']
    date = request.form['date']

    appointments.append({
        'patient': patient,
        'doctor': doctor,
        'date': date
    })

    return render_template('index.html', message="Appointment Booked Successfully!")

if __name__ == '__main__':
    app.run(debug=True)
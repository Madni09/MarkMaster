from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# MySQL Database configuration (change according to your MySQL setup)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://msearch:msearchpasswd@localhost/vidhyanagari'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for storing marks for five fixed subjects
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll_number = db.Column(db.String(20), unique=True, nullable=False)
    DAA = db.Column(db.Integer, nullable=False)
    ML = db.Column(db.Integer, nullable=False)
    SE = db.Column(db.Integer, nullable=False)
    CC = db.Column(db.Integer, nullable=False)
    NCS = db.Column(db.Integer, nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

# Route for the teacher to enter marks for five subjects
#It is thhe basic version of teacher page working conditon 😂😁
"""@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
    if request.method == 'POST':
        roll_number = request.form['roll_number']
        daa = request.form['DAA']
        ml = request.form['ML']
        se = request.form['SE']
        cc = request.form['CC']
        ncs = request.form['NCS']
        
        # Create a new student entry
        student = Student(roll_number=roll_number, DAA=daa, ML=ml, SE=se, CC=cc, NCS=ncs)
        db.session.add(student)
        db.session.commit()
        
        return redirect('/teacher')
    
    return render_template('teacher.html')"""

@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
    if request.method == 'POST':
        # If the form is submitted, add new marks for a student
        roll_number = request.form['roll_number']
        daa = request.form['DAA']
        ml = request.form['ML']
        se = request.form['SE']
        cc = request.form['CC']
        ncs = request.form['NCS']
        
        # Create a new student entry
        student = Student(roll_number=roll_number, DAA=daa, ML=ml, SE=se, CC=cc, NCS=ncs)
        db.session.add(student)
        db.session.commit()
        
        return redirect('/teacher')

    # Query all student records to display in the table
    students = Student.query.all()
    
    return render_template('teacher.html', students=students)

# Route to delete a specific student record by id
@app.route('/delete/<int:id>')
def delete(id):
    student_to_delete = Student.query.get_or_404(id)
    
    try:
        db.session.delete(student_to_delete)
        db.session.commit()
        return redirect('/teacher')
    except:
        return "There was a problem deleting the record."
    


# Route for students to check their marks
@app.route('/student', methods=['GET', 'POST'])
def student():
    student_data = None
    if request.method == 'POST':
        roll_number = request.form['roll_number']
        student_data = Student.query.filter_by(roll_number=roll_number).first()
    
    return render_template('student.html', student=student_data)

if __name__ == '__main__':
    app.run(debug=True)

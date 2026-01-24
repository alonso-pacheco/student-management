from flask import Blueprint, jsonify, request
from models.student_model import Student, db

students_bp = Blueprint('students', __name__)

@students_bp.route('/')
def home():
    return "Hello world"

# CRUD
# Get students
@students_bp.route('/students', methods=['GET'])
def list_students():
    students = Student.query.all()
    return jsonify([
        {'id': s.id, 'name': s.name, 'age': s.age, 'email': s.email}
        for s in students
    ])


# Get student by id
@students_bp.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify({
        'id': student.id,
        'name': student.name,
        'age': student.age,
        'email': student.email
        })


# Create student
@students_bp.route('/students', methods=['POST'])
def create_student():
    data = request.json
    new_student = Student(name=data['name'], age=data['age'], email=data['email'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Estudiante creado correctamente'}), 201


# Update student
@students_bp.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.json
    student.name = data.get('name', student.name)
    student.age = data.get('age', student.age)
    student.email = data.get('email', student.email)
    db.session.commit()
    return jsonify({'message': 'Estudiante actualizado correctamente'})


# Delete student
@students_bp.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Estudiante eliminado correctamente'})
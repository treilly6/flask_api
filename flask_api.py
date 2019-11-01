from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from json import dumps


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:545679@localhost/flask_api_db'
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
db = SQLAlchemy(app)
api = Api(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    address = db.Column(db.String(100))
    salary = db.Column(db.Integer)
    date_hired = db.Column(db.DateTime)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

class Employees_ID(Resource):
    def get(self):
        query = Employee.query.with_entities(Employee.id).all()
        response = [id for id, in query]
        return {"employee_ids": response}

class Employee_Names(Resource):
    def get(self):
        query = db.session.query(Employee).all()
        response = []
        for emp in query:
            response.append(str(emp))
        return {"employees":response}

class Employee_Record(Resource):
    def get(self):
        query = Employee.query.all()
        response = []
        for emp in query:
            emp_dict = {
                "id" : emp.id,
                "Name" : str(emp),
                "Address" : emp.address,
                "Salary": emp.salary,
                "Date_Hired" : str(emp.date_hired),
            }
            response.append(emp_dict)
        return {"data":response}

class Employee_Record_ID(Resource):
    def get(self, id):
        query = Employee.query.filter(Employee.id == id)
        response = []
        for emp in query:
            emp_dict = {
                "id" : emp.id,
                "Name" : str(emp),
                "Address" : emp.address,
                "Salary": emp.salary,
                "Date_Hired" : str(emp.date_hired),
            }
            response.append(emp_dict)
        return {"data":response}

class Salaries(Resource):
    def get(self):
        query = Employee.query.with_entities(Employee.salary).all()
        response = [salary for salary, in query]
        return {"salaries" : response}


@app.route('/')
def index():
    # add a template with some of the api documentation
    return "<h1>FLASK IS RUNNING</h1>"


# API ROUTES #
api.add_resource(Employees_ID,'/api/employees_id')
api.add_resource(Employee_Names,'/api/employee_names')
api.add_resource(Employee_Record,'/api/employee_records')
api.add_resource(Employee_Record_ID, '/api/employee_records/<int:id>')
api.add_resource(Salaries, '/api/salaries')

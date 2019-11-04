from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from json import dumps
import datetime


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

    def post(self):
        body = request.json

        # add validations to this data
        first_name = body['first_name'].capitalize()
        last_name = body['last_name'].capitalize()
        salary = int(body['salary'].replace(',',''))
        address = body['address']

        date_hired = body['date_hired']
        date_split = date_hired.split("/")
        date_hired = datetime.date(int(date_split[2]), int(date_split[0]), int(date_split[1]))

        new_employee = Employee(first_name = first_name, last_name = last_name, salary = salary, address = address, date_hired = date_hired)
        db.session.add(new_employee)
        db.session.commit()

        return jsonify({"success" : "Successfully created record"})

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
        return jsonify({"data":response})

    def delete(self, id):
        record = Employee.query.filter(Employee.id == id).first()
        if record == None:
            return jsonify({"error" : "ID did not match any record"})
        else:
            db.session.delete(record)
            db.session.commit()
            return jsonify({"success":"Successfully Deleted Record"})


    def put(self, id):
        record = Employee.query.filter(Employee.id == id).first()
        if record == None:
            return jsonify({"error" : "ID did not match any record"})
        else:
            try:
                body = request.json
                first_name = body['first_name']
                last_name = body['last_name']
                address = body['address']
                salary = body['salary']
                date_hired = body['date_hired']
            except:
                return jsonify({"error" : "Missing Inputs"})

            if first_name != '':
                record.first_name = first_name
            if last_name != '':
                record.last_name = last_name
            if address != '':
                record.address = address
            if salary != '':
                record.salary = salary
            if date_hired != '':
                record.date_hired = date_hired

            db.session.commit()
            return jsonify({"success" : "Record Successfully Updated"})

class Employee_Record_Name(Resource):
    def get(self, name):
        split_name = name.split("_")

        if len(split_name) < 2:
            return jsonify({"error":"No Record Matching Name"})

        first_name = split_name[0]
        last_name = split_name[1]
        record = Employee.query.filter(Employee.first_name == first_name, Employee.last_name == last_name).first()

        if not record:
            return jsonify({"error" : "No Record Matching Name 2"})

        response = []
        employee_dict = {
            "id" : record.id,
            "Name" : str(record),
            "Address" : record.address,
            "Salary": record.salary,
            "Date_Hired" : str(record.date_hired),
        }
        response.append(employee_dict)
        return {"data":response}

    def delete(self, name):
        split_name = name.split("_")

        if len(split_name) < 2:
            return jsonify({"error":"No Record Matching Name"})

        first_name = split_name[0]
        last_name = split_name[1]
        record = Employee.query.filter(Employee.first_name == first_name, Employee.last_name == last_name).first()

        if record == None:
            return jsonify({"error" : "Name did not match any record"})
        else:
            db.session.delete(record)
            db.session.commit()
            return jsonify({"success":"Successfully Deleted Record"})



class Salaries(Resource):
    def get(self):
        query = Employee.query.with_entities(Employee.salary).all()
        response = [salary for salary, in query]
        return {"salaries" : response}

class Addresses(Resource):
    def get(self):
        query = Employee.query.with_entities(Employee.address).all()
        response = [address for address, in query]
        return {"addresses" : response}


@app.route('/')
def index():
    return render_template('index.html')



# API ROUTES #
api.add_resource(Employees_ID,'/api/employees_id')
api.add_resource(Employee_Names,'/api/employee_names')
api.add_resource(Employee_Record,'/api/employee_records')
api.add_resource(Employee_Record_ID, '/api/employee_records/<int:id>')
api.add_resource(Employee_Record_Name, '/api/employee_records/<string:name>')
api.add_resource(Salaries, '/api/salaries')
api.add_resource(Addresses, '/api/addresses')

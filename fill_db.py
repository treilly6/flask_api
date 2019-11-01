from flask_api import db, Employee
import random
import datetime


streets_list = [
    "North St", "South St", "East St", "West St", "1st Ave", "2nd Ave", "3rd Ave", "4th Ave", "5th Ave",
    "Albano Circle","St David's Quadrant","Bromyard Crescent","Osmond Close","Post Office Nook","Burnham Side",
    "Celandine Ridings","St Margaret's Buildings","Centenary Knoll","Wingate Esplanade","The Old Coal Yard",
    "Hinton Dale","Markham Lawns","Jesmond Top","Stocks Hill","Borough Pines","Sandy Fairway","Collins Hey","Allenfields",
    "Henley Grove","Collins Wood","Stretton Fairway","North Farm","Sheene Road","Netherton Green","Ripley Brook","Burleigh Croft",
    "Timberly Close","Paradise Village","Lambourne Firs","Burgh Mill Gardens","Broadoaks Court","Mount Bank","Tamar Lawn","Alice Leas",
    "Andrews Town","Prince's Glen","Preston Dale","Levernside Road","Coombe Heath","Kennedy Nook",
]

first_names_list = [
    "Janis","Shondra","Rolf","Marguerita","Myrtie","Shelley","Gina","Bill","Glynda","Lavonda","Camelia","Joaquin",
    "Keesha","Laurena","Catalina","Mariko","Eboni","Anne","Cheryl","Maire","Thuy","Tawna","Marin","Nickolas","Gertrude",
    "Roseann","Sacha","Magdalene","Idell","Iliana","Gilma","Vannesa","Ellen","Slyvia","Victoria","Mana","Joe","Kylie",
    "Gwyn","Aline","Aldo","Anika","Ardith","Tinisha","Larry","Phillip","Ma","Cameron","Hong","Idella"
]

last_names_list = [
    "Rodgers","Ryan","Sanchez","Compton","Newman","Trevino","David","Gallagher","Bird","Hinton","Brandt",
    "Moreno","Robbins","Collins","Matthews","Sparks","Aguilar","Dorsey","Davidson","Russell","Gates","Gibson",
    "Bradley","Bentley","Leonard","Little","Galloway","Hardin","Fischer","Thomas","Gordon","Fletcher","Goodwin",
    "Carroll","Kennedy","Rios","Mosley","Cole","Ho","King","Glenn","Rodriguez","Spencer","Crosby","Conrad","Nichols",
    "Carrillo","Schaefer","Rangel","Ochoa",
]

def make_random_date():
    random_year = random.randint(1995,2019)
    random_month = random.randint(1,12)
    months_30 = {4,6,9,11}
    months_31 = {1,3,5,7,8,10,12}
    if random_month == 2:
        random_day = random.randint(1,28)
    elif random_month in months_30:
        random_day = random.randint(1,30)
    elif random_month in months_31:
        random_day = random.randint(1,31)

    return datetime.date(random_year, random_month, random_day)

for _ in range(100):

    street_number = random.randint(1,300)
    street = streets_list[random.randint(0, len(streets_list) - 1)]
    address = str(street_number) + " " + street

    first_name = first_names_list[random.randint(0, len(first_names_list) - 1)]
    last_name = last_names_list[random.randint(0, len(last_names_list) - 1)]

    salary = random.randrange(40000, 215000, 500)

    date_hired = make_random_date()

    print(f"{first_name} {last_name}, {address} {salary} {date_hired}")

    employee = Employee(first_name = first_name, last_name = last_name, address = address, salary = salary, date_hired = date_hired)
    db.session.add(employee)

db.session.commit()

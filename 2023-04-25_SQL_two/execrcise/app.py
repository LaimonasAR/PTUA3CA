from main import Employee
from session import session


def enter_new():
    name = input("Enter name ")
    surname = input("Enter surname ")
    birthday = input("Enter birthday ")
    position = input("Enter position ")
    salary = input("Enter salary ")

    employee = Employee(
        name=name, surname=surname, birthday=birthday, position=position, salary=salary
    )
    session.add(employee)
    session.commit()


def list_all():
    all_employees = session.query(Employee).all()
    for one in all_employees:
        print(one)


# def update_one():
#     empl_id = 1
#     nameee = "name"
#     chosen_id = session.query(Employee).get(empl_id)
#     chosen_id.name = input("Enter desired value")
#     session.commit()
def update_one():
    empl_id = 1
    chosen_id = session.query(Employee).get(empl_id)
    chosen_id.name = (input("Enter desired value"))
    session.commit()


update_one()
# list_all()

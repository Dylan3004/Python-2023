import random
import random as rd


class Employer:
    name = None
    firstname = None
    workstatus = None
    employeespead = None
    coordspead = None
    temledspead = None
    first_responder = None

    # initializing of employer

    def __init__(self, name, firstname, workstatus, first_responder):
        self.name = name
        self.firstname = firstname
        self.first_responder = first_responder
        self.workstatus = workstatus
        if workstatus != "Employee" and workstatus != "Team Leader" and workstatus != "Coordinator":
            raise Exception("Unknown workstatus for employer")
        else:
            self.workstatus_creator(self.workstatus)

    # Function that generate speed of worker by workstatus
    def workstatus_creator(self, workstatus):
        if workstatus == "Employee":
            self.employeespead = random.randint(2, 5)
            print("Speed of employer", self.employeespead)
        if workstatus == "Coordinator":
            self.coordspead = random.uniform(1.2, 1.4)
        if workstatus == "Team Leader":
            self.temledspead = random.uniform(1.15, 1.3)

    # make a function which returns everything about the employer by print
    def get_employer(self):
        print("Name: " + self.name)
        print("Firstname: " + self.firstname)
        print("Workstatus: " + self.workstatus)
        print("First Responder: " + str(self.first_responder))
        if self.workstatus == "Employee":
            print("Employee spead :", self.employeespead)
        elif self.workstatus == "Coordinator":
            print("Coordinator pressure :", self.coordspead)
        elif self.workstatus == "Team Leader":
            print("Team Leader pressure :", self.temledspead)

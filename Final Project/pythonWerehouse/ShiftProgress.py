import time


class ShiftProgress:
    EmployersArray = None

    def __init__(self, OrdersArray, EmployersArray):
        self.OrdersArray = OrdersArray
        self.EmployersArray = EmployersArray

    # Function count a speed of orders
    def ProgressProgress(self):
        OrdersSpeed = 0
        SupervisorPressure = 1
        slower = 1
        OrdersSpeed = self.EmployeeNumber() * self.CoordinatorNumber() * self.TeamLeaderNumber()
        # print("Order Speed: " + str(OrdersSpeed))
        # it is in orders per minute
        if OrdersSpeed == 0:
            return 0
        OrdersProgress = OrdersSpeed
        return OrdersProgress/100

    # TO DO - make a process slower than it actually is
    def SlowerProgress(self):
        return None

    def check_nested(self, lst):
        for item in lst:
            if not isinstance(item, dict):
                print("aaa")
                return False
        return True

    # Function that shows percentage of Order that has been done
    def ProgressStatus(self):
        OrdersProgress = self.ProgressProgress()
        if not self.check_nested(self.OrdersArray):
            print("aaa")
            for element in self.OrdersArray:
                time.sleep(OrdersProgress)
                print("Order Completed " + str(element), self.OrdersArray[element])
                print("Progress: " + str(((element + 1) / len(self.OrdersArray) * 100) // 1) + "%")
        else:
            print("aaa")
            for element in self.OrdersArray:
                print("Executing Order number", element)
                for key, value in element.items():
                    time.sleep(OrdersProgress)
                    print("Order Completed " + str(key), value)
                    print("Progress: " + str(((key + 1) / len(element) * 100) // 1) + "%")

    # Function that counts how many employees are working on shift
    def EmployeeNumber(self):
        out = 0
        employerTotalspeed = 0
        for i in range(len(self.EmployersArray)):
            if self.EmployersArray[i].employeespead is not None:
                out += 1
                employerTotalspeed += self.EmployersArray[i].employeespead
        return employerTotalspeed
    # Function that counts how many coordinators are working on shift
    def CoordinatorNumber(self):
        out = 0
        coordinatorPressure = 1
        for i in range(len(self.EmployersArray)):
            if self.EmployersArray[i].workstatus == "Coordinator":
                out += 1
                coordinatorPressure *= self.EmployersArray[i].coordspead
        return coordinatorPressure
    # Function that counts how many team leaders are working on shift
    def TeamLeaderNumber(self):
        out = 0
        teamledPressure = 1
        for i in range(len(self.EmployersArray)):
            if self.EmployersArray[i].workstatus == "Team Leader":
                out += 1
                teamledPressure *= self.EmployersArray[i].temledspead
        return teamledPressure

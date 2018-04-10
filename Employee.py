class Employee:
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 40

    def printNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)

class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 45

    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()

employee = Employee()
employee.setNumberOfWorkingHours()
print("Number of employee working hours",end=' ')
employee.printNumberOfWorkingHours()

trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Number of trainee working hours",end=' ')
trainee.printNumberOfWorkingHours()
trainee.resetNumberOfWorkingHours()
print("Number of trainee working hours after call to super ",end=' ')
trainee.printNumberOfWorkingHours()

print('End of file')

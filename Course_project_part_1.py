

def employeename():
    empname = input("Enter employee name: ")
    return empname

def grosstaxnet(totalhours, hourlyrate, taxrate):
    gross = totalhours*hourlyrate
    income = gross*taxrate
    net = gross - income
    print(gross, income, net)

def printing(empname, hours, hourlyrate, gross, taxrate, income, net):
    print("Name: ", empname)
    print("Hours worked: ",f"{hours:..2f}")
    print("Hourly rate:", hourlyrate)
    print("Gross pay: ", gross)
    print("Tax rate: ", taxrate)
    print("Income pay: ", income)
    print("Net pay: ", net)

def otherprinting(totalemp, totalhours, totalgrosspay, totaltax, totalnetpay):
    print(f"Total number of employees: {totalemp}")
    print(f"Total number of hours worked: {totalhours:..2f}")
    print(f"Total gross pay: {totalgrosspay:..2f}")
    print(f"Total tax: {totaltax:..2f}")
    print(f"Total netpay: {totalnetpay:..2f")

if __name__ == "__main__":
    totalemp = 0
    totalhours = 0.0
    totalgrosspay = 0.0
    totaltax = 0.0
    totalnetpay = 0.0
    while true:
        empname = employeename()
        if (empname.upper() == "END"):
            break




def employeename():
    empname = input("Enter employee name: ")
    return empname

def hours():
    totalhours = float(input("Enter toal hours worked: "))
    return totalhours

def rate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate

def incometaxrate():
    income = float(input("Enter Income tax rate: "))
    return income

def grosstaxnet(totalhours, hourlyrate, taxrate):
    gross = totalhours*hourlyrate
    income = gross*taxrate
    net = gross - income
    return gross, income, net

def printing(empname, hours, hourlyrate, gross, taxrate, income, net):
    print("Name: ", empname)
    print("Hours worked: ",f"{hours:..2f}")
    print("Hourly rate: f{hourlyrate:..2f}")
    print("Gross pay: f{gross:..2f}")
    print("Tax rate: f{taxrate:..0%}")
    print("Income pay: f{income:..2f}")
    print("Net pay: f{net:..2f}")

def otherprinting(totalemp, totalhours, totalgrosspay, totaltax, totalnetpay):
    print(f"Total number of employees: {totalemp}")
    print(f"Total number of hours worked: {totalhours:..2f}")
    print(f"Total gross pay: {totalgrosspay:..2f}")
    print(f"Total tax: {totaltax:..2f}")
    print(f"Total netpay: {totalnetpay:..2f}")

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
        totalhours = hours()
        hourlyrate = rate()
        taxrate = incometaxrate()
        gross, income, totalnetpay = grosstaxnet(totalhours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, gross, taxrate, income, netpay)
        totalemp += 1
        totalhours += hours
        print(totalemp,totalhours, gross, totaltax, totalnetpay)
    print()
print("END")







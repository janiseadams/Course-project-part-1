

def GetEmpName():
    empname = input("Enter Employee name: ")
    return empname

def hoursworked():
    totalhours = float(input("Enter Total hours worked: "))
    return totalhours

def getrate():
    hourlyrate = float(input("Enter Hourly rate: "))
    return hourlyrate

def incometaxrate():
    incometax = float(input("Enter Income tax rate: "))
    return incometax

def gettaxandnet(totalhours, hourlyrate, taxrate):
    grosspay = totalhours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, totalhours, hourlyrate, grosspay, taxrate, incometax, netpay):
    print("Name:  ", empname) 
    print("Hours Worked: {:.2f}".format(totalhours))
    print("Hourly rate: {:.2f}".format(hourlyrate))
    print("Total Gross Pay: {:.2f}".format(grosspay))
    print("Total Tax Rate: {:.0%}".format(taxrate))
    print("Income Tax Rate : {:.2f}".format(incometax))
    print("Total Net Pay: {:.2f}".format(netpay))
    print()

def PrintTotals(empname, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print("Total Number Of Employees: {TotEmployees}")
    print("Total Hours Worked: {:.2f}".format(TotHours))
    print("Total Gross Pay: {:.2f}".format(TotGrossPay))
    print("Total Income Tax Rate: {:.0%}".format(TotTax))
    print("Total Net Pay: {:.2f}".format(TotNetPay))


if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        totalhours = hoursworked()
        hourlyrate = getrate()
        taxrate = incometaxrate()
        grosspay, incometax, netpay = gettaxandnet(totalhours, hourlyrate, taxrate)
        printinfo(empname, totalhours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        totalhours += totalhours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
print("Goodbye!")

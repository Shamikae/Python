from tabulate import tabulate

table = []

E = 1
while E <= 5:
    E += 1

    print("Welcome to ACME Corporation!\n")
    name = (input("Enter your name: \n"))
    wage = float(input("How much do you make per hour?\n"))
    hours = float(input("How many hours for the week?\n"))
    FedTaxRate = float(input("Enter Federal tax withholding rate: "))
    StateTaxRate = float(input("Enter State tax witholding rate: "))
    FRate = float(input("Enter FICA rate: "))

    def payroll_app(amount):
        if amount >= 0:
            return '${:,.2f}'.format(amount)
        else:
            return '-${:,.2f}'.format(-amount)
    if hours <= 40:
        weekincome = wage*hours
        monthincome = weekincome*4
        FedTax = weekincome*FedTaxRate/100
        StateTax = weekincome*StateTaxRate/100
        FicaRate = weekincome*FRate/100
        NetPay = weekincome - FicaRate - StateTax - FedTax
        NOT = 0
        print("Hi, {} \nIt has been calculated that if you work {} hours at a rate of {}, your Gross Pay should be a total of {}/week ({}/month) Federal Tax: {} State Tax: {} FICA Rate: {} Net Pay: {}/week".format(str(name),int(round(hours)),payroll_app(wage),payroll_app(weekincome),payroll_app(monthincome),payroll_app(FedTax),payroll_app(StateTax),payroll_app(FicaRate),payroll_app(NetPay)))

        table.append([name,hours,wage,weekincome,NOT,FedTax,StateTax,FicaRate,NetPay])
        headers = ["Name", "Hours", "Rate", "Gross Pay","OT Pay", "Fed Tax", "State Tax", "FICA", "Net Pay"]
        print(tabulate(table, headers, tablefmt="fancy_grid"))

    else:
        regularpay = wage*40
        overtimehours = hours - 40
        overtimerate = wage*1.5
        overtimeincome = (overtimehours * overtimerate)
        print("Hi, {} \nRegular pay: {}/wk + your overtime rate of {}/hr".format(str(name),payroll_app(regularpay),payroll_app(overtimerate)))
        print("Hours of overtime: {}".format(int(round(overtimehours))))
        print("Total overtime income: {}".format(payroll_app(overtimeincome)))
        weekincome = (40*wage) + overtimeincome
        FedTax = weekincome*FedTaxRate/100
        StateTax = weekincome*StateTaxRate/100
        FicaRate = weekincome*FRate/100
        NetPay = weekincome - FicaRate - StateTax - FedTax
        #if worked overtime every week
        monthincome = weekincome*4
        overtimeonce = weekincome + (regularpay*3)
        print("It has been calculated that your Gross Pay should be a total of {}/week with overtime ({}/month) if worked {} hours every week. Federal Tax: {} State Tax: {} FICA Rate: {} Net Pay: {}/week ".format(payroll_app(weekincome),payroll_app(monthincome),int(round(hours)),payroll_app(FedTax),payroll_app(StateTax),payroll_app(FicaRate),payroll_app(NetPay)))

        table.append([name,hours,wage,weekincome,overtimerate,FedTax,StateTax,FicaRate,NetPay])
        headers = ["Name", "Hours", "Rate", "Gross Pay", "OT Pay", "Fed Tax", "State Tax", "FICA", "Net Pay"]
        print(tabulate(table, headers, tablefmt="fancy_grid"))
print(payroll_app)
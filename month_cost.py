

def main():
    month = 12

    while True:
        try:
            gas = float(input('What is your monthly cost of gas for your automobile?: '))
        except ValueError:
            print('Error!, Invalid input')
            continue
        gas_cost = '${:,.2f}'.format(gas)
        annual_gas = '${:,.2f}'.format(gas * month)
        break
        
    while True:
        try:
            loan = float(input('What is your monthly cost of loan payment for your automobile?: '))
        except ValueError:
            print('Error!, Invalid input')
            continue
        loan_cost = '${:,.2f}'.format(loan)
        annual_loan = '${:,.2f}'.format(loan * month)
        break
        
    while True:
        try:
            ins = float(input('What is your monthly cost of insurance for your automobile?: '))
        except ValueError:
            print('Error!, Invalid input')
            continue
        ins_cost = '${:,.2f}'.format(ins)
        annual_ins = '${:,.2f}'.format(ins * month)
        break

    while True:
        try:
            maint = float(input('What is your maintenance cost of gas for your automobile?: '))
        except ValueError:
            print('Error!, Invalid input')
            continue
        maint_cost = '${:,.2f}'.format(maint)
        annual_maint = '${:,.2f}'.format(maint * month)
        break

    print('Your total monthly cost of gas is ' + str(gas_cost) + ' while your annual gas cost is ' + str(annual_gas))
    print('Your total monthly cost of loan is ' + str(loan_cost) + ' while your annual gas cost is ' + str(annual_loan))
    print('Your total monthly cost of ins is ' + str(ins_cost) + ' while your annual gas cost is ' + str(annual_ins))
    print('Your total monthly cost of maint is ' + str(maint_cost) + ' while your annual gas cost is ' + str(annual_maint))


main()

    
def get_sales():
    monthly_sales = float(input("Enter the monthly sales: "))
    while monthly_sales < 0:
        monthly_sales = float(input("Re-enter the monthly sales: "))
    return monthly_sales

def get_advanced_pay():
    advanced_pay = float(input("Enter the amount of advanced pay: "))
    while advanced_pay < 0 or advanced_pay > 2000:
        advanced_pay = float(input("Re-enter the amount of advanced pay: "))
    return advanced_pay

def determine_commission_rate(sales):
    if sales < 10000:
        return 0.10
    elif sales <= 14999.99:
        return 0.12
    elif sales <= 17999.99:
        return 0.14
    elif sales <= 21999.99:
        return 0.16
    else:
        return 0.18

def show_Commission_and_Paycheck(sales, commission_rate, advanced_pay, paycheck_amount):
    print("|---------------PAY CHECK CALCULATION---------------|")
    print(f"Sales: ${sales:.2f}")
    print(f"Commission rate: {commission_rate*100}%")
    print(f"Advanced pay: ${advanced_pay:.2f}")
    print(f"Paycheck amount: ${paycheck_amount:.2f}")

    if paycheck_amount < 0:
        print("The salesperson must reimburse the company.")
    print("|--------------------------------------------------|")

def main():

    sales = get_sales()

    advanced_pay_amount = get_advanced_pay()

    commission_rate = determine_commission_rate(sales)

    commission_amount = sales * commission_rate

    paycheck_amount = commission_amount - advanced_pay_amount

    show_Commission_and_Paycheck(sales, commission_rate, advanced_pay_amount, paycheck_amount)

if __name__ == "__main__":
    main()
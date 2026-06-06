acc_balance=int(18000)
def withdraw(acc_balance):
    amt_debit=int(input("Enter the amount to withdraw:"))
    acc_balance=acc_balance-amt_debit
    print("Please collect the amount")
def Enquiry(acc_balance):
    print("your current balance is:",acc_balance)    
pin=5402
print("Hello User!")
pinuser=int(input("Please enter your pin:"))
if pin==pinuser:
    value=int(input("\n 1.withdraw \n 2.enquiry\n choose your option:"))
    match value:
        case 1: withdraw(acc_balance)
        case 2: Enquiry(acc_balance)
else:
    print("Invalid pin!")
print("Thank you for banking with us :)")

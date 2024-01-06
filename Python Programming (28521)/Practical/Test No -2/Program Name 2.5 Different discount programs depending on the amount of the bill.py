# Different discount programs depending on the amount of the bill
# input net amount
amt = int(input("Enter the Amount: "))
# calclate amount with discount
if(amt > 0):
    if amt<=5000:
        dis= amt*0.10

    elif amt<=15000:
        dis= amt*0.15

    elif amt<=25000:
        dis= 0.20* amt

    else:
        dis= 0.5* amt

    print("The discount Amount: ",dis)
    print("To be Paid by customer: ",amt-dis)

else:
    print("Sorry invalic Amount")

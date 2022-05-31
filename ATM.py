#Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5,
#and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges).
#For each successful withdrawal the bank charges 0.50 Rs.
#Calculate Pooja's account balance after an attempted transaction.

atm=input("Enter the balance of ATM")
n=input("Kindly enter the amount to withdraw")
n= int(n)
atm= float(atm)
if (n+0.5<=atm and n%5==0):
    print("You withdraw successfully", n)
    print("Current Balance of Account is",atm-n-0.5)
else:
    print("ATM machine will only accept the transaction if amount is a multiple of 5")
    print("Current Balance of Account is", atm)
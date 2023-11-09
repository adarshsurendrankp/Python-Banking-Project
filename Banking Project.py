username=["John","Tom","Elsa","Tina","Mini","Racheal","Sarah"]
accountnumber=['123456','789101','111213','141516','171819','202122','232425']
password=['JOHN@123','TOM@123','ELSA@123','TINA@123','MINI@123','RACHEAL@123','SARAH@123']
balance=[10000,12000,5000,7500,17000,25000,2000]

def start():
    print("1. Banking\n"
          "2. Exit")
    menu_selection = str(input())
    if menu_selection=="1":
        login()
    if menu_selection=="2":
        print("Thankyou\n" 'visit again')
        start()
    else:
        print("Select menu 1 or 2")
        start()
def stop():
    print("Thank You\n Visit Again")
def login():
   accountnumber=input("Enter your accountnumber:")
   password=input("Enter your password")
   if accountnumber  not in accountnumber:
       print("Accountnumber not found")
   else:
       global accountindex
       accountindex=accountnumber.index(accountnumber)
       if password[accountindex]==password:
          print("Successfully login")
          services()
       else:
          print("Incorrect password\n" 'Try again')

def services():
    print('''1.Deposit Money
    2.Withdraw money
    3.Check Account balance''')

    serv=int(input("Enter your choices:"))

    if serv == 1:
      deposit = DepositMoney()
    elif serv == 2:
      withdraw = Withdrawmoney()
    elif serv == 3:
     balance = AccountBalance()
    else:
        print("Invalid Choice")

def DepositMoney():
    global money_deposit
    moneydeposit=int(input("Enter amount to be deposited"))
    if moneydeposit >0:
        balance[accountindex]+=moneydeposit
        print("Transaction completed" )
        start()

    else:
        print("Invalid amount transaction aborted")
        print('''1.Services
        2.Exit''')
        S=int(input("enter the choice:"))
        if S==1:
            services()
        elif S==2:
            stop()
        else:
            print("Invalid choice")
            stop()
def Withdrawmoney():
    global moneywithdraw
    moneywithdraw=int(input("Enter the amount"))
    if moneywithdraw >=balance[accountindex]:
        print("Insufficient funds")
        start()
        S = int(input("enter the choice:"))
        if S == 1:
            services()
        elif S == 2:
            stop()
        else:
            print("Invalid choice")
            stop()
    else:
        balance[accountindex]-=moneywithdraw
        print("Withdraw successfull")

def AccountBalance():
    y=balance[accountindex]
    print("Your Account Balance is:" 'Rs',y,)
    S=int(input("enter the choice:"))
    if S==1:
     services()
    elif S==2:
     stop()
    else:
     print("Invalid choice")
     stop()



start()
login()




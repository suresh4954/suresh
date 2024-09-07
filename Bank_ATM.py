def AccountInfo():
    if acno!=" ":
        print("Account Number       : ",acno)
        print("Account Holder Name  : ",acname)
        print("Pin                  : ",pin)
        wait=input("Press Enter Key to Continue.....")
    else:
        print("Account Not Found ")
        wait=input("Press Enter Key to Continue.....")
    

def BalanceInfo():
    if acno!=" ":
        print("Balance Amount : ",balance)
        wait=input("Press Enter Key to Continue.....")
    else:
        print("Account Details Not Found, Create Account ")
        wait=input("Press Enter Key to Continue.....")
    
def Deposit():
    if acno!=" ":
        tpin=input("Enter Pin : ")
        if pin==tpin:
            amount=int(input("Enter Deposit Amount : "))
            if amount<=0:
                print("Amount must be greater than zero(o)")
                wait=input("Press Enter Key to Continue.....")
                return 0
            else:
                return amount
        
        else:
            print("Invalid Pin Number ")
            wait=input("Press Enter Key to Continue.....")
            return 0
            
    else:
        print("Account Details Not Found, Create Account ")
        wait=input("Press Enter Key to Continue.....")
        return 0
    
def Withdraw():
    if acno!=" ":
        tpin=input("Enter Pin : ")
        if pin==tpin:
            amount=int(input("Enter Withdraw Amount : "))
            if amount<=0:
                print("Amount must be greater than zero(o)")
                wait=input("Press Enter Key to Continue.....")
                
                return 0
            elif (balance-amount)>=500:
                print("Transaction Successfull")
                wait=input("Press Enter Key to Continue.....")
                return amount
            else:
                print("Insufficient Balance Amount ")
                wait=input("Press Enter Key to Continue.....")
                return 0
        else:
            print("Invalid Pin Number ")
            wait=input("Press Enter Key to Continue.....")
            return 0
    else:
        print("Account Details Not Found, Create Account ")
        wait=input("Press Enter Key to Continue.....")
        return 0

    
    
#Main Program 
balance=0
acno=" "
acname=" "
pin=" "


Condition=True
while Condition:
    print("Welcome to Andhra Bank ")
    print("Kirlampudi")
    print("-----------------------------")
    print("Main Menu")
    print("---------")
    print("1. New Account ")
    print("2. Check Balance")
    print("3. A/c Informatoin ")
    print("4. Deposit")
    print("5. Withdraw ")
    print("6. Change Pin ")
    print("7. Exit")
    ch=int(input("Choose Your Option "))
    if ch==7:
        Condition=False
        print("Thanking You, Visit Again")
    elif ch==1:
        acno=input("Enter Account Number : ")
        acname=input("Enter Account Name : ")
        pin=input("Enter Pin ")
        balance=int(input("Enter Deposit Amount, Minimum Deposit Amount 500 : "))
        if balance<500:
            print("Account Creation Failed")
            acno=" "
            acname=" "
            pin=" "
            wait=input("Press Enter Key to Continue.....")
        else:
            print("Account Successfully Created ")
            wait=input("Press Enter Key to Continue.....")
    elif ch==3:
        AccountInfo()
    elif ch==2:
        BalanceInfo()
    elif ch==4:
        balance+=Deposit()
    elif ch==5:
        balance-=Withdraw()
    elif ch==6:
        if acno!=" ":
            tpin=input("Enter Current Pin  : ")
            if pin==tpin:
                pin=input("Enter New Pin Number : ")
        
            else:
                print("Invalid Pin Number ")
                wait=input("Press Enter Key to Continue.....")
        else:
            print("Account Details Not Found, Create Account ")
            wait=input("Press Enter Key to Continue.....")
        
        
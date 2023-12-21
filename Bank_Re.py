class Bank:
    def __init__(self,Account_Number,Account_holder_Name,Username,Password,Balance=0):
        self.Account_Number =Account_Number
        self.Account_holder_Name=Account_holder_Name
        self.Username=Username
        self.Password=Password
        self.Balance=Balance
    def login(self):
        Acc_num=int(input("Enter your account number :"))
        ent_Username=input("Enter the user name :")
        ent_Password=input("Enter your password :")
        if Acc_num==self.Account_Number and ent_Username==self.Username and ent_Password==self.Password:
            print(f"Welcome, {self.Account_holder_Name}")
            while True:
             print("Press '3' for check balance")
             print("Press '2' for deposit")
             print("Press '1' for withdrawal")
             print("Press '0' for exit")
             option = int(input("Enter your option :"))
             if option== 3:
                Account.balance_check()
             elif option ==2:
                Account.deposit()
             elif option==1:
                Account.withdrawal()
             elif option == 0:
                print("Exit")
                break
             else:
                print("Login failed. Retry")
    def balance_check(self):
        print(f"Your account balance is {self.Balance}")
    def deposit(self):
        amount=int(input("Enter the deposit amount :"))
        self.Balance+=amount
        print(f"Dear Customer, Rs.{amount} has credited to your account")
    def withdrawal (self):
        amount=int(input("Enter the amount:"))
        if self.Balance>=amount:
         print(f"Dear Customer,Rs,{amount} debited from your account.")
         self.Balance-=amount
        else:
            print("You have no sufficient balance in your account.Please check your balance.")
Account=Bank(Account_Number=55042381,Account_holder_Name="Nima",Username="Nima2021",Password="nima@123")
Account.login()



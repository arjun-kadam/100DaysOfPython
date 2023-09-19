from termcolor import colored

class ATM:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.set_pin()
        self.display_menu()
        
    def display_menu(self):
        print("1.Deposit Amount \n2.Withdraw Money \n3.Check Balance \n4.Reset Pin \n5.Exit")
        while(True):
            userInput=input("===>")
            if userInput=="1":
                self.deposit_amount()
                self.display_menu()
            elif userInput=="2":
                self.withdraw_money()
                self.display_menu()
            elif userInput=="3":
                self.check_bal()
                self.display_menu()
            elif userInput=="4":
                self.reset_pin()
                self.display_menu()
            elif userInput=="5":
                print("Thank You For Using Our ATM Services!!! Safe ForNever")
                break
            else:
                print(colored('Enter Correct Option','red'),"\n=====================")
                self.display_menu()
    

    def pin_checker(self):
        self.user_check_pin=input("Enter Your Pin\n")
        if self.pin==self.user_check_pin:
            return True
        
    
    def set_pin(self):
        self.user_pin=input("To Use ATM Services, First Set New 4 Digit Pin \nEnter Your Pin ===>")
        self.pin=self.user_pin
        print(colored('Pin Set Successfully!!! ','green'),"\n====================")
    

    def deposit_amount(self):
        if self.pin_checker()==True:
            self.user_amount=int(input("Enter Amount To Deposit===>"))
            self.balance=self.user_amount
            print(colored(self.user_amount,'blue'),colored('Deposit Successful','green'),"\n=====================")
        else:
            print(colored('Enter Correct Pin !!!','red'),"\n=====================")
        

    def withdraw_money(self):
        if self.pin_checker()==True:
            self.with_amt=int(input("Enter Amount For Withdraw===>"))
            if self.with_amt==self.balance:
                self.balance=self.balance-self.with_amt
                print(colored(self.with_amt,'red'),colored("Withdraw Successful","green"),"\n=====================")
            else:
                print(colored('Insufficient Balance !!!','red'),"\n=====================")
        else:
            print(colored('Enter Correct Pin !!!','red'),"\n=====================")
        

    def check_bal(self):
        if self.pin_checker()==True:
            print(colored(self.balance,'blue'), colored('Rs Only','green'),"\n=====================")
        else:
             print(colored('Enter Correct Pin !!!','red'),"\n=====================")
        
    

    def reset_pin(self):
        if self.pin_checker()==True:
            self.new_pin=input("Enter New Pin===>")
            self.pin=self.new_pin
            print(colored("New Pin Reset Successful.",'green'),"\n=====================")
        else:
            print(colored('Incorrect Old Pin !!!','red'),"\n=====================")
        


ppm=ATM()
class Bank:

    BANK_NAME = "Indian Overseas Bank"
    BRANCH = "Sivagangai"
    IFSC_CODE = "IOBA00528"

    def __init__(self,name,acc_no,pin,balance):
        self.name = name
        self.__acc_no = acc_no
        self.__pin = pin
        self.__balance = balance
        self.__last_transactions = []

    def __authenticate(self):
        try:
            user = int(input(f"Enter Account Number : "))
            password = int(input(f"Enter Pin : "))
            return self.__acc_no == user and self.__pin == password
        except ValueError:
            print("Enter Numbers only !!")
            return False
    
    def __deposit_money(self,amount):
        self.__balance += amount
        print(f"Amount deposited succesfully")
        print(f"Current balance : {self.__balance}")

    def __withdraw_money(self,amount):
        self.__balance -= amount
        print(f"Amount withdrawal successfully")
        print(f"Current balance : {self.__balance}")

    def __transaction_details(self,transaction_type,amount):
        self.__last_transactions.append(f"Transaction type: {transaction_type}\n"
                                        f"Amount          : {amount}\n"
                                        f"---------------------------")

    def login(self):
        if self.__authenticate():
            return True
        return False

    def deposit(self):
        while True:
            try:
                amount = int(input("Enter Amount : "))
                break
            except ValueError:
                print("Enter numbers only")

        if amount > 0 :
            self.__deposit_money(amount)
            self.__transaction_details("Deposit",amount)
        else:
            print(f"Enter valid amount")

    def withdraw(self):
        while True:
            try:
                amount = int(input("Enter amount : "))
                break
            except ValueError:
                print("Enter numbers only")

        if amount <= 0 :
            print(f"Enter valid amount")
        elif amount > self.__balance:
            print(f"Insufficient balance")
        else:
            self.__withdraw_money(amount)
            self.__transaction_details("Withdrawal",amount)

    def show_balance(self):
        print(f"Account balance : {self.__balance}")
        
    def show_details(self):
        
        print(f"----- Account holder details -----\n"
              f"Bank name           : {Bank.BANK_NAME}\n" 
              f"Branch              : {Bank.BRANCH}\n"
              f"IFSC code           : {Bank.IFSC_CODE}\n" 
              f"Account holder name : {self.name}\n"
              f"Account number      : {self.__acc_no}\n"
              f"Account balance     : {self.__balance} ")

    def show_transactions(self):
        print(f"Transaction details :-\n----------------------")
        if not self.__last_transactions:
            print("No transactions")
        else:
            for i in self.__last_transactions:
                print(i)
    
user1 = Bank("Abi",24,12,1000)

run_login = True
run_transaction = False

while run_login:
    print(f"1. Login\n"
          f"2. Exit")
    try:
        user_option = int(input("Choose option : "))
    except ValueError:
        print("Enter numbers only")
        continue
    if user_option == 1 :
        if user1.login() :
            run_login = False
            run_transaction = True
        else:
            print(f"Enter valid details")
    elif user_option == 2 :
        print(f"Thankyou for visiting")
        break
    else:
        print("Enter valid option")

while run_transaction:
    print(f"{'----- Welcome to IOB bank !!! -----':<20} \n {'1. Deposit amount':<20}\n {'2. Withdraw amount':<20}\n {'3. Check balance':<20}\n {'4. View transaction details':<20}\n {'5. View account details':<20}\n {'6. Exit':<20}\n")
    try:
        user_input = int(input("Choose option : "))
    except ValueError:
        print("Enter numbers only")
        continue

    if user_input == 1:
            user1.deposit()
    elif user_input == 2:
            user1.withdraw()
    elif user_input == 3:
        user1.show_balance()
    elif user_input == 4:
        user1.show_transactions()
    elif user_input == 5:
        user1.show_details()
    elif user_input == 6:
        print(f"Thankyou for using IOB bank , Visit again !!")
        run_transaction = False
    else:
        print(f"Enter valid option")
    

    





            


        
        
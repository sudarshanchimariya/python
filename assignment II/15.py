class Customer:
    def __init__(self, full_name, mobile_number, email_address, account_number, account_type, balance, ):
        self.full_name = full_name
        self.mobile_number = mobile_number
        self.email_address = email_address
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def amount_deposit(self):
        amount = float(input("Enter the amount you want to deposit: "))
        self.balance += amount
        print("\n Deposited Amount:", amount)
        print("\n New Balance=", self.balance)

    def amount_withdraw(self):
        amount = float(input("Enter the amount you want to withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n Withdrew Amount:", amount)
        else:
            print("\n Insufficient balance  ")
        print("\n New Balance=", self.balance)

    def customer_info(self):
        print("\n Name =", self.full_name, )
        print("Mobile : ", self.mobile_number, "\n Email : ", self.email_address)
        print("\n Account Number=", self.account_number, "\t\t Account Type : ", self.account_type)
        print("\n Total Balance=", self.balance)


customer_details = Customer('Sudarshan Chimariya', '9860746027', 'sudarshan@gmail.com', '0291360', 'Current', 5000)
print("SELECT -\n 1. To Deposit\n 2. To Withdraw \n 3.View Account Details")

select = int(input("Select 1 or 2 or 3:"))

if select == 1:
    customer_details.amount_deposit()
elif select == 2:
    customer_details.amount_withdraw()
elif select == 3:
    customer_details.customer_info()
else:
    print("Invalid input")
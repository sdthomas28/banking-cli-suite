class User: 
    def __init__(self, name, pin, password):
            self.name = name
            self.pin = pin
            self.password = password


    def change_name(self, name):
         self.name = name
         
    def change_pin(self, pin):
         self.pin = pin
         
    def change_password(self, password):
         self.password = password



class BankUser(User):
     def __init__(self, name, pin, password):
          super().__init__(name, pin, password)
          self.balance = 0

     def show_balance(self):
          print(f"{self.name} has an account balance of: ${self.balance:.2f}")
          print()

     def withdraw(self, amount): 
          if amount > self.balance: 
            print("Insufficient Funds")
          else:
               self.balance -= amount
               print(f"Withdrew: {amount:.2f}")

     def deposit(self, amount):
          self.balance += amount
          
     
     def transfer_money(self, user, amount, pin):
          print(f"You are transferring ${amount:.2f} to {user.name}")
          print("User authentication is required...")
          print()
     
          pin = input(f"Enter {self.name}'s PIN: ")
          if pin != self.pin:
               print("Invalid PIN. Transaction cancelled")
               return False
          if amount > self.balance:
               print("Insufficient funds. Transaction cancelled.")
               return False
          
          self.balance -= amount
          user.balance += amount
          
          print("Transfer Authorized")
          print(f"Transferring ${amount:.2f} to {user.name}")

          return True
          
     def request_money(self, user, amount, pin, password):
          print(f"You are requesting ${amount:.2f} from {user.name}")
          print("User authentication is required..")
          print()


          pin = input(f"Enter {user.name} PIN: ")
          if pin != user.pin:
            print("Invalid PIN. Transaction cancelled.")
            print()
            return False
          
          password = input(f"Enter your password: ")
          if password != self.password: 
                 print("Invalid password. Request cancelled.")
                 print()
                 return False
            
          print("Request Authorized.")

          user.balance -= amount
          self.balance += amount
          print(f"{user.name} sent ${amount}")
          print()
          return True
     



"""
Driver code for task 1
username = User("Bob","1234","bobpassword")
print(username.name, username.pin, username.password)
"""

"""
Driver Code for Task 2 
username = User("Bob","1234","bobpassword")
print(username.name, username.pin, username.password)
username.change_name("Bobby")
username.change_pin("8220")
username.change_password("bobbypassword")
print(username.name, username.pin, username.password)
"""

"""
Driver code for task 3
bankclient1 = BankUser("Bob","1234","bobpassword")
print(bankclient1.name, bankclient1.pin, bankclient1.password, bankclient1.balance)
"""

"""
Driver code for task 4
bankclient1 = BankUser("Bob","1234","bobpassword")
bankclient1.show_balance()
bankclient1.deposit(100)
bankclient1.show_balance()
bankclient1.withdraw(100)
bankclient1.show_balance()
"""


#Driver code for task 5
bankclient1 = BankUser("Bob","1234","bobpassword")
bankclient2 = BankUser("Steve", "4321","stevepassword")

bankclient2.deposit(5000)
bankclient2.show_balance() 
bankclient1.show_balance()

transfer_completed = bankclient2.transfer_money(bankclient1, 500, "4321")
bankclient2.show_balance()
bankclient1.show_balance()

if transfer_completed:
     print("Transfer Complete")
     print()
     bankclient2.request_money(bankclient1, 250, "1234", "stevepassword")
     bankclient2.show_balance()
     bankclient1.show_balance()





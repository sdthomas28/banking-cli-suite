# Bank User Management System
This project models a basic banking environment where users can be created, manage their profiles, and perform financial transactions. It was built as a learning exercise to solidify understanding of key software development concepts, including class design, inheritance, encapsulation, and method implementation.

The system features two main classes: a base User class for identity management and a derived BankUser class that handles all financial operations.

Key Features:
    User Account Management: Create users with a name, PIN, and password.

    Secure Profile Updates: Users can securely change their name, PIN, or password.

    Banking Operations:

        Check account balance.

        Deposit funds.

        Withdraw funds (with insufficient funds validation).

    Secure Transactions:

        Transfer Money: Send money to another user, requiring the sender's PIN for authentication.

        Request Money: Request money from another user, requiring the recipient's PIN and the requester's password for dual authentication.

    Input/Output Interface: A clear console-based interface for demonstrating all operations.

CODE STRUCTURE:
User Class

The base class representing a generic user.

    Attributes: name, pin, password.

    Methods:

        change_name(new_name)

        change_pin(new_pin)

        change_password(new_password)

BankUser Class (Inherits from User)

Extends the User class to include banking-specific functionality.

    Attribute: balance (initialized to 0).

    Methods:

        show_balance(): Displays the current balance.

        deposit(amount): Adds funds to the balance.

        withdraw(amount): Removes funds from the balance, with a check for sufficient funds.

        transfer_money(other_user, amount, pin): Transfers money to another user after PIN verification.

        request_money(other_user, amount, pin, password): Requests money from another user after dual authentication (their PIN and your password).

How to run the demo:
  Clone this repository.
  
  Navigate to the directory containing workshop4.py
  
  Run the scrip in your terminal as python workshop4.py or py workshop4.py

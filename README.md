# ATM Simulation in Python

## Project Description

This project is a simple **ATM Simulation System** made using Python.

The main purpose of this project is to understand the basic concepts of Python programming by creating a small ATM system. It allows a user to create an account, log in using an account number and PIN, and perform basic ATM operations.

This project is made for educational purposes and is suitable for a beginner-level Python project.

## Features

The ATM Simulation provides the following features:

1. Create a new account
2. Login using account number and PIN
3. Check account balance
4. Deposit money
5. Withdraw money
6. View mini statement
7. Change PIN
8. Logout
9. Exit the program

## Technologies Used

* Python
* Basic input and output
* Conditional statements
* While loops
* Variables

No external libraries are used in this project.

## Requirements

To run this project, you need:

* Python 3.x
* Any Python IDE such as:

  * IDLE
  * VS Code
  * PyCharm
  * Jupyter Notebook

## How to Run

1. Install Python 3 on your computer.
2. Open the Python file containing the ATM program.
3. Run the program.
4. Select an option from the ATM menu.
5. First create an account.
6. Login using the account number and PIN.
7. Use the available ATM services.

## Working of the Project

### 1. Create Account

The user enters:

* Name
* Account number
* 4 digit PIN

After entering the details, the account is created.

### 2. Login

The user enters the account number and PIN.

If the entered details are correct, the user gets access to the ATM services.

### 3. Check Balance

The user can check the current amount available in the account.

### 4. Deposit Money

The user enters an amount to deposit.

The amount is added to the current balance.

### 5. Withdraw Money

The user enters the amount they want to withdraw.

The program checks whether sufficient balance is available. If sufficient balance is present, the amount is deducted.

### 6. Mini Statement

The mini statement displays:

* Account holder name
* Account number
* Current balance
* Recent deposits
* Recent withdrawals

### 7. Change PIN

The user first enters the old PIN.

If the old PIN is correct, a new 4-digit PIN can be created.

### 8. Logout

The user can logout from the ATM services and return to the main menu.

## Python Concepts Used

This project uses basic Python concepts such as:

* Variables
* `input()`
* `print()`
* `if-else`
* `while` loop
* Comparison operators
* Arithmetic operators
* Basic string operations

## Example Menu

```text
================================
       WELCOME TO SIMPLE ATM
================================

----------- ATM MENU -----------
1. Create Account
2. Login
3. Exit
```

After login:

```text
-------- ATM SERVICES --------
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Mini Statement
5. Change PIN
6. Logout
```

## Limitations

This is a basic educational ATM simulation.

* It stores account information only while the program is running.
* It does not use a database.
* It does not save information permanently.
* It is not designed for real banking use.
* It supports a simple single-account simulation.

## Future Improvements

The project can be improved in the future by adding:

* Multiple user accounts
* Transaction history
* Database storage
* Money transfer between accounts
* Better PIN security
* Permanent data storage
* More detailed bank statements

## Conclusion

The ATM Simulation project demonstrates how basic Python programming concepts can be combined to create a useful application.

Through this project, basic concepts such as variables, conditions, loops, input/output, and arithmetic operations can be understood and applied in a practical way.
# ATM-simulation-

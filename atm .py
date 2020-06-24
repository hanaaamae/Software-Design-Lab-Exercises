"""
File: atm.py
This module defines the ATM class, which provides a window
for bank customers to perform deposits, withdrawals, and check
balances.
"""
import random
from bank import Bank, createBank
from breezypythongui import EasyFrame


class ATM(EasyFrame):
    """Represents an ATM window.
    The window tracks the bank and the current account.
    The current account is None at startup and logout.
    """

    def __init__(self, bank):
        """Initialize the frame and establish the data model."""
        EasyFrame.__init__(self, title = "ATM")
        # Create refernces to the data model.
        self.bank = bank
        self.account = None
        self.error = 0
        # Create and add the widgets to the window."""
        self.nameLabel = self.addLabel(row = 0, column = 0,
                                       text = "Name")
        self.pinLabel = self.addLabel(row = 1, column = 0,
                                      text = "PIN")
        self.amountLabel = self.addLabel(row = 2, column = 0,
                                         text = "Amount")
        self.statusLabel = self.addLabel(row = 3, column = 0,
                                         text = "Status")
        self.nameField = self.addTextField(row = 0, column = 1,
                                           text = "")
        self.pinField = self.addTextField(row = 1, column = 1,
                                          text = "")
        self.amountField = self.addFloatField(row = 2, column = 1,
                                              value = 0.0)
        self.statusField = self.addTextField(row = 3, column = 1,
                                             text = "Welcome to the Bank!",
                                             state = "readonly")
        self.balanceButton = self.addButton(row = 0, column = 2,
                                            text = "Balance",
                                            command = self.getBalance,
                                            state = "disabled")
        self.depositButton = self.addButton(row = 1, column = 2,
                                            text = "Deposit",
                                            command = self.deposit,
                                            state = "disabled")
        self.withdrawButton = self.addButton(row = 2, column = 2,
                                             text = "Withdraw",
                                             command = self.withdraw,
                                             state = "disabled")
        self.loginButton = self.addButton(row = 3, column = 2,
                                          text = "Login",
                                          command = self.login)
        
        
    def login(self):
        """Attempts to login the customer.  If successful,
        enables the buttons, including logout.""" 
        "Adding the security measures if log in fails 3 times, the cops will be called and lock the login button "
        while True:
            name = self.nameField.getText()
            pin = self.pinField.getText()
            self.account = self.bank.get(name, pin)
            if self.account:
                self.statusField.setText("Hello, " + name + "!")
                self.balanceButton["state"] = "normal"
                self.depositButton["state"] = "normal"
                self.withdrawButton["state"] = "normal"
                self.loginButton["text"] = "Logout"
                self.loginButton["command"] = self.logout
                return False

            elif(self.error >= 3):
                self.statusField.setText("The police are called!")
                self.loginButton["command"] = None
                return True
            
            elif(self.account==None):
                self.statusField.setText("Name and pin not found!!")
                self.error += 1
                print("Attempt no. " + str(self.error) + " is incorrect, try again")
                return True
    
    def logout(self):
        """Logs the cusomer out, clears the fields, disables the
        buttons, and enables login."""
        self.account = None
        self.nameField.setText("")
        self.pinField.setText("")
        self.amountField.setNumber(0.0)
        self.statusField.setText("Welcome to the Bank!")
        self.balanceButton["state"] = "disabled"
        self.depositButton["state"] = "disabled"
        self.withdrawButton["state"] = "disabled"
        self.loginButton["text"] = "Login"
        self.loginButton["command"] = self.login

    def getBalance(self):
        """Displays the current balance in the status field."""
        text = "Balance = $" + str(self.account.getBalance())
        self.statusField.setText(text)

    def deposit(self):
        """Attempts a deposit. If not successful, displays
        error message in statusfield; otherwise, announces
        success."""
        amount = self.amountField.getNumber()
        message = self.account.deposit(amount)
        if not message:
            self.statusField.setText("Deposit successful")
        else:
           self.statusField.setText(message)
        
    def withdraw(self):
        """Attempts a withdrawal. If not successful, displays
        error message in statusfield; otherwise, announces
        success."""
        amount = self.amountField.getNumber()
        message = self.account.withdraw(amount)
        if not message:
            self.statusField.setText("Withdrawal successful")
        else:
           self.statusField.setText(message)
        
def main(fileName = None):
    """Creates the bank with the optional file name,
    wraps the window around it, and opens the window.
    Saves the bank when the window closes."""
    if not fileName:
        bank = createBank(5)
    else:
        bank = Bank(fileName)
    print(bank)
    atm = ATM(bank)
    atm.mainloop()

if __name__ == "__main__":
    main()

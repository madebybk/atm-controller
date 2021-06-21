"""
This program is a simple ATM controller with the following flow:
Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw
"""

import time
import threading
import sys


class BankAPI:
    """Provides data from the bank API connected to the ATM."""
    __user_info = {  # Key: ID, Value: Password
        'sample_id': 1234,
    }
    balance_checking = 1000
    balance_savings = 5000

    def verify_password(self, entered_user_id, input_password):
        """Determines if the input PIN number matches."""
        if self.__user_info[entered_user_id] == input_password:
            return True


class CustomerBasicInfo:
    """Stores basic information (ID) of the user.

    In the future, a function to gather more information from user's card should be here.
    """
    user_id = None


def insert_card():
    """Simulates the card insertion process"""
    print("\nPlease insert card to begin transaction")
    time.sleep(1)
    print("\nProcessing...")
    threading.Event().wait(1)  # LOCK isn't held in wait() as opposed to sleep()
    # This following line should be changed to a card processing function once the bank API is integrated
    CustomerBasicInfo.user_id = "sample_id"
    return CustomerBasicInfo.user_id


def enter_pin(cs_info):
    """Asks user to input PIN number.

    Determines if the PIN is correct through verify_password().
    If the user enters a wrong PIN more than 3 times, program will terminate.
    Return True if the password is valid; return False if it isn't.
    """
    input_password = int(input("\nPlease enter your PIN: "))
    tries_count = 0
    # Given there are 3 PIN attemps total, obtain the user PIN input:
    while(tries_count < 2):
        if BankAPI().verify_password(cs_info, input_password) == True:
            # return input_password
            return True
        else:
            print("Incorrect PIN. Try again (" +
                  str(2-tries_count) + " attemp(s) remaining)")
            input_password = int(input("Please enter your PIN: "))
            tries_count += 1
    return False


def handle_wrong_PIN():
    """Exits the program if user misses all 3 PIN attempts."""
    print("\n\n\nTransaction failed. Inquire at your local bank.\n\n\n")
    time.sleep(2)
    terminate_transaction()


def select_account():
    """Asks user to select either Checking or Savings account.

    Asks the user to select a transaction action with the selected account
    through select_action(). The user has the option to exit the transaction,
    and terminate_transaction() function will be called to exit the program.
    """
    print("""
    Select Account:
    (1) Checking          (2) Savings          (3) [Finish Transaction]
    """
          )
    account_int = int(input("Please select account: "))
    if account_int == 3:
        terminate_transaction()
    elif account_int == 1:
        select_action('checking')
    elif account_int == 2:
        select_action('savings')
    else:
        print("Please enter valid option.")
        time.sleep(2)
        select_account()


def select_action(account):
    """Asks user to select a transaction action with their selected account.

    Prints out the current balance of selected account through see_balance().
    The user has the option to:
    1. See balance -> see_balance()
    2. Deposit Cash -> deposit()
    3. Withdraw Cash -> withdraw()
    4. Select a different account -> select_account()
    5. Cancel and exit transaction -> terminate_transaction()
    """
    print("""
    (1) See Balance    (2) Deposit    (3) Withdraw    (4) [Back to Select Account]    (5) [Finish Transaction]
    """)
    option = int(input("Please select your transaction: "))
    if option == 1:
        see_balance(account)
    elif option == 2:
        deposit(account)
    elif option == 3:
        withdraw(account)
    elif option == 4:
        select_account()
    elif option == 5:
        terminate_transaction()
    else:
        print("Please enter valid option.")
        time.sleep(2)
        select_action()


def see_balance(account):
    """Shows balance of selected account then asks to select transaction through select_action."""
    if account == 'checking':
        message = "\nYour balance is " + \
            "$" + str(BankAPI.balance_checking)
    elif account == 'savings':
        message = "\nYour balance is " + "$" + str(BankAPI.balance_savings)
    print(message)
    select_action(account)


def deposit(account):
    """Deposits cash into selected account then shows the updated balance."""
    print("""
    Please enter the amount (in USD) to deposit. Enter 0 to cancel the deposit.
    """)
    amount_deposit = int((input("\nAmount: ")))
    if amount_deposit == 0:
        # If input is 0, asks user to choose transaction action:
        print("\n\nTransaction cancelled")
        time.sleep(2)
        select_action(account)
    elif isinstance(amount_deposit, int) == False:
        # Try again if user input is invalid:
        print("\nPlease enter a valid amount")
        time.sleep(2)
        deposit(account)
    elif account == 'checking':
        BankAPI.balance_checking += amount_deposit
    elif account == 'savings':
        BankAPI.balance_savings += amount_deposit
    print("\nDepositing " + str(amount_deposit) + " ...")
    time.sleep(2)
    see_balance(account)


def withdraw(account):
    """Withdraws cash from selected account then shows the updated balance.

    If user requests to withdraw more than balance, send error message and ask
    user to choose transaction action again.
    """
    print("""
    Please enter the amount (in USD) to withdraw. Enter 0 to cancel the withdrawal.
    """)
    amount_withdraw = int((input("\nAmount: ")))
    if amount_withdraw == 0:
        # If input is 0, asks user to choose transaction action:
        print("\n\nTransaction cancelled.")
        time.sleep(2)
        select_action(account)
    elif isinstance(amount_withdraw, int) == False:
        # Try again if user input is invalid:
        print("\nPlease enter a valid amount.")
        time.sleep(2)
        withdraw(account)
    elif account == 'checking':
        if (BankAPI.balance_checking >= amount_withdraw):
            BankAPI.balance_checking -= amount_withdraw
        else:
            print("\nNot enough balance to complete the transaction.")
            print("Your current balance is $" + str(BankAPI.balance_checking))
            time.sleep(2)
            select_action(account)
    elif account == 'savings':
        if (BankAPI.balance_savings >= amount_withdraw):
            BankAPI.balance_savings -= amount_withdraw
        else:
            print("\nNot enough balance to complete the transaction.")
            print("Your current balance is $" + str(BankAPI.balance_savings))
            time.sleep(2)
            select_action(account)

    print("\nWithdrawing " + str(amount_withdraw) + " ...")
    time.sleep(2)
    see_balance(account)


def terminate_transaction():
    """Exits the program."""
    print("\nThank you. Have a great day.\n")
    sys.exit()


def atm_controller():
    """Main function for the program."""
    cs_info = insert_card()
    is_validated = enter_pin(cs_info)
    if is_validated == False:
        handle_wrong_PIN()
    account = select_account()
    select_action(account)


atm_controller()

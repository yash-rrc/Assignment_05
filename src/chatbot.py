"""
Description: Chatbot application.  Allows user to perform 
balance inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: {Student Name}
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:
def get_account():
    while True:    
        try:
            account_number = int(input("Please enter your account number: "))
            if account_number in ACCOUNTS:
                return account_number
            else:
                raise Exception("Account number entered does not exist.")
        except ValueError:
            raise ValueError("Account number must be a whole number.")

def get_amount() -> float:
    """
    gives output of the ebntered amount the usr enters 

    Returns:
        float: The entered amount

    Raises:
        ValueError: If the entered amount is not numeric it gives error 
    """
    while True:
        try:
            amount_string = input("Enter the transaction amount: ")

            try:
                amount = float(amount_string)
            except ValueError:
                raise ValueError("Invalid amount. Amount must be numeric.")

            if amount <= 0:
                raise ValueError("Invalid amount. Please enter a positive number.")

            return amount

        except ValueError as error:
            raise(error)

def get_balance(account: int) -> str:
    if account not in ACCOUNTS:
        raise Exception("Account number does not exist.")
    balance = ACCOUNTS[account]["balance"]
    return f'Your current balance for account {account} is ${balance:.2f}.'

def make_deposit(account: int, amount: float) -> str:
    """
    Deposits the specified amount

    Args:
        account (int): gets acc no. 
        amount (float): gets amount value

    Returns:
        str: prints succesful transaction message 

    Raises:
        Exception: is not in the 'ACCOUNTS'
        ValueError: is greater than 0 
    """
    if account not in ACCOUNTS:
        raise Exception("Account number does not exist.")

    if amount <= 0:
        raise ValueError("Invalid Amount. Amount must be positive.")

    ACCOUNTS[account]["balance"] += amount

    return f"You have made a deposit of ${amount:.2f} to account {account}."

def user_selection() -> str:
    VALID_TASKS = ["balance", "deposit", "exit"]
    
    while True:
        task = input("What would you like to do (balance/deposit/exit)? ").lower()

        if task in VALID_TASKS:
            return task
        else:
            raise ValueError("Invalid task. Please choose balance, deposit, or exit.")



## GIVEN CHATBOT FUNCTION
## REQUIRES REVISION
"""
def chatbot():
    '''
    The main program.  Uses the functionality of the functions:
        get_account()
        get_amount()
        get_balance()
        make_deposit()
        user_selection()
    '''

    print("Welcome! I'm the PiXELL River Financial Chatbot!  Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            ## CALL THE user_selection FUNCTION HERE 
            ## CAPTURING THE RESULTS IN A VARIABLE CALLED
            ## selection:


            if selection != "exit":
                
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        ## CALL THE get_account FUNCTION HERE
                        ## CAPTURING THE RESULTS IN A VARIABLE 
                        ## CALLED account:


                        valid_account = True
                    except Exception as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                        ## CALL THE get_balance FUNCTION HERE
                        ## PASSING THE account VARIABLE DEFINED 
                        ## ABOVE, AND PRINT THE RESULTS:

                else:

                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            ## CALL THE get_amount FUNCTION HERE
                            ## AND CAPTURE THE RESULTS IN A VARIABLE 
                            ## CALLED amount:


                            valid_amount = True
                        except Exception as e:
                            # Invalid amount.
                            print(e)
                    ## CALL THE make_deposit FUNCTION HERE PASSING THE 
                    ## VARIABLES account AND amount DEFINED ABOVE AND 
                    ## PRINT THE RESULTS:


            else:
                # User selected 'exit'
                keep_going = False
        except Exception as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")
"""
    
"""
if __name__ == "__main__":
    chatbot()
"""
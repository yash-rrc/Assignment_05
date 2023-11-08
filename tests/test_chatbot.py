"""
Description: creating tests for the chatbot 
Author:Yash 
Date:2023/11/08
Usage:it will verufy the excution of evry function written in the chtbot.py file
"""
import unittest
from unittest.mock import patch
from src.chatbot import get_account, VALID_TASKS, ACCOUNTS, get_amount,get_balance , make_deposit

class ChatbotTests(unittest.TestCase):
    def test_get_account(self):
        # Act
        with patch("builtins.input") as mock_input:
           mock_input.side_effect = ["123456"]
            
           account_number = get_account()
            # Assert
           self.assertEqual(account_number, 123456)
    
    def test_get_account_non_num(self):
        # Act
        with patch("builtins.input", side_effect=["non_numeric_data"]):
            with self.assertRaises(ValueError) as context:
                get_account()
            # Assert
            self.assertEqual(str(context.exception), "Account number must be a whole number.")

    def test_get_account_no(self):
        # Act
        with patch("builtins.input", side_effect=["112233"]):
            with self.assertRaises(Exception) as context:
                get_account()
            # Assert
            self.assertEqual(str(context.exception), "Account number entered does not exist.")
    
    def test_get_amount_for_valid(self):
        # Act
        with patch("builtins.input", side_effect=["500.01"]):
            result = get_amount()
            # Assert
            self.assertEqual(result, 500.01)
    
    def test_get_amount_non_numeric(self):
        # Act
        with patch("builtins.input", side_effect=["non_numeric_data"]):
            with self.assertRaises(ValueError) as context:
                get_amount()
            # Assert
            self.assertEqual(str(context.exception), "Invalid amount. Amount must be numeric.")
    
    def test_get_amount_zero_amt(self):
        # Act
        with patch("builtins.input", side_effect=["0"]):
            with self.assertRaises(ValueError) as context:
                get_amount()
            # Assert
            self.assertEqual(str(context.exception), "Invalid amount. Please enter a positive number.")
    
    def test_get_balance_valid(self):
        #Act
        with patch("builtins.input", side_effect=["123456"]):
            balance_info = get_balance(int(input("Enter account number: ")))
            expected_output = 'Your current balance for account 123456 is $1000.00.'
            # Assert
            self.assertEqual(balance_info, expected_output)

    def test_get_balance_noaccount(self):
        #Act
        with patch("builtins.input", return_value="112233"):  # Input an account number not in ACCOUNTS
            with self.assertRaises(Exception) as context:
                get_balance(int(input("Enter account number: ")))
        # Assert
        self.assertEqual(str(context.exception), "Account number does not exist.")
    
    def test_make_deposit_update(self):
        # Arrange
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0
        deposit_amount = 1500.01
        # Act
        make_deposit(account_number, deposit_amount)
        # Assert
        self.assertEqual(ACCOUNTS[account_number]["balance"], 2500.01)

    def test_make_deposit_successful(self):
        # Arrange
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0
        # Act
        result = make_deposit(account_number, 1500.01)
        # Assert
        self.assertEqual(result, "You have made a deposit of $1500.01 to account 123456.")


    def test_make_deposit_notexist(self):
        #Arrange
        account_number = 112233
        deposit_amount = 1500.01
        # Act
        with self.assertRaises(Exception) as context:
            make_deposit(account_number, deposit_amount)
        #Assert
        self.assertEqual(str(context.exception), "Account number does not exist.")


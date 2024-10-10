from django.test import TestCase

import unittest
from atm import ATM  # Make sure to adjust the import statement based on your directory structure

class TestATM(unittest.TestCase):
    def setUp(self):
        """Create an instance of the ATM class for testing."""
        self.atm = ATM(balance=1000)  # Initial balance of ₹1000

    def test_initial_balance(self):
        """Test initial balance is set correctly."""
        self.assertEqual(self.atm.balance, 1000)

    def test_check_balance(self):
        """Test balance checking functionality."""
        self.assertEqual(self.atm.check_balance(), "Current balance: ₹1000")

    def test_deposit(self):
        """Test the deposit functionality."""
        response = self.atm.deposit(500)
        self.assertEqual(response, "₹500 deposited successfully. New balance: ₹1500")
        self.assertEqual(self.atm.balance, 1500)

    def test_invalid_deposit(self):
        """Test invalid deposit amount."""
        response = self.atm.deposit(-100)
        self.assertEqual(response, "Invalid amount. Please enter a positive value.")

    def test_withdraw(self):
        """Test the withdrawal functionality."""
        response = self.atm.withdraw(400)
        self.assertEqual(response, "₹400 withdrawn successfully. New balance: ₹600")
        self.assertEqual(self.atm.balance, 600)

    def test_withdraw_exceeding_balance(self):
        """Test withdrawal exceeding balance."""
        response = self.atm.withdraw(1500)
        self.assertEqual(response, "Insufficient balance.")

    def test_withdraw_min_balance(self):
        """Test withdrawal that violates minimum balance requirement."""
        response = self.atm.withdraw(600)
        self.assertEqual(response, "Cannot withdraw. You must maintain a minimum balance of ₹500.")

    def test_withdraw_daily_limit(self):
        """Test daily withdrawal limit."""
        self.atm.daily_withdrawn = 15000  # Set the already withdrawn amount
        response = self.atm.withdraw(6000)
        self.assertEqual(response, "Exceeded daily withdrawal limit of ₹20000. You can withdraw up to ₹5000 more today.")

    def test_calculate_interest(self):
        """Test interest calculation functionality."""
        response = self.atm.calculate_interest(5, 12)  # 5% interest for 12 months
        self.assertEqual(response, "Interest for 12 months at 5%: ₹50.00")

    def test_view_transaction_history(self):
        """Test transaction history functionality."""
        self.atm.deposit(500)
        self.atm.withdraw(200)
        history = self.atm.view_transaction_history()
        self.assertIn("Transaction History:", history)
        self.assertIn("Deposit: ₹500", history)
        self.assertIn("Withdraw: ₹200", history)

    def test_empty_transaction_history(self):
        """Test viewing transaction history when empty."""
        response = self.atm.view_transaction_history()
        self.assertEqual(response, "No transactions yet.")

if __name__ == "__main__":
    unittest.main()

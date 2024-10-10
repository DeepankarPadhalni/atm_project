from datetime import datetime

class ATM:
    def __init__(self, balance=0, daily_withdrawal_limit=20000, min_balance=500):
        self.balance = max(balance, 0)  # Ensure initial balance is not negative
        self.daily_withdrawal_limit = daily_withdrawal_limit
        self.min_balance = min_balance
        self.transaction_history = []
        self.daily_withdrawn = 0

    def check_balance(self):
        """Returns the current balance."""
        return f"Current balance: ₹{self.balance:.2f}"  # Format to two decimal places

    def deposit(self, amount):
        """Deposits a specified amount into the ATM account."""
        if amount > 0:
            self.balance += amount
            self._log_transaction('Deposit', amount)
            return f"₹{amount:.2f} deposited successfully. {self.check_balance()}"
        else:
            return "Invalid amount. Please enter a positive value."

    def withdraw(self, amount):
        """Withdraws a specified amount from the ATM account."""
        # Ensure valid amount
        if amount <= 0:
            return "Invalid amount. Please enter a positive value."

        # Check daily withdrawal limit
        if self.daily_withdrawn + amount > self.daily_withdrawal_limit:
            return f"Exceeded daily withdrawal limit of ₹{self.daily_withdrawal_limit}. You can withdraw up to ₹{self.daily_withdrawal_limit - self.daily_withdrawn} more today."

        # Check sufficient balance and minimum balance rule
        if amount > self.balance:
            return "Insufficient balance."
        elif self.balance - amount < self.min_balance:
            return f"Cannot withdraw. You must maintain a minimum balance of ₹{self.min_balance}."

        # Perform withdrawal
        self.balance -= amount
        self.daily_withdrawn += amount
        self._log_transaction('Withdraw', amount)
        return f"₹{amount:.2f} withdrawn successfully. {self.check_balance()}"

    def calculate_interest(self, interest_rate, months=12):
        """Calculates interest on the current balance."""
        interest = self.balance * (interest_rate / 100) * (months / 12)
        return f"Interest for {months} months at {interest_rate}%: ₹{interest:.2f}"

    def _log_transaction(self, transaction_type, amount):
        """Logs transactions for history."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append({
            'type': transaction_type,
            'amount': amount,
            'timestamp': timestamp
        })

    def view_transaction_history(self):
        """Returns transaction history in a readable format."""
        if not self.transaction_history:
            return "No transactions yet."
        
        history = ["Transaction History:"]
        for transaction in self.transaction_history:
            history.append(f"{transaction['timestamp']} - {transaction['type']}: ₹{transaction['amount']:.2f}")
        return "\n".join(history)

    def reset_daily_withdrawal(self):
        """Resets the daily withdrawal amount, typically called at the end of the day."""
        self.daily_withdrawn = 0

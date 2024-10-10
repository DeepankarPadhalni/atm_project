from django.shortcuts import render
from .atm_logic import ATM  # Ensure atm_logic.py is correctly placed

def atm_menu(request):
    message = ""

    # Initialize ATM instance with session balance
    if 'atm_balance' not in request.session:
        request.session['atm_balance'] = 5000  # Initial balance
    atm = ATM(balance=request.session['atm_balance'])

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'check_balance':
            balance = atm.check_balance()  # Assuming this method returns the current balance
            message = f"Your current balance is: ₹{balance}"

        elif action in ['deposit', 'withdraw']:  # Simplified check
            try:
                amount = float(request.POST.get('amount', 0))
                if amount <= 0:
                    message = "Please enter a positive amount."
                else:
                    if action == 'deposit':
                        message = atm.deposit(amount)  # Update balance message
                        request.session['atm_balance'] += amount  # Update session balance
                    elif action == 'withdraw':
                        withdrawal_message = atm.withdraw(amount)
                        if "Insufficient balance" in withdrawal_message:
                            message = withdrawal_message
                        else:
                            request.session['atm_balance'] -= amount  # Update session balance
                            message = withdrawal_message
            except ValueError:
                message = "Invalid amount entered. Please enter a numeric value."
                
    return render(request, 'atm/menu.html', {'message': message})

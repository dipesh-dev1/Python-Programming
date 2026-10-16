class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds balance."""
    pass

balance = 20000

amount = 1500

try:
    if amount > balance:
        raise InsufficientFundsError("Not enough balance for this withdrawal")
    balance = balance - amount
    print("Withdrawal successful. New balance:", balance)

except InsufficientFundsError as e:
    print("Transaction failed:", e)

finally:
    print("Thank you for banking with us.")
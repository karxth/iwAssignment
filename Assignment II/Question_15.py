""" Imagine you are designing a banking application. What would a customer look like?
What attributes would she have? What methods would she have?"""

class BankingApp(object):
    def __int__(self, account_no, balance):
        self._acc_num = account_no
        self._total_balance = balance

    def cash_withdraw(self, amt):
        self._total_balance -= self.amt
        
    def cash_deposit(self, amt):
        self._total_balance += self.amt

    def show_balance(self):
        return f'Account No.: {self._acc_num} \nTotal Balance: {self._total_balance} '


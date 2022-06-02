# Add these methods to class Account - deposit, withdraw. Create two instances of account and verify they work as expected.
class Account:
   def __init__(self,balance,accountno,accountname,withdraws,deposits):
      self.balance=balance
      self.accountno=accountno
      self.accountname=accountname
      self.withdraws=withdraws
      self.deposits=deposits
   def deposit(self):
      self.balance+=self.deposits
      return self.balance

   def withdraw(self):
      self.balance-=self.withdraws
      return self.balance

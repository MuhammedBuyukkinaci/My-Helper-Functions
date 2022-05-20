import requests

class Employee:

    raise_amt = 1.05

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"
    
    @property
    def fullname(self):
        return f"{self.first } {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


    def monthly_schedule(self,month):
        response = requests.get(f"http://company.com/{self.last}/{month}")

        if response.ok:
            return response.text
        else:
            return 'Bad Response !'
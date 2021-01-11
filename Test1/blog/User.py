from webbrowser import get


class Users:
    def __init__(self,user_id,user_password,user_email,user_balance):
        self.name=str(self)
        self.user_id=user_id
        self.user_password=user_password
        self.user_email=user_email
        self.user_balance=user_balance

    def get_name(self):
        return self.name
    def get_id(self):
        return self.user_id
    def get_password(self):
        return self.user_password
    def get_email(self):
        return self.user_email
    def get_balamce(self):
        return self.user_balance
        


Logged_user=Users()
'''Logged_user.name=
Logged_user.user_id=
Logged_user.user_password=
Logged_user.user_email=
Logged_user.user_balance='''

Guest=Users("Guest ID","00000000","0000@gmail.com",0)



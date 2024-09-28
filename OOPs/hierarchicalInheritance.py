class Email:
    def send_email(self,mssg):
        print()

class Gmail(Email):
    def send_email(self,mssg):
        print("Sending '{}' from Gmail".format(mssg))
    
class Yahoo(Email):
    def send_email(self,mssg):
        print("Sending '{}' from yahoo".format(mssg))

e1= Gmail()
e1.send_email('Hello')
e2= Yahoo()
e2.send_email("Bol bhai")


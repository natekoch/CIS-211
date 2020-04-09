"""
Nate Koch
CIS 211
Lab 2
"""

class Phone:

    def __init__(self, name: str):
        self.name = name

    def pickUp(self):
        print(f"Picking up {self.name}")
    
    def dial(self, num: str):
        print(f"dialing {num}")

    def speak(self, msg: str):
        print(f"speaking: {msg}")

    def call(self, num: str, msg: str):
        self.pickUp()
        self.dial(num)
        self.speak(msg)
    
class SmartPhone(Phone):

    def openPhoneApp(self):
        print(f"opening Phone App on {self.name}")

    def call(self, num: str, msg: str):
        self.openPhoneApp()
        self.dial(num)
        self.speak(msg)

def main():
    ph1 = Phone("Panasonic")
    ph2 = Phone("AT&T")
    sPh1 = SmartPhone("iPhone")
    sPh2 = SmartPhone("Google")
    phoneList = [ph1, ph2, sPh1, sPh2]
    for phone in phoneList:
        phone.call("5413461000", "This is CIS 211 Lab.")
        print("________________________________________")

if __name__ == '__main__':
    main()


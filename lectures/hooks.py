from typing import List

class Listener:
    def notify(self, desc: str, val: int):
        raise NotImplementedError("Oops")

class Listenable:
    def __init__(self):
        self.listeners: List[Listener] = []

    def attach_listener(self, listener: Listener):
        self.listeners.append(listener)

    def notify_all(self, desc: str, val: int):
        for listener in self.listeners:
            listener.notify(desc, val)

class Press(Listenable):

    def __init__(self):
        super().__init__()

    def lmk(self):
        self.notify_all("event happened", 1)

def Event(Listener):

    def __init__(self):
        self.val = 0

    def notify(self, desc: str, val: int = 0):
        self.val += 1

    def query(self) -> int:
        return self.val

p = Press()
q = Press()
r = Press()
e = Event()
p.attach_listener(e)
q.attach_listener(e)
r.attach_listener(e)
p.lmk()
p.lmk()
p.lmk()
q.lmk()
print(e.query())


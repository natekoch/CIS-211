class List_v2(list):

    def __init__(self, name: str, l = []):
        super().__init__(l)
        self.name = name

    def append(self, element: object):
        self.insert(0, element)

    def print_contents(self) -> str:
        print(f"Name: {self.name}")
        for i in range(len(self)):
            print(f"[{i}] {self[i]}")

    def __str__(self):
        raise NotImplementedError("Use print_contents method instead")

    def __repr__(self):
        raise NotImplementedError("Use print_contents method instead")
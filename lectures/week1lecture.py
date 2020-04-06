class Event:
    '''
    '''

    def __init__(self, year: int, desc: str):
        '''
        '''
        self.year = year
        self.desc = desc
        self.disasters = None

    def catastrophe(self):
        self.disasters = 1

    def __str__(self) -> str:
        return f"{self.year}: {self.desc}"

    def __repr__(self) -> str:
        return f"Event({self.year}, {self.desc})"



class Era:

    def __init__(self, begin_year: int, end_year: int, list_events: list = []):
        self.begin_year = begin_year
        self.end_year = end_year
        self.list_events = list_events

    def append(self, new_event: Event):
        self.list_events.append(new_event)

    def __str__(self):
        return f"Era: {self.begin_year} - {self.end_year} // Events: {self.list_events}"

    def is_within_period(self, event: Event):
        return self.begin_year <= event.year <= self.end_year 

    
def main():
    space = Event(1969, "The first moon landing.")
    print(space)
    era1 = Era(1960, 1969, [str(space)])
    print(era1)
    
if __name__ == '__main__':
    main()
    

        
        

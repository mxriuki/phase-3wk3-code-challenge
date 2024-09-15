from classes.concert import Concert

class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise Exception("Invalid name")
    
    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, hometown):
        if isinstance(hometown, str) and len(hometown) > 0:
            self._hometown = hometown
        else:
            raise Exception("Invalid hometown")
    
    def concerts(self):
        return [concert for concert in Concert.all if concert.band == self]
    
    def play_in_venue(self, venue, date):
        return Concert(date, self, venue)
    
    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts()]

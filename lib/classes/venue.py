from classes.concert import Concert

class Venue:
    def __init__(self, title, city):
        self.title = title
        self.city = city
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception("Invalid title")
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        if isinstance(city, str) and len(city) > 0:
            self._city = city
        else:
            raise Exception("Invalid city")
    
    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]
    
    def bands(self):
        return [concert.band for concert in self.concerts()]
    
    def concert_on(self, date):
        for concert in self.concerts():
            if concert.date == date:
                return concert
        return None

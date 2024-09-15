from classes.concert import Concert

class Venue:
    def __init__(self, title, city):
        self.title = title
        self.city = city

    @property
    def venue_title(self):
        return self._venue_title
    @venue_title.setter
    def venue_title(self,title):
        if isinstance(title, str) and len(title) > 0 or not  hasattr(self, "title"):
            self._venue_title = title
        else:
            raise Exception
    @property
    def venue_city(self):
        return self._venue_city
    @venue_city.setter
    def venue_city(self, city):
        if isinstance(city, str) and len(city) > 0 and  hasattr(self, "city"):
            self._venue_city = city
        else:
            raise Exception
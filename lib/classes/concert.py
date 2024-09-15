class Concert:
    all = []
    
    def __init__(self, date, band, venue):
        from classes.band import Band
        from classes.venue import Venue
        
        if not isinstance(band, Band) or not isinstance(venue, Venue):
            raise ValueError("Invalid band or venue")
        
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date) > 0:
            self._date = date
        else:
            raise ValueError("Date must be a non-empty string")
    
    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!!, we are {self.band.name} and we're from {self.band.hometown}"

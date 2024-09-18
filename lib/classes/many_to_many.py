class Venue:
    def __init__(self, name, city):
        self._name = name  # Initialize name attribute
        self._city = city  # Initialize city attribute
        self._concerts = []  # List to store Concert instances
        self._bands = set()  # Set to store unique Band instances

    @property
    def name(self):
        return self._name  # This is where the getter method for name attribute is.

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:  # Validate input for it to be a string and the len of the string must be greater than 0 meaning its not empty.
            self._name = value  # Setter method for attribute name that us defined as value
        else:
            ValueError("Name must be a non-empty string")  #  ValueError for invalid input is raised when the input does not meet the required .
    @property
    def city(self):
        return self._city  # ita method that gets city attribute

    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:  # input validation for it to be a string and length value greater than 0.
            self._city = value  # Setter method for attribute city
        else:
            ValueError("City must be a non-empty string")  # Raise ValueError for invalid input 

    def add_concert(self, concert):
        """Add a concert to the venue."""
        if concert not in self._concerts:
            self._concerts.append(concert)
            self.add_band(concert.band)  # automatically adds the band of the concert to the venue

    def remove_concert(self, concert):
        """Remove a concert from the venue."""
        if concert in self._concerts:
            self._concerts.remove(concert)  # Remove the concert from the venue

    def add_band(self, band):
        """Add a band to the venue."""
        if band not in self._bands:
            self._bands.add(band)  # Add the band to the venue

    def remove_band(self, band):
        """Remove a band from the venue."""
        if band in self._bands:
            self._bands.remove(band)  # Remove the band from the venue

    def concerts(self):
        """Return a list of concerts at the venue."""
        return self._concerts  # Return the list of concerts

    def bands(self):
        """Return a list of unique bands that have played at the venue."""
        return list(self._bands)  # Return the list of unique bands


class Band:
    def __init__(self, name, hometown):
        self._name = name  # Initialize name attribute
        self._hometown = hometown  # Initialize hometown attribute
        self._concerts = []  # List to store Concert instances

    @property
    def name(self):
        return self._name  # Getter method for name attribute

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:  # Validation of input
            self._name = value  # Setter method for name attribute
        else:
            ValueError("Name must be a non-empty string")  # Raise ValueError for invalid input

    @property
    def hometown(self):
        return self._hometown  # Getter method for hometown attribute

    @hometown.setter
    def hometown(self, value):
        if isinstance(value, str) and len(value) > 0:  # Validate input
            self._hometown = value  # Setter method for hometown attribute
        else:
            ValueError("Hometown must be a non-empty string")  # Raise ValueError for invalid input

    def add_concert(self, concert):
        if concert not in self._concerts:
            self._concerts.append(concert)  # Add the concert to the band

    def concerts(self):
        return self._concerts  # Return the list of concerts

    def venues(self):
        return list({concert.venue for concert in self._concerts if isinstance(concert.venue, Venue)})  # Return the list of venues where the band has played

    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)  # Create a new concert
        self.add_concert(concert)  # Add the concert to the band
        venue.add_concert(concert)  # Add the concert to the venue
        return concert  # Return the newly created concert

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts]  # Return a list of introductions for all concerts


class Concert:
    all = []  # Class variable to store all Concert instances

    def __init__(self, date, band, venue):
        self._date = date  # Initialize date attribute
        self._band = band  # Initialize band attribute
        self._venue = venue  # Initialize venue attribute
        self._band.add_concert(self)  # Add the concert to the band
        self._venue.add_concert(self)  # Add the concert to the venue
        Concert.all.append(self)  # Add the concert to the list of all concerts

    @property
    def date(self):
        return self._date  # Getter method for date attribute

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:  # Validate input
            self._date = value  # Setter method for date attribute
        else:
            ValueError("Date must be a non-empty string.")  # Raise ValueError for invalid input

    @property
    def band(self):
        return self._band  # Getter method for band attribute

    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value  # Setter method for band attribute
        else:
            ValueError("Band must be an instance of Band class.")  # Raise ValueError for invalid input

    @property
    def venue(self):
        return self._venue  # Getter method for venue attribute

    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value  # Setter method for venue attribute
        else:
            ValueError("Venue must be an instance of Venue class.")  # Raise ValueError for invalid input

    def hometown_show(self):
        return self._venue.city == self._band.hometown  # Check if the concert is a hometown show for the band

    def introduction(self):
        return f"Hello {self._venue.city}!!!!! We are {self._band.name} and we're from {self._band.hometown}"  # Generate an introduction for the concert
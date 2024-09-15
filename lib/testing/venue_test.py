import pytest
from classes.band import Band
from classes.venue import Venue
from classes.concert import Concert

class TestVenue:
    '''Venue in venue.py'''

    def test_has_title_and_city(self):
        '''has an attribute "title" and "city", set in __init__().'''
        venue = Venue(title="Ace of Spades", city='SAC')
        assert venue.title == "Ace of Spades"
        assert venue.city == 'SAC'

    def test_title_city_is_string_of_more_than_zero_length(self):
        '''requires "title" and "city" to be string of >0 characters.'''
        with pytest.raises(Exception):
            Venue(title="", city='SAC')
        with pytest.raises(Exception):
            Venue(title="Ace of Spades", city='')

    def test_concert_on(self):
        '''has method "concert_on(date)" that returns the first concert on that date.'''
        band = Band(name='boygenius', hometown='NYC')
        venue = Venue(title="Theatre", city='NYC')
        venue2 = Venue(title="Ace of Spades", city='SAC')
        Concert(date='Nov 22', band=band, venue=venue)
        Concert(date='Nov 27', band=band, venue=venue2)

        # Ensure the method returns the correct concert
        assert venue.concert_on('Nov 22') == venue.concerts()[0]
        assert venue2.concert_on('Nov 27') == venue2.concerts()[0]
        assert venue.concert_on('Nov 25') is None

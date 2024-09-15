import pytest

from classes.band import Band
from classes.venue import Venue
from classes.concert import Concert

class TestConcert:
    '''Concert in concert.py'''

    def test_has_venue_band_date(self):
        '''initializes with venue, band, and date'''
        band = Band(name='boygenius', hometown='NYC')
        venue = Venue(title="Theatre", city='NYC')
        concert = Concert(date="Nov 5", band=band, venue=venue)


    def test_requires_date_band_venue(self):
        '''requires date, band, venue to be the correct types.'''
        band = Band(name='boygenius', hometown='NYC')
        venue = Venue(title="Theatre", city='NYC')
        with pytest.raises(Exception):
            Concert(date="", band=band, venue=venue)
        with pytest.raises(Exception):
            Concert(date="Nov 5", band='invalid input', venue=venue)
        with pytest.raises(Exception):
            Concert(date="Nov 5", band= band, venue='invalid input')


    def test_hometown_show(self):
        '''"hometown_show" returns true if concert is in bands hometown.'''
        band = Band(name='boygenius', hometown='NYC')
        venue = Venue(title="Theatre", city='NYC')
        venue2 = Venue(title="Ace of Spades", city='Sac')

        band.play_in_venue(venue= venue, date ='Nov 3')
        band.play_in_venue(venue= venue2, date ='Nov 5')

        assert band.concerts[0].hometown_show() == True
        assert band.concerts[1].hometown_show() == False


    def test_introduction(self):
        '''"introduction" returns true if concert is in bands hometown.'''
        band = Band(name='boygenius', hometown='NYC')
        venue = Venue(title="Theatre", city='NYC')
        venue2 = Venue(title="Ace of Spades", city='Sac')

        band.play_in_venue(venue= venue, date ='Nov 3')
        band.play_in_venue(venue= venue2, date ='Nov 5')

        assert band.concerts[0].introduction() == "Hello NYC!!!!!, we are boygenius and we're from NYC"
        assert band.concerts[1].introduction() == "Hello Sac!!!!!, we are boygenius and we're from NYC"

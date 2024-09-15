import pytest
from classes.band import Band
from classes.venue import Venue
from classes.concert import Concert

class TestBand:
    '''Band in band.py'''

    def test_has_name_hometown(self):
        '''has the name and hometown passed into __init__().'''
        Band(name='boygenius', hometown='NYC')


    def test_name_hometown_are_strings(self):
        '''Name and hometown must be strings.'''
        with pytest.raises(Exception):
            Band(name=1, hometown='NYC')
        with pytest.raises(Exception):
            Band(name="boygenius", hometown=4)

    def test_play_in_venue(self):
        '''play_in_venue adds concert for the band()'''
        band = Band(name='boygenius', hometown='NYC')
        venue = Venue(title="Theatre", city='NYC')
        venue2 = Venue(title="Ace of Spades", city='SAC')
        band.play_in_venue(venue= venue, date= 'Nov 22')

        assert len(band.concerts) == 1
        assert band.concerts[0].band == band 
        assert band.concerts[0].venue == venue 
        band.play_in_venue(venue= venue2, date= 'Nov 27')
        assert len(band.concerts) == 2
        assert band.concerts[1].band == band 
        assert band.concerts[1].venue == venue2

    def test_all_introductions(self):
        '''returns all introductions for the band'''
        band = Band(name='boygenius', hometown='NYC')
        venue = Venue(title="Theatre", city='NYC')
        venue2 = Venue(title="Ace of Spades", city='SAC')
        band.play_in_venue(venue= venue, date= 'Nov 22')
        band.play_in_venue(venue= venue2, date= 'Nov 27')

        assert band.all_introductions()[0] == "Hello NYC!!!!!, we are boygenius and we're from NYC"
        assert band.all_introductions()[1] == "Hello SAC!!!!!, we are boygenius and we're from NYC"
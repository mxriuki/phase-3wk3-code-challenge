from classes.concert import Concert
class Band:
    def  __init__( self, name , hometown):
        self.name= name
        self.hometown = hometown
        
    @property
    def band_name(self):
        return self._band_name
    @band_name.setter
    def band_name(self, name):
        if isinstance(name, str) and len(name) >= 1 and hasattr(self, "name"):
            self._band_name = name
        else:
            raise Exception
    @property
    def band_hometown(self):
        return self._band_hometown
    @band_hometown.setter
    def brand_hometown(self, hometown):
        if isinstance(hometown, str) and len(hometown) >= 1 and hasattr(self, "hometown"):
            self._band_hometown = hometown
        else:
            raise Exception
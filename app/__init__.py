from .menu import MainMenu

# App inherits from base classes containing related methods. Code is easier to
# navigate and maintain.
class App ( MainMenu ):
    def __init__ ( self ):
        super ( App, self ).__init__ ()

        self.species_data = []

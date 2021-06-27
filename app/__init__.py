from .data_display    import DataDisplayMethods
from .data_input      import DataInputMethods
from .menu            import MainMenuMethods
from .record_editing  import RecordEditingMethods
from .record_deleting import RecordDeletingMethods
from .sorting         import SortingMethods
from .csv_file_io     import CSVFileIOMethods

# App inherits from base classes containing related methods. Code is easier to
# navigate and maintain.
class App (
        DataDisplayMethods,
        DataInputMethods,
        MainMenuMethods,
        RecordEditingMethods,
        RecordDeletingMethods,
        SortingMethods,
        CSVFileIOMethods
        ):
    def __init__ ( self ):
        super ( App, self ).__init__ ()

        self.species_data = []

    def main ( self ):
        while True:
            self.displayMainMenu ()

            main_menu_choice = int ( self.inputMainMenuChoice () )

            if main_menu_choice == 1:
                self.displaySpeciesDataAsTable ()

            elif main_menu_choice == 2:
                self.displaySpeciesDataAsBarChart ()

            elif main_menu_choice == 3:
                self.inputSpeciesData ()

            elif main_menu_choice == 4:
                self.pickAndEditRecord ()

            elif main_menu_choice == 5:
                self.pickAndDeleteRecord ()

            elif main_menu_choice == 6:
                self.sortRecords ()

            elif main_menu_choice == 7:
                self.clearCurrentRecords ()

            elif main_menu_choice == 8:
                self.saveAsCSV ()

            elif main_menu_choice == 9:
                self.loadDataFromCSV ()

            elif main_menu_choice == 10:
                confirmation = input ( "Are you sure you want to quit [y/n]: " )
                
                if confirmation.lower () == 'y':
                    print ( "QUITTING." )
                    break
                else:
                    print ()

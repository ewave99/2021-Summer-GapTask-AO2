"""
A botanist wants to be able to record the species they find in a meadow.

They use a quadrat to select 5 areas of the meadow at various points of the
year.

They would like to be able to record the different species they see and how
many plants of each species are present.

Program requirements:
    - Allows the data to be collected 
    - Allows the data to be displayed in a tabulated format
    - Allows the user to edit the collected data
    - Allows the user to save the collected data in a CSV format
    - Allow data from previous years to be loaded from a CSV file in order to
      be edited, displayed or resaved
    - Display the species seen over the year to be displayed in a simple graph
      to show how many times each species has been found.
"""

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
        DataDisplayMethods.__init__ ( self )
        MainMenuMethods.__init__ ( self )
        DataInputMethods.__init__ ( self )
        RecordEditingMethods.__init__ ( self )
        RecordDeletingMethods.__init__ ( self )
        SortingMethods.__init__ ( self )
        CSVFileIOMethods.__init__ ( self )

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

from .generic import GenericMethods

from .data_display    import DataDisplayMethods
from .data_input      import DataInputMethods
from .record_editing  import RecordEditingMethods
from .record_deleting import RecordDeletingMethods
from .sorting         import SortingMethods
from .csv_file_io     import CSVFileIOMethods

class MainMenuMethods ( GenericMethods ):
    def __init__ ( self ):
        super ( MainMenuMethods, self ).__init__ ()

    # Methods for main menu

    def displayMainMenu ( self ):
        print ( "MAIN MENU:"                     )
        print ( "(1) Display data as table"      )
        print ( "(2) Display data as bar chart"  )
        print ( "(3) Input new data"             )
        print ( "(4) Edit record"                )
        print ( "(5) Delete record"              )
        print ( "(6) Sort records"               )
        print ( "(7) Clear all current records"  )
        print ( "(8) Save as CSV"                )
        print ( "(9) Load data from CSV"         )
        print ( "(10) Quit"                       )

        print ()

    def inputMainMenuChoice ( self ):
        user_input = input ( "Enter number of main menu option: " )

        while self.validateRangeBoundNumericChoice ( user_input, 1, 11 ) == False:
            print ( "Invalid main menu option." )

            user_input = input ( "Enter number of main menu option: " )

        print ()

        return user_input

class MainMenu (
        DataDisplayMethods,
        DataInputMethods,
        MainMenuMethods,
        RecordEditingMethods,
        RecordDeletingMethods,
        SortingMethods,
        CSVFileIOMethods
        ):
    def __init__ ( self ):
        super ( MainMenu, self ).__init__ ()

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

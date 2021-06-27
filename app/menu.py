from .generic import GenericMethods

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

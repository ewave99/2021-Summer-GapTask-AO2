from .generic import GenericMethods

class SortingMethods ( GenericMethods ):
    def __init__ ( self ):
        GenericMethods.__init__ ( self )

    # Methods for sorting records

    def sortRecords ( self ):
        print ( "SORT RECORDS:" )

        if len ( self.species_data ) == 0:
            print ( "No records to sort." )
            print ()

        elif len ( self.species_data ) == 1:
            print ( "Only one record in data." )
            print ()

        else:
            self.displaySortingOptions ()

            sorting_choice = int ( self.inputSortingChoice () )

            self.displayOptionsOfReverseSorting ()

            reverse_choice = int ( self.inputChoiceOfWhetherToReverseSort () )
            
            if reverse_choice == 1:
                reverse_bool = False

            elif reverse_choice == 2:
                reverse_bool = True

            if sorting_choice == 1:
                self.species_data.sort ( key=lambda record: record.name, reverse=reverse_bool )

            elif sorting_choice == 2:
                self.species_data.sort ( key=lambda record: record.count, reverse=reverse_bool )

            print ( "RECORDS SORTED." )
            print ()

    # Methods for inputting sorting options

    def displaySortingOptions ( self ):
        print ( "Sort by:" )
        print ( "(1) Name (alphabetical)" )
        print ( "(2) Count (numeric)" )
        print ()

    def inputSortingChoice ( self ):
        user_input = input ( "Enter number of chosen sorting option: " )

        while self.validateRangeBoundNumericChoice ( user_input, 1, 3 ) == False:
            print ( "Invalid option." )

            user_input = input ( "Enter number of chosen sorting option: " )

        print ()

        return user_input

    # Methods for inputting options for reverse sorting

    def displayOptionsOfReverseSorting ( self ):
        print ( "Sort in reverse?" )
        print ( "(1) No" )
        print ( "(2) Yes" )
        print ()

    def inputChoiceOfWhetherToReverseSort ( self ):
        user_input = input ( "Enter number of chosen option: " )

        while self.validateRangeBoundNumericChoice ( user_input, 1, 3 ) == False:
            print ( "Invalid option." )

            user_input = input ( "Enter number of chosen option: " )

        print ()

        return user_input


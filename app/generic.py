from collections import namedtuple

import re

Species = namedtuple ( typename="Species", field_names=[ "name", "count" ] )

class BaseMixin:
    # Generic methods

    def validateRangeBoundNumericChoice ( self, string_to_test, lower_bound, upper_bound ):
        regex_to_match = re.compile ( "^[0-9]+$" )
        
        if regex_to_match.match ( string_to_test ):
            number_to_test = int ( string_to_test )

            if number_to_test not in range ( lower_bound, upper_bound ):
                return False

            return True

        return False

class GenericMethods ( BaseMixin ):
    def __init__ ( self ):
        super ( GenericMethods, self ).__init__ ()

class RecordInputMixin ( BaseMixin ):
    def __init__ ( self ):
        super ( RecordInputMixin, self ).__init__ ()

    def inputChoiceOfRecord ( self ):
        user_input = input ( "Enter number of chosen record: " )

        while self.validateRangeBoundNumericChoice ( user_input, 1, len ( self.species_data ) + 1 ) == False:
            print ( "Invalid option." )

            user_input = input ( "Enter number of chosen record: " )

        print ()

        return user_input

import re

from .generic import Species

class DataInputMethods:
    # Methods to do with inputting species data

    def inputSpeciesData ( self ):
        current_record = None

        print ( "INPUT SPECIES DATA:" )

        print ( "Inputting species data. Leave either field blank to stop." )
        print ()

        user_input = self.inputSpeciesName ()

        while user_input != "":
            name = user_input

            user_input = self.inputSpeciesCount ()

            if user_input != "":
                count = int ( user_input )

                current_record = Species ( name, count )
                self.species_data.append ( current_record )

                print ()

                user_input = self.inputSpeciesName ()

        print ()
        print ( "Finished inputting species data." )
        
        print ()

    # Methods for inputting species name

    def inputSpeciesName ( self ):
        user_input = input ( "Enter species name: " )

        is_valid = self.validateSpeciesName ( user_input )

        while is_valid == False and user_input != "":
            print ( "Invalid name." )

            user_input = input ( "Enter species name: " )
            
            is_valid = self.validateSpeciesName ( user_input )

        name_already_exists = self.checkIfNameAlreadyExists ( user_input )

        while name_already_exists and user_input != "":
            print ( "Error: Name already exists in records." )

            user_input = input ( "Enter species name: " )

            is_valid = self.validateSpeciesName ( user_input )

            while is_valid == False and user_input != "":
                print ( "Invalid name." )

                user_input = input ( "Enter species name: " )
                
                is_valid = self.validateSpeciesName ( user_input )

            name_already_exists = self.checkIfNameAlreadyExists ( user_input )

        return user_input

    def validateSpeciesName ( self, string_to_test ):
        regex_to_match = re.compile ( r"^[a-z0-9]$|^[a-z0-9]+[a-z0-9\-]*([\s][a-z0-9\-]*)*[a-z0-9]+$" )

        if regex_to_match.match ( string_to_test.lower () ):
            return True
        
        return False

    def checkIfNameAlreadyExists ( self, string_to_test ):
        reference_string = string_to_test.lower ()

        name_already_exists = False

        i = 0

        while name_already_exists == False and i < len ( self.species_data ):
            record = self.species_data [ i ]

            if reference_string == record.name.lower ():
                name_already_exists = True

            i += 1
        
        return name_already_exists

    # Methods for inputting species count

    def inputSpeciesCount ( self ):
        user_input = input ( "Enter specimen count: " )

        while self.validateSpeciesCount ( user_input ) == False and user_input != "":
            print ( "Invalid count." )

            user_input = input ( "Enter specimen count: " )

        return user_input

    def validateSpeciesCount ( self, string_to_test ):
        regex_to_match = re.compile ( r"^[0-9]+$" )

        if regex_to_match.match ( string_to_test ):
            return True

        return False


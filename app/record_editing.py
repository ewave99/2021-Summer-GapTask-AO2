from .generic import GenericMethods, RecordInputMixin, Species

class RecordEditingMethods ( GenericMethods, RecordInputMixin ):
    def __init__ ( self ):
        super ( RecordEditingMethods, self ).__init__ ()

    # Methods for editing a record

    def pickAndEditRecord ( self ):
        print ( "EDITING RECORDS:" )

        if len ( self.species_data ) == 0:
            print ( 'No records to edit.' )
            print ()

        else:
            self.displayListOfRecordNames ()

            # taking into account indexing that starts at 0; the '- 1' is only
            # necessary since we will be working with a list.
            chosen_record_index = int ( self.inputChoiceOfRecord () ) - 1

            # we use pop here in order to not have duplicates
            chosen_record = self.species_data.pop ( chosen_record_index )

            current_name = chosen_record.name
            current_count = chosen_record.count

            self.displayChoiceOfFields ()

            # the '- 1' not needed here
            chosen_field = int ( self.inputChoiceOfField () )

            if chosen_field == 1:
                print ( f"Current name: {current_name}" )

                new_name = self.inputNewSpeciesName ()

                new_record = Species ( new_name, current_count )

                self.species_data.insert ( chosen_record_index, new_record )

            elif chosen_field == 2:
                print ( f"Current count value: {current_count}" )

                new_count = self.inputNewSpeciesCount ()

                new_record = Species ( current_name, new_count )

                self.species_data.insert ( chosen_record_index, new_record )

            print ()

    # Methods for choosing record

    def displayListOfRecordNames ( self ):
        for i in range ( len ( self.species_data ) ):
            record = self.species_data [ i ]

            print ( f"({i + 1}) {record.name}, {record.count}" )

        print ()

    # Methods for choosing field

    def displayChoiceOfFields ( self ):
        print ( "(1) Name" )
        print ( "(2) Count" )

        print ()

    def inputChoiceOfField ( self ):
        user_input = input ( "Enter number of chosen field: " )

        while self.validateRangeBoundNumericChoice ( user_input, 1, 3 ) == False:
            print ( "Invalid option." )

            user_input = input ( "Enter number of chosen field: " )

        print ()

        return user_input

    # Methods for updating species name

    def inputNewSpeciesName ( self ):
        user_input = input ( "Enter new species name: " )

        is_valid = self.validateSpeciesName ( user_input )

        while is_valid == False and user_input != "":
            print ( "Invalid name." )

            user_input = input ( "Enter new species name: " )
            
            is_valid = self.validateSpeciesName ( user_input )

        name_already_exists = self.checkIfNameAlreadyExists ( user_input )

        while name_already_exists and user_input != "":
            print ( "Error: Name already exists in records." )

            user_input = input ( "Enter new species name: " )

            is_valid = self.validateSpeciesName ( user_input )

            while is_valid == False and user_input != "":
                print ( "Invalid name." )

                user_input = input ( "Enter new species name: " )
                
                is_valid = self.validateSpeciesName ( user_input )

            name_already_exists = self.checkIfNameAlreadyExists ( user_input )

        return user_input

    # Methods for updating species count

    def inputNewSpeciesCount ( self ):
        user_input = input ( "Enter new specimen count: " )

        while self.validateSpeciesCount ( user_input ) == False and user_input != "":
            print ( "Invalid count." )

            user_input = input ( "Enter new specimen count: " )

        return user_input


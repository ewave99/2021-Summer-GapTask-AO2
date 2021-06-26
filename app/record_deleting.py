from .generic import RecordInputMixin

class RecordDeletingMethods ( RecordInputMixin ):
    def __init__ ( self ):
        super ( RecordDeletingMethods, self ).__init__ ()

    # Methods for deleting a record

    def pickAndDeleteRecord ( self ):
        print ( "DELETE RECORD:" )

        if len ( self.species_data ) == 0:
            print ( 'No records to delete.' )
            print ()

        else:
            self.displayListOfRecordNames ()

            # taking into account indexing that starts at 0; the '- 1' is only
            # necessary since we will be working with a list.
            chosen_record_index = int ( self.inputChoiceOfRecord () ) - 1

            confirmation = input ( "If you are sure, type 'yes': " )

            if confirmation.lower () == "yes":
                self.species_data.pop ( chosen_record_index )

                print ( "RECORD DELETED." )
                print ()

            else:
                print ( "ABORTED." )
                print ()

    # Methods for clearing records

    def clearCurrentRecords ( self ):
        print ( "CLEARING ALL RECORDS:" )
        
        if len ( self.species_data ) == 0:
            print ( "No records to clear." )
            print ()

        else:
            confirmation = input ( "If you are sure, type 'yes': " )

            if confirmation.lower () == "yes":
                self.species_data.clear ()

                print ( "CLEARED ALL CURRENT RECORDS." )
                print ()

            else:
                print ( "ABORTED." )
                print ()


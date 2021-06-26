import csv
import re
import os.path

from .generic import GenericMethods, Species

class CSVFileIOMethods ( GenericMethods ):
    def __init__ ( self ):
        GenericMethods.__init__ ( self )

    # Methods for saving to CSV

    def saveAsCSV ( self ):
        print ( "SAVE AS CSV:" )

        if len ( self.species_data ) == 0:
            print ( "No species data to save." )
            print ()

        else:
            name_to_save_to = self.getFilenameToSaveTo ()

            if name_to_save_to == ".csv":
                print ( "Error: filename \".csv\" not allowed." )
                print ()

            else:
                print ( f"Name to save to: \"{name_to_save_to}\"" )

                with open ( name_to_save_to, mode='w' ) as file_to_save_to:
                    field_names = [ "name", "count" ]

                    csv_writer = csv.DictWriter ( file_to_save_to, delimiter=',', fieldnames=field_names )

                    csv_writer.writeheader ()

                    for record in self.species_data:
                        csv_writer.writerow ( record._asdict () )

                print ( "SAVED." )
                print ()

    def getFilenameToSaveTo ( self ):
        name_to_save_to = input ( "Enter name to save to: " )

        if self.checkFilenameForExtension ( name_to_save_to ) == False:
            name_to_save_to += ".csv"

        return name_to_save_to

    def checkFilenameForExtension ( self, string_to_test ):
        regex_to_match = re.compile ( r"^.*\..+$" )

        if regex_to_match.match ( string_to_test ):
            return True

        return False

    # Methods for loading from CSV

    def loadDataFromCSV ( self ):
        print ( "LOAD DATA FROM CSV FILE:" )

        self.displayModesForLoadingCSV ()

        load_mode_choice = int ( self.inputChoiceOfModeForLoadingCSV () )

        filename_to_load_from = input ( "Enter filename to load from: " )

        if os.path.exists ( filename_to_load_from ):
            if load_mode_choice == 1:
                pass
            elif load_mode_choice == 2:
                self.species_data.clear ()

            with open ( filename_to_load_from, mode='r' ) as file_to_load_from:
                try:
                    csv_reader = csv.DictReader ( file_to_load_from, delimiter=',' )

                    for row_dict in csv_reader:
                        record = Species ( row_dict [ 'name' ], int ( row_dict [ 'count' ] ) )
                        
                        self.species_data.append ( record )

                    print ( "LOADED DATA." )
                    print ()

                except Exception as error:
                    print ( "Error:", error )
                    #print ( "Invalid CSV file." )
                    print ()

        else:
            print ( f"Error: file \"{filename_to_load_from}\" does not exist." )
            print ()

    def displayModesForLoadingCSV ( self ):
        print ( "CSV load mode:" )
        print ( "(1) Append to existing data in memory" )
        print ( "(2) Overwrite existing data in memory (WARNING: all data will be deleted)" )

        print ()

    def inputChoiceOfModeForLoadingCSV ( self ):
        user_input = input ( "Enter number of chosen option: " )

        while self.validateRangeBoundNumericChoice ( user_input, 1, 3 ) == False:
            print ( "Invalid option." )

            user_input = input ( "Enter number of chosen option: " )

        print ()

        return user_input

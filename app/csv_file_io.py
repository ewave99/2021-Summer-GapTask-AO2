import csv
import re
import os.path

from .generic import GenericMethods, Species

# Methods for saving to & loading from a CSV file.
class CSVFileIOMethods ( GenericMethods ):
    def __init__ ( self ):
        super ( CSVFileIOMethods, self ).__init__ ()

    # --- Methods for saving to CSV ---

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

    def inputWhetherWantToAddCSVExtension ( self ):
        user_input = input ( "Add .csv extension [y/n]? " )

        while user_input != 'y' and user_input != 'n':
            print ( "Invalid option." )

            user_input = input ( "Add .csv extension [y/n]? " )

        if user_input == 'y':
            return True

        return False

    def getFilenameToSaveTo ( self ):
        name_to_save_to = input ( "Enter name to save to: " )

        if self.checkFilenameForExtension ( name_to_save_to ) == False:
            add_csv_extension = self.inputWhetherWantToAddCSVExtension ()

            if add_csv_extension == True:
                name_to_save_to += ".csv"

        return name_to_save_to

    def checkFilenameForExtension ( self, string_to_test ):
        # checks for: any string of characters of length at least 0 + . + any string of characters of length at least 1
        regex_to_match = re.compile ( r"^.*\..+$" )

        if regex_to_match.match ( string_to_test ):
            return True

        return False

    # --- Methods for loading from CSV ---

    def loadDataFromCSV ( self ):
        print ( "LOAD DATA FROM CSV FILE:" )

        self.displayModesForLoadingCSV ()

        load_mode_choice = int ( self.inputChoiceOfModeForLoadingCSV () )

        filename_to_load_from = input ( "Enter filename to load from: " )

        if os.path.exists ( filename_to_load_from ):
            # if Append mode, do nothing since we are using the .append method
            # anyway
            if load_mode_choice == 1:
                pass

            # if Overwrite method, simply delete all the data first before
            # appending to the empty list remaining
            elif load_mode_choice == 2:
                self.species_data.clear ()

            with open ( filename_to_load_from, mode='r' ) as file_to_load_from:
                try:
                    # specialised csv reader to read in and return each row as
                    # a dict in the form { "name": ..., "count": ... }
                    csv_reader = csv.DictReader ( file_to_load_from, delimiter=',' )

                    for row_dict in csv_reader:
                        # tried doing Species ( **row_dict )
                        # but this breaks things as the count is read in as a
                        # str, so we must convert it explicitly to an int.
                        record = Species ( row_dict [ 'name' ], int ( row_dict [ 'count' ] ) )
                        
                        self.species_data.append ( record )

                    print ( "LOADED DATA." )
                    print ()

                # This is for if the file is not in valid CSV file format.
                # (Or for any other errors)
                except Exception as error:
                    # decided to stick to printing the error, since otherwise 
                    # has proved hard to debug
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

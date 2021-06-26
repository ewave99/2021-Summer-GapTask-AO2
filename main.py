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

from collections import namedtuple

import re

import os.path
import csv

from matplotlib import pyplot as plt

Species = namedtuple ( typename="Species", field_names=[ "name", "count" ] )

class App:
    def __init__ ( self ):
        self.species_data = []

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

    def validateSpeciesCount ( self, string_to_test ):
        regex_to_match = re.compile ( r"^[0-9]+$" )

        if regex_to_match.match ( string_to_test ):
            return True

        return False

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

    def inputSpeciesCount ( self ):
        user_input = input ( "Enter specimen count: " )

        while self.validateSpeciesCount ( user_input ) == False and user_input != "":
            print ( "Invalid count." )

            user_input = input ( "Enter specimen count: " )

        return user_input

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

    def getWidthForNameColumn ( self ):
        if len ( self.species_data ) != 0:
            name_lengths = [ len ( record.name ) for record in self.species_data ]
            max_name_length = max ( name_lengths )
        else:
            max_name_length = 0

        # len ( "Name" ) == 4
        # This ensures that the width for the Name column is not shorter than the
        # literal string "Name", since we are displaying the header too.
        width_for_name_column = max ( 4, max_name_length )
        # this is a constant gap that will be there regardless
        width_for_name_column += 4

        return width_for_name_column

    def getWidthForCountColumn ( self ):
        if len ( self.species_data ) != 0:
            count_lengths = [ len ( str ( record.count ) ) for record in self.species_data ]
            max_count_length = max ( count_lengths )
        else:
            max_count_length = 0

        # len ( "Count" ) == 5
        # This ensures that the width for the Count column is not shorter than the
        # literal string "Count", since we are displaying the header too.
        width_for_count_column = max ( 5, max_count_length )
        # this is a constant space that will be there regardless
        width_for_count_column += 1

        return width_for_count_column

    def printTableHeader ( self, width_for_name_column, width_for_count_column ):
        total_width = width_for_name_column + width_for_count_column

        name_cell = "Name".ljust ( width_for_name_column )
        count_cell = "Count".ljust ( width_for_count_column )

        row_string = name_cell + count_cell

        print ( row_string )

        row_string = '-' * total_width

        print ( row_string )

    def printRecordForTable ( self, width_for_name_column, width_for_count_column, record ):
        name_cell = record.name.ljust ( width_for_name_column )
        count_cell = str ( record.count ).ljust ( width_for_count_column )

        row_string = name_cell + count_cell

        print ( row_string )

    def displaySpeciesDataAsTable ( self ):
        print ( "SPECIES DATA:" )

        width_for_name_column = self.getWidthForNameColumn ()
        width_for_count_column = self.getWidthForCountColumn ()

        self.printTableHeader ( width_for_name_column, width_for_count_column )

        for record in self.species_data:
            self.printRecordForTable ( width_for_name_column, width_for_name_column, record )

        print ()

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

    def validateRangeBoundNumericChoice ( self, string_to_test, lower_bound, upper_bound ):
        regex_to_match = re.compile ( "^[0-9]+$" )
        
        if regex_to_match.match ( string_to_test ):
            number_to_test = int ( string_to_test )

            if number_to_test not in range ( lower_bound, upper_bound ):
                return False

            return True

        return False

    def inputMainMenuChoice ( self ):
        user_input = input ( "Enter number of main menu option: " )

        while self.validateRangeBoundNumericChoice ( user_input, 1, 10 ) == False:
            print ( "Invalid main menu option." )

            user_input = input ( "Enter number of main menu option: " )

        print ()

        return user_input

    def inputChoiceOfRecord ( self ):
        user_input = input ( "Enter number of chosen record: " )

        while self.validateRangeBoundNumericChoice ( user_input, 1, len ( self.species_data ) + 1 ) == False:
            print ( "Invalid option." )

            user_input = input ( "Enter number of chosen record: " )

        print ()

        return user_input

    def displayListOfRecordNames ( self ):
        for i in range ( len ( self.species_data ) ):
            record = self.species_data [ i ]

            print ( f"({i + 1}) {record.name}, {record.count}" )

        print ()

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

    def inputNewSpeciesCount ( self ):
        user_input = input ( "Enter new specimen count: " )

        while self.validateSpeciesCount ( user_input ) == False and user_input != "":
            print ( "Invalid count." )

            user_input = input ( "Enter new specimen count: " )

        return user_input

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

    def checkFilenameForExtension ( self, string_to_test ):
        regex_to_match = re.compile ( r"^.*\..+$" )

        if regex_to_match.match ( string_to_test ):
            return True

        return False

    def getFilenameToSaveTo ( self ):
        name_to_save_to = input ( "Enter name to save to: " )

        if self.checkFilenameForExtension ( name_to_save_to ) == False:
            name_to_save_to += ".csv"

        return name_to_save_to

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

    def loadDataFromCSV ( self ):
        print ( "LOAD DATA FROM CSV FILE:" )

        self.displayModesForLoadingCSV ()

        load_mode_choice = self.inputChoiceOfModeForLoadingCSV ()

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
                        record = Species ( **row_dict )
                        
                        self.species_data.append ( record )

                    print ( "LOADED DATA." )
                    print ()

                except Exception as error:
                    # print ( "Error:", error )
                    print ( "Invalid CSV file." )
                    print ()

        else:
            print ( f"Error: file \"{filename_to_load_from}\" does not exist." )
            print ()

    def displaySpeciesDataAsBarChart ( self ):
        if len ( self.species_data ) == 0:
            print ( "No species data to display." )
            print ()

        else:
            counts = [ record.count for record in self.species_data ]
            names = [ record.name for record in self.species_data ]

            plt.xticks ( range ( len ( names ) ), names )

            plt.xlabel ( "Species name" )
            plt.ylabel ( "Specimen count" )

            plt.title ( "Specimen count for each species seen" )

            plt.bar ( range ( len ( counts ) ), counts )

            plt.show ()

    def displayMainMenu ( self ):
        print ( "MAIN MENU:"                     )
        print ( "(1) Display data as table"      )
        print ( "(2) Input new data"             )
        print ( "(3) Edit record"                )
        print ( "(4) Delete record"              )
        print ( "(5) Sort records"               )
        print ( "(6) Clear all current records"  )
        print ( "(7) Save as CSV"                )
        print ( "(8) Load data from CSV"         )
        print ( "(9) Quit"                       )

        print ()

    def main ( self ):
        while True:
            self.displayMainMenu ()

            main_menu_choice = int ( self.inputMainMenuChoice () )

            if main_menu_choice == 1:
                self.displaySpeciesDataAsTable ()

            elif main_menu_choice == 2:
                self.inputSpeciesData ()

            elif main_menu_choice == 3:
                self.pickAndEditRecord ()

            elif main_menu_choice == 4:
                self.pickAndDeleteRecord ()

            elif main_menu_choice == 5:
                self.sortRecords ()

            elif main_menu_choice == 6:
                self.clearCurrentRecords ()

            elif main_menu_choice == 7:
                self.saveAsCSV ()

            elif main_menu_choice == 8:
                self.loadDataFromCSV ()

            elif main_menu_choice == 9:
                confirmation = input ( "Are you sure you want to quit [y/n]: " )
                
                if confirmation.lower () == 'y':
                    print ( "QUITTING." )
                    break
                else:
                    print ()

if __name__ == '__main__':
    app = App ()
    app.main ()

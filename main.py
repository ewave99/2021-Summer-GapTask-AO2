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

Species = namedtuple ( typename="Species", field_names=[ "name", "count" ] )

species_data = []

def validateSpeciesName ( string_to_test ):
    regex_to_match = re.compile ( r"^[a-z0-9]$|^[a-z0-9]+[a-z0-9\-]*([\s][a-z0-9\-]*)*[a-z0-9]+$" )

    if regex_to_match.match ( string_to_test.lower () ):
        return True
    
    return False

def validateSpeciesCount ( string_to_test ):
    regex_to_match = re.compile ( r"^[0-9]+$" )

    if regex_to_match.match ( string_to_test ):
        return True

    return False

def inputSpeciesName ():
    user_input = input ( "Enter species name: " )

    while validateSpeciesName ( user_input ) == False and user_input != "":
        print ( "Invalid name." )

        user_input = input ( "Enter species name: " )

    return user_input

def inputSpeciesCount ():
    user_input = input ( "Enter specimen count: " )

    while validateSpeciesCount ( user_input ) == False and user_input != "":
        print ( "Invalid count." )

        user_input = input ( "Enter specimen count: " )

    return user_input

def inputSpeciesData ():
    species_data = []
    current_record = None

    print ( "Inputting species data. Leave either field blank to stop." )
    print ()

    user_input = inputSpeciesName ()

    while user_input != "":
        name = user_input

        user_input = inputSpeciesCount ()

        if user_input != "":
            count = int ( user_input )

            current_record = Species ( name, count )
            species_data.append ( current_record )

            print ()

            user_input = inputSpeciesName ()

    print ()
    print ( "Finished inputting species data." )
    
    print ()

    return species_data

def getWidthForNameColumn ( species_data ):
    if len ( species_data ) != 0:
        name_lengths = [ len ( record.name ) for record in species_data ]
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

def getWidthForCountColumn ( species_data ):
    if len ( species_data ) != 0:
        count_lengths = [ len ( str ( record.count ) ) for record in species_data ]
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

def printTableHeader ( width_for_name_column, width_for_count_column ):
    total_width = width_for_name_column + width_for_count_column

    name_cell = "Name".ljust ( width_for_name_column )
    count_cell = "Count".ljust ( width_for_count_column )

    row_string = name_cell + count_cell

    print ( row_string )

    row_string = '-' * total_width

    print ( row_string )

def printRecordForTable ( width_for_name_column, width_for_count_column, record ):
    name_cell = record.name.ljust ( width_for_name_column )
    count_cell = str ( record.count ).ljust ( width_for_count_column )

    row_string = name_cell + count_cell

    print ( row_string )

def displaySpeciesDataAsTable ( species_data ):
    width_for_name_column = getWidthForNameColumn ( species_data )
    width_for_count_column = getWidthForCountColumn ( species_data )

    printTableHeader ( width_for_name_column, width_for_count_column )

    for record in species_data:
        printRecordForTable ( width_for_name_column, width_for_name_column, record )

    print ()

def main ():
    species_data = inputSpeciesData ()

    displaySpeciesDataAsTable ( species_data )

if __name__ == '__main__':
    main ()

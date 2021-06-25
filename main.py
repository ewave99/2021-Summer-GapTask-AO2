"""
A botanist wants to be able to record the species they find in a meadow.

They use a quadrat to select 5 areas of the meadow at various points of the
year.

They would like to be able to record the different species they see and how
many plants of each species are present.

Program requirements:
    - Allows the data to be collected and displayed in a tabulated format
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
    regex_to_match = re.compile ( r"^[a-z]+([\s][a-z]+)*$" )

    if regex_to_match.match ( string_to_test.lower () ):
        return True
    
    return False

def validateSpeciesCount ( string_to_test ):
    regex_to_match = re.compile ( r"^[0-9]+$" )

    if regex_to_match.match ( string_to_test ):
        return True

    return False

def inputSpeciesData ():
    print ( "Inputting species data. Leave either field blank to stop." )

    prompt_for_name = "Enter species name: "
    prompt_for_count = "Enter specimen count: "

    user_input = input ( prompt_for_name )

    while validateSpeciesName ( user_input ) == False and user_input != "":
        print ( "Invalid name." )

        user_input = input ( prompt_for_name )

    while user_input != "":
        name = user_input

        user_input = input ( prompt_for_count )

        while validateSpeciesCount ( user_input ) == False and user_input != "":
            print ( "Invalid count." )

            user_input = input ( prompt_for_count )

        if user_input != "":
            count = user_input

            print ()

            user_input = input ( prompt_for_name )

            while validateSpeciesName ( user_input ) == False and user_input != "":
                print ( "Invalid name." )

                user_input = input ( prompt_for_name )

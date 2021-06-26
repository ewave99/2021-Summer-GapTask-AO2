from matplotlib import pyplot as plt

class DataDisplayMethods:
    # Methods for displaying data in table

    def displaySpeciesDataAsTable ( self ):
        print ( "SPECIES DATA:" )

        width_for_name_column = self.getWidthForNameColumn ()
        width_for_count_column = self.getWidthForCountColumn ()

        self.printTableHeader ( width_for_name_column, width_for_count_column )

        for record in self.species_data:
            self.printRecordForTable ( width_for_name_column, width_for_name_column, record )

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

    # Methods for displaying data as bar chart

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

            plt.ylim ( 0, max ( counts ) )

            plt.bar ( range ( len ( counts ) ), counts )

            plt.show ()

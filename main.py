import argparse
import csv
import os
import sys
from prettytable import PrettyTable
from art import ASCIIART, SEPERATOR, TICK, CROSS
# from classes import Section

# Arg Parsing
parser = argparse.ArgumentParser(description="Tool to keep track of things to do. By default, the script will show all tables.")
parser.add_argument('-c',
                    '--create-table',
                    action='store',
                    help='Create a new table.'
                    )
args = parser.parse_args()

# Functions
def get_sections(csv_file):
    """Creates/returns the sections.csv file which stores all sections."""
    if not os.path.exists(csv_file):
        with open(csv_file, mode="w") as sections_csv:
            pass
    
    # Add default sections
    if os.stat(csv_file).st_size == 0:
            with open(csv_file, mode="w") as section_csv:
                data = ['Dailies', 'Short Term Goals', 'Long Term Goals']
                writer = csv.writer(section_csv)
                writer.writerow(data)
    
    # Return the sections
    sections_list = []
    with open(csv_file, mode="r") as sections_csv:
        sections = csv.reader(sections_csv, delimiter=',')
        for section in sections:
            sections_list += section
    return(sections_list)


def format_output(output):

    if output.lower() == 'in progress':
        output = CROSS
    elif output.lower() == 'complete' or output.lower() == 'completed':
        output = TICK
    else:
        pass

    return(output)


def create_folders():
    """Checks if sections & archive directories exists and creates them if not."""

    # Check for sections
    user_input = ""
    if not os.path.exists('sections'):
        os.makedirs('sections')
        os.makedirs('sections/archive')
    
    #Check for sections/archive
    if not os.path.exists('sections/archive'):
        os.makedirs('sections/archive')

    # If there is a sections file, delete it and create folder, or exit.
    while os.path.isdir('sections') is False:
        user_input = input("A file named 'sections' exists. Would you like to delete it in order to create the sections folder? Y/n: ")
        if user_input.lower() == "y" or user_input.lower() == "":
            print("Removing sections file.")
            os.remove('sections')
            print("Creating sections directory.")
            os.makedirs('sections')
            os.makedirs('sections/archive')
        elif user_input.lower() == "n":
            print("Exitting.")
            sys.exit()


def create_sections(list_of_sections, sections_all):
    """Checks if csv files exist for default sections and creates them if not."""
    for section in list_of_sections:

        #check if csv exists
        if not os.path.exists(f'sections/{section}.csv'):
            with open(f"sections/{section}.csv", mode="w") as section_csv:
                pass

        # Check to see if there is any data in the csv file.
        # Add some data if none.
        if os.stat(f"sections/{section}.csv").st_size == 0:
            with open(f"sections/{section}.csv", mode="w") as section_csv:
                data = ['Add goals', 'In Progress']
                writer = csv.writer(section_csv)
                writer.writerow(data)

        # Create table and return it to sections
        # Either choose a decent emoji or leave index blank
        table = PrettyTable()
        table.field_names = ["👨", f"{section}", "Status"]

        with open(f"sections/{section}.csv") as section_csv:
            data = list(csv.reader(section_csv))

            for line in data:
                index = line[0]
                goal = line[1]
                progress = line[2]

                progress = format_output(progress)
                table.add_row([index, goal, progress])

        print(type(table))
        print(table)
        sections_all += table

        # for sectiontest in sections_all:
        #     print(type(sectiontest))
        #     print(sectiontest)

    return(sections_all)

# Variables
SECTIONS_CSV = "sections.csv"
sections = get_sections(SECTIONS_CSV)
section_tables = []

# Actions
if not len(sys.argv) > 1:
    create_folders()
    create_sections(sections, section_tables)

    # Print output
    print(ASCIIART)
    for section_table in section_tables:
        pass
    # print(section_table)
else:
    print(vars(args))

##TODO:
# Add archiving
# Add index/id to row items/tables
# Add args for creating/deleting items and tables
# Add args for archiving / restoring from archive
# Add args for backups

# get list of all csv
# delete from list if they are in sections
# whatever is left, move to archive
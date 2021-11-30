import argparse
import csv
import os
import sys
from prettytable import PrettyTable
from art import SEPERATOR, TICK, CROSS
from classes import Section

parser = argparse.ArgumentParser(description="Tool to keep track of things to do. By default, the script will show all tables.")

parser.add_argument('-c',
                    '--create-table',
                    action='store',
                    help='Create a new table.'
                    )

args = parser.parse_args()

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

    if output == 'in progress':
        output = CROSS
    elif output == 'completed':
        output = TICK
    else:
        pass

    return(output)


def create_section_folder():
    """Checks if sections directory exists and creates it if not."""

    user_input = ""
    if not os.path.exists('sections'):
        os.makedirs('sections')

    while os.path.isdir('sections') is False:
        user_input = input("A file named 'sections' exists. Would you like to delete it in order to create the sections folder? Y/n: ")
        if user_input.lower() == "y" or user_input.lower() == "":
            print("Removing sections file.")
            os.remove('sections')
            print("Creating sections directory.")
            os.makedirs('sections')
        elif user_input.lower() == "n":
            print("Exitting.")
            sys.exit()


def create_sections(list_of__sections, sections_all):
    """Checks if csv files exist for default sections and creates them if not."""
    for section in list_of__sections:
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
        table = PrettyTable()
        table.field_names = [f"{section}", "Status"]

        with open(f"sections/{section}.csv") as section_csv:
            data = list(csv.reader(section_csv))

            for line in data:
                goal = line[0]
                progress = line[1]

                progress = format_output(progress)
                table.add_row([goal, progress])

        sections_all += table

    return(sections_all)

# Variables
SECTIONS_CSV = "sections.csv"
sections = get_sections(SECTIONS_CSV)
section_tables = []


# Actions
if not len(sys.argv) > 1:
    create_section_folder()
    create_sections(sections, section_tables)

    for section_table in section_tables:
        print(section_table)
else:
    print(vars(args))
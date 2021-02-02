import model.covid_model as model
import view.covid_view as view


def print_list():
    """
    Calls on the view to print the list
    """
    view.print_list(model.get_list())


def create_database():
    """
    Commands the model to create a table
    """
    model.create_table()


def initialize_list():
    """
    Calls on the model to initialize the data
    If the model cannot find the file then it will call on the view to display so
    """
    if model.initialize_list() is True:
        view.display_list_initialized()
    else:
        view.display_file_not_found()


def display_default_menu():
    """
    Calls on the view to display a menu
    """
    view.display_default_menu()


def write_to_file():
    """
    Writes the data into a file
    """
    file = open('output_file.txt', 'w')
    for element in model.get_list():
        file.write('[')
        for i in range(7):
            file.write(str(element[i]))
            if i != 6:
                file.write(',')
        file.write('],')

    view.display_write_to_list()


def create_record():
    """
    Takes user input for a new record then calls on the model to create it
    """
    view.display_enter_country_id()
    country_id = input()
    view.display_enter_date()
    date = input()
    view.display_enter_cases()
    cases = input()
    view.display_enter_deaths()
    deaths = input()
    view.display_enter_name_fr()
    name_fr = input()
    view.display_enter_name_en()
    name_en = input()

    model.add(country_id, date, cases, deaths, name_fr, name_en)
    view.display_added()


def select_record(edit):
    """
    It will select a record from the list and the call the appropriate edit/delete functions
    :param edit: True if we wish to select for editing, False for deleting
    """
    view.display_select_index()
    rowid = input()
    if rowid.isnumeric():
        if model.select_by_id(rowid) is True:
            if edit:
                edit_record(rowid)
            else:
                delete_record(rowid)
        else:
            view.display_index_out_of_bounds()
    else:
        view.display_invalid_format()


def edit_record(rowid):
    """
    Takes user input for the new values of the selected record
    and saves the changes
    :param rowid: id of the element to be edited
    """
    view.display_confirm_edit(rowid)
    flag = input()
    if flag == 'Y' or flag == 'y':
        view.display_start_edit()

        view.display_enter_country_id()
        country_id = input()

        view.display_enter_date()
        date = input()

        view.display_enter_cases()
        cases = input()

        view.display_enter_deaths()
        deaths = input()

        view.display_enter_name_fr()
        names_fr = input()

        view.display_enter_name_en()
        names_en = input()

        model.update(country_id, date, cases, deaths, names_fr, names_en, rowid)
        view.display_edit_completed()


def delete_record(rowid):
    """
    Calls on the model to delete a record
    :param rowid: The record id of the record to be deleted
    """
    view.display_confirm_delete(rowid)
    flag = input()
    if flag == 'Y' or flag == 'y':
        model.delete(rowid)
        view.display_delete_completed()


def close():
    """
    Closes the connection in model when terminating the program
    """
    model.close()


def print_ordered():
    """
    The method prompts a user to select columns to order the list by.
    It sends instructions to view and model based on the user input.
    """
    # Selected columns are empty at the start. They are to be filled by user selections.
    selected_columns = []
    # These are the default columns contained in the table
    columns = ['rowid', 'country_id', 'date', 'cases', 'deaths', 'name_fr', 'name_en']
    # Loop runs until the user inputs a selection indicating otherwise
    selection = ''
    while len(columns) >= 0 and selection != 'X' and selection != 'x':
        view.display_select_column(columns, selected_columns)
        selection = input()
        # Cancel case
        if selection == 'X' or selection == 'x':
            view.display_cancel_sort()
        # If an index from the columns list is selected
        elif selection.isnumeric():
            index = int(selection) - 1
            # If index passes error checking it is added to the selected list and removed from the available list
            if 0 <= index < len(columns):
                selected_columns.append(columns[index])
                del columns[index]
            else:
                view.display_index_out_of_bounds()
        # The submit option
        elif selection == 'Y' or selection == 'y':
            # Checks if there are columns selected
            if len(selected_columns) == 0:
                view.display_no_columns_selected()
            # If columns are selected the user is asked to select descending/ascending. Then model is called
            else:
                view.display_descending_option()
                desc = False
                order = input()
                if order == 'D' or order == 'd':
                    desc = True
                selection = 'X'
                view.display_selected_columns(selected_columns)
                view.print_list(model.get_ordered_list(selected_columns, desc))
        else:
            view.display_invalid_format()


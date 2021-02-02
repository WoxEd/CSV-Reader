import model.covid_model as model


def print_list(data):
    """
    Loops through each data element and prints the __str__ output
    """
    print('There are currently ' + str(len(data)) + ' elements in the list')
    for element in data:
        print(element)


def display_default_menu():
    """
    Displays a selection screen for users to choose an option
    """
    print('Project by Woxing Zhang: Select one of the following functions:\n'
          + '1: Print Data\n'
          + '2: Reload Data\n'
          + '3: Write Data to File\n'
          + '4: Create New Record\n'
          + '5: Select Record to Edit\n'
          + '6: Select Record to Delete\n'
          + '7: Print data ordered by column(s)\n'
          + '0: Exit Program')


def display_file_not_found():
    """
    Prints a message for file not found
    """
    print('File not found!')


def display_list_initialized():
    """
    Prints a message for data initialized
    """
    print('Data initialized!')


def display_write_to_list():
    """
    Prints a message confirming data written to list
    """
    print('Data written to file')


def display_enter_country_id():
    """
    Prints a message for entering country id
    """
    print('Enter Country ID')


def display_enter_date():
    """
    Prints a message for entering date
    """
    print('Enter Date')


def display_enter_cases():
    """
    Prints a message for entering cases
    """
    print('Enter Cases')


def display_enter_deaths():
    """
    Prints a message for entering deaths
    """
    print('Enter Deaths')


def display_enter_name_fr():
    """
    Prints a message for entering name in French
    """
    print('Enter Country Name in French')


def display_enter_name_en():
    """
    Prints a message for entering name in English
    """
    print('Enter Country Name in English')


def display_added():
    """
    Prints a message for confirming data added
    """
    print('Data has been added to the list')


def display_select_index():
    """
    Prints a message for the element selected, or prints a message indicating list is empty
    """
    size = model.get_size()
    if size > 0:
        print('Enter the id of the data you wish to select')
    else:
        print('The list is empty')


def display_index_out_of_bounds():
    """
    Prints a message for index out of bounds
    """
    print('The id you selected is not in the database')


def display_invalid_format():
    """
    Prints a message for invalid input type
    """
    print('Invalid data type, index should be a number')


def display_confirm_edit(selected):
    """
    Prints a message for confirming edit
    """
    print('Are you sure you want to edit: ' + selected.__str__() + '? (Y/N)')


def display_start_edit():
    """
    Prints a message for starting edit
    """
    print('Enter new values')


def display_edit_completed():
    """
    Prints a message confirm edit was completed
    """
    print('Edit saved')


def display_confirm_delete(selected):
    """
    Prints a message for confirming delete
    """
    print('Are you sure you want to delete: ' + selected.__str__() + '? (Y/N)')


def display_delete_completed():
    """
    Prints a message for confirming data was deleted
    """
    print('Data deleted')


def display_select_column(columns, selected_columns):
    selection = 0
    print('Program by Woxing Zhang: Select a column from the following')

    if len(selected_columns) > 0:
        print('Currently selected' + str(selected_columns))

    for col in columns:
        print('\t' + str(selection + 1) + ': ' + col)
        selection += 1
    print('\t' + 'Y: Submit')
    print('\t' + 'X: Cancel')


def display_cancel_sort():
    print('Sort cancelled')


def display_no_columns_selected():
    print('No columns selected')


def display_selected_columns(columns):
    print('Sorting by the following columns: ' + str(columns))


def display_descending_option():
    print("Press 'D' if you want descending order. Press any other key for ascending")




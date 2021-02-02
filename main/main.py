import controller.covid_controller as controller
"""
This is the main file of a MVC model program. 
It uses user input to select controller functions to execute.
"""


def start_program():
    """
    Main method which displays a menu. Runs until user selects 0. It uses controller to control program.
    """
    # initializes the data
    controller.create_database()
    # variable responsible for holding user input
    selection = ''

    while selection != '0':
        controller.display_default_menu()
        selection = input()
        if selection == '1':
            controller.print_list()
        elif selection == '2':
            controller.initialize_list()
        elif selection == '3':
            controller.write_to_file()
        elif selection == '4':
            controller.create_record()
        elif selection == '5':
            controller.select_record(True)
        elif selection == '6':
            controller.select_record(False)
        elif selection == '7':
            controller.print_ordered()
        elif selection == '0':
            controller.close()
            break
        else:
            print('invalid entry')


if __name__ == '__main__':
    start_program()

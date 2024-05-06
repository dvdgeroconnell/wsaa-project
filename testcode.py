# testcode.py (Applied Databases project)
#
# A Python function to draw a menu of options, check the entered choice is a valid integer and returns
# the value to the main program. Range checking is done by the main program.
#
# Author: David O'Connell
#
# ***************************************************************************************************

# Define the function that will be called from the main program
def do_menu():

    choices = ('1', '2', '3', '4', '5', 'x')

    # The do_menu() function just draws the menu and returns the choice
    print("\n====================================")
    print("                MENU               ")
    print("====================================")
    print("1 - Get all Records")
    print("2 - Get a Record by ID")
    print("3 - Create a Record")
    print("4 - Update a Record")
    print("5 - Delete a Record")
    print("x - Exit application")

    # Check that the entered value is one of the menu options
    choice = input("Choice: ")
    if choice not in choices:
        choice = '0'
    return choice

def main():

    run = True
    while (run):
        choice = apm.do_menu()
        match choice:

            case 'x':
                print("Exiting...")
                run = False

            case '0':
                # Just let the menu display again, per specification
                pass

            case '1':
                choice = input("\nEnter Country : ")
                cbc.cities_by_country(choice)

            case '2':
                result = False
                while not result:
                    choice = input("\nEnter City ID : ")
                    if choice.isdigit():
                        result = cp.city_population(choice)
                    else:
                        print("Not a valid City ID")

            case '3':
                print("Add New Person")
                print("---------------")
                # ID is a primary key, but not auto-incremented
                id = input("ID : ")
                name = input("Name : ")
                age = input("Age : ")
                salary = input("Salary : ")
                city = input("City : ")
                
                if id.isdigit():
                    ap.add_person(id, name, age, salary, city)
                else:
                    print("Error: ID must be an integer")

            case '4':
                success = False
                delete_id = input("Enter ID of Person to Delete : ")
                success = dp.delete_person(delete_id)
                if success:
                    print("Person ID:", delete_id, "deleted")
                # Error handling will be done in the function

            case '5':
                # Loop until the user enters one of <, >, =, and a valid integer population
                proceed = False
                gle_options = ('<','>','=')
                print("Countries by Pop")
                print("----------------")

                while not proceed:
                    gle = input("Enter < > or = : ")
                    if gle in gle_options:
                        proceed = True

                proceed = False

                while not proceed:
                    pop = input("Enter population : ")
                    if pop.isdigit():
                        proceed = True
                cpl.country_pop(gle, pop)




            case _:
                # Catch-all for entries other than the ones listed above
                print("Invalid entry, exiting...")
                run = False

if __name__=="__main__":
    main()
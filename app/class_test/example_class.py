from class_usr_serch import UserDatabase
#from "filename" without ".py" import "class_name"
#you need to use "from classes import . או קלאס ספסיפי במקרה ועובדים רק עליו"

# Example usage:
db = UserDatabase()

# Search by first name
search_by_first_name = input("Enter the first name to search: ")
results = db.get_by_name(search_by_first_name)

if results:
    print("Matching users by first name:")
    for result in results:
        user_id, first_name, last_name = result
        print(f"ID: {user_id}, First Name: {first_name}, Last Name: {last_name}")
else:
    print("No matching records found for the provided first name.")

# Close the database connection
db.close_connection()

#db.the def name בשביל להשתמש בפונקציה שאנחנו צריכים
#db = "class_name" בגלל זה אנחנו קוראים לו ד.ב. נקדוה השם של הפונקציה
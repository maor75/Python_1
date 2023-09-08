from class_usr_serch import UserDatabase



# Example usage:
db = UserDatabase()

# Search by first name
search_first_name = input("Enter the first name to search: ")
results = db.get_by_name(search_first_name)

if results:
    print("Matching users by first name:")
    for result in results:
        user_id, first_name, last_name = result
        print(f"ID: {user_id}, First Name: {first_name}, Last Name: {last_name}")
else:
    print("No matching records found for the provided first name.")

# Close the database connection
db.close_connection()
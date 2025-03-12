import re

def validate_query(query):
    # Validate the input query to ensure it only contains alphanumeric characters, spaces, 
    # question marks, periods, commas, and hyphens.
    if re.match("^[a-zA-Z0-9\s\?\.\,\-]+$", query):
        return True
    return False

def main():
    # Prompt the user to enter a query
    query = input("Enter your query: ")
    
    # Validate the entered query
    if validate_query(query):
        # If the query is valid, print a confirmation message
        print("Valid query")
    else:
        # If the query is invalid, print an error message
        print("Invalid query")

if __name__ == "__main__":
    main()

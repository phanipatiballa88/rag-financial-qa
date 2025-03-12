import re

def validate_query(query):
    if re.match("^[a-zA-Z0-9\s\?\.\,\-]+$", query):
        return True
    return False

def main():
    query = input("Enter your query: ")
    if validate_query(query):
        print("Valid query")
    else:
        print("Invalid query")

if __name__ == "__main__":
    main()
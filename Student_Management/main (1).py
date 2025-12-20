from database import add_student, view_students, search_student

FILE_PATH = './students.csv'

def main():
    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter name: ")
            id = input("Enter ID: ")
            department = input("Enter department: ")
            add_student(FILE_PATH, name, id, department)

        elif choice == '2':
            data = view_students(FILE_PATH)
            print("\n", data)

        elif choice == '3':
            id = input("Enter ID to search: ")
            search_student(FILE_PATH, id)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

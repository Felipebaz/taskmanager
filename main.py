def main ():
    while True:
        print("\n -- Intelligent Task Manager --")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                pass
            case "2": 
                pass
            case "3":
                pass
            case "4": 
                pass
            case "5":
                print("Exiting the Task Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
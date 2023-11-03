from movies import Movies

movies = Movies('./movies.txt')

def main():
    while True:
        print("\nMenu:")
        print("q: Quit")

        choice = input("Enter your choice: ")

        if choice == "q":
            print("Qutting")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

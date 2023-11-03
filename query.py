from movies import Movies


movies = Movies('./movies.txt')


def main():
    while True:
        print("\nMenu:")
        print("q: Quit")
        print("list: List all movie names")
        choice = input("enter your choice: ")


        if choice == "q":
            print("Quiting...")
            break
        elif choice == "list":
            list_all_movie_names()
       
        else:
            print("Invalid option, try again.")


def list_all_movie_names():
    print("Listing all movie names:")
    [print(movie_info['name']) for movie_info in movies._movies]




if __name__ == "__main__":
    main()




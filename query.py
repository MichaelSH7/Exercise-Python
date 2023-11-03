from movies import Movies


movies = Movies('./movies.txt')


def main():
    while True:
        print("\nMenu:")
        print("q: Quit")
        print("list: List all movie names")
        print("sn: Search movies by name")



        choice = input("enter your choice: ")


        if choice == "q":
            print("Quitting...")
            break
        elif choice == "list":
            list_all_movie_names()
        elif choice == "sn":
            keyword = input("type to search for movies by name: ")
            movies_by_name(keyword)
        else:
            print("Invalid option, try again.")


def list_all_movie_names():
    print("Listing all movie names:")
    [print(movie_info['name']) for movie_info in movies._movies]


def movies_by_name(keyword):
    matching_movies = [movie_info['name'] for movie_info in movies._movies if keyword.lower() in movie_info['name'].lower()]
    print("Matches:")
    [print(movie) for movie in matching_movies]





if __name__ == "__main__":
    main()




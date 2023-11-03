from movies import Movies


movies = Movies('./movies.txt')


def main():
    while True:
        print("\nMenu:")
        print("q: Quit")
        print("list: List all movie names")
        print("sn: Search movies by name")
        print("sc: Search movies by cast")


        choice = input("enter you choice: ")


        if choice == "q":
            print("Quitting...")
            break
        elif choice == "list":
            list_all_movie_names()
        elif choice == "sn":
            keyword = input("type to search for movies by name: ")
            movies_by_name(keyword)
        elif choice == "sc":
            keyword = input("type to search for movies by cast: ")
            movies_by_cast(keyword)
        else:
            print("Invalid option, try again.")


def list_all_movie_names():
    print("Listing all movie names:")
    [print(movie_info['name']) for movie_info in movies._movies]


def movies_by_name(keyword):
    matching_movies = [movie_info['name'] for movie_info in movies._movies if keyword.lower() in movie_info['name'].lower()]
    print("Matches:")
    [print(movie) for movie in matching_movies]


def movies_by_cast(keyword):
    matching_movies = [movie_info['name'] for movie_info in movies._movies if any(keyword.lower() in actor.lower() for actor in movie_info['cast'])]
    matching_actors = [actor for movie_info in movies._movies for actor in movie_info['cast'] if keyword.lower() in actor.lower()]
    print("Matches:")
    [print(movie) for movie in matching_movies]
    print("Matching actors/actresses:")
    [print(actor) for actor in matching_actors]


if __name__ == "__main__":
    main()




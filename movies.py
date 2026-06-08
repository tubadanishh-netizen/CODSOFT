#we need the two built-in python tools
#urllib.request=fetches data from the internet and json reads the data that comes back
import urllib.request
import json

#key that proves we're allowed to use TMDB
API_KEY="658cb6354797b100d46fa931ff2ce06b"

#TMDB doesn't understand words like horror or action, instead it uses numbers (genres IDs)
#So this dictionary translates genre names to genre id numbers. E.g.- User types 'action', we send 28
#to TMDB
GENRES={
    "action":28,
    "comedy":35,
    "drama":18,
    "horror":27,
    "romance":10749,
    "sci-fi":878,
    "thriller":53,
    "animation":16,
    "fantasy":14,
    "adventure":12,
    "mystery":9648,
    "crime":80
    }
#This function takes a genre name and fetches movies from TMDB
def get_movies(genre_name):
    genre_name=genre_name.lower().strip()
    #checks if the genre_name exists in our dictionary but if user types 'bollywood', it won't be found
    if genre_name not in GENRES:
        return None
    genre_id=GENRES[genre_name]
    #building the TMDB website link & asking TMDB: give me movies of this genre and sort it by the
    #most popular ones.
    url=f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}&sort_by=popularity.desc"
    #try block fetches movie-if anything goes wrong, control will go to except
    try:
        #open the url and get response
        response=urllib.request.urlopen(url)
        #converts response into python readable data
        data=json.loads(response.read())
        #since TMDB returns several movies and we only want first 10
        #so [:10] means 'give me items from start up to position 10' using slice concept
        movies=data["results"][:10]
        #Sends the movie list back to whoever called this function
        return movies
    except: #if something went wrong (no internet connection or wrong API key,etc),this block
        #will catch it
        return None
    
#MAIN FUNCTION RUNNING THE PROGRAM
def main():
    print("Welcome to the Movie Recommender!")
    print("Available genres:",",".join(GENRES.keys()))#.keys only gets the names from dict &
    #",".join()puts commas between them for clean display
    print()

    #keep asking the user for input until they type quit forever
    while True:
        user_input=input("Enter a genre (or 'quit' to exit):").lower()
        #if user types quit,stop the loop
        if user_input=="quit":
            print("Goodbye!")
            break
        #call get_movies function with what user typed & store the result in movies variable
        movies=get_movies(user_input)
        if movies is None:
            print("Genre not found! Try from the list above.\n")
        else:
            print(f"\nTop 10 {user_input} movies:\n")
            #enumerate gives us a counter (i) starting from 1
            #so we get a numbered list: 1.Movie, 2. Movie etc
            for i, movie in enumerate(movies,1):
                #Extract just the title from the movie data
                title=movie["title"]
                #Extract the rating score
                rating=movie["vote_average"]
                #extract just the year from full date "2023-05-12"
                #[:4] means take only 4 characters = "2023"
                year=movie["release_date"][:4]
                #print each movie separately
                print(f"{i},{title},{year} - Rating: {rating}/10")
            print()
#start the program
main()                     
        

import csv
from importlib.resources import contents

movie_path = "data/movies.csv"
movie_path_semicolon = "data/movies_semicolon.csv"

# CSV READING

# ,

def csv_read():
    with open(movie_path, mode="r") as file:
        movies = csv.reader(file, delimiter=",")

        for movie in movies:
            print(movie)

def csv_read_semicolon():
    with open(movie_path_semicolon, mode="r") as file:
        movies = csv.reader(file, delimiter=";")

        for movie in movies:
            print(movie)

"""
Dialect is a format for reading csv files.
"""

def csv_read_dialect():
    csv.register_dialect(
        "normal_read",
        delimiter=",",
        quoting=csv.QUOTE_MINIMAL
    )

    with open(movie_path, "r") as file:
        movies = csv.reader(
            file,
            dialect="normal_read"
        )

        for movie in movies:
            print(movie)

def csv_sniffer():
    with open(movie_path, "r") as file:
        content = file.read()
        has_reader = csv.Sniffer().has_header(content)
        print("CSV Has Valid Reader:", has_reader)

        dialect = csv.Sniffer().sniff(content)
        print("Delimeter:", dialect.delimiter)

movie_to_add = ["1","The Shawshank Redemption","1994","R","14 Oct 1994","142 min","Crime, Drama","Frank Darabont","Stephen King (short story ""Rita Hayworth and Shawshank Redemption""), Frank Darabont (screenplay)","Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler","Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.","English","USA","Nominated for 7 Oscars. Another 19 wins & 30 nominations.","https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX300.jpg","Internet Movie Database","9.3/10","80","9.3","1,825,626","tt0111161","movie","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","http://www.rottentomatoes.com/m/shawshank_redemption/","27 Jan 1998","N/A","Columbia Pictures","N/A","True"]

def csv_write():
    with open(movie_path, "a", newline="") as file:
        writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_ALL)
        writer.writerow(movie_to_add)

def csv_copy():
    new_movie_path = "data/movies_copy.csv"

    # create the new file
    open(new_movie_path, "x")

    with open(movie_path, "r") as movies, open(new_movie_path, "a", newline="") as movies_copy:
        movies_to_copy = csv.reader(movies)

        writer = csv.writer(movies_copy, quoting=csv.QUOTE_ALL)

        for movie in movies_to_copy:
            writer.writerow(movie)
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

# with open("movies.csv", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")

    """ if you want to extract in csv just rename them as movies.txt to movies.csv """
""" Initially movies.txt file is not created but when you run the program movies.txt file is created with top 100 movies. """

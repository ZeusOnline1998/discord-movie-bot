from page import *
from scraper import *


def details(movie_search_name):

    #Get Movie Url
    movie_url = search_query_url(movie_search_name)
    movie_info = {}
    # Get Movie Soup
    movie_page_data = get_url_data(movie_url)
    movie_soup = get_soup(movie_page_data)

    # time.sleep(1)

    # movie_section = movie_soup.find('section',class_='header poster')
    
    # Get Movie Title
    movie_title = movie_name(movie_soup)
    # print(movie_title)

    # Get Movie Ratings
    ratings = movie_ratings(movie_soup)
    # print(ratings)

    # Get Movie Genres 
    genre = movie_genres(movie_soup)
    # print(genre)

    # Get Movie Release Date 
    release_date = movie_release_date(movie_soup)
    # print(release_date)

    # Get Movie Runtime 
    runtime = movie_runtime(movie_soup)
    # print(runtime)

    # Get Movie Director 
    director = movie_director(movie_soup)
    # print(director)

    movie_info = {
        'Name': movie_title,
        'Rating': ratings,
        'Genre': genre,
        'Release Date': release_date,
        'Runtime': runtime,
        'Director': director,
        'Url': movie_url
    }

    return movie_info
    
    # print(movie_name(soup))
    # print(movie_director(soup))
    # print(movie_genres(soup))
    # print(movie_ratings(soup))
    # print(movie_runtime(soup))
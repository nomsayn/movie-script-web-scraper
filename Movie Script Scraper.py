import Scraper_Functions as scraper_functs

website_url = "https://subslikescript.com/movie/The_Matrix-133093"

if website_url == "":
    website_url = scraper_functs.get_url_from_user()

soup = scraper_functs.get_website_html_code(website_url)

# save the HTML code to a file
scraper_functs.save_html_to_file(soup)

# get the movie title and script from the HTML code within soup object
title_of_movie, movie_script = scraper_functs.get_movie_script(soup)

print(f"\nMovie Title:\t{title_of_movie}")

# save the movie script to a file
scraper_functs.save_script_to_file(title_of_movie, movie_script)


# if the movie is "The Matrix", count the # of times Neo is mentioned by his name
#  and the # of times he is called "The One"
if "The Matrix" in title_of_movie:
    scraper_functs.count_neos(movie_script)
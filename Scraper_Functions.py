from bs4 import BeautifulSoup
import requests

DISALLOWED_FILENAME_CHARS = ['|', '?', '*', '<', '>', ':', '"', '/']


### remove disallowed characters from the file name
def remove_disallowed_filename_chars(file_name):
    for character in DISALLOWED_FILENAME_CHARS:
        file_name = file_name.replace(character, '-')

    return file_name

def get_url_from_user():
    website_url = input("Enter the URL of the movie script from the website\n"
                        "  'subslikescript.com' that you want to scrape: ")
    return website_url

### takes in a website URL and returns HTML code as a beautiful soup object
def get_website_html_code(website_url):
    request_response = requests.get(website_url)
    url_content = request_response.text
    soup = BeautifulSoup(url_content, 'html.parser')

    return soup


### takes the HTML code as beautiful soup object and saves it to a file
def save_html_to_file(html_code):
    # get the title of the HTML code from soup object
    file_name = html_code.find('title').get_text().replace(' ', '_')

    # limit the length of the file name to 45 characters
    if len(file_name) > 45:
        file_name = file_name[:45]
        file_name = file_name + '.html'

    file_name = remove_disallowed_filename_chars(file_name)

    # prettify changes the HTML code to be more readable
    writeable_html_code = html_code.prettify()

    with open(file_name, 'w') as file:
        file.write(writeable_html_code)


### Takes the HTML code as beautiful soup object and returns the movie title and script text
def get_movie_script(html_soup):
    # Finds the root of the data in the HTML code.
    #  class_ in the find method has an underscore to differentiate it from the class keyword
    root_of_data = html_soup.find('article', class_='main-article')
    title_of_movie = root_of_data.find('h1').get_text()

    # data is found by identifying the HTML element that contains the movie script.
    # The HTML Element has the tag, "div" and the class "full-script".
    movie_script = root_of_data.find('div', class_='full-script').get_text()

    return title_of_movie, movie_script

def save_script_to_file(title_of_movie, movie_script):
    title_of_movie = remove_disallowed_filename_chars(title_of_movie)

    with open(f"{title_of_movie}.txt", 'w') as file:
        file.write(title_of_movie)
        file.write("\n")
        file.write(movie_script)

# count # of times Neo is mentioned by his name and # of times he is called "The One" in the movie script
def count_neos(movie_script):
    number_of_neos = movie_script.lower().count("neo")
    number_of_The_Ones = movie_script.lower().count("the one")

    print(f"\n# of times Neo is mentioned by his name :\t {number_of_neos}")
    print(f"# of times Neo is called 'The One' :\t\t {number_of_The_Ones}")
from bs4 import BeautifulSoup
import requests

### STEP 0: Follow along by opening this Google Doc:
# https://docs.google.com/document/d/1Vuj0rvVYVv5XRkfKR1CA9b-Hdv9lsB18CawGXoQGkyU/edit#

### STEP 1: DOWNLOAD ALL THE HTML OF A WEBSITE
WEBSITE_URL = 'http://miniature-calendar.com/2017/09/'
response = requests.get(WEBSITE_URL)

### STEP 2: USE BEAUTIFULSOUP TO CREATE AN OBJECT THAT ALLOWS US TO SEARCH THE HTML
soup = BeautifulSoup(response.text, "lxml")


### STEP 3: USE REQUESTS AND BEAUTIFULSOUP TO WRITE USEFUL FUNCTIONS
def get_links(soup):
    """
    This function takes in a Soup object and returns a list of urls of images.
    For example:

        >>> links = get_links(soup)
        >>> print(links)
        >>> ['http://miniature-calendar.com/wp-content/uploads/2017/09/170901fri-250x250.jpg',
             'http://miniature-calendar.com/wp-content/uploads/2017/09/170902sat-250x250.jpg',
             'http://miniature-calendar.com/wp-content/uploads/2017/09/170903sun-250x250.jpg' ... ]
    """
    # NOTE: You need to modify the code in this function if you want to download
    # other types of files or if the HTML of the website you're scraping looks different.
    links = soup.find_all("img")
    return links

def download_image(url):
    """
    This function takes in a url of an image and saves the image to a specific folder

    For example:

        >>> url = 'http://miniature-calendar.com/wp-content/uploads/2017/09/170901fri-250x250.jpg'
        >>> download_image(url)
        >>> # Now, a file named 170901fri-250x250.jpg should have been downloaded to my Desktop folder
    """
    image = requests.get(url)
    filename = get_filename_from_url(url)
    # NOTE: You will have to modify the code below since it's specific to my computer
    with open('/Users/cshan/Desktop/tempdir/' + filename, 'wb') as f:
        f.write(image.content)

def get_filename_from_url(url):
    """
    This function takes a url and returns the filename.
    For example:

        >>> url = 'http://miniature-calendar.com/wp-content/uploads/2017/09/170901fri-250x250.jpg'
        >>> filename = get_filename_from_url(url)
        >>> print(filename)
        >>> '170901fri-250x250.jpg'
    """
    split = url.split('/') # this splits a string on a character and returns a list
    name = split[-1]
    return name


def download_all_images(soup):
    """
    This is the main function where I use all of my other functions to
    actually download all the images.
    """
    all_image_links = get_links(soup)
    for url in all_image_links:
        download_image(url)


### STEP 4: ACTUALLY USE OUR FUNCTIONS TO GET THE IMAGES
download_all_images(soup)

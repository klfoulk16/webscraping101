def example1():
    """
    Extracts title from simple webpage
    """
    from urllib.request import urlopen
    # open url
    url = "http://olympus.realpython.org/profiles/aphrodite"
    page = urlopen(url)

    # extract html from the page
    html_bytes = page.read()
    # decode the bytes to a string using UTF-8
    html = html_bytes.decode('utf-8')

    # .find() returns the index of the first occurrence of a substring
    title_index = html.find('<title>')
    print('title_index', title_index)

    start_index = title_index + len("<title>")
    print('start_index', start_index)

    end_index = html.find("</title>")
    print('end_index', end_index)

    # you can extract the title by slicing the html string
    title = html[start_index:end_index]
    print('title', title)

def example2():
    """
    Example of what happens when .find() can't find the exact string you're looking for
    """
    from urllib.request import urlopen
    url = "http://olympus.realpython.org/profiles/poseidon"

    page = urlopen(url)
    html = page.read().decode("utf-8")
    print(html)
    start_index = html.find("<title>") + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    print(title)

def exampleRegularExpressions():

    import re
    from urllib.request import urlopen
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    pattern = "<title.*?>.*?</title.*?>"
    match_results = re.search(pattern, html, re.IGNORECASE)
    title = match_results.group()
    title = re.sub("<.*?>", "", title) # Remove HTML tags
    print(title)

def test1():
    from urllib.request import urlopen
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    html = page.read().decode('utf-8')
    #print(html)

    start_name = html.find('Name: ') + len('Name: ')
    end_name = html.find('</h2>')
    name = html[start_name:end_name]
    print(name)

    start_color = html.find('Color: ') + len('Color: ')
    end_color = html.find('\n</center>')
    color = html[start_color:end_color]
    print(color)

# Part Two: Using HTML Parser for Web Scraping in Python

def soupExample1():
    from bs4 import BeautifulSoup as bs
    from urllib.request import urlopen

    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = bs(html, 'html.parser')
    #print(soup.get_text())
    img1, img2 = soup.find_all('img')

    print(img1['src'])

def soupTest():
    """
    Find all links on the page and return their href.
    """
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    url = 'http://olympus.realpython.org/profiles'
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    links = soup.find_all('a')
    base_url = "http://olympus.realpython.org"
    for link in links:
        print(base_url+link['href'])

def mechanicalSoupLogin():
    """
    Log in to a webpage and explore the following page
    """

    import mechanicalsoup
    browser = mechanicalsoup.Browser()
    url = "http://olympus.realpython.org/login"
    page = browser.get(url)
    html = page.soup

    form = html.form
    form.select('input')[0]['value'] = 'zeus'
    form.select('input')[1]['value'] = 'ThunderDude'

    profiles_page = browser.submit(form, page.url)
    print(profiles_page.soup.title)

    links = profiles_page.soup.select("a")

    for link in links:
        address = link['href']
        text = link.text
        print(f'{text}: {address}')

def mechanicalSoupGet():
    import mechanicalsoup

    browser = mechanicalsoup.Browser()

    for i in range(5):
        page = browser.get("http://olympus.realpython.org/dice")
        tag = page.soup.select('#result')[0]
        result = tag.text

        print(f"The result of your dice roll is: {result}")

mechanicalSoupGet()

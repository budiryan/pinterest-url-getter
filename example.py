from pinterest.pinterest import Pinterest


# Constants here
YOUR_EMAIL_ADDRESS = 'bbudihaha@gmail.com'
YOUR_PASSWORD = 'budihaha12345'

if __name__ == '__main__':
    # See this example
    example_queries = ['Jakarta', 'Indonesia', 'Kayak']
    pinterest_scraper = Pinterest(YOUR_EMAIL_ADDRESS, YOUR_PASSWORD)
    # Get the urls
    urls = pinterest_scraper.get_urls(example_queries)
    # Print the urls
    print(urls)

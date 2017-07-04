from pinterest.pinterest import Pinterest
import sys

# Follow this script for a guideline on how to use the library

# I created a dummy pinterest account for you guys, lol
YOUR_EMAIL_ADDRESS = 'bbudihaha@gmail.com'
YOUR_PASSWORD = 'budihaha12345'

if __name__ == '__main__':
    example_queries = sys.argv[1:]
    example_queries = [q.replace("_", " ") for q in example_queries]
    print(example_queries)
    pinterest_scraper = Pinterest(YOUR_EMAIL_ADDRESS, YOUR_PASSWORD)
    # Get the urls
    urls = pinterest_scraper.get_urls(example_queries)
    # Exit gracefully
    pinterest_scraper.finish()
    # Print the urls
    print('The urls are: ')
    print(urls)

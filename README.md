# Dependencies
- Python 3
- Selenium Webdriver
- Chrome Webdriver

# Install Dependencies (sorry its long)
- `sudo apt-get update`
- `sudo apt-get install build-essential libssl-dev libffi-dev python3-dev xvfb python-virtualenv unzip`
- Clone this repository and `cd` into it
- `virtualenv -p python3 env --no-site-packages`
- `pip install -r requirements.txt`
- `wget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip`
- `unzip chromedriver_linux64.zip`
- `chmod +x chromedriver`
- `sudo mv -f chromedriver /usr/local/share/chromedriver`
- `sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver`
- `sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver`


# How to Use
- `source env/bin/activate` 
- `python get_url.py [YOUR LIST OF QUERIES SEPARATED BY SPACE]`

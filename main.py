from selenium import webdriver


# options to make web scraping easier
def get_drver():
  options = webdriver.ChromeOptions()
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-dev-shm-usage')
  options.add_argument('--start-maximized')
  options.add_argument('--disable-infobars')
  options.add_argument('--disable-extensions')
  options.add_argument('--disable-blink-features=AutomationControlled')

  #specify the url
  drver = webdriver.Chrome(options=options)
  drver.get("http://automated.pythonanywhere.com")
  return drver


  #specify what we are scraping from the page
def main():
  drver = get_drver()
  element = drver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
  return element.text


print(main())

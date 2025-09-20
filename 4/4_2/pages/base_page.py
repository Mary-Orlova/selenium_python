class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url


    def open(self):
        self.browser.get(self.url)

    def find_element(self, *args):
        return self.browser.find_element(*args)
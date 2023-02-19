import urllib.request as urllib

#
def fct(url):
    print("Checking the conectivity")
    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print(f"The response code {response.getcode()}")


fct("https://www.google.com/")

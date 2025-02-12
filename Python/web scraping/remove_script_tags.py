# Print HTML code with script tags removed.
# Input: paste the HTML code of the page into the `page` variable.
# Output: standard output.

from bs4 import BeautifulSoup
page = '''

'''
soup = BeautifulSoup(page,'lxml')
for tag in soup.find_all('script'):
    tag.decompose()
print(soup)

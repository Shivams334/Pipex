# Import all the modules 
import webbrowser, sys, requests, bs4
def searchgoogle():
	search_keyword = input("What you want to search")
	if len(sys.argv) > 1:
		search_keyword = ' '.join(sys.argv[1:])
	else:
		keyword = search_keyword
	req = requests.get('http://google.com/search?q=' + keyword)
	req.raise_for_status()
	soup = bs4.BeautifulSoup(req.text, "html.parser")
	linkelem = soup.select('.r a')
	num = min(2, len(linkelem)
	for x in range(0,num):
		webbrowser.open('http://google.com' + linkelem[x].get('href'))

searchgoogle()

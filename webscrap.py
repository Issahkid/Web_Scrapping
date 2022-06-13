from bs4 import BeautifulSoup

with open("nation.africa",'r') as nation_data:
    content = nation_data.read()
    print(content)
soup = BeautifulSoup(content,"lxml")
print(soup.prettify) # see codes in a more pretty way
headlines = soup.find_all("h3") #finds all the headlines and displays them with the help of print statement
print(headlines)
for head in headlines:
    print(head.text)
  

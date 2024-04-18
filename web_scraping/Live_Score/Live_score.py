from requests_html import HTMLSession
import csv 
import requests
from bs4 import BeautifulSoup
import csv

def getdate() :
    global day
    day = input("Plz enter the day\n")
    if int(day) < 10 :
        day = "0"+str(day) 
    global month    
    month = input("Plz enter the month\n")
    if int(month) < 10 :
        month = "0"+str(month) 
    global year
    year = input("Plz enter the year\n")    
getdate()

url= f"https://www.sportinglife.com/football/fixtures-results/{year}-{month}-{day}"
page = requests.get(url)
matchList=[]
matchLinks=[]

src = page.content
soup = BeautifulSoup(src , "lxml")

for a in soup.find_all( 'a'  ,{'data-test-id':"football-live-match-link"} , href=True   ):
    matchLinks.append(a['href'])



def getdetails(link) :
    
    hfurl = "https://www.sportinglife.com"
    
    page2 = requests.get(hfurl+link) 
    src2 = page2.content
    soup2 = BeautifulSoup(src2, "lxml")

    ChampTitle= soup2.find('span' , {'class' : 'SummaryStyles__SummaryLeagueTitle-sc-1cm0pns-2 XxaRa'}).get_text()
    teams = soup2.find_all('span' , {'class' : 'StickyMatchHeaderstyles__StickyMatchHeaderTeamName-zufm40-10 jPrXOi'} , string=True)
   
   
    try :
        score = soup2.find ('div' , {"class":"StickyMatchHeaderstyles__StickyMatchScoreContainer-zufm40-11 bhBQAF"}).get_text()      
    except:
        score = "-:-"
       
    Team1 = teams[0].get_text()
    Team2 = teams[1].get_text()
  
      
    matchList.append( { "ChampionShip" :ChampTitle ,
                  "Team1" : Team1 
                 ,"team2" : Team2  
                 ,"score": score
    
                })
    
for x in matchLinks :
    getdetails(x)    


if not matchLinks :
    print("inpte right date plz")
    getdate()  
keys = matchList[0].keys()

   
   
with open("D:\Projects\web scraping\list.csv" , 'w') as output_file :
    dict_writer = csv.DictWriter(output_file , keys)
    dict_writer.writeheader()
    dict_writer.writerows(matchList)
    print('file created')


















import requests
from datetime import date

response = requests.get('https://api.bseindia.com/BseIndiaAPI/api/Corpforthresults/w')
data = response.json()

today = date.today().strftime('%d %b %Y')

for x in data:
  if x['meeting_date'] == today:
    print(x['Long_Name'])
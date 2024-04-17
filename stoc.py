import requests
from bs4 import BeautifulSoup
import pandas as pd
import yfinance as yf

GameStop = yf.Ticker("GME")
gme_data = GameStop.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head()
url = ("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN"
       "-SkillsNetwork/labs/project/stock.html")

html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html5lib")

gme_revenue = pd.DataFrame(columns=['Date', 'Revenue'])

for table in soup.find_all('table'):

    if ('GameStop Quarterly Revenue' in table.find('th').text):
        rows = table.find_all('tr')

        for row in rows:
            col = row.find_all('td')

            if col != []:
                date = col[0].text
                revenue = col[1].text.replace(',', '').replace('$', '')

            #   gme_revenue = gme_revenue.append({"Date": date, "Revenue": revenue}, ignore_index=True)

print(gme_revenue.tail())


def make_graph():
    var = (tesla_data, tesla_revenue, 'Tesla')


# var = (gme_data, gme_revenue, 'GameStop Stock Data Graph')

make_graph()

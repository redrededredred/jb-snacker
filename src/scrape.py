# Scraping functions here
import datetime
import requests
from tabula import read_pdf

BASE_URL = "https://www.jugendgaestehaus-johannesburg.de/fileadmin/user_upload/"
#menu = "speisenplan_jgh_kw23.pdf"
current_date = datetime.datetime.now()
current_calender_week = current_date.month * 4
menu_url = f"{BASE_URL}speisenplan_jgh_kw{current_calender_week}.pdf"

if __name__ == "__main__":
  print("(+) - Running tests!")
  data = "data.pdf"
  with open(data, "wb") as f:
    f.write(requests.get(menu_url).content)
  dfs = tabula.read_pdf("data.pdf", pages='all')

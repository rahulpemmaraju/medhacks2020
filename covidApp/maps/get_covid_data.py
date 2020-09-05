import numpy as np
import requests
import csv

#needed in order to read from the url
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

#urls for the daily cases and deaths
daily_cases_url="https://enigmaforensics.com/covid-19/us/state/NewJersey_Cases_Delta_By_Date.csv"
daily_deaths_url="https://enigmaforensics.com/covid-19/us/state/NewJersey_Deaths_Delta_By_Date.csv"

#read the cases
cases= requests.get(daily_cases_url, headers=header)
decoded_cases = cases.content.decode('utf-8')

#read the deaths
deaths= requests.get(daily_deaths_url, headers=header)
decoded_deaths = deaths.content.decode('utf-8')

#convert the cases to an array
casereader = csv.reader(decoded_cases.splitlines(), delimiter=',')
cases_list = np.asarray(list(casereader))

#convert the deaths to an array
deathreader = csv.reader(decoded_deaths.splitlines(), delimiter=',')
deaths_list = np.asarray(list(deathreader))

#clean arrays
cases_list = np.delete(cases_list, (16,21), axis=0)
deaths_list = np.delete(deaths_list, (16,21), axis=0)
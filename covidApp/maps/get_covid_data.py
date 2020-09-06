import numpy as np
import requests
import csv

def sum_minus_fourteen(input):
  output=np.zeros(input.shape)
  for i in range(output.shape[0]):
    for j in range(output.shape[1]):
      if (j>0):
        output[i][j]=input[i][j]+output[i][j-1]
        if(j>=14):
          output[i][j]=max(0,output[i][j]-output[i][j-14])
      else:
        output[i][j]=input[i][j]
  return output

def read_data():
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

  return cases_list,deaths_list

#outputs all of the data in alphabetical order: population (N), cases, deaths
def clean_data():
  pops=np.array([265429,936692,445384,507078,92560,150972,799767,291408,
      676061,124714,369811,829685,621354,494228,
      601651,503310,62607,331164,140799,558067,105779])

  cases,deaths=read_data() #both in alphabetical order

  case_data=np.asarray(cases[1:,1:]) #remove dates and names *dates start at 3/24
  case_data= case_data.astype(int) #convert to int
  case_data=sum_minus_fourteen(case_data) #convert to cumulative sum: but subtracts 14 days prior for recovery

  death_data=np.asarray(deaths[1:,1:]) #remove dates and names *dates start at 3/24
  death_data= death_data.astype(int) #convert to int
  death_data=sum_minus_fourteen(death_data) #convert to cumulative sum: but subtracts 14 days prior for recovery

  return pops,case_data,death_data 


def read_all_data():
  pops=np.array([265429,936692,445384,507078,92560,150972,799767,291408,
      676061,124714,369811,829685,621354,494228,
      601651,503310,62607,331164,140799,558067,105779])

  results = []
  with open("./cases.csv") as csvfile:
      reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
      for row in reader: # each row is a list
          results.append(row)

  return results
import csv
import requests
from time import sleep
import pandas as pd
import dns.resolver
import sys
from datetime import date
arg = sys.argv[1]
currentline = 0
try:
        df = pd.read_csv(arg)
except:
        print('Wrong filename or usage.')
        print('correct: py start.py "filename.csv"')
        exit()
today = date.today()


def whois(str):
        rvalue = requests.get("https://rdap.nic.ch/domain/" + str)
        print(rvalue)
        rspns = rvalue.status_code
        #print(rspns)
        if rspns == 200:
                print("domain already registered")
                df.loc[currentline, 'LASTUNAVAILABLE'] = today
                df.to_csv(arg, index=False)
                #print(df)
                
        else:
                print("domain available")
                df.loc[currentline, 'LASTAVAILABLE'] = today
                df.to_csv(arg, index=False)
                #print(df)

for row in df.values:
        print(row)
        print(currentline)
        try:
                result = dns.resolver.resolve(row[0], 'NS')
                #print(result)
                print (row[0] + " already registered")
                #for val in result:
                        #print('The NS Record is : ', val.to_text())
                df.loc[currentline, 'LASTUNAVAILABLE'] = today
                df.to_csv(arg, index=False)
                #print(df)
                        
        except:
                print("no nameservers found for: " + row[0])
                print("trying whois request")
                whois(row[0])
                
        sleep(1)
        currentline = currentline + 1

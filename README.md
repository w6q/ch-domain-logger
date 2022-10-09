# ch-domain-logger
Checking availability of .ch is normally a little tricky so i made this tool to bulk check .ch domains using nslookup + whois and log results in a csv file.


## Requirements
- Pandas  `pip install pandas`
- Dnspython  `pip install dnspython`

## Usage
Make sure to close the csv file before running the script!

`py main.py "filename.csv"`
after script finished checking domains you can open the csv file.

csv file should be structured like this:
![image](https://user-images.githubusercontent.com/46498087/194782034-677f5110-d504-4bf8-9ff0-4d2bf1e2e492.png)



### Todos
- Add proxy support
- Add auto buy mode using openprovider api
### USE AT YOUR OWN RISK

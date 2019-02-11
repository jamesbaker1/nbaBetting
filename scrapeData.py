import requests
import pandas as pd
import re

team_stats_page = "http://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=10%2F17%2F2017&DateTo="

team_stats_page2 = "&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision="

beginningDate = "12%2F" + "01" + "%2F2018"

url = team_stats_page + beginningDate + team_stats_page2
user_agent = {'User-agent': 'Mozilla/5.0'}

# print(data)

# DAY BEFORE FOR MODEL
novemberData = []
full_cols = []

for i in range(1, 32):
    if i < 10:
        day = "0" + str(i)
        beginningDate = "11%2F" + day + "%2F2017"
        fileName = day + ".csv"
    else:
        beginningDate = "11%2F" + str(i) + "%2F2017"
        fileName = str(i) + ".csv"
    print(fileName)
    url = team_stats_page + beginningDate + team_stats_page2
    resp = requests.get(url, headers = user_agent)
    try:
        data = resp.json()
        cols = data["resultSets"][0]["headers"]
        cols.append("DATE")
        rows = data["resultSets"][0]["rowSet"]
        for i in rows:
            i.append(re.sub("%2F", "", beginningDate))
        # df = pd.DataFrame(rows,columns=cols)
        # df.to_csv(fileName)
        novemberData.extend(rows)
        full_cols = cols
    except:
        break
        # print("lmao something went wrong")
        # print(e)
    # finally:
    #     break
df = pd.DataFrame(novemberData,columns=full_cols)
df.to_csv("november2017.csv")

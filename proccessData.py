import pandas as pd
from datetime import datetime


# before_game_data = pd.read_csv("./november.csv")
#
# print(before_game_data.head())

# box_score = pd.read_csv("./2017-18_officialBoxScore.csv")
game_results = pd.read_csv("./november_results.csv")
team_stats = pd.read_csv("./november.csv")
game_results = game_results[["Date","Visitor/Neutral", "Home/Neutral","PTS","PTS.1"]]
game_results["Home Team Wins"] = game_results["PTS.1"] > game_results["PTS"]
game_results["Date"] = pd.to_datetime(game_results['Date'])
game_results["Date"] = game_results["Date"].dt.strftime('%m%d%Y')
team_stats["DATE"] = team_stats["DATE"].astype(int)
game_results["Date"] = game_results["Date"].astype(int)
#  Need the day before stats!
team_stats["DATE"] = team_stats["DATE"] - 10000


# print(game_results.head())
# print()
# print(game_results.dtypes)
# print(team_stats.dtypes)


# print(game_results.head())
count = 0
for index, row in game_results.iterrows():
    if count > 20:
        break
    home_team_stats = team_stats[(team_stats['TEAM_NAME'] == row["Home/Neutral"]) & (team_stats["DATE"] == row["Date"])]
    print(home_team_stats)

    home_team_stats = home_team_stats[["W_PCT", "FG_PCT", "FG3_PCT", "OREB", "DREB", "AST", "TOV", "STL", "BLK", "PTS"]]
    home_team_stats.rename(columns=lambda x: "HOME_" + x, inplace=True)

    away_team_stats = team_stats[(team_stats['TEAM_NAME'] == row["Visitor/Neutral"]) & (team_stats["DATE"]== row["Date"])]
    away_team_stats = home_team_stats[["W_PCT", "FG_PCT", "FG3_PCT", "OREB", "DREB", "AST", "TOV", "STL", "BLK", "PTS"]]
    away_team_stats.rename(columns=lambda x: "AWAY_" + x, inplace=True)

    print(home_team_stats)
    # print(away_team_stats)
    # home_team_stats = home_team_stats[["Date","Visitor/Neutral", "Home/Neutral","PTS","PTS.1"]]
    break
    # away_team_stats = team_stats[team_stats['C']>1]
# print(game_results.iloc(0)[0][0])
# print(team_stats.head())
# print(team_stats.head())

# opptPTS
# opptDayOff
# teamPTS
# teamDayOff
# gmDate
# gmTime?
# teamRslt?


# W_PCT
# FG_PCT
# FG3_PCT
# OREB
# DREB
# AST
# TOV
# STL
# BLK
# PTS




# use matchup data to determine team result
# clean data
# box_score_what_I_need = box_score[["teamAbbr", "opptAbbr","gmDate","teamRslt"]]
# box_score_what_I_need = box_score_what_I_need.drop_duplicates()
# box_score_what_I_need = box_score_what_I_need.apply(lambda r: sorted(r), axis = 1).drop_duplicates()
# print(box_score_what_I_need.shape)
#
# rows_i_want = []
# already_seen = {}
# count = 0
#
# for index, row in box_score_what_I_need.iterrows():
#     if row["gmDate"] not in already_seen:
#         already_seen["gmDate"] = set().add((row["teamAbbr"],row["opptAbbr"]))
#         rows_i_want.append(row)
#     else:
#         if (row["opptAbbr"],row["teamAbbr"]) in already_seen["gmDate"]:
#             continue
#         else:
#             already_seen["gmDate"].add((row["teamAbbr"],row["opptAbbr"]))
#             rows_i_want.append(row)
# print(len(rows_i_want))

import csv
import numpy as np 
import pandas as pd 

#1
with open("players.csv","r") as file:
    reader=file.read()
    print(reader)
    
#2
with open("players.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
        
#3
with open("players.csv","r") as file:
    reader=file.readlines()
print("Players Count:",len(reader)-1)

#4
with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    high=0
    scorerh=""
    for row in reader:
        if int(row[4])>high:
            high=int(row[4])
            scorerh=row[1]
            
print("Highest run scorer:",scorerh)    

#5
with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    low=high
    scorerl=''
    for row in reader:
        if int(row[4])<low:
            low=int(row[4])
            scorerl=row[1]
print("Lowest run scorer:",scorerl)
            
            
#6
with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    sum1=0
    cnt=0
    for row in reader:
        sum1+=int(row[4])
        cnt+=1
    avg=sum1/cnt
print("Average run score:",avg)

#7
with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    print("Players more than 600 runs:")
    for row in reader:
        if int(row[4])>600:
            print(row[1])
            
#8
with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    print("Players less than 500 runs:")
    for row in reader:
        if int(row[4])<500:
            print(row[1])
            
#9
with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    player_team={}
    for row in reader:
        team=row[2]
        if team in player_team:
            player_team[team]+=1
        else:
            player_team[team]=1
print("Count of players by team :",player_team)

#10
with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    team_runs={}
    for row in reader:
        team=row[2]
        run=int(row[4])
        if team in team_runs:
            team_runs[team]+=run
        else:
            team_runs[team]=run
print("Total runs by team :",team_runs)

#11
print("Highest runs team :",max(team_runs, key=team_runs.get))

#12
print("Lowest runs team :",min(team_runs, key=team_runs.get))

#13
with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    high=0
    scorerF=""
    for row in reader:
        if int(row[5])>high:
            high=int(row[5])
            scorerF=row[1]
print("Player with most four:",scorerF)
            

#14
with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    high=0
    scorerS=""
    for row in reader:
        if int(row[6])>high:
            high=int(row[6])
            scorerS=row[1]
print("Player with most sixes:",scorerS)
            
#15
with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    totF=0
    for row in reader:
        totF+=int(row[5])
print("Total Fours:",totF)

#16
with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    totS=0
    for row in reader:
        totS+=int(row[6])
print("Total Sixes:",totS)

#17
with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    players=[]
    for row in reader:
        players.append(row[1])
    players.sort()
print("Players :",players)

#18
with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    teams=set()
    for row in reader:
        teams.add(row[2])
print("Teams :",teams)

#19
print("Teams dictionary",team_runs)

#20
with open("players.csv","r") as file:
    reader= csv.reader(file)
    next(reader)
    player_run={}
    for row in reader:
        player=row[1]
        run=int(row[4])
        if player in player_run:
            player_run[player]+=run
        else:
            player_run[player]=run
print("Players with runs :",player_run)

#21
def find_top_scorer():
    print("Top Scorer :",max(player_run, key=player_run.get))
find_top_scorer()

#22
def calculate_average_runs():
    with open("players.csv","r") as file:
        reader=csv.reader(file)
        next(reader)
        sum1=0
        cnt=0
        for row in reader:
            sum1+=int(row[4])
            cnt+=1
    return sum1/cnt
print("Average runs:",calculate_average_runs())

#23
def find_best_team():
    return max(team_runs,key=team_runs.get)
print("The best team :",find_best_team())

#24
def find_total_boundaries():
    with open("players.csv","r") as file:
        reader=csv.reader(file)
        next(reader)
        tot=0
        for row in reader:
            tot+=int(row[5])
    return tot
print("Total boundaries:",find_total_boundaries())

#25
try:
    with open("players.csv","r"):
        print("File opened")
except FileNotFoundException:
    print("players.csv file not found")
    
#26
try:
    with open("players.csv","r") as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            runs=int(row[4])
    print("Runs read susscessfully")
except ValueError:
    print("Invalid run value found")
    
#27
try:
    with open("players.csv","r") as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            matches=int(row[3])
    print("Matches read susscessfully")
except ValueError:
    print("Invalid macth count found")
    
#28
with open("players.csv","r") as file:
        reader=csv.reader(file)
        next(reader)
        lit=[]
        for row in reader:
            lit.append(int(row[4]))

arr=np.array(lit)
print("Numpy total runs",np.sum(arr))
print("Numpy average runs",np.mean(arr))
print("Numpy maximum runs",np.max(arr))
print("Numpy minimum runs",np.min(arr))
print("Numpy STD of runs",np.std(arr))
print("Numpy median of runs",np.median(arr))

#29
pf=pd.read_csv("players.csv")
print(pf)

#30
print(pf.sort_values("runs",ascending=False).head(5))

#31
print(pf.sort_values("runs",ascending=False))

#32
print(pf.groupby("team")["runs"].sum())

#33
print(pf.groupby("team")["runs"].mean())

#34
print(pf[pf["runs"]>600])

#35
tt=pf.groupby("team")["runs"].sum().sort_values(ascending=False)
print("Top team :\n",tt.head(1))

# report generation
with open("cricket_report.txt", "w") as file:
    file.write("Total Players : " + str(len(pf)) + "\n")
    file.write("Total Runs : " + str(pf["runs"].sum()) + "\n")
    file.write("Average Runs : " + str(pf["runs"].mean()) + "\n")
    file.write("Highest Scorer : " + str(pf.loc[pf["runs"].idxmax(), "player_name"]) + " - " + str(pf["runs"].max()) + "\n")
    file.write("Lowest Scorer : " + str(pf.loc[pf["runs"].idxmin(), "player_name"]) + " - " + str(pf["runs"].min()) + "\n\n")

    file.write("Team Wise Runs\n")
    file.write(str(pf.groupby("team")["runs"].sum()) + "\n\n")

    file.write("Top 5 Players\n")
    file.write(str(pf.sort_values("runs", ascending=False).head(5)[["player_name", "runs"]]) + "\n\n")

    file.write("Most Fours\n")
    file.write(str(pf.loc[pf["fours"].idxmax(), "player_name"]) + " - " + str(pf["fours"].max()) + "\n\n")

    file.write("Most Sixes\n")
    file.write(str(pf.loc[pf["sixes"].idxmax(), "player_name"]) + " - " + str(pf["sixes"].max()) + "\n")

print("cricket_report.txt created")

#36
top_players = pf[pf["runs"] > 600]
top_players.to_csv("top_players.csv", index=False)
print("top_players.csv created")

#37
team_summary = pf.groupby("team").agg(
    Total_Runs=("runs", "sum"),
    Average_Runs=("runs", "mean"),
    Player_Count=("player_id", "count")
).reset_index()
team_summary.to_csv("team_summary.csv", index=False)
print("team_summary.csv created")

#38
while True:
    print("\n1. Player Analysis")
    print("2. Team Analysis")
    print("3. Boundary Analysis")
    print("4. Export Reports")
    print("5. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        print("Highest Run Scorer :", scorerh, high)
        print("Lowest Run Scorer :", scorerl, low)
        print("Average Runs :", avg)
        print("Players scoring more than 600 runs :")
        print(pf[pf["runs"] > 600][["player_name", "runs"]])

    elif choice == "2":
        print("Players by Team :")
        print(pf["team"].value_counts())
        print("Total Runs by Team :")
        print(pf.groupby("team")["runs"].sum())
        print("Average Runs by Team :")
        print(pf.groupby("team")["runs"].mean())

    elif choice == "3":
        print("Player with Most Fours :", scorerF, totF)
        print("Player with Most Sixes :", scorerS, totS)
        print("Total Fours :", totF)
        print("Total Sixes :", totS)

    elif choice == "4":
        top_players.to_csv("top_players.csv", index=False)
        team_summary.to_csv("team_summary.csv", index=False)
        print("Reports exported successfully")

    elif choice == "5":
        print("Exited")
        break

    else:
        print("Invalid Choice")

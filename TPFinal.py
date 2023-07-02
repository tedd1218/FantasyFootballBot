#################################################
# TPFinal.py
# 
# Your name: Tedd
# Your andrew id: tyjung
#################################################

import math, copy
import csv
from cmu_112_graphics import *

#csv file categories
playerRank = 0
playerName = 1
playerTeam = 2
playerOpponent = 3
playerMatchup = 4
playerStartorSit = 5
playerProjectedPoints = 6
    
#################################################
# Fantasy Football Bot Viewer
#################################################

##########################################
# Intro Screen Mode (Taken from https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#usingModes)
##########################################

def introScreenMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "OrangeRed2")
    canvas.create_rectangle(20,20,app.width-20,app.height-20, width=5)
    canvas.create_rectangle(30,30,app.width-30,app.height-30, width=3)
    canvas.create_text(app.width/2, 110, text='Welcome to Fantasy Football Bot!',
                       font='Impact 45 bold', fill='black')
    canvas.create_text(app.width/2, 180, text='First choose a position and scoring format \n    then choose a mode you want to view!',
                       font='Impact 20 bold', fill='black')
    canvas.create_text(app.width/2, 240, text='Press any key to begin!',
                       font='Impact 20 bold', fill='black')
    #Image taken from https://www.coastalgolfaway.com/wp-content/uploads/2015/02/fantasy-football.png
    canvas.create_image(app.width/2, app.height/2+100, image=ImageTk.PhotoImage(app.introPic))

def introScreenMode_keyPressed(app, event):
    app.mode = 'positionMode'

##########################################
# Position Mode
##########################################

def positionMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'OrangeRed2')
    canvas.create_rectangle(20,20,app.width-20,app.height-20, width=5)
    canvas.create_rectangle(30,30,app.width-30,app.height-30, width=3)
    canvas.create_text(app.width/2,70, text="Choose A Position",
                       font='impact 45 bold', fill='black')
    canvas.create_rectangle(app.width/3 - 100, 120, app.width/3 + 100, 180, fill = "orange", outline = "black", width = 3)
    canvas.create_text(app.width/3, 150, text="Quarterback",
                       font='impact 30 bold', fill='black')
    canvas.create_rectangle(app.width/3 - 100, 220, app.width/3 + 100, 280, fill = "dark orange", outline = "black", width = 3)
    canvas.create_text(app.width/3, 250, text="Wide Receiver",
                       font='impact 30 bold', fill='black')
    canvas.create_rectangle(app.width/3 - 100, 320, app.width/3 + 100, 380, fill = "coral", outline = "black", width = 3)
    canvas.create_text(app.width/3, 350, text="Running Back",
                       font='impact 30 bold', fill='black')
    canvas.create_rectangle(2*app.width/3 - 100, 120, 2*app.width/3 + 100, 180, fill = "tomato", outline = "black", width = 3)
    canvas.create_text(2*app.width/3, 150, text="Tight End",
                       font='impact 30 bold', fill='black')
    canvas.create_rectangle(2*app.width/3 - 100, 220, 2*app.width/3 + 100, 280, fill = "orange red", outline = "black", width = 3)
    canvas.create_text(2*app.width/3, 250, text="Kicker",
                       font='impact 30 bold', fill='black')
    canvas.create_rectangle(2*app.width/3 - 100, 320, 2*app.width/3 + 100, 380, fill = "red", outline = "black", width = 3)
    canvas.create_text(2*app.width/3, 350, text="Defense/ST",
                       font='impact 30 bold', fill='black')

def positionMode_mousePressed(app,event):
    #QB
    if (app.width/3-100<=event.x<=app.width/3+100) and (120<=event.y<=180):
        app.position = "QB"
        app.mode = 'scoringMode'
    #WR
    if (app.width/3-100<=event.x<=app.width/3+100) and (220<=event.y<=280):
        app.position = "WR"
        app.mode = 'scoringMode'
    #RB
    if (app.width/3-100<=event.x<=app.width/3+100) and (320<=event.y<=380):
        app.position = "RB"
        app.mode = 'scoringMode'
    #TE
    if (2*app.width/3-100<=event.x<=2*app.width/3+100) and (120<=event.y<=180):
        app.position = "TE"
        app.mode = 'scoringMode'
    #K
    if (2*app.width/3-100<=event.x<=2*app.width/3+100) and (220<=event.y<=280):
        app.position = "K"
        app.mode = 'scoringMode'
    #DST
    if (2*app.width/3-100<=event.x<=2*app.width/3+100) and (320<=event.y<=380):
        app.position = "DST"
        app.mode = 'scoringMode'

##########################################
# Scoring Mode
##########################################

def scoringMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'OrangeRed2')
    canvas.create_rectangle(20,20,app.width-20,app.height-20, width=5)
    canvas.create_rectangle(30,30,app.width-30,app.height-30, width=3)
    canvas.create_text(app.width/2, 70, text="Choose A Scoring Format",
                       font='impact 45 bold', fill='black')
    canvas.create_rectangle(app.width/2 - 80, 120, app.width/2 + 80, 180, fill = "orange", outline = "black", width = 3)
    canvas.create_text(app.width/2, 150, text="HALF PPR",
                       font='impact 30 bold', fill='black')
    canvas.create_rectangle(app.width/2 - 80, 220, app.width/2 + 80, 280, fill = "darkorange", outline = "black", width = 3)
    canvas.create_text(app.width/2, 250, text="PPR",
                       font='impact 30 bold', fill='black')
    canvas.create_rectangle(app.width/2 - 80, 320, app.width/2 + 80, 380, fill = "coral", outline = "black", width = 3)
    canvas.create_text(app.width/2, 350, text="STANDARD",
                       font='impact 30 bold', fill='black')

def scoringMode_mousePressed(app,event):
    #Half PPR
    if (app.width/2-80<=event.x<=app.width/2+80) and (120<=event.y<=180):
        app.scoring = "HALF PPR"
        app.mode = 'chooseMode'
    #PPR
    if (app.width/2-80<=event.x<=app.width/2+80) and (220<=event.y<=280):
        app.scoring = "PPR"
        app.mode = 'chooseMode'
    #Standard
    if (app.width/2-80<=event.x<=app.width/2+80) and (320<=event.y<=380):
        app.scoring = "STANDARD"
        app.mode = 'chooseMode'

##########################################
# Choose Mode
##########################################

def chooseMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "OrangeRed2")
    canvas.create_rectangle(20,20,app.width-20,app.height-20, width=5)
    canvas.create_rectangle(30,30,app.width-30,app.height-30, width=3)
    canvas.create_text(app.width/2, 70, text='Choose A Mode',
                       font='Impact 45 bold', fill='black')
    canvas.create_rectangle(app.width/2 - 120, 130, app.width/2 + 120, 190, fill = "#f6bc76", outline = "black", width = 3)
    canvas.create_text(app.width/2, 160, text="Start/Sit Analyzer",
                       font='impact 30 bold', fill='black')
    canvas.create_rectangle(app.width/2 - 120, 230, app.width/2 + 120, 330, fill = "#ffb4a3", outline = "black", width = 3)
    canvas.create_text(app.width/2, 280, text="Cluster Graph \n  (ECR vs. AER)",
                       font='impact 30 bold', fill='black')

def chooseMode_mousePressed(app,event):
    if (app.width/2-120<=event.x<=app.width/2+120) and (130<=event.y<=190):
        app.mode = 'playerInput'
    if (app.width/2-120<=event.x<=app.width/2+120) and (230<=event.y<=330):
        #Variables for Clustering
        app.mode = 'clusterGraphSetUp'

##########################################
# Player Input Mode
##########################################
import requests 
from bs4 import BeautifulSoup 

def getdata(url): 
    r = requests.get(url) 
    return r.text

def playerInput_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'OrangeRed2')
    canvas.create_rectangle(20,20,app.width-20,app.height-20, width=5)
    canvas.create_rectangle(30,30,app.width-30,app.height-30, width=3)
    canvas.create_text(app.width/2, 70, text="Input Player Names",
                       font='impact 45 bold', fill='black')
    canvas.create_text(app.width/3, 150, text="Player 1: ", font = "impact 30 bold", 
                        fill = "black")
    canvas.create_text(app.width/3, 250, text="Player 2: ", font = "impact 30 bold", 
                        fill = "black")
    canvas.create_rectangle(app.width/2-60, 130, app.width/2+140, 170, 
                            fill = 'light salmon', outline = 'black', width = 3)
    canvas.create_text(app.width/2+40, 150, text="Click to enter player name", 
                        font="impact 15 bold", fill="black")
    canvas.create_rectangle(app.width/2-60, 230, app.width/2+140, 270, 
                            fill = 'light salmon', outline = 'black', width = 3)
    canvas.create_text(app.width/2+40, 250, text="Click to enter player name", 
                        font="impact 15 bold", fill="black")
    canvas.create_text(app.width/2, 350, text="***Please write player inputs in all lowercase***", 
                        font="impact 30 bold", fill="black")
    if app.player1NameMatches:
        canvas.create_rectangle(app.width/2-60, 130, app.width/2+140, 170, 
                            fill = 'OrangeRed2', outline = 'OrangeRed2', width = 3)
        canvas.create_text(app.width/2+40, 150, text=app.player1Name.title(), 
                            font = "impact 25 bold", fill = 'black')
    if app.player2NameMatches:
        canvas.create_rectangle(app.width/2-60, 230, app.width/2+140, 270, 
                            fill = 'OrangeRed2', outline = 'OrangeRed2', width = 3)
        canvas.create_text(app.width/2+40, 250, text=app.player2Name.title(), 
                            font = "impact 25 bold", fill = 'black')
    if app.player1NameMatches and app.player2NameMatches:
        canvas.create_rectangle(app.width/2-100, 400, app.width/2+100, 
                                450, fill = "light salmon", outline = 'black', width = 3)
        canvas.create_text(app.width/2, 425, text = 'Press to continue', 
                            font = 'impact 25 bold', fill = 'black')

def playerInput_mousePressed(app, event):
    if (app.width/2-60<=event.x<=app.width/2+140) and (130<=event.y<=170):
        app.playerName = app.getUserInput("What is the first player's name?: ")
        if app.playerName == None:
            app.mode = 'playerInput'
        else:
            player1Input_csvReader(app, app.playerName.title())
    if (app.width/2-60<=event.x<=app.width/2+140) and (230<=event.y<=270):
        app.playerName = app.getUserInput("What is the second player's name?: ")
        if app.playerName == None:
            app.mode = 'playerInput'
        else:
            player2Input_csvReader(app, app.playerName.title())
    if app.player1NameMatches and app.player2NameMatches:
        if (app.width/2-100<=event.x<=app.width/2+100) and (400<=event.y<=450):
            app.mode = "playerComparisonMode"

teamNames = ["Arizona Cardinals", "Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills",
             "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns",
             "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Green Bay Packers", 
             "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs",
             "Las Vegas Raiders", "Los Angeles Chargers", "Los Angeles Rams", "Miami Dolphins",
             "Minnesota Vikings", "New England Patriots", "New Orleans Saints", "New York Giants",
             "New York Jets", "Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers",
             "Seattle Seahawks", "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Commanders"]

def player1Input_csvReader(app, userInputPlayer1Name):
    app.team1 = False
    listofplayerNames = []
    #CSV File from fantasypros.com
    with open(f'{app.scoring}/StartSit/FantasyPros_2022_Week_14_{app.position}_Rankings.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            listofplayerNames.append(row[playerName])
            if userInputPlayer1Name in row:
                app.twoPlayersStats[row[playerName]] = [row[playerTeam], row[playerProjectedPoints], 
                                    row[playerOpponent], row[playerStartorSit]]
                app.player1NameMatches = True
                app.player1Name = userInputPlayer1Name  
                
                #Using HTML Request to get player image
                if app.player1Name.title() in teamNames:
                    nameDashPlayer1 = app.player1Name.lower().replace(" ", "-")
                    #Webscrape from bleacherreport.com
                    htmldata = getdata(f"https://bleacherreport.com/{nameDashPlayer1}")
                    soup = BeautifulSoup(htmldata, 'html.parser') 
                    for item in soup.find_all('img'):
                        if app.player1Name in item['alt']:
                            player1ImageUrl = item['src']
                            player1Image = app.loadImage(player1ImageUrl)
                            app.player1ScaledImage = app.scaleImage(player1Image, 1/2)
                            app.team1 = True
                else:
                    if not app.player1Name.strip().replace(" ", "").isalnum():
                        noSpecialCharactersPlayer1 = app.player1Name.replace(".", "").replace("'", "")
                        nameDashPlayer1 = noSpecialCharactersPlayer1.lower().replace(" ", "-")
                    else:
                        nameDashPlayer1 = app.player1Name.lower().replace(" ", "-")
                    if app.player1Name.lower() == 'josh allen':
                        nameDashPlayer1 = 'josh-allen-qb'
                    if app.player1Name.lower() == 'travis etienne jr.':
                        nameDashPlayer1 = 'travis-etienne'
                    if app.player1Name.lower() == 'jeff wilson jr.':
                        nameDashPlayer1 = 'jeffery-wilson'
                    if app.player1Name.lower() == 'kenneth walker iii':
                        nameDashPlayer1 = 'kenneth-walker-rb'
                    if app.player1Name.lower() == 'marquez valdes scantling':
                        nameDashPlayer1 = 'marquez-valdesscantling'
                    if app.player1Name.lower() == 'marvin jones jr.':
                        nameDashPlayer1 = 'marvin-jones'
                    if app.player1Name.lower() == 'nick westbrook-ikhine':
                        nameDashPlayer1 = 'nick-westbrook'
                    #Webscrape from fantasypros.com
                    htmldata = getdata(f"https://www.fantasypros.com/nfl/stats/{nameDashPlayer1}.php")
                    soup = BeautifulSoup(htmldata, 'html.parser') 
                    for item in soup.find_all('img'):
                        if "250" in item['src']:
                            player1ImageUrl = item['src']
                            player1Image = app.loadImage(player1ImageUrl)
                            app.player1ScaledImage = app.scaleImage(player1Image, 3/5)
                            break
                        else:
                            player1Image = app.loadImage("https://media.istockphoto.com/id/1399859917/vector/no-image-vector-symbol-missing-available-icon-no-gallery-for-this-moment-placeholder.jpg?b=1&s=170667a&w=0&k=20&c=jBE3Ul6LpRXO5UhCYTmLArfdFc6YEWwhzarxTmtZI2U=")
                            app.player1ScaledImage = app.scaleImage(player1Image, 1/3)

        if userInputPlayer1Name not in listofplayerNames:
            userInputPlayer1Name = app.getUserInput("Player/Team name is not in database or is on a Bye Week! Try again!").title()
            player1Input_csvReader(app, userInputPlayer1Name)

def player2Input_csvReader(app, userInputPlayer2Name):
    app.team2 = False
    listofplayerNames = []
    #CSV File from fantasypros.com
    with open(f'{app.scoring}/StartSit/FantasyPros_2022_Week_14_{app.position}_Rankings.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            listofplayerNames.append(row[playerName])
            if userInputPlayer2Name in row:
                app.twoPlayersStats[row[playerName]] = [row[playerTeam], row[playerProjectedPoints], 
                                    row[playerOpponent], row[playerStartorSit]]
                app.player2NameMatches = True
                app.player2Name = userInputPlayer2Name

                #Using HTML Request to get player image
                if app.player2Name.title() in teamNames:
                    nameDashPlayer2 = app.player2Name.lower().replace(" ", "-")
                    #Webscrape from bleacherreport.com
                    htmldata = getdata(f"https://bleacherreport.com/{nameDashPlayer2}")
                    soup = BeautifulSoup(htmldata, 'html.parser') 
                    for item in soup.find_all('img'):
                        if app.player2Name.title() in item['alt']:
                            player2ImageUrl = item['src']
                            player2Image = app.loadImage(player2ImageUrl)
                            app.player2ScaledImage = app.scaleImage(player2Image, 1/2)
                            app.team2 = True
                else:
                    if not app.player2Name.strip().replace(" ", "").isalnum():
                        noSpecialCharactersPlayer2 = app.player2Name.replace(".", "").replace("'", "")
                        nameDashPlayer2 = noSpecialCharactersPlayer2.lower().replace(" ", "-")
                    else:
                        nameDashPlayer2 = app.player2Name.lower().replace(" ", "-")
                    if app.player2Name.lower() == 'josh allen':
                        nameDashPlayer2 = 'josh-allen-qb'
                    if app.player2Name.lower() == 'travis etienne jr.':
                        nameDashPlayer2 = 'travis-etienne'
                    if app.player2Name.lower() == 'jeff wilson jr.':
                        nameDashPlayer2 = 'jeffery-wilson'
                    if app.player2Name.lower() == 'kenneth walker':
                        nameDashPlayer2 = 'kenneth-walker-rb'
                    if app.player2Name.lower() == 'marquez valdes-scantling':
                        nameDashPlayer2 = 'marquez-valdesscantling'
                    if app.player2Name.lower() == 'marvin jones jr.':
                        nameDashPlayer2 = 'marvin-jones'
                    if app.player2Name.lower() == 'nick westbrook-ikhine':
                        nameDashPlayer2 = 'nick-westbrook'
                    #Webscrape from fantasypros.com
                    htmldata = getdata(f"https://www.fantasypros.com/nfl/stats/{nameDashPlayer2}.php")
                    soup = BeautifulSoup(htmldata, 'html.parser') 
                    for item in soup.find_all('img'):
                        if "250" in item['src']:
                            player2ImageUrl = item['src']
                            player2Image = app.loadImage(player2ImageUrl)
                            app.player2ScaledImage = app.scaleImage(player2Image, 3/5)
                            break
                        else:
                            player2Image = app.loadImage("https://media.istockphoto.com/id/1399859917/vector/no-image-vector-symbol-missing-available-icon-no-gallery-for-this-moment-placeholder.jpg?b=1&s=170667a&w=0&k=20&c=jBE3Ul6LpRXO5UhCYTmLArfdFc6YEWwhzarxTmtZI2U=")
                            app.player2ScaledImage = app.scaleImage(player2Image, 1/3)

        if userInputPlayer2Name not in listofplayerNames:
            userInputPlayer2Name = app.getUserInput("Player/Team name is not in database or is on a Bye Week! Try again!").title()
            player2Input_csvReader(app, userInputPlayer2Name)
            
##########################################
# Player Comparison Mode
##########################################

def playerComparisonMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'OrangeRed2')
    canvas.create_rectangle(20,20,app.width-20,app.height-20, width=5)
    canvas.create_rectangle(30,30,app.width-30,app.height-30, width=3)
    canvas.create_text(app.width/2, 70, text="Fantasy Football Analyzer",
                       font='impact 45 bold', fill='black')
    canvas.create_image(app.width/2, 185, image=ImageTk.PhotoImage(app.nflPic))

    if float(app.twoPlayersStats[app.player1Name][1]) > float(app.twoPlayersStats[app.player2Name][1]):
        canvas.create_text(app.width/4, 370, text = app.twoPlayersStats[app.player1Name][1], font = "impact 30 bold", fill = "green")
        canvas.create_text(3*app.width/4, 370, text = app.twoPlayersStats[app.player2Name][1], font = "impact 30 bold", fill = "#8B0000")
    elif float(app.twoPlayersStats[app.player1Name][1]) < float(app.twoPlayersStats[app.player2Name][1]):
        canvas.create_text(app.width/4, 370, text = app.twoPlayersStats[app.player1Name][1], font = "impact 30 bold", fill = "#8B0000")
        canvas.create_text(3*app.width/4, 370, text = app.twoPlayersStats[app.player2Name][1], font = "impact 30 bold", fill = "green")
    elif float(app.twoPlayersStats[app.player1Name][1]) == float(app.twoPlayersStats[app.player2Name][1]):
        canvas.create_text(app.width/4, 370, text = app.twoPlayersStats[app.player1Name][1], font = "impact 30 bold", fill = "#FDDA0D")
        canvas.create_text(3*app.width/4, 370, text = app.twoPlayersStats[app.player2Name][1], font = "impact 30 bold", fill = "#FDDA0D")

    if app.matchupTiers.index(app.twoPlayersStats[app.player1Name][3]) < app.matchupTiers.index(app.twoPlayersStats[app.player2Name][3]):
        canvas.create_text(app.width/4, 510, text = app.twoPlayersStats[app.player1Name][3], font = "impact 30 bold", fill = "green")
        canvas.create_text(3*app.width/4, 510, text = app.twoPlayersStats[app.player2Name][3], font = "impact 30 bold", fill = "#8B0000")
    elif app.matchupTiers.index(app.twoPlayersStats[app.player1Name][3]) > app.matchupTiers.index(app.twoPlayersStats[app.player2Name][3]):
        canvas.create_text(app.width/4, 510, text = app.twoPlayersStats[app.player1Name][3], font = "impact 30 bold", fill = "#8B0000")
        canvas.create_text(3*app.width/4, 510, text = app.twoPlayersStats[app.player2Name][3], font = "impact 30 bold", fill = "green")
    elif app.matchupTiers.index(app.twoPlayersStats[app.player1Name][3]) == app.matchupTiers.index(app.twoPlayersStats[app.player2Name][3]):
        canvas.create_text(app.width/4, 510, text = app.twoPlayersStats[app.player1Name][3], font = "impact 30 bold", fill = "#FDDA0D")
        canvas.create_text(3*app.width/4, 510, text = app.twoPlayersStats[app.player2Name][3], font = "impact 30 bold", fill = "#FDDA0D")

    #Player1
    if app.team1:
        canvas.create_image(app.width/4, 205, image=ImageTk.PhotoImage(app.player1ScaledImage))
    else:
        canvas.create_image(app.width/4, 200, image=ImageTk.PhotoImage(app.player1ScaledImage))
    canvas.create_text(app.width/4, 115, text = app.player1Name, font = "impact 30 bold", fill = "black")
    canvas.create_text(app.width/4, 300, text = app.twoPlayersStats[app.player1Name][0], font = "impact 30 bold", fill = "black")
    canvas.create_text(app.width/4, 440, text = app.twoPlayersStats[app.player1Name][2], font = "impact 30 bold", fill = "black")

    #Player2
    if app.team2:
        canvas.create_image(3*app.width/4, 205, image=ImageTk.PhotoImage(app.player2ScaledImage))
    else:
        canvas.create_image(3*app.width/4, 200, image=ImageTk.PhotoImage(app.player2ScaledImage))
    canvas.create_text(3*app.width/4, 115, text = app.player2Name, font = "impact 30 bold", fill = "black")
    canvas.create_text(3*app.width/4, 300, text = app.twoPlayersStats[app.player2Name][0], font = "impact 30 bold", fill = "black")
    canvas.create_text(3*app.width/4, 440, text = app.twoPlayersStats[app.player2Name][2], font = "impact 30 bold", fill = "black")

    #Categories
    canvas.create_text(app.width/2, 300, text = "Team", font = "impact 30 bold", fill = "black")
    canvas.create_text(app.width/2, 370, text = "Projected Pts", font = "impact 30 bold", fill = "black")
    canvas.create_text(app.width/2, 440, text = "Opponent", font = "impact 30 bold", fill = "black")
    canvas.create_text(app.width/2, 510, text = "Start/Sit", font = "impact 30 bold", fill = "black")

    canvas.create_text(app.width/2, 550, text = "***Press 'r' to restart bot!***", font = "impact 20 bold", fill = "black")
    
def playerComparisonMode_keyPressed(app, event):
    if event.key == 'r':
        app.mode = 'introScreenMode'
        app.position = ""
        app.scoring = ""
        app.redo = ""

        #Player1 Variables
        app.player1Name = ""
        app.player1NameMatches = False
        app.player1ScaledImage = None

        #Player2 Variables
        app.player2Name = ""
        app.player2NameMatches = False
        app.player2ScaledImage = None

        #Both player variables
        app.playerName = ""
        app.twoPlayersStats = dict()

        #Team variables
        app.team1 = False
        app.team2 = False

##########################################
# Cluster Graph Set Up
##########################################
import pandas as pd
from sklearn.cluster import KMeans

def clusterGraphSetUp_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'OrangeRed2')
    canvas.create_rectangle(20,20,app.width-20,app.height-20, width=5)
    canvas.create_rectangle(30,30,app.width-30,app.height-30, width=3)
    canvas.create_text(app.width/2, 70, text="Cluster Graph Visualization",
                       font='impact 45 bold', fill='black')

    canvas.create_text(app.width/2, 150, text="Visualizing Cluster Graph For...",
                       font='impact 30 bold', fill='black')
                 
    canvas.create_rectangle(app.width/3 - 40, 200, app.width/3 + 40, 260, fill = "#f67690", outline = "black", width = 3)
    canvas.create_text(app.width/3, 230, text=f"{app.position}",
                       font='impact 30 bold', fill='black')

    if app.scoring == "PPR":
        canvas.create_rectangle(2*app.width/3 - 40, 200, 2*app.width/3 + 40, 260, 
                                fill = "#f9a6b7", outline = "black", width = 3)
    if app.scoring == "HALF PPR":
        canvas.create_rectangle(2*app.width/3 - 70, 200, 2*app.width/3 + 70, 260, 
                                fill = "#f9a6b7", outline = "black", width = 3)
    if app.scoring == "STANDARD":
        canvas.create_rectangle(2*app.width/3 - 80, 200, 2*app.width/3 + 80, 260, 
                                fill = "#f9a6b7", outline = "black", width = 3)
    canvas.create_text(2*app.width/3, 230, text=f"{app.scoring}",
                       font='impact 30 bold', fill='black')
    
    canvas.create_rectangle(app.width/2 - 130, 320, app.width/2 + 130, 380, fill = "#f9a6e1", outline = "black", width = 3)
    canvas.create_text(app.width/2, 350, text="Press To Visualize",
                       font='impact 30 bold', fill='black')
    
    canvas.create_rectangle(app.width/2 - 130, 430, app.width/2 + 130, 490, fill = "#e8a6f9", outline = "black", width = 3)
    canvas.create_text(app.width/2, 460, text="Press To Restart",
                       font='impact 30 bold', fill='black')
    
    canvas.create_text(app.width/2, 530, text="***Cluster Graph only displays the top 50 ranked players***",
                       font='impact 20 bold', fill='black')
    
def clusterGraphSetUp_mousePressed(app, event):
    if (app.width/2-130<=event.x<=app.width/2+130) and (320<=event.y<=380):
        app.playerNamesList = []
        app.maximumWorstNumber = 0
        app.df = pd.read_csv(f'{app.scoring}/ClusterGraph/FantasyPros_2022_Week_14_{app.position}_Rankings.csv', nrows=50)
        datareader(app)
        app.setSize(width=1792, height=1067)
        # pd.set_option('display.max_rows', None) 
        X = app.df[['AVG.']].values
        k = 13
            
        model = KMeans(n_clusters=k)
        model.fit(X)
        app.labels = model.predict(X)

        def assign_tiers(labels):
            uniqueLabels = []
            tiers = []
            for i in labels:
                if i not in uniqueLabels:
                    uniqueLabels.append(i)

                tiers.append(
                    len(set(uniqueLabels))
                )
            return tiers

        app.tiers = assign_tiers(app.labels)
        app.setSize(width=1792, height=1067)
        app.mode = 'clusterGraphMainMode'
    if (app.width/2-130<=event.x<=app.width/2+130) and (430<=event.y<=490):
        app.mode = 'introScreenMode'

##########################################
# Cluster Graph Main Mode
##########################################

def getdata(url): 
    r = requests.get(url) 
    return r.text

def datareader(app):
    worstNum = []
    with open(f'{app.scoring}/ClusterGraph/FantasyPros_2022_Week_14_{app.position}_Rankings.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            app.playerNamesList.append((row[1], row[3], row[4], row[5]))
            worstNum.append(int(row[4]))
    app.maximumWorstNumber = math.ceil(max(worstNum)/10)*10
    app.numberofPlayers = len(app.playerNamesList)
    
#round highest rank to nearest 10 (upwards)

def clusterGraphMainMode_redrawAll(app, canvas):
    canvas.create_rectangle(app.width/12, app.height/12, 11*app.width/12, 11*app.height/12, outline = 'snow3')
    canvas.create_rectangle(app.width/12, app.height/12-(11*app.height/12- app.height/12)/app.numberofPlayers, 11*app.width/12, 11*app.height/12, outline = 'snow3')

    canvas.create_text(app.width/2, app.height/12-40, text = 'Tiers for Week 14 of the NFL Season', fill = 'black', font = 'DejaVu 20 bold')
    canvas.create_text(app.width/12-25, app.height/2, text = 'Expert Consensus Rank', fill = 'black', font = 'DejaVu 20 bold', angle = 90)
    canvas.create_text(app.width/2, 11*app.height/12+45, text = 'Average Expert Rank', fill = 'black', font = 'DejaVu 20 bold')


    for rank in range(app.maximumWorstNumber//5+1):
        canvas.create_line(app.width/12+rank*(11*app.width/12-app.width/12)/(app.maximumWorstNumber//5), app.height/12-(11*app.height/12- app.height/12)/app.numberofPlayers, app.width/12+rank*(11*app.width/12-app.width/12)/(app.maximumWorstNumber//5), 11*app.height/12, fill = 'snow3')
        canvas.create_text(app.width/12+rank*(11*app.width/12-app.width/12)/(app.maximumWorstNumber//5), 11*app.height/12+15, text = rank*5, fill = 'black')
    
    for player in range(app.numberofPlayers):
        colors = ['red', '#FFAC1C', '#FDDA0D', '#AFE1AF', '#50C878', '#89CFF0',
                '#4169E1', '#6082B6', '#CCCCFF', '#CF9FFF', 'violet', '#AA98A9', '#673147']
        
        #Scatterplot dots
        cx = app.width/12 + (float(app.playerNamesList[player][3])/app.maximumWorstNumber)*(11*app.width/12-app.width/12)
        cy = ((app.height/12+(11*app.height/12 - app.height/12)/app.numberofPlayers)+player*(11*app.height/12 - app.height/12)/app.numberofPlayers)-(11*app.height/12- app.height/12)/app.numberofPlayers
        canvas.create_oval(cx-2, cy-2, cx+2, cy+2, fill = 'black', outline = 'black')
        
        leftxval = app.width/12 + (int(app.playerNamesList[player][1])/app.maximumWorstNumber)*(11*app.width/12-app.width/12)
        rightxval = app.width/12 + (int(app.playerNamesList[player][2])/app.maximumWorstNumber)*(11*app.width/12-app.width/12)
        canvas.create_line(leftxval, cy, rightxval, cy, fill = colors[app.tiers[player]-1], width = '2')

        canvas.create_line(app.width/12, (app.height/12+(11*app.height/12 - app.height/12)/app.numberofPlayers)+player*(11*app.height/12 - app.height/12)/app.numberofPlayers, 11*app.width/12, (app.height/12+(11*app.height/12 - app.height/12)/app.numberofPlayers)+player*(11*app.height/12 - app.height/12)/app.numberofPlayers, fill = 'snow3')
        canvas.create_text(leftxval-100, (app.height/12)+player*(11*app.height/12- app.height/12)/app.numberofPlayers, text = app.playerNamesList[player][0], fill = colors[app.tiers[player]-1], font = 'DejaVu 13 bold')

    canvas.create_rectangle(10*app.width/12-10, app.height/12-10, 11*app.width/12-10, app.height/12+300, fill = 'white', outline = 'snow3')
    for color in range(len(colors)):
        canvas.create_rectangle(10*app.width/12+15, app.height/12+5+color*22, 10*app.width/12+50, app.height/12+20+color*22, fill = colors[color])
        canvas.create_text(10*app.width/12+95, (app.height/12+5+color*22)+7, text = f"Tier {color+1}", fill = 'black', font = 'DejaVu 14 bold')

    canvas.create_text(10*app.width/12, app.height/12-50, text = "***Press 'r' to return to previous screen***", fill = 'black', font = 'DejaVu 20 bold')

def clusterGraphMainMode_keyPressed(app, event):
    if event.key == 'r':
        app.setSize(width = 800, height = 600)
        app.mode = 'clusterGraphSetUp'

##########################################
# Main App
##########################################

def appStarted(app):
    app.mode = 'introScreenMode'
    app.score = 0
    app.timerDelay = 50
    app.makeAnMVCViolation = False

    #Intro Pic URL
    introURL="https://www.coastalgolfaway.com/wp-content/uploads/2015/02/fantasy-football.png"
    app.image1 = app.loadImage(introURL)
    app.introPic = app.scaleImage(app.image1, 2/3)

    #NFL Logo URL
    nflURL = "https://loodibee.com/wp-content/uploads/nfl-league-logo.png"
    app.nflimage = app.loadImage(nflURL)
    app.nflPic = app.scaleImage(app.nflimage, 1/8)

    app.position = ""
    app.scoring = ""
    app.redo = ""

    #Player1 Variables
    app.player1Name = ""
    app.player1NameMatches = False
    app.player1ScaledImage = None

    #Player2 Variables
    app.player2Name = ""
    app.player2NameMatches = False
    app.player2ScaledImage = None

    #Both player variables
    app.playerName = ""
    app.twoPlayersStats = dict()

    app.matchupTiers = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", 
                            "D-", "F+", "F", "F-"]

runApp(width=800, height=600)


    

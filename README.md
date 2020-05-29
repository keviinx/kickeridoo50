# Kickeridoo50

# TL;DR

[![CS50x Final Project: Kickeridoo50](https://img.youtube.com/vi/elE42RiLW10/0.jpg)](https://youtu.be/elE42RiLW10)

## Table of contents

* [About Kickeridoo50](#about-kickeridoo50)
* [Kickeridoo50 features](#kickeridoo50-features)
  * [Main page](#main-page)
  * [Add result](#add-result)
  * [Add player](#add-player)
  * [Player ranking](#player-ranking)
  * [Team ranking](#team-ranking)
* [Implementation](#implementation)
* [Setting up and running it](#setting-up-and-running-it)

## About Kickeridoo50

The name **Kickeridoo** came to be by fusing the word **Kicker** which is the German nickname of *foosball* and Didger**idoo** *(No idea how we came up with that name)*. Me and my colleague loves to play foosball during our break time and to keep track of the scores, I have been using spreadsheet. 

![Kickeridoo spreadsheet](https://user-images.githubusercontent.com/60583511/82753669-a590bb80-9dc7-11ea-9267-baab264ba237.png)

So then I had the idea of making a web application so that updating the score of the player will be easier. The application is called **Kickeridoo50**.

![The Kickeridoo50 app](https://user-images.githubusercontent.com/60583511/82727457-05656480-9ceb-11ea-9d3d-8d75a16f597c.png)

## Kickeridoo50 features

### Main page

This is the first page when you access the application. The page basically lists out the features of **Kickeridoo50** and a short description explaining the feature.

### Add result

This page allows the user to add the result of a match. The game type can be chosen whether it was a solo match (1 vs 1) or team (2 vs 2). The user can then select players using the drop-down list. The player name list is based on the players added into the database. The user can then decide whether team 1 won, team 2 won or the match was a draw.

![Add result user interface](https://user-images.githubusercontent.com/60583511/82757749-d8947880-9de2-11ea-8f74-6ac306af860a.png)

### Add player

This page allows the user to add a new player into the database. The new player will then be accessible in the **Add result** feature.

![Add player user interface](https://user-images.githubusercontent.com/60583511/82757811-198c8d00-9de3-11ea-97ea-34c6f6d18b76.png)

### Player ranking

This page displays the ranking of each player. The result is displayed in alphabetical order but the result can be sorted by clicking the table header. The total points is calculated using this formula: `(win * 3 points) + (draw * 1 point)`

![Player ranking user interface](https://user-images.githubusercontent.com/60583511/82758009-455c4280-9de4-11ea-9515-a8793a9d1523.png)

### Team ranking

This page displays the ranking of teams. The result displayed is similar to **Player ranking** page. The result is sorted alphabetically for Player 1. The result can also be sorted by clicking the table header.

![Team ranking user interface](https://user-images.githubusercontent.com/60583511/82758294-f44d4e00-9de5-11ea-969a-167a79e15c27.png)

## Implementation

The application was developed using `bootstrap` and `flask`.

## Setting up and running it

Just clone the repo, then `export FLASK_APP=application.py` and finally `flask run`.

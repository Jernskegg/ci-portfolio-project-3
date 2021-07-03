![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Casper Hille

Full-Stack Development course (5p) | Portfolio project 3 (Python focused project)
***

# Purpose of the Project

The purpose of this project is to make a Battleship game in Python.

# User Stories

as a user I want to play a game of logic.

# Features

  * Random spreadsheet ids

    Due to google speadsheets being an online service, If multiple people would be using the application at the same time it would update the same worksheets, therefor I have implemented a random id worksheet generetor that aswell prevents duplicates being used, so that multiple people can use the application at the same time. 
    
  * User and computer position guessing

    When the game is intialized and ready to be played, you are ready to guess the row and the collums on the enemy sheet and hopefully sink the ships before the computer sinks yours.

  * Exit application

    When the game is done. the application automatically closes the used worksheets and makes rooms for the next player.

 # Future Features

 * visual feedback by grid
   
# Technology

  ## python
  Python is a easy and basic programming language, but it is powerfull with the use libraries to bring out capabilities to use in multiple applications of use.

  ## google spreadsheet
  Google speadsheets is a calculus applications offered by google where you can make speadsheets, charts and advanced caluclations

  in this project Googlespeadsheet is used for the battlemaps, There is probably a better way but I want to incorperate the spreadsheet for the manipulation of a realworld situation where the python application would need to manipulate a spreadsheet.

# testing

   ## code validation

  Code has been validated, During development the python extension has been used, aftwards it has been validated in pep8
  
   ## fixed bugs and issues found.
  
  * there is an issue if the user forcefully stops the application. it wont remove worksheets and would leave worksheets open and makes the duplication detection halt if there are greater number of unused worksheets open.

  * (Fixed) if multiple people use the application it would update the same worksheet.
    
    Implemented a worksheet creation function with detection if that id is already in use, in case it is being used it tries a new id.
  
  * There is an issue if too many users use the application it will halt due to it sending to many http calls to the api and stop application.

  * Ship could be overwritten by enemy on his sheet resulting in a loss since you cant destroy the amount of predetermed ships

  * heroku + CI console template does not like newlines(\n) with inputs , putting new lines into seperate Print statements works.

  * Horisontal and vertical input does not work.

# Deployment
   ## via gitpod

 * To use gitpod you have to start a repository on Github. 
   from there if you have the gitpod plugin on your browser a green button stating "Gitpod" is available. that button redirects you to the GitPod IDE
   
 * When it's done loading you will see down in the bottom a few tabs, when you press on terminal you will be able to input a command 
   
 * to deploy your application through a http server you can write "Python3 -m http.server". this will open the http service and GitPod will give you a notification "A service is available on port 8000" with three buttons ( make public, open preview, open browser) so when you open your browser it will open the  index.html files, if that doesn't exist it will open the readme.md file instead.

 * to run a python code, you type python3 FILENAME.py in the terminal.
 
 * This is a good place to test your applications before pushing to github.

   ## via Heroku

# My personal achievements and what I feel I need to work on.



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

  * vertical and horizontal position

    You will be able to choose if you ship is vertical or horizontal according to the grid.

  * Exit application

    When the game is done. the application automatically closes the used worksheets and makes rooms for the next player.
   
# Technology

  ## python
  Python is a easy and basic programming language, but it is powerfull with the use libraries to bring out capabilities to use in multiple applications of use.

  ## google spreadsheet
  Google speadsheets is a calculus applications offered by google where you can make speadsheets, charts and advanced caluclations

  in this project Googlespeadsheet is used for the battlemaps, There is probably a better way but I want to incorperate the spreadsheet for the manipulation of a realworld situation where the python application would need to manipulate a spreadsheet.

  ## Gspread
  Gspread is an API between Python and Google Spreadsheets. 
  This has been used to make all the changes, look ups, creation and deletion of the google spreadsheet for this project.

# testing

   ## code validation

  Code has been validated, During development the python extension has been used, aftwards it has been validated in pep8
  
   ## fixed bugs and issues found.

  * (Fixed) if multiple people use the application it would update the same worksheet. this has been fixed by the implemented worksheet creation.
  
  * (Fixed) there is an issue if the user forcefully stops the application. it wont remove worksheets and would leave worksheets open and makes the duplication detection halt if there are greater number of unused worksheets open. 
  
    The system now reports which worksheets that are generated.

    Implemented a worksheet creation function with detection if that id is already in use, in case it is being used it tries a new id.
  
  * (Unresolved) There is an issue if too many users use the application it will halt due to it sending to many http calls to the api and stop application.
    

  * (Fixed) Ship could be overwritten by enemy on his sheet resulting in a loss since you cant destroy the amount of predetermed ships

  * (Fixed) heroku + CI console template does not like newlines(\n) with inputs , putting new lines into seperate Print statements works.

  * (Fixed) Horisontal and vertical input does not work. This has been fixed by correcting code.

# Deployment
  ## via gitpod

 * To use gitpod you have to start a repository on Github. 
   from there if you have the gitpod plugin on your browser a green button stating "Gitpod" is available. that button redirects you to the GitPod IDE
   
 * When it's done loading you will see down in the bottom a few tabs, when you press on terminal you will be able to input a command 
   
 * to deploy your application through a http server you can write "Python3 -m http.server". this will open the http service and GitPod will give you a notification "A service is available on port 8000" with three buttons ( make public, open preview, open browser) so when you open your browser it will open the  index.html files, if that doesn't exist it will open the readme.md file instead.

 * to run a python code, you type python3 FILENAME.py in the terminal.
 
 * This is a good place to test your applications before pushing to github.

  ## via Heroku

  * Before you deploy make sure you have your requirements.txt is updated and accounted for and get your api keys ready.

  * to deploy a application through Heroku you need to make an account. once you have made an account you can have up to 5 projects on the free plan.

  * To create a new app. Log in and you'll see a "Create app" button.
  Once pressed you'll be able to name your poject and choose hosting. The name needs to be unique.

  * You'll need to setup all your setting before you can deploy your project. You can find the setting in the tabs in the dashboard.

    If you have api keys you can insert them in the Config Vars section and there is a button to reveal the keys. once clicked you can input the Const used in the poject in "KEY" and all the content of your creds.json in the "VALUE"

    Next we'll set up build packs. Press the build pack and add the buildpacks you need, if you need more than one, make sure you put them in the correct order, You can drag and drop them list items.

  * now we can start the deployment by heading over to the deploy tab. in this project I chose to deploy trough github.

    After I clicked trough github I had to connect heroku to my github account, therafter I had to search for my project. once selected.
  I could choose which branch.

    Now I can sellect automatic deployment, which updates the app once github updates or manual deployment that only will update heroku when I press on that button again.

    Now we'll wait for heroku to download all plugins and install all the requirements. once done there will be a message telling it completed, or failed. once succesful it will show a button to view your deployed application.

  * Now you have your deployed page. Now you can test if everything works as it should or send the links to your friends to show off you accomplishments.

# My personal achievements and what I feel I need to work on.

I have managed to make a game out of something not made for it. It can be great for automating your spreadsheet. But playing games on it- A no no.

Still looking for a git commit naming convention. If you have a good one. Please do notify me.


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

    Due to google spreadsheets being an online service, If multiple people were using the application simultaneously, it would update the same worksheets. Therefore, I have implemented a random id worksheet generator that prevents duplicates from being used so that multiple people can use the application simultaneously. 
    
  * User and computer position guessing

    When the game is initialised and ready to be played, you are prepared to guess the row and the columns on the enemy sheet and hopefully sink the ships before the computer sinks yours.

  * vertical and horizontal position

    You will be able to choose if your ship is vertical or horizontal according to the grid.

  * Exit application

    When the game is done. The application automatically closes the used worksheets and makes room for the next player.
   
# Technology

  ## python
  Python is an easy and basic programming language, but it is powerful with libraries to bring out capabilities to use in multiple 

  ## google spreadsheet
  Google spreadsheets is a calculus application offered by Google to make spreadsheets, charts and advanced calculations.

  In this project, Google spreadsheets are used for the battle maps, There is probably a better way, but I want to incorporate the spreadsheet to manipulate a real-world situation where the python application would need to manipulate a spreadsheet.

  ## Gspread
  Gspread is an API between Python and Google Spreadsheets. 
  During the project’s development, it has been utilised to make changes, look-ups, create and delete the spreadsheet.


# testing

  ## code validation

  Code has been validated. During development, the python extension has been used. Afterwards, it has been validated in pep8.
  
  ## fixed bugs and issues found.

  * (Fixed) if multiple people use the application, it would update the same worksheet. This has been fixed by the implemented worksheet creation.
  
  * (Fixed) there is an issue if the user forcefully stops the application. It won’t remove worksheets, leave worksheets open, and halt the duplication detection if there are more unused worksheets open.  
  
    The system now reports which worksheets are generated.

    Implemented a worksheet creation function with detection if that id is already in use. In case it is being used, it tries a new id.
  
  * (Unresolved) There is an issue if too many users use the application. It will halt due to it sending too many HTTP calls to the API and stops the application.
    
  * (Fixed) Ship could be overwritten by the enemy on his sheet resulting in a loss since you can’t destroy the number of predetermined ships.

  * (Fixed) Heroku + CI console template does not like newlines(\n) with inputs. Putting new lines into separate Print statements works.

  * (Fixed) Horizontal and vertical input does not work. This has been fixed by correcting the code.

# Deployment
  ## via Gitpod

  * To use Gitpod, you have to start a repository on Github. 
   from there, if you have the Gitpod plugin on your browser, a green button stating "Gitpod" is available. that button redirects you to the GitPod IDE
   
  * When it's done loading, you will see down in the bottom a few tabs. When you press on the terminal, you will be able to input a command 
   
  * to deploy your application through an http server, you can write "Python3 -m http.server". This will open the HTTP service, and GitPod will give you a notification "A service is available on port 8000" with three buttons ( make public, open preview, open browser) so when you open your browser, it will open the  index.html files if that doesn't exist it will open the readme.md file instead.

  * to run a python code, you type python3 FILENAME.py in the terminal.
 
  * This is an excellent place to test your applications before pushing them to Github.

  ## via Heroku

  * Before you deploy, ensure your requirements.txt is updated and accounted for and get your API keys ready.

  * to deploy an application through Heroku, you need to make an account. Once you have created an account, you can have up to 5 projects on the free plan.

  * To create a new app. Log in, and you'll see a "Create app" button.
  Once pressed, you'll be able to name your project and choose which region your application will host. The name needs to be unique.

  * You'll need to set up all your setting before you can deploy your project. You can find the “setting” in the tabs in the dashboard.

    If you have API keys, you can insert them in the Config Vars section, and there is a button to reveal the keys. 
    once clicked,  the const you used in the poject should be in "KEY" and creds.json in the "VALUE"

    Next, we'll set up build packs. Press the build pack and add the buildpacks you need. If you need more than one, make sure you put them in the correct order, You can drag and drop their list items.

  * now, we can start the deployment by heading over to the deploy tab. in this project, I chose to deploy through GitHub.

    After I clicked through GitHub, I had to connect Heroku to my GitHub account. Thereafter I had to search for my project. Once selected.
  I could choose which branch.

    Now I can select an automatic deployment, which updates the app once GitHub updates or manual deployment that will only update Heroku when I press that button again.

    Now we'll wait for Heroku to download all plugins and install all the requirements. Once done, there will be a message telling it completed or failed. Once successful, it will show a button to view your deployed application.

  * Now you have your deployed page. Now you can test if everything works as it should or send the links to your friends to show off those accomplishments you have made.


# My personal achievements and what I feel I need to work on.

I have managed to make a game out of something not made for it. It can be great for automating your spreadsheet. But playing games on it- A no no.

Still looking for a git commit naming convention. If you have a good one. Please do notify me.

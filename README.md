# Deploying Machine Learning Models using Flask

## Files:
* Data: There is a csv file in it.
* Templates: The template of my flask application in HTML. (I'm aware that it's a terrible design :) )
* Procfile: Heroku apps include a Procfile that specifies the commands that are executed by the app on startup.
* app.py: Flask part of my app.
* model.py: My machine learning model. (That's a simple model. Nothing special.)
* regression_model.pkl: This is the pickle module which is created by running model.py.
* requirements.txt: Determination of the version of different modules. If we don't have this file, we might have some issues because of the version differences.

## Heroku Part
* Upload your files on a Github repo. (The files above)
* Create an account on heroku.com
* From the dashboard click on "Create New App"
![Test Image 1](https://hizliresim.com/9DmMzs)
* Find an app name and select a region.
* Chose the deployment method as Github
* You need to connect your github account. If you have connected, write your repo's name and click connect.
* On the manual deploy part, click on deploy branch.
* After a while you can see a "view" button. That means your site is ready to work!


[Click here to see the Heroku app](https://model-deployment-app.herokuapp.com)

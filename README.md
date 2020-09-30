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
**1. Upload your files on a Github repo. (The files above)**

**2. Create an account on heroku.com**

**3. From the dashboard click on "Create New App"**
![Test Image 1](https://i.hizliresim.com/9DmMzs.png)

**4. Find an app name and select a region.**
![Test Image 2](https://i.hizliresim.com/YgR4jW.png)

**5. Chose the deployment method as Github**
![Test Image 2](https://i.hizliresim.com/w1XVz4.png)

**6. You need to connect your github account. If you have connected, write your repo's name and click connect.**
![Test Image 2](https://i.hizliresim.com/7L7rwy.png)

**7. On the manual deploy part, click on deploy branch.**
![Test Image 2](https://i.hizliresim.com/wwL5fH.png)

**8. After a while you can see a "view" button. That means your site is ready to work!**
![Test Image 2](https://i.hizliresim.com/Wm2u8O.png)



[Click here to see the Heroku app](https://model-deployment-app.herokuapp.com)

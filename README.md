# Image_to_Sketch 😁
- This WebApp is used to convert Image to Sketch using OpenCV

## Usage
1. Clone the repository and navigate to the directory.
2. Run the command py app.py
3. This will run the web app in the localhost and would look like this. Feel free to play around. 😋
<img src="https://github.com/avinjoseph/Image_to_Sketch/blob/master/img1.png">
4. The result will be :
<img src="https://github.com/avinjoseph/Image_to_Sketch/blob/master/img2.png">

## Deployment on Heroku

1. pip install gunicorn
2. Create a Procfile :- Heroku apps include a Procfile that specifies the commands that are executed by the app on startup.
    -- Add  web : gunicorn app:app in the procfile
3. pip freeze > requirements.txt  :- text file will be created with all the requirements used to create the app.
4. git init :- In order to push the files into heroku
5. git add .
6. git commit -m 'Initial commit'
7. heroku login  :- login to heroku
8. heroku create appname
9. git push heroku master
10. Url will be appeared in the cmd. Copy & paste the url in the web browser.

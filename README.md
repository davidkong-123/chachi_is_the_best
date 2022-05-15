
<!-- TABLE OF CONTENTS -->



<!--Chess -->
### About The Project -- E commerce website

This is a project to build a template e-commerce website for a fashion designer-- Nour, to sell his designed sweater to the public. 

Website Template deployed on Heroku: https://chachi-the-best.herokuapp.com/


Demo:

![Screenshot 2022-05-15 020002](https://user-images.githubusercontent.com/57188393/168459351-c995c399-e97e-442c-ae34-08e2d34ac9c5.jpg)



### Built With

* Python
* Django
* HTML
* CSS
* JavaScript
* Heroku
* Github


### Manual and Intro git command
1. create virtual environmet
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate

2. download required pipleine
pip install -r requirements.txt

3. migrate database
python manage.py makemigrations
python manage.py migrate


*****Pull changes from github and activate venv <- do this first before working on anything*****

git status // Do this to check your current branch before doing any work
git fetch
git pull
git checkout -b <branch1> //branch1 is the branch name

cd ecommerce

*****activate venv*****

type v and press tab -> automatically goes to .\venv
type S and press tab -> automatically goes to \script
type A and press tab -> automatically goes to \activate
Tab goes through alphabetically

*****Getting into the website*****

cd ecommerce

activate venv

pip install -r requirements.txt <-- sync up pipelines


python manage.py runserver

*****Creating superuser for website*****

cd ecommerce

python manage.py createsuperuser

Add username, password, email

Go to http://127.0.0.1:8000/admin

log in using your username, password credentials

*****Updating image*****

To update the image, Click on products -> product name (e.g. challenger jacket), then upload image file (must be JPG)

*****last step*****

git status //check your work on your current branch

git add -A

git commit -m "Meaningful message"

git push


**/end/**

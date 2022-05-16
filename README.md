
<!-- TABLE OF CONTENTS -->



<!--Chess -->
### About The Project -- E commerce website

This is a project to build a template e-commerce website for a fashion designer-- Nour, to sell his designed sweater to the public. 

Website Template deployed on Heroku: https://chachi-the-best.herokuapp.com/


Demo:


1. Add items


https://user-images.githubusercontent.com/57188393/168517990-0c43c2f9-b9c4-4dbd-866b-c17a8d1b22af.mp4


2. Delete items


https://user-images.githubusercontent.com/57188393/168518015-4e2bad17-5cd5-486a-bf63-6aaf2fdff7c6.mp4


3. Checkout items 



https://user-images.githubusercontent.com/57188393/168518169-8240e463-f42f-4ef7-923c-663b95a167be.mp4


4. Pay with Paypal



https://user-images.githubusercontent.com/57188393/168518172-df05dc10-85ac-41d2-96d8-20bdf8a5b349.mp4


<p align="right">(<a href="#top">back to top</a>)</p>

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

  
  <p align="right">(<a href="#top">back to top</a>)</p>

**/end/**

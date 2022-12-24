how to do everything?

create virtual env
conda create --name MoMaShop django
conda activate MoMaShop

pip install -r requirements.txt

navigate to directory
cd "PATH TO YOUR DIRACTORY"


do the following
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser --optional

python manage.py shell < setup.py

python manage.py runserver

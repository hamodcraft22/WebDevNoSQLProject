

This is a Univertsity Project for Bahrain Polytechnic 3rd year course - WebDevelpmoment with NoSQL Dony By Mohamed Adel Hasan | 202002789

---

# Django MoMa Shop

This is a complete e-commerce website built with Django and linked with Djongo, Bootstrap and custome CSS styling as well.

---

## Project Summary

The website displays products. Users can add and remove products to/from their cart while also specifying or updating or even deleting the quantity of each item. Users can also comment on each prodect or even review the whole webside in the reviews tab. a superuser is also able to add to remove items from the store. 

![image](https://user-images.githubusercontent.com/67144555/209437945-704456f1-f78a-4c51-a4f8-16deae1cbb43.png)

---

## Running this project

To get this project up and running you should start by having Python, MongoDB installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You are recomended to use the cmd prompt from anaconda navigator


Clone or download this repository and open it in your editor of choice. In an anconda CMD terminal, run the following command in the base directory of this project

```
conda create --name MoMaShop django
```

That will create a new envaormint `MoMaShop` in your project directory. Next activate it with this command:

```
conda activate MoMaShop
```

Then install the project dependencies with

```
pip install -r requirements.txt
```


Then setup all the database linkages + defult data

```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py shell < setup.py
```


--optional, create a superuser account to be bale to chnage store config (limited to super users only)

```
python manage.py createsuperuser 
```


Now you can run the project with this command

```
python manage.py runserver
```

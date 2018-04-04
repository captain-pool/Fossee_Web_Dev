#FOSSEE Summer Fellowship Assignment

##Topic : Spoken Tutorial Project Web Development Work
Python Version-: 3.5
Packages used:
* Django 2.0.3  ``` pip install django```
* mathfilters   ```pip install mathfilters```

##Database Required
* DB Name ```Fossee```
* DB Username -: export the username as an environment variable of name "FOSS_UNAME"
	* Linux/UNIX Users
		```
		export FOSS_UNAME=<your_username>
		```
	* Windows Users
		```
		SET FOSS_UNAME=<your_username>
		```

* DB Password -: export the username as an environment variable of name "FOSS_PWD"
	* Linux/UNIX Users
		```
		export FOSS_PWD=<your_password>
		```
	* Windows Users
		```
		SET FOSS_PWD=<your_password>
		```

#Database Setup
* Linux/UNIX Users with Python 3 installed
	```
	python3 manage.py makemigrations
	python3 manage.py migrate
	```
* Windows Users with Python 3 installed
	```
	python manage.py makemigrations
	python manage.py migrate
	```
#Creating Admin Account
* Linux/UNIX Users with Python 3 installed
	```
	python3 manage.py createsuperuser
	```
* Windows Users with Python 3 installed
	```
	python manage.py createsuperuser
	```

**All the Data of the database is entered through the Django Admin Account**

#Run the Project:
* Linux/UNIX Users with Python 3 installed
	```
	python3 manage.py runserver
	```
* Windows Users with Python 3 installed
	```
	python manage.py runserver
	```



# django timezone
It is django based timezone project.

# Instructions 

1) ### Installations
  Make sure to have python version 3 install on you pc or laptop. 
  If not install it from [here](https://www.python.org) <br>
  **Clone repository** <br>
  `https://github.com/surajkarale15/timezone.git`<br>
  `cd timezone`
  
2) ### Installing dependencies 
  It will install all required dependies in the project.<br>
  `pip install -r requirements.txt`
  
3) Add 'Country,Task_Type,timezone_details,timezone_output,User' to your 'INSTALLED_APPS' setting.
	INSTALLED_APPS={
		...
		'Country',
		'Task_Type',
		'timezone_details',
		'timezone_output',
		'User',
		
		...
	}
	
	Add the following to your projects 'urls.py' file, substituting 'api/v1/'
	for whatever you want the service base url to be.
	urlpatterns = [
    ...
    url('country/',include('Country.urls')),
    url('task_type/',include('Task_Type.urls')),
    url('user/',include('User.urls')),
    url('timezone_detail/',include('timezone_details.urls')),
    url('timezone_output/',include('timezone_output.urls')),
	...
	]
	
4) ### Migrations 
  To run migrations. <br>
  `python manage.py makemigrations`<br>
  `python manage.py migrate`

5) ### Running locally
  To run at localhost. It will run on port 8000 by default.<br>
  `python manage.py runserver` 
 
 

  

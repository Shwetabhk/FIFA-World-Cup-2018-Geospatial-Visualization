# FIFA-World-Cup-2018-Geospatial-Visualization

This app is made with the purpose of visualising a spatio temporal dataset of FIFA World Cup through Geospatial Visualization
using map box. You can see various categories:

	1.Teams
	2.Stadiums
	3.Channels
	4.Matches
	
You can see the whole bracket of FIFA World Cup 2018 and click on "Plot Match" to create a marker on the stadium that match was held in and when you click on the marker you can see the details of the match and you can comment too.

When you open the app you have to login first or you can click "create one" to register. The website is hosted on Heroku
the link is
	
	https://gentle-chamber-24928.herokuapp.com/

This app runs on Python 3.6. Make sure you have Python 3.6 and pip installed.


# Clone the Repository

Open the terminal and run the command:

		git clone https://github.com/Shwetabhk/FIFA-World-Cup-2018-Geospatial-Visualization.git

# Create a virtual environment

open your working directory in the terminal and run the following commands:

		pip install virtualenv

		python -m virtualenv Skylark

		source Skylark/bin/activate


# Install the requirements

Open the cloned folder in the terminal(virtual environment) and run the following commands:

		pip install -r requirements.txt


# Run the following command

	python manage.py collectstatic


# Run the server

		python manage.py runserver
    
Now open the app in localhost:8000



	

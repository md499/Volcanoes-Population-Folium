# Volcanoes-Population-Folium

This is a program that uses the built in python libraries- folium and pandas- to visualize volcanoes across the world by using the "volcanoes.txt" file. This program also analayzes population of countries
 
Map1.html: Has a base layer and map layer. There is also a layer control panel that helps the user see either volcanoes across the world, or population of countries. 
Map1.py: Contains the final code for the program. 

All updated changes will be stored in map1.html
The other .py programs(map_popup, map_advacned, etc) and .html files contain a step-by-step implementation of the this program with each version having a new feature. 

Volcanoes.txt: Contains data of volcanoes across the world - which are analyzed using pandas library in python
world.json: Contains country name, population - also analyzed using pandas library


Clone this repository: git clone https://github.com/md499/Volcanoes-Population-Folium.git


Check images folder to see output: 

complete.png: contains the final output of volcanoes, poulation and a layer control. 

volcanoes.png: contains picture of "pins" of volcanoes around the world-with popup that contains info about volcanoes. 

population.png: contains picture of "blocks" of countries with popup about population stats.


1. Installing dependencies
#Library
install pip
pip install python
pip install folium

2. What are the files present(If a file name isnt listed below, you dont need to use it!)
map1_initial.py 
Creates a based map(using folium) and adds pins for volcanoes 

map1_popup_simple.py 
Adds a popup message box to the pins which provides info about volcanoes. 
Navigate to map1_popup_simple.html and map1_popup_advanced.hmtl to see output.

map1.py: 
Contains the final output: popup about volcanoes and population and adds a layer control panel using folium
Navigate to Map1.html to view output


3. Running the code:
#make sure you have pip and folium installed, else refer to 1.

Clone this repo:
$ git clone https://github.com/md499/Volcanoes-Population-Folium.git

Navigate to the repo: 
$ cd Volcanoes-Population-Folium 

Open up Python inside the directory Volcanoes-Population-Folium: 

$ python

This will open up python inside your Command Line Interface. 

Next, copy and paste the code from map1.py into the Command Line Interface

Open up map1.html to see the final output.





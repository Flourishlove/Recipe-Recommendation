##########################################################################
############ C S E  6 2 4 2  G R O U P  P R O J E C T ####################
##########################################################################
############## T E A M  1 4   H E A L T H N I N J A ######################
##########################################################################

DESCRIPTION 
##########################################################################
There is the final result of team 14 (Healthninja!!!). Our project is to make a recipe recommendation system.

People always face same problem in their daily life: What to eat and how to eat healthily. What’s more, people who love cooking usually don’t know how to start when facing too many ingredient pairings. Our Recipe Recommendation System gives users nutritious recipe choices which also satisfy their personal taste. Our target users are busy students and professionals who want to eat healthy. Our goal is to help people with their meal decision and bring up their health consciousness.

 Our data is mainly from a recipe website called yummly. We combined API and crawling approaches to get over 19,000 pieces of recipe information. We also used table of nutrition facts from Kaggle. 

We adopted a new approach in which we analyze recipes using their ingredients. Different ingredient has different compound, and thus they have different flavor. Based on this, we used clustering algorithm (Hierarchy and DBSCAN) to categorize recipes and label them. Then we used Silhouette method to evaluate the clustering result, and adopted DBSCAN as our main cluster algorithm. After that, we use user’s flavor preference and body condition to further filter out the recipe to recommend. We used Estimated Energy Requirements equations to meet individual needs for dietary intake. Finally, the result recipes is presented as a website with user-friendly interface.
##########################################################################

INSTALLATION
##########################################################################
In command prompt, enter “CODE” folder and install all necessary python libraries:
$ cd CODE
$ sudo pip install -r requirements.txt
$ python application.py
Then you will see something like * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit), Which means you run our demo successfully. Go to you browse and enter localhost:5000, you will see our webapplication.

If you don’t want to install all the libraries and packages in your system, you can use virtualenv to setup virtual environment:
$ sudo pip install virtualenv
$ cd CODE
$ virtualenv venv
$ . venv/bin/activate  (For Windows user: $ venv\Scripts\activate)
$ pip install -r requirements.txt
$ python application.py

This option provides you with a virtual environment in folder venv. Whenever you want to run the demo, you can just use command $ . venv/bin/activate. After testing demo, use 
$ deactivate 
to exist virtual environment.
##########################################################################


EXECUTION 
##########################################################################
while running our demo locally, you can go to your browse and enter localhost:5000 to see the webapplication. 
On the right side, there are totally 9 flavors for you to choose. After choose a flavor, you should enter you body condition and apply get recommendation. Then you will be directed to the second page, which contains the recommended recipes. Each row contains three recipes as one recommendation and thus there may be repeating recipes across rows. You can simply select one of the rows as your today’s food plan, which has already satisfy your flavor and nutritional need.
########################################################################


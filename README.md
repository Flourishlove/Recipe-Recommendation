# Recipe-Recommendation

## Introduction
People always face same problem in their daily life: What to eat and how to eat healthily. What’s more, people who love cooking usually don’t know how to start when facing too many ingredient pairings. Our Recipe Recommendation System gives users nutritious recipe choices which also satisfy their personal taste. Our target users are busy students and professionals who want to eat healthy. Our goal is to help people with their meal decision and bring up their health consciousness.

## Data
[Yummly’s API](https://developer.yummly.com/) <br />
[Open Food Facts Dataset](https://www.kaggle.com/openfoodfacts/world-food-facts) <br />
[Ingredient and Compound matching](https://www.nature.com/articles/srep00196) <br />
Estimated Energy Requirements Diagram

## Project Architecture
![alt tag](https://raw.githubusercontent.com/Flourishlove/Recipe-Recommendation/master/Architecture.png) <br />
1. Combine two original dataset into one big recipe-compound matrix. 
2. With recipe-compound data on hand, we use two machine learning algorithms, hierarchical clustering and DBSCAN, to cluster flavor of recipes based on their compound. In final implementation, we use DBSCAN because it discard those isolated recipes and make recipe distribution better.
3. Use information of user’s body condition to further filter out the recipes to recommend.


## Installation
### 1. Running locally
In command prompt, enter code folder and install all necessary python libraries:
```
$ cd code
$ sudo pip install -r requirements.txt
$ python application.py
```
Then you will see something like
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 103-344-409
```
Which means you run our demo successfully. Go to you browse and enter [localhost:5000](http://127.0.0.1:5000/), you will see our webapplication.

If you don’t want to install all the libraries and packages in your system, you can use virtualenv to setup virtual environment:
```
$ sudo pip install virtualenv
$ cd code
$ virtualenv venv
$ . venv/bin/activate  (For Windows user: $ venv\Scripts\activate)
$ pip install -r requirements.txt
$ python application.py
```
This option provides you with a virtual environment in folder venv. Whenever you want to run the demo, you can just use command $ . venv/bin/activate. After testing demo, use
```
$ deactivate
```
to exist virtual environment.

## Interface 
There are two pages of our webapp. <br />
Choose flavor and enter body condition in the first page.
![alt tag](https://raw.githubusercontent.com/Flourishlove/Recipe-Recommendation/master/page1.png) <br />

Display recommendation on the second page.
![alt tag](https://raw.githubusercontent.com/Flourishlove/Recipe-Recommendation/master/page2.png) <br />

## Dependencies
Flask <br />
scikit-learn <br />

## Solutions to some problems
[Create and Connect to a MySQL Database with Amazon RDS](https://aws.amazon.com/getting-started/tutorials/create-mysql-db/) <br />
[Deploy a flask application on AWS](https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80) <br />
[Import CSV file into MySQL](https://dev.mysql.com/doc/workbench/en/wb-admin-export-import-table.html) <br />


### SQL to load CSV data in workbench for escapsing comma:
```
USE recipe;
LOAD DATA LOCAL INFILE '/Users/meteor/Gatech/Recipe-Recommendation/cleaned_data/recipe_final.csv' INTO TABLE recipe_info FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
```

# Recipe-Recommendation

## Introduction
People always face same problem in their daily life: What to eat and how to eat healthily. What’s more, people who love cooking usually don’t know how to start when facing too many ingredient pairings. Our Recipe Recommendation System gives users nutritious recipe choices which also satisfy their personal taste. Our target users are busy students and professionals who want to eat healthy. Our goal is to help people with their meal decision and bring up their health consciousness.

## Data
[Yummly’s API](https://developer.yummly.com/) <br />
[Open Food Facts Dataset](https://www.kaggle.com/openfoodfacts/world-food-facts) <br />
[Ingredient and Compound matching](https://www.nature.com/articles/srep00196) <br />
Estimated Energy Requirements Diagram

## Project Architecture

## Installation
### 1. Running locally
In command prompt, enter “webflask” folder and install all necessary python libraries:
```
$ cd webflask
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
$ cd webflask
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




## Solutions to some problems
[Create and Connect to a MySQL Database with Amazon RDS](https://aws.amazon.com/getting-started/tutorials/create-mysql-db/) <br />
[Deploy a flask application on AWS](https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80) <br />
[Import CSV file into MySQL](https://dev.mysql.com/doc/workbench/en/wb-admin-export-import-table.html) <br />


### SQL to load CSV data in workbench for escapsing comma:
```
USE recipe;
LOAD DATA LOCAL INFILE '/Users/meteor/Gatech/Recipe-Recommendation/cleaned_data/recipe_final.csv' INTO TABLE recipe_info FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
```

# Recipe-Recommendation
[Create and Connect to a MySQL Database with Amazon RDS](https://aws.amazon.com/getting-started/tutorials/create-mysql-db/)

[Deploy a flask application on AWS](https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80)

[Import CSV file into MySQL](https://dev.mysql.com/doc/workbench/en/wb-admin-export-import-table.html)


### SQL to load CSV data in workbench for escapsing comma:
```
USE recipe;
LOAD DATA LOCAL INFILE '/Users/meteor/Gatech/Recipe-Recommendation/cleaned_data/recipe_final.csv' INTO TABLE recipe_info FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
```

'''use Yummly's API
search ~20 cuisines, 2000 recipes each, only main dishes
Remove dishes with ambiguous cuisine labels

this api only left thousands of calls, so might not be enough to run this code again
'''
import requests
import json
import pandas as pd
import numpy as np
import time

from crawing_recipe import *

def initial_df(cykey,scuisine1,scourse,sresults):
    '''use one cuisine to request and build the inital dataframe
    
    '''
    #r = (requests.get('http://api.yummly.com/v1/api/recipes?' + cykey + '&q=onion+soup&requirePictures=true')).json()
    r = (requests.get('http://api.yummly.com/v1/api/recipes?' + cykey + scuisine1 + scourse + sresults)).json()

    print(r.keys())
    print (r)
    #print (len(r['matches']))
    #build the inital data frame
    yum = pd.DataFrame(r['matches'])
    #parse cuisine and course from 'attributes' and take the first item
    yum['cuisine'] = yum['attributes'].apply(lambda x: x['cuisine'][0])
    yum['course'] = yum['attributes'].apply(lambda x: x['course'][0])
    print (yum['cuisine'].value_counts())
    #remove the first label in cuisine is not 'chinese'
    yum = yum[yum['cuisine']=='Chinese']
    return yum

def grow_df(cuisinedic,cykey,scourse,sresults,yum):
    '''request recipes for all keys in cuisinedic and screen cuisine labels by values in cuisinedic.
    Merge new recipes with exisiting dataframe
    '''
    for cs in cuisinedic:
        try:
            scuisine = '&allowedCuisine[]=cuisine^cuisine-' + cs
            r = (requests.get('http://api.yummly.com/v1/api/recipes?' + cykey + scuisine + scourse + sresults)) .json()
            print (scuisine)

            newrecipes = pd.DataFrame(r['matches'])

            course = []
            cuisine = []
            for item in r['matches']:
                course.append(item['attributes'].get('course', None)[0])
                cuisine.append(item['attributes'].get('cuisine', None)[0])
            newrecipes['course'] = course
            newrecipes['cuisine'] = cuisine

            newrecipes = newrecipes[newrecipes['cuisine']==cuisinedic[cs]]
        
            yum = pd.concat([yum,newrecipes],axis=0,ignore_index=True)
            print (yum.shape)
        except:
            print("Skipping one ......\n")
            pass
        #sleep 5 minutes before next request
        time.sleep(300)
    return yum

def get_more(rec_id, cykey):
    '''use cuisine's id to get more detailed info
    '''
    r = (requests.get('http://api.yummly.com/v1/api/recipe/' +rec_id+'?' + cykey )).json()     
    return r

if __name__ =='__main__':

    cykey = '_app_id=32e5170b&_app_key=fc05363ddbaf8d50bd053ef549eb4980'
    scuisine1 = '&allowedCuisine[]=cuisine^cuisine-' + 'chinese'
    scourse = '&allowedCourse[]=course^course-Main Dishes'
    sresults = '&maxResult=' + '10'
    #build inital dataframe
    yum = initial_df(cykey,scuisine1,scourse,sresults)

    #map the search query with lower case to true labels in 'attributes'
    cuisinedic = {'italian':'Italian', 'mexican':'Mexican', 'southern':'Southern & Soul Food', 'french':'French', 'southwestern':'Southwestern', 'indian':'Indian', 'cajun':'Cajun & Creole', 'english':'English', 'mediterranean':'Mediterranean', 'greek':'Greek', \
    'spanish': 'Spanish', 'german':'German', 'thai':'Thai', 'moroccan':'Moroccan', 'irish':'Irish', 'japanese':'Japanese', 'cuban':'Cuban', 'swidish':'Swidish', 'hungarian':'Hungarain', 'portuguese':'Portuguese','american':'American'}

    yum = grow_df(cuisinedic,cykey,scourse,sresults,yum)

    yum.to_pickle('temp_data/yummly.pkl')
    
    #use api again to get more infomation
    column=list(['index', 'numberOfServings',  'images', 'nutritionEstimates', 'ingredientLines'])
    new_data = pd.DataFrame( columns=column)
    for i in range(7676, len(yum)):
      print(i)
      rec_id=yum['id'][i]
      cykey = '_app_id=32e5170b&_app_key=fc05363ddbaf8d50bd053ef549eb4980'
      try:
        r = get_more(rec_id, cykey)
        df = pd.DataFrame([[i, r['numberOfServings'],  r['images'][0]['imageUrlsBySize']['360'], r['nutritionEstimates'], r['ingredientLines']]], columns=column)
        new_data = new_data.append(df)
      except:
        print('skipped',i)
    
    new_data.to_pickle('temp_data/new_data.pkl')
    
    #crawling some image
    recipe = crawling_image(yum)   
    recipe.to_pickle('temp_data/recipe.pkl')
    
    
    new_data_all= pd.concat([yum,new_data], axis=1, ignore_index=True)


    new_data_all = new_data_all.drop(new_data_all.columns[[13]], axis = 1)

    new_data_all.to_csv('final_data/yum_list.csv')

    

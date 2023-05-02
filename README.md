# Clustering data Using Self Organizing Maps

## Problem Formulation

First all the attributes have been normalized so that the clustering is not dominated by one attribute just because of its range in higher numbers. The input dataset has entries, each having a value for each attribute. After normalizing the data vectors (for all attributes), we follow the SOM algorithm by choosing an input vector randomly. We then find its distance with each cluster (with respect to weights). The cluster with smallest distance is our Best Matching Unit. We calculate how much influence does it have to its neighbouring clusters. Less the radius, more the influence and vice versa. For this we use the exponential function. We then adjust the weights of clusters as per the influence. Since the lattice width decreases with time, so will the influence on far away clusters. Thus the neighbourhood will shrink with time. Learning rate also decreases with time. 

## IRIS data set: 

In order to test the basic implementation, the algorithm was first tested on iris data set with 2 epoch, 25 clusters. The initial learning rate, initial lattice width and the time constant are kept as 0.5, 20 and 3 respectively. You can see the grid as follows

![image](https://user-images.githubusercontent.com/110885397/235714417-8260dd98-268d-46a0-87b3-b025624dbe02.png)

Notice that setosa has the right bottom part (in green).virginica has the left part of the grid and versicolor is on the darker shade of purple, This makes sense as the data set is of 3 different flower species!!!

## World Population Data - 2020:

Dataset obtained from: https://www.kaggle.com/datasets/tanuprabhu/population-by-country-2020 
The data set was obtained from Kaggle. Following are the features that are catered in this library:
• Population (2020)
• Yearly Change
• Net Change Density (P/Km²)
• Land Area (Km²)
• Migrants (net)
• Fert. Rate
• Med. Age
• Urban Pop %
• World Share

Data cleaning was customized as per the dataset provided. Other than data cleaning, all the functions are generic. Note that since geopandas library was used, therefore, some countries did not match the list of countries that the library permitted. Some mismatches of names of countries were manually corrected in the dataset for instance United States was renamed to United States of America. The countries that the library did not support (or found a match of) were printed on the screen so as to highlight that these entries are not visualized. Moreover, countries with Urban Pop % of N.A. are removed from the data set. The identifier / name of the country is labelled on the clusters. 

![image](https://user-images.githubusercontent.com/110885397/235715394-e06cce48-21c8-42ea-8a4e-88a2858a3c5c.png)


## World Happiness Report 2019 
Dataset obtained from: https://www.kaggle.com/datasets/tanuprabhu/population-by-country-2020

Features:
• Score
• GDP per capita
• Social support
• Healthy life expectancy
• Freedom to make life choices
• Generosity
• Perceptions of corruption

![image](https://user-images.githubusercontent.com/110885397/235715616-006260f5-9b73-4542-b113-b132b7942e26.png)

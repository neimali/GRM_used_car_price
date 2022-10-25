# price of used cars in Montreal
+ Created a tool that estimates price of used car to help buyers and sellers know better the market price.
+ Scraped over 4000 advertiments of used cars from Kijiji using python and beautifulsoup4
+ Performed EDA and Engineered attributes of used cars into features that can be fed to models
+ Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
+ Built a client facing API with flask

## Code and Resources Used
+ Python version: 3.7
+ Packages: pandas, numpy, sklearn, matplotlib, seaborn, beautifulsoup4, flask, json, pickle
+ Scraper notebook: [https://nbviewer.org/github/Pyligent/Car_ETL_PROJECT/blob/master/kijii_car_scaper.ipynb](https://nbviewer.org/github/Pyligent/Car_ETL_PROJECT/blob/master/kijii_car_scaper.ipynb)
+ Flask Productionization: [https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2](https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2)

## Web scraping
From Kijiji.com scraped over 4000 used cars advertisements. With each job, we got the following:
+ Brand
+ Model
+ Year of production
+ Price
+ Color
+ Configuration
+ Condition
+ BodyType
+ Drive Wheel Configuration
+ Transmission Type
+ Fuel Type
+ Mileage 
+ Carproof

## Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:
+ Removed rows without _price_
+ Parsed numeric data out of _price_
+ Replace all bed values in _Configuration_ by 'na' 
+ Translate French content into English
+ Drop column _Condition_
+ convert minors _color_ and 'na' to other
+ convert the data format of _Mileage_ from string to integer
+ convert _Carproof_ into binary feature (whether has carproof)

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights pictures.
![heat map of numerical features](https://github.com/neimali/GRM_used_car_price/blob/main/heatmap.png)
![histogram of brands](https://github.com/neimali/GRM_used_car_price/blob/main/brand.png)
Pivot table of body type
| body type     | Average price |
| ------------- |:-------------:|
| Convertible   | 48410         | 
| Coupe (2 door)| 47804         |  
| Hatchback     | 23796         |
| Other         | 28374         | 
| Pickup Truck  | 39439         | 
| SUV           | 33556         | 
| Sedan         | 23558         | 
| Van           | 31818         | 
| Wagon         | 18171         | 

## Model Building
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 30%.

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

Three different models:
+ **Multiple Linear Regression** – Baseline for the model
+ **Lasso Regression** Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
+ **Random Forest** Again, with the sparsity associated with the data, I thought that this would be a good fit.

## Model Performance
the Random Forest model far outperformed the other approaches on the test sets.
+ **Multiple Linear Regression** - 10423
+ **Lasso Regression** - 9115
+ **Random Forest** - 8548

## Productionization
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the tutorial in the reference section above. The API endpoint takes in a request with a list of values from an used car advertisement and returns an estimated price.


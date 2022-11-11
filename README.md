# Surfs_up_Challenge

## Overview of the statistical analysis:

#### After initial analysis of the weather data, W. Avy delivered the task of providing temperature trends for June and December. The Hawaii.SQLite database was accessed using sqlalchemy. Next, a query was created for each month to filter for their daily temperature. With this information, two data frames were created and used to calculate the temperature statistics for each month. With this information, we can show W. Avey whether or not the ice cream shop is sustainable year-round. 

## Results:

June Temperature Statistics:

<img width="137" alt="june_temp_stats" src="https://user-images.githubusercontent.com/108249510/201273569-bc9e3ffa-3f6e-4055-9e34-6aef375d8203.png">

December Temperature Statistics:

<img width="134" alt="dec_temp_stats" src="https://user-images.githubusercontent.com/108249510/201273610-ac98a9a2-2014-4205-bd51-96e06d194c00.png">


### Below are three key weather differences between June and December:

#### 1. One key difference is the min temperature for each month. The    lowest temperature for June is 64 compared to 56 for December.

#### 2. A second key difference is the station count for each month. June has 1,700 temperature counts, while December only has 1,517.

#### 3. The third key difference is the variance in temperature. For example, in June, the temperature tends to stay in the 70s, while the temperature may drop into the 60s and 50s in December.  

## Summary:

#### From the statistics, we learned that the temperature could drop into the 60s and 50s during December. We also learned that there are more temperature recordings for June compared to December. Although there are differences between June and December temperatures, they aren't drastic. One thing to remember is that Hawaii has a lot of humidity. As a result, this can cause people to think it's warmer than it is. 

## Below are two queries that can assist W. Avy in making a confident decision.

#### 1. Rain is another aspect that W. Avy might ask us about. Therefore it would be a good idea to create a query that calculates the statistics for precipitation.

#### 2. As mentioned before, humidity is another common type of weather in Hawaii. As a result, it would be helpful to show the humidity statistics, especially considering the rain and temperature drop.

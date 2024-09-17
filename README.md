# EXPERIMENT 3: PYTHON DATA ANALYSIS (PANDAS)

Name: Barretto, Aron Caleb R.

Section: 2ECE-D

Date Submitted: September 16, 2024

## I. Learning Objectives: 

1. To identify the codes and functions incorporated in the Pandas library

2. To be able to apply and use the different codes and functions in creating a Python program using a
Pandas library

## II. Instructions:

Write a Python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter
notebook in the dedicated submission bin.

For this programming assignment, download the following file and save to your default user folder:
http://bit.ly/Cars_file

## III. Documentation

### Problem 1:

Using knowledge obtained from the experiment and demonstrations:

a. Load the corresponding .csv file into a data frame named cars using pandas

In order to load the .csv file into the data frame, first, we must import the pandas as pd to use pandas to import the file

```ruby
import pandas as pd
```


After importing the pandas library, make a variable to import the .csv file to the data frame:

```ruby
cars = pd.read_csv('cars.csv')
cars
```
Therefore, the .csv file is now stored in the data frame.

![image](https://github.com/user-attachments/assets/7d9bbdd0-b40a-441c-b491-cfbc71771595)
![image](https://github.com/user-attachments/assets/74d33e6e-8149-4734-95da-a8d2180f0c95)

b. Display the first five and last five rows of the resulting cars.

In order to show the first 5 rows only, this code was typed:

```ruby
cars.head()
```
Therefore, the output is shown:

![image](https://github.com/user-attachments/assets/a627b62a-38f0-4a49-ae87-5db6bfd4d2dd)

To show the last 5 rows only, this code was typed:

```ruby
cars.tail()
```

Therefore, the output is shown:

![image](https://github.com/user-attachments/assets/72c3e3be-12af-4048-93c1-0d9044afede1)

This concludes the first problem.


### Problem 2:

Using the data frame cars in problem 1, extract the following information using subsetting, slicing and
indexing operations:

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.

The problem states that the first rows must be the output but only the odd-numbered columns. Since the index starts from 0, it must start with the first column and increment by 2. Therefore the code is now written like this:

```ruby
output_cars = cars.iloc[:, 1::2]
output_cars.head()
```

I used the .iloc function so I can choose the rows and columns of the data frame, allowing all rows to be chosen, but for the columns, starting from the 1st column, then I increment by 2 so the order (column 1,3,5,7,...) was followed.

Which results to this output:

![image](https://github.com/user-attachments/assets/e0ffb488-ce1e-4425-9097-bafd576a2f44)

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

In order to show only the row of the Model of 'Mazda RX4', this code was followed:

```ruby
cars.loc[cars['Model'] == 'Mazda RX4']
```

The output will be shown like this:

![image](https://github.com/user-attachments/assets/298951c9-b53b-4a1a-a856-934dae889f0a)

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

In order to answer the question, the code was written below:

```ruby
cars.loc[(cars['Model'] == 'Camaro Z28'), ['Model','cyl']]
```

This code looks for the model of 'Camaro Z28', then will show the 'Model' and the value of 'cyl'.

![image](https://github.com/user-attachments/assets/a38a4c89-7d4e-4ac1-9b51-27f02b9b77bc)

Therefore, the answer is 8 cylinders.

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

For this question, I used a list of the given car models, then using the code below, this is how I used indexing to find the cylinders and gear for the given car models.

```ruby
car_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(car_models)][['Model','cyl', 'gear']]
```

I used the code 
```
.isin
```
to filter out the car models and check if the given car model matches the list. Then the output would show the given car model with the given cylinders(cyl) and gear.

![image](https://github.com/user-attachments/assets/c0cfe91f-47dc-42fb-8d0e-3f301ffa8729)

Therefore here are the answers:

Mazda RX4 Wag = 6 cylinders and 4 gears

Ford Pantera L = 8	cylinders and 5 gears

Honda Civic = 4 cylinders and 4 gears


The last part of problem 2 was pretty hard because when I try to add '==' instead of '.isin', it gives very long errors. All in all, this experiment is super fun to finish.



## VERSIONS:

v2.0 Uploaded the second problem (with outputs as pictures)

v1.75 - Minor Explanation Fixed

v1.5 - Uploaded the first problem (with outputs as pictures)

v1.0 - The repository was created



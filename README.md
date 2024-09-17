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




## VERSIONS:

v1.75 - Minor Fixing of Explanations

v1.5 - Uploaded the first problem (with outputs as pictures)

v1.0 - The repository was created



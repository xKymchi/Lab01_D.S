# Lab01_D.S
The following script ‘Assignment_01.py’ reads data from given CSV file ('Automobile.csv') into a pandas DataFrame ('df').
This data is then filtered to only include rows of where the 'horsepower' value is greater than 190. 
It then creates a new DataFrame for this condition ('filtered_df') where the filtered data is then saved into a SQLite database ('Automobile.db' - table name : 'AutomobileHorseP') . 
This script also uses Python's built-in loggin module to keep track of its executions as well as it saves the log messages ('log.log').

In our ‘tests.py’ file we have two functions,
One function ('is_correlation_true()') which tests the hypothesis that cars with higher horsepower tend to have lower acceleration time, 
and a second function ('compare_avg_hk_origin()') which compares the average horsepower of cars from two different origins (American vs European cars).

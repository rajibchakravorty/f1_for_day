### Calculation of F1 score for a specific weekday

#### Data reading

The data in the file MUST be in the following format

```
# some comment in the first list
dates|y|yhat
1999-11-01|0|0
...
```
#### Weekday specification

The weekday MUST be specified by one of the following

"Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"

If this is not maintained, there might be an answer but the validity of the answer CANNOT
be guranteed.

#### Misc Notes

1) Handling missing data:
The first day in the given file is "Monday". Therefore, a simple logic would have been
to collect all the 7th line starting from the 4th line (the first Thursday). However, in this
approach, there is no way to check if there is any date missing in the data.
Therefore, this code reads each line and converts the date to its correspoding weekday and
then collect the result of the desired weekday.

2) Parallelization:

At least 2 points where this could be parallelized - the collection of the data from file and
convering the date to "weekday".

3) Error Handling:

Could be improved immensely (non-existent now)

#### Running the code

1. Change the variable `f1_for_day` in `main.py1` to the desired weekday
2. Save `main.py`
3. Execute `main.py`

The f1 score will be printed on the console

```
F1 for Thursday 0.307692307692
```

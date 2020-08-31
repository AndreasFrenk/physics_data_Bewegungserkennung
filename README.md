# physics_data_Bewegungserkennung

The goal of this project was to identify certain movement patterns that were recorded by the user. The basic idea was that by applying different statistical methods to the data you can recognize the recorded movement. The statistical methods were first applied in Python and then we analyzed that data in WEKA, which is a perfect tool for this kind of task.

The data from https://github.com/makeabilitylab/signals/tree/master/Projects/GestureRecognizer/GestureLogs are used.

This repository already contains all test and training data. First, the data was smoothed or adjusted. The rest phases of the movement, i.e. in time intervals in which "nothing happens" are sorted out (see clean_raw_data_physics.py).

Then the data was divided into 3 categories. There are WindowSize 5, 10 and 20. In each case 5, 10 or 20 data records are combined. The statistical methods that have been used are:

Average value, standard deviation, variance, median, minimum value, maximum value, average absolute deviation from the mean

The test data is written in clean_data_to_statistical_methods_physics.py. The training data is written in create_training_data_physics_statistical_methods.py.

There are a total of 5 users and 3 movements (backhand tennis, midair-S, shake). Each user has 5 records of these movements. 3 of the 5 data sets were selected for the training data and 2 for the test data.

Good results (mostly 80-90%) could be achieved with Weka. The exception was Bryan's movement, although this only happened once or twice.

The data can be visualized in 3 ways:

Visualize_Data.py (Visualization of raw data)

![Alt text](./images/raw_data_backhand_tennis.png?raw=true "Title")

(Visualization of the cleaned raw data) 
The sorting out of the "resting phase" can be clearly seen

![Alt text](./images/cleaned_raw_data_backhand_tennis.png?raw=true "Title")


Visualize_Statistical_Methods.py (Visualization of the statistical methods)

![Alt text](./images/Statistical_Methods_datasets_backhand_tennis.png?raw=true "Title")



compare_statistical_Methods.py (difference of the statistical methods between two
datasets)

![Alt text](./images/Statistical_Methods_datasets_backhand_tennis_Comparison.png?raw=true "Title")


WEKA-RESULT ON AVERAGE between 80-90%
![Alt text](./images/Weka_Ergebnis_Backhand_WindowSize_5.PNG?raw=true "Title")



There are also other CSV files here, which are the result of splitting a large data set with several movements. The result contains only one movement at a time.

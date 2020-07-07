import csv
import pandas as pd 
import random
import numpy as np


def transform_sensor_data_to_array(datasets,patterns,distance):

    
    entire_array = []

    for i in range(0,len(datasets)):
            x_values = []
            y_values = []
            z_values = []


            for element in range(0, len(datasets[i])):

                x = datasets[i][' X'][element]
                y = datasets[i][' Y'][element]
                z = datasets[i][' Z'][element]

                x_values.append(x)
                y_values.append(y)
                z_values.append(z)


                if element % distance == 0:
                    if element != 0:
                        x_mean = np.mean(x_values)
                        x_std_deviation = np.std(x_values)
                        x_variance = x_std_deviation * x_std_deviation
                        x_median = np.median(x_values)
                        x_min = np.min(x_values)
                        x_max = np.max(x_values)
                        # average absolute distance https://github.com/arturjordao/WearableSensorData/blob/master/Catal2015.py line 23
                        x_add = np.mean(np.absolute(x_values - x_mean))

                        y_mean = np.mean(y_values)
                        y_std_deviation = np.std(y_values)
                        y_variance = y_std_deviation * y_std_deviation
                        y_median = np.median(y_values)
                        y_min = np.min(y_values)
                        y_max = np.max(y_values)
                        y_add = np.mean(np.absolute(y_values - y_mean))


                        z_mean = np.mean(z_values)
                        z_std_deviation = np.std(z_values)
                        z_variance = z_std_deviation * z_std_deviation
                        z_median = np.median(z_values)
                        z_min = np.min(z_values)
                        z_max = np.max(z_values)
                        z_add = np.mean(np.absolute(z_values - z_mean))

                        # Average of the square roots of the sum of the values of each axis squared √(xi^2 + yi^2+ zi^2) over the ED 
                        # https://github.com/arturjordao/WearableSensorData/blob/master/Catal2015.py
                        average_resultant_acceleration = np.sqrt(np.power(x_mean,2) + np.power(y_mean,2) + np.power(z_mean,2))
                        entire_array.append([x_mean,x_std_deviation,x_variance,x_median,x_min,x_max, x_add,
                                            y_mean,y_std_deviation,y_variance,y_median,y_min,y_max, y_add,
                                            z_mean,z_std_deviation,z_variance,z_median,z_min,z_max, z_add, 
                                            average_resultant_acceleration,
                                            patterns[i]])

                        x_values = []
                        y_values = []
                        z_values = []
                        acc_Total_values = []
                    #Sliding Window 50%
                    element -= distance/2


    return entire_array


def write_csv_file_statistical_methods_physics(datasets, file_path, patterns, distance):
    dataset = transform_sensor_data_to_array(datasets, patterns, distance)


    with open(file_path + '.csv', mode='w') as new_file:
        writer = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow([' accX_mean',' accX_std_deviation',' accX_variance',' accX_median',' accX_min',' accX_max', ' accX_add',
                        ' accY_mean',' accY_std_deviation',' accY_variance',' accY_median',' accY_min',' accY_max', ' accY_add',
                        ' accZ_mean',' accZ_std_deviation',' accZ_variance',' accZ_median',' accZ_min',' accZ_max', ' accZ_add',
                        ' average_resultant_acceleration',
                         'class'])

        for row in dataset:
            writer.writerow(row)



## This is an example method
## You can now join several datasets and their respective patterns
## Then you can decide how to name your file

# write_csv_file_statistical_methods([data_kreis_1], 'path/to/file' , ['Kreis'])


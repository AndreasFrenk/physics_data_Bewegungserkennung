import csv
import pandas as pd 
import random
import numpy as np 


def transform_sensor_data_to_array(datasets, patterns, windowsize):

    entire_array = []
    for i in range(0, len(datasets)):
        x_values = []
        y_values = []
        z_values = []


        for element in range(0, len(datasets[i])):
            # Glätten der Daten 
            # Daten ,in denen "nichts" passiert, werden aussortiert
            x_total_max = np.max(datasets[i][' X'])
            y_total_max = np.max(datasets[i][' Y'])
            z_total_max = np.max(datasets[i][' Z'])

            x_total_min = np.min(datasets[i][' X'])
            y_total_min = np.min(datasets[i][' Y'])
            z_total_min = np.min(datasets[i][' Z'])

            total_change = x_total_max + y_total_max + z_total_max - x_total_min - y_total_min - z_total_min

            if element + windowsize < len(datasets[i]):
                x_max = np.max(datasets[i][' X'][element:element+windowsize])
                x_min = np.min(datasets[i][' X'][element:element+windowsize])
                y_max = np.max(datasets[i][' Y'][element:element+windowsize])
                y_min = np.min(datasets[i][' Y'][element:element+windowsize])
                z_max = np.max(datasets[i][' Z'][element:element+windowsize])
                z_min = np.min(datasets[i][' Z'][element:element+windowsize])

                x_change = np.abs(x_max - x_min)
                y_change = np.abs(y_max - y_min)
                z_change = np.abs(z_max - z_min)

                total_change_window = x_change + y_change + z_change

                # x_total_mean = np.abs(np.mean(datasets[i][' X'][element:element+windowsize]))
                # y_total_mean = np.abs(np.mean(datasets[i][' Y'][element:element+windowsize]))
                # z_total_mean = np.abs(np.mean(datasets[i][' Z'][element:element+windowsize]))

                # summed_mean = x_total_mean + y_total_mean + z_total_mean
                
                if total_change * 0.05 < total_change_window:
                    x = datasets[i][' X'][element]
                    y = datasets[i][' Y'][element]
                    z = datasets[i][' Z'][element]
                    entire_array.append([x,y,z,patterns[i]])
 
    return entire_array


def write_csv_file_physics(datasets, file_path, patterns, windowsize):
    dataset = transform_sensor_data_to_array(datasets, patterns, windowsize)
    with open(file_path + '.csv', mode='w') as new_file:
        writer = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow([' X', ' Y', ' Z', 'class'])

        for row in dataset:
            writer.writerow(row)


# write_csv_file(data_kreis,data_kreis,'Kreis_1','Kreis_2')


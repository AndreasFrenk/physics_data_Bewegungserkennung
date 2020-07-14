import csv
import pandas as pd 
import random
import numpy as np 
from Visualize_Data import visualize_data

def transform_sensor_data_to_array(datasets, patterns, windowsize, startposition):

    entire_array = []
    for i in range(0, len(datasets)):

        x_values = []
        y_values = []
        z_values = []
        interval_of_no_motion = 0
        # Glätten der Daten 
        # Daten ,in denen "nichts" passiert, werden aussortiert
        x_total_max = np.max(datasets[i][' X'])
        y_total_max = np.max(datasets[i][' Y'])
        z_total_max = np.max(datasets[i][' Z'])

        x_total_min = np.min(datasets[i][' X'])
        y_total_min = np.min(datasets[i][' Y'])
        z_total_min = np.min(datasets[i][' Z'])
        
        x_total_change = np.abs(x_total_max - x_total_min)
        y_total_change = np.abs(y_total_max - y_total_min)
        z_total_change = np.abs(z_total_max - z_total_min)


        total_change = x_total_change + y_total_change + z_total_change


        for element in range(startposition, len(datasets[i])):

            interval_of_no_motion +=1
            
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


                if (x_total_change  * 0.1 < x_change) and (y_total_change  * 0.1 < y_change) and (z_total_change  * 0.1 < z_change):
                    interval_of_no_motion = 0


                if total_change * 0.1 < total_change_window:
                    x = datasets[i][' X'][element]
                    y = datasets[i][' Y'][element]
                    z = datasets[i][' Z'][element]
                    entire_array.append([x,y,z,patterns[i]])

                if interval_of_no_motion > 20 and len(entire_array) > 80:
                    break

    return entire_array,element


def write_csv_file_physics(datasets, file_path, patterns, windowsize):

    position = 0
    while position < len(datasets[0]):
        dataset, endposition = transform_sensor_data_to_array(datasets, patterns, 10, position)
        interval = endposition - position
        if interval == 0:
            break

        with open(file_path + str(position) + '.csv', mode='w') as new_file:
            writer = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            writer.writerow([' X', ' Y', ' Z', 'class'])

            for row in dataset:
                writer.writerow(row)

        chunked_file = pd.read_csv(file_path + str(position) + '.csv')
        visualize_data([chunked_file], False,True, False, ['Chunk of Fulldatastream'], '')

        position += interval





fulldatastream = pd.read_csv('./fulldatastream.csv')

visualize_data([fulldatastream], False,True, False, ['Full Datastream'], '')

write_csv_file_physics([fulldatastream],'./testmovement', ['muster'],10)


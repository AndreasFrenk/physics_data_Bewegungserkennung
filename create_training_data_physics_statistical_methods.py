import pandas as pd 
from Visualize_Data import visualize_data
from Visualize_Statistical_Methods import visualize_statistical_data
from transform_csv_sensor_data_statistical_methods_physics_data import write_csv_file_statistical_methods_physics
from transform_csv_sensor_data_physics import write_csv_file_physics
from compare_statistical_Methods import compare_statistical_data


user = ['Alexis', 'Bryan', 'Clay', 'Nan', 'Stacy']

movements = ['Midair-S', 'Backhand Tennis', 'Shake']

movements_string = '-Midair-S Backhand Tennis Shake'
window_size_int = [5, 10, 20]
window_size = ['5', '10', '20']

def create_training_set(): 
    
    for b in range(0, len(window_size)):
        filenames = []
        for i in range(0, len(user)):
            for a in range(0, len(movements)):
                
                filenames.append('./relevant_data/Test/' + user[i] + '/'+ movements[a] + '/WindowSize-'+ 
                window_size[b] +'/statistics_data_WindowSize-'+ window_size[b] +'_'+ movements[a] + '_' + user[i] + '_' + str(a + 1) + '.csv')



        training_csv = pd.concat([pd.read_csv(f) for f in filenames])
        training_csv.to_csv('./relevant_data/Training/' + 'WindowSize-'+ window_size[b] + 
        '/Training_WindowSize-' + window_size[b] + movements_string + '.csv', index=False )

create_training_set()

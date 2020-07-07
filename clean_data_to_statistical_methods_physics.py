import pandas as pd 

from Visualize_Data import visualize_data
from Visualize_Statistical_Methods import visualize_statistical_data
from transform_csv_sensor_data_statistical_methods_physics_data import write_csv_file_statistical_methods_physics
from transform_csv_sensor_data_physics import write_csv_file_physics
from compare_statistical_Methods import compare_statistical_data


user = ['Alexis', 'Bryan', 'Clay', 'Nan', 'Stacy']

movements = ['Midair-S', 'Backhand Tennis', 'Shake']

window_size_int = [5, 10, 20]
window_size = ['5', '10', '20']
for i in range(0, len(user)):
    for a in range(0, len(movements)):
        for b in range(0, len(window_size)):

            movement_v1_raw_clean = pd.read_csv('./relevant_data/Test/' + user[i] + '/'+ movements[a] + '/raw_cleaned/raw_data_clean_'+ movements[a] + '_' + user[i] + '_1.csv')
            movement_v2_raw_clean = pd.read_csv('./relevant_data/Test/' + user[i] + '/'+ movements[a] + '/raw_cleaned/raw_data_clean_'+ movements[a] + '_' + user[i] + '_2.csv')
            movement_v3_raw_clean = pd.read_csv('./relevant_data/Test/' + user[i] + '/'+ movements[a] + '/raw_cleaned/raw_data_clean_'+ movements[a] + '_' + user[i] + '_3.csv')
            movement_v4_raw_clean = pd.read_csv('./relevant_data/Test/' + user[i] + '/'+ movements[a] + '/raw_cleaned/raw_data_clean_'+ movements[a] + '_' + user[i] + '_4.csv')
            movement_v5_raw_clean = pd.read_csv('./relevant_data/Test/' + user[i] + '/'+ movements[a] + '/raw_cleaned/raw_data_clean_'+ movements[a] + '_' + user[i] + '_5.csv')


            write_csv_file_statistical_methods_physics([movement_v1_raw_clean], './relevant_data/Test/' + user[i] + '/'+ movements[a] + '/WindowSize-'+ window_size[b] +'/statistics_data_WindowSize-'+ window_size[b] +'_' + movements[a] + '_' + user[i] + '_1',[movements[a]], window_size_int[b])
            write_csv_file_statistical_methods_physics([movement_v2_raw_clean], './relevant_data/Test/' + user[i] + '/'+ movements[a] + '/WindowSize-'+ window_size[b] +'/statistics_data_WindowSize-'+ window_size[b] +'_' + movements[a] + '_' + user[i] + '_2',[movements[a]], window_size_int[b])
            write_csv_file_statistical_methods_physics([movement_v3_raw_clean], './relevant_data/Test/' + user[i] + '/'+ movements[a] + '/WindowSize-'+ window_size[b] +'/statistics_data_WindowSize-'+ window_size[b] +'_' + movements[a] + '_' + user[i] + '_3',[movements[a]], window_size_int[b])
            write_csv_file_statistical_methods_physics([movement_v4_raw_clean], './relevant_data/Test/' + user[i] + '/'+ movements[a] + '/WindowSize-'+ window_size[b] +'/statistics_data_WindowSize-'+ window_size[b] +'_' + movements[a] + '_' + user[i] + '_4',[movements[a]], window_size_int[b])
            write_csv_file_statistical_methods_physics([movement_v5_raw_clean], './relevant_data/Test/' + user[i] + '/'+ movements[a] + '/WindowSize-'+ window_size[b] +'/statistics_data_WindowSize-'+ window_size[b] +'_' + movements[a] + '_' + user[i] + '_5',[movements[a]], window_size_int[b])


            movement_v1_statistical_methods = pd.read_csv('./relevant_data/Test/' + user[i] + '/'+ movements[a] + '/WindowSize-'+ window_size[b] +'/statistics_data_WindowSize-'+ window_size[b] +'_'+ movements[a] + '_' + user[i] + '_1.csv')
            movement_v2_statistical_methods = pd.read_csv('./relevant_data/Test/' + user[i] + '/'+ movements[a] + '/WindowSize-'+ window_size[b] +'/statistics_data_WindowSize-'+ window_size[b] +'_'+ movements[a] + '_' + user[i] + '_2.csv')
            movement_v3_statistical_methods = pd.read_csv('./relevant_data/Test/' + user[i] + '/'+ movements[a] + '/WindowSize-'+ window_size[b] +'/statistics_data_WindowSize-'+ window_size[b] +'_'+ movements[a] + '_' + user[i] + '_3.csv')
            movement_v4_statistical_methods = pd.read_csv('./relevant_data/Test/' + user[i] + '/'+ movements[a] + '/WindowSize-'+ window_size[b] +'/statistics_data_WindowSize-'+ window_size[b] +'_'+ movements[a] + '_' + user[i] + '_4.csv')
            movement_v5_statistical_methods = pd.read_csv('./relevant_data/Test/' + user[i] + '/'+ movements[a] + '/WindowSize-'+ window_size[b] +'/statistics_data_WindowSize-'+ window_size[b] +'_'+ movements[a] + '_' + user[i] + '_5.csv')

            # visualize_statistical_data([movement_v1_statistical_methods, movement_v2_statistical_methods],
            #  ['all'], [movements[a], movements[a]])

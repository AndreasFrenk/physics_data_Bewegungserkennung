import pandas as pd 
from Visualize_Data import visualize_data
from Visualize_Statistical_Methods import visualize_statistical_data
from transform_csv_sensor_data_statistical_methods_physics_data import write_csv_file_statistical_methods_physics
from transform_csv_sensor_data_physics import write_csv_file_physics
from compare_statistical_Methods import compare_statistical_data


user = ['Alexis', 'Bryan', 'Clay', 'Nan', 'Stacy']

movements = ['Midair-S', 'Backhand Tennis', 'Shake']

for i in range(0, len(user)):
    for a in range(0, len(movements)):

        movement_v1 = pd.read_csv('./relevant_data/' + user[i] + 'Gestures/'+ movements[a] + '_1.csv')
        movement_v2 = pd.read_csv('./relevant_data/' + user[i] + 'Gestures/'+ movements[a] + '_2.csv')
        movement_v3 = pd.read_csv('./relevant_data/' + user[i] + 'Gestures/'+ movements[a] + '_3.csv')
        movement_v4 = pd.read_csv('./relevant_data/' + user[i] + 'Gestures/'+ movements[a] + '_4.csv')
        movement_v5 = pd.read_csv('./relevant_data/' + user[i] + 'Gestures/'+ movements[a] + '_5.csv')


        write_csv_file_physics([movement_v1], './relevant_data/Test/' + user[i] + '/'+ movements[a] + '/raw_cleaned/raw_data_clean_'+ movements[a] + '_' + user[i] + '_1',[movements[a]], 10)
        write_csv_file_physics([movement_v2], './relevant_data/Test/' + user[i] + '/'+ movements[a] + '/raw_cleaned/raw_data_clean_'+ movements[a] + '_' + user[i] + '_2',[movements[a]], 10)
        write_csv_file_physics([movement_v3], './relevant_data/Test/' + user[i] + '/'+ movements[a] + '/raw_cleaned/raw_data_clean_'+ movements[a] + '_' + user[i] + '_3',[movements[a]], 10)
        write_csv_file_physics([movement_v4], './relevant_data/Test/' + user[i] + '/'+ movements[a] + '/raw_cleaned/raw_data_clean_'+ movements[a] + '_' + user[i] + '_4',[movements[a]], 10)
        write_csv_file_physics([movement_v5], './relevant_data/Test/' + user[i] + '/'+ movements[a] + '/raw_cleaned/raw_data_clean_'+ movements[a] + '_' + user[i] + '_5',[movements[a]], 10)


        movement_v1_raw_clean = pd.read_csv('./relevant_data/Test/' + user[i] + '/'+ movements[a] + '/raw_cleaned/raw_data_clean_'+ movements[a] + '_' + user[i] + '_1.csv')
        movement_v2_raw_clean = pd.read_csv('./relevant_data/Test/' + user[i] + '/'+ movements[a] + '/raw_cleaned/raw_data_clean_'+ movements[a] + '_' + user[i] + '_2.csv')
        movement_v3_raw_clean = pd.read_csv('./relevant_data/Test/' + user[i] + '/'+ movements[a] + '/raw_cleaned/raw_data_clean_'+ movements[a] + '_' + user[i] + '_3.csv')
        movement_v4_raw_clean = pd.read_csv('./relevant_data/Test/' + user[i] + '/'+ movements[a] + '/raw_cleaned/raw_data_clean_'+ movements[a] + '_' + user[i] + '_4.csv')
        movement_v5_raw_clean = pd.read_csv('./relevant_data/Test/' + user[i] + '/'+ movements[a] + '/raw_cleaned/raw_data_clean_'+ movements[a] + '_' + user[i] + '_5.csv')

        # visualize_data([movement_v1_raw_clean, movement_v2_raw_clean, movement_v3_raw_clean, movement_v4_raw_clean, movement_v5_raw_clean],
        #  False, True, False, [movements[a],movements[a],movements[a],movements[a],movements[a]], user[i])

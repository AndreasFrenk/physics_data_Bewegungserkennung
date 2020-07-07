import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def compare_statistical_data(dataset_1, dataset_2, method): 
    fig, axes = plt.subplots(3, figsize=(10, 10))
    fig.tight_layout(pad=3) # add vertical spacing
    position = 0

    position += 1
    X_mean_difference = []
    Y_mean_difference = []
    Z_mean_difference = []
    # acc_Total_mean_difference = []

    X_std_deviation_difference = []
    Y_std_deviation_difference = []
    Z_std_deviation_difference = []
    acc_Total_std_deviation_difference = []

    X_median_difference = []
    Y_median_difference = []
    Z_median_difference = []
    #acc_Total_median_difference = []

    X_min_difference = []
    Y_min_difference = []
    Z_min_difference = []
    # acc_Total_min = []

    X_max_difference = []
    Y_max_difference = []
    Z_max_difference = []


    Position = []

    length = len(dataset_1) if len(dataset_1) < len(dataset_2) else len(dataset_2)
    for element in range(0,length):
        X_mean_difference.append(dataset_1[' accX_mean'][element] - dataset_2[' accX_mean'][element])
        Y_mean_difference.append(dataset_1[' accY_mean'][element] - dataset_2[' accY_mean'][element])
        Z_mean_difference.append(dataset_1[' accZ_mean'][element] - dataset_2[' accZ_mean'][element])
        # acc_Total_mean.append(dataset_1[ ' accTotal_mean'][element])
        
        X_std_deviation_difference.append(dataset_1[' accX_std_deviation'][element] - dataset_2[' accX_std_deviation'][element])
        Y_std_deviation_difference.append(dataset_1[' accY_std_deviation'][element] - dataset_2[' accY_std_deviation'][element])
        Z_std_deviation_difference.append(dataset_1[' accZ_std_deviation'][element] - dataset_2[' accZ_std_deviation'][element])
        # acc_Total_std_deviation.append(dataset_1[' accTotal_std_deviation'])

        X_median_difference.append(dataset_1[' accX_median'][element] - dataset_2[' accX_median'][element])
        Y_median_difference.append(dataset_1[' accY_median'][element] - dataset_2[' accY_median'][element])
        Z_median_difference.append(dataset_1[' accZ_median'][element] - dataset_2[' accZ_median'][element])
        # acc_Total_median.append(dataset_1[' accTotal_median'])

        X_min_difference.append(dataset_1[' accX_min'][element] - dataset_2[' accX_min'][element])
        Y_min_difference.append(dataset_1[' accY_min'][element] - dataset_2[' accY_min'][element])
        Z_min_difference.append(dataset_1[' accZ_min'][element] - dataset_2[' accZ_min'][element])
        # acc_Total_min.append(dataset[' accTotal_min'])

        X_max_difference.append(dataset_1[' accX_max'][element] - dataset_2[' accX_max'][element])
        Y_max_difference.append(dataset_1[' accY_max'][element] - dataset_2[' accY_max'][element])
        Z_max_difference.append(dataset_1[' accZ_max'][element] - dataset_2[' accZ_max'][element])
        # acc_Total_max.append(dataset[' accTotal_max'])


        Position.append(element)


    methods = ' '
    for a in range(0, len(method)):
        if a == 0:
            methods += method[a]
        else:
            methods += ', ' + method[a]
        if(method[a] == 'mean'):
            axes[0].plot(X_mean_difference, alpha=0.7, label="difference accX_mean {}".format(position))
            axes[1].plot(Y_mean_difference, alpha=0.7, label="difference accY_mean {}".format(position))
            axes[2].plot(Z_mean_difference, alpha=0.7, label="difference accZ_mean {}".format(position))


            for i in range(0, 3):
                axes[i].legend()

        if(method[a] == 'std_deviation'):
            axes[0].plot(X_std_deviation_difference, alpha=0.7, label="difference accX_std_deviation {}".format(position))
            axes[1].plot(Y_std_deviation_difference, alpha=0.7, label="difference accY_std_deviation {}".format(position))
            axes[2].plot(Z_std_deviation_difference, alpha=0.7, label="difference accZ_std_deviation {}".format(position))
            
            for i in range(0, 3):
                axes[i].legend()

        if(method[a] == 'median'):
            axes[0].plot(X_median_difference, alpha=0.7, label="difference accX_median {}".format(position))
            axes[1].plot(Y_median_difference, alpha=0.7, label="difference accY_median {}".format(position))
            axes[2].plot(Z_median_difference, alpha=0.7, label="difference accZ_median {}".format(position))

            for i in range(0, 3):
                axes[i].legend()

        if(method[a] == 'min'):
            axes[0].plot(X_min_difference, alpha=0.7, label="difference accX_min {}".format(position))
            axes[1].plot(Y_min_difference, alpha=0.7, label="difference accY_min {}".format(position))
            axes[2].plot(Z_min_difference, alpha=0.7, label="difference accZ_min {}".format(position))

            for i in range(0, 3):
                axes[i].legend()

        if(method[a] == 'max'):
            axes[0].plot(X_max_difference, alpha=0.7, label="difference accX_max {}".format(position))
            axes[1].plot(Y_max_difference, alpha=0.7, label="difference accY_max {}".format(position))
            axes[2].plot(Z_max_difference, alpha=0.7, label="difference accZ_max {}".format(position))

            for i in range(0, 3):
                axes[i].legend()

    axes[0].set_title("Difference Accel X" + methods)
    axes[1].set_title("Difference Accel Y" + methods)
    axes[2].set_title("Difference Accel Z" + methods)
    plt.show()



movement_v3_statistical_methods = pd.read_csv('./relevant_data/Test/Alexis/Backhand Tennis/WindowSize-10/statistics_data_WindowSize-10_Backhand Tennis_Alexis_3.csv')
movement_v4_statistical_methods = pd.read_csv('./relevant_data/Test/Alexis/Backhand Tennis/WindowSize-10/statistics_data_WindowSize-10_Backhand Tennis_Alexis_4.csv')


compare_statistical_data(movement_v3_statistical_methods, movement_v4_statistical_methods,
 ['mean', 'std_deviation'])

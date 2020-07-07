import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def visualize_statistical_data(datasets, method, pattern): 
    fig, axes = plt.subplots(3, figsize=(18, 18))
    fig.tight_layout(pad=3) # add vertical spacing
    position = 0
    for dataset in datasets: 
        position += 1
        X_mean = []
        Y_mean = []
        Z_mean = []
        # acc_Total_mean = []

        X_std_deviation = []
        Y_std_deviation = []
        Z_std_deviation = []
        X_add = []

        acc_Total_std_deviation = []

        X_median = []
        Y_median = []
        Z_median = []
        #acc_Total_median = []

        X_min = []
        Y_min = []
        Z_min = []
        # acc_Total_min = []

        X_max = []
        Y_max = []
        Z_max = []
        # acc_Total_max = []

        X_add = []
        Y_add = []
        Z_add = []
        
        # Average of the square roots of the sum of the values of each axis squared √(xi^2 + yi^2+ zi^2) over the ED
        # https://github.com/arturjordao/WearableSensorData/blob/master/Catal2015.py
        ARA = []
        Position = []

        for element in range(0,len(dataset)):
            X_mean.append(dataset[' accX_mean'][element])
            Y_mean.append(dataset[' accY_mean'][element])
            Z_mean.append(dataset[' accZ_mean'][element])
            # acc_Total_mean.append(dataset[ ' accTotal_mean'][element])
            
            X_std_deviation.append(dataset[' accX_std_deviation'][element])
            Y_std_deviation.append(dataset[' accY_std_deviation'][element])
            Z_std_deviation.append(dataset[' accZ_std_deviation'][element])
            # acc_Total_std_deviation.append(dataset[' accTotal_std_deviation'])

            X_median.append(dataset[' accX_median'][element])
            Y_median.append(dataset[' accY_median'][element])
            Z_median.append(dataset[' accZ_median'][element])
            # acc_Total_median.append(dataset[' accTotal_median'])

            X_min.append(dataset[' accX_min'][element])
            Y_min.append(dataset[' accY_min'][element])
            Z_min.append(dataset[' accZ_min'][element])
            # acc_Total_min.append(dataset[' accTotal_min'])

            X_max.append(dataset[' accX_max'][element])
            Y_max.append(dataset[' accY_max'][element])
            Z_max.append(dataset[' accZ_max'][element])
            # acc_Total_max.append(dataset[' accTotal_max'])

            X_add.append(dataset[' accX_add'][element])
            Y_add.append(dataset[' accY_add'][element])
            Z_add.append(dataset[' accZ_add'][element])

            ARA.append(dataset[' average_resultant_acceleration'][element])
            Position.append(element)


        methods = ' '
        for a in range(0, len(method)):
            if a == 0:
                methods += method[a]
            else:
                methods += ', ' + method[a]
            if(method[a] == 'mean' or method[a] == 'all'):
                axes[0].plot(X_mean, alpha=0.7, label="accX_mean {}".format(position) + ' ' + '{}'.format(pattern[position-1]))
                axes[1].plot(Y_mean, alpha=0.7, label="accY_mean {}".format(position) + ' ' + '{}'.format(pattern[position-1]))
                axes[2].plot(Z_mean, alpha=0.7, label="accZ_mean {}".format(position) + ' ' + '{}'.format(pattern[position-1]))

                axes[0].set_title("Accel X mean")
                axes[1].set_title("Accel Y mean")
                axes[2].set_title("Accel Z mean")

                for i in range(0, 3):
                    axes[i].legend()

            if(method[a] == 'std_deviation' or method[a] == 'all'):
                axes[0].plot(X_std_deviation, alpha=0.7, label="accX_std_deviation {}".format(position) + ' ' + '{}'.format(pattern[position-1]))
                axes[1].plot(Y_std_deviation, alpha=0.7, label="accY_std_deviation {}".format(position) + ' ' + '{}'.format(pattern[position-1]))
                axes[2].plot(Z_std_deviation, alpha=0.7, label="accZ_std_deviation {}".format(position) + ' ' + '{}'.format(pattern[position-1]))

                axes[0].set_title("Accel X std deviation")
                axes[1].set_title("Accel Y std deviation")
                axes[2].set_title("Accel Z std deviation")
                
                for i in range(0, 3):
                    axes[i].legend()

            if(method[a] == 'median' or method[a] == 'all'):
                axes[0].plot(X_median, alpha=0.7, label="accX_median {}".format(position) + ' ' + '{}'.format(pattern[position-1]))
                axes[1].plot(Y_median, alpha=0.7, label="accY_median {}".format(position) + ' ' + '{}'.format(pattern[position-1]))
                axes[2].plot(Z_median, alpha=0.7, label="accZ_median {}".format(position) + ' ' + '{}'.format(pattern[position-1]))

                for i in range(0, 3):
                    axes[i].legend()

            if(method[a] == 'min' or method[a] == 'all'):
                axes[0].plot(X_min, alpha=0.7, label="accX_min {}".format(position) + ' ' + '{}'.format(pattern[position-1]))
                axes[1].plot(Y_min, alpha=0.7, label="accY_min {}".format(position) + ' ' + '{}'.format(pattern[position-1]))
                axes[2].plot(Z_min, alpha=0.7, label="accZ_min {}".format(position) + ' ' + '{}'.format(pattern[position-1]))

                for i in range(0, 3):
                    axes[i].legend()

            if(method[a] == 'max' or method[a] == 'all'):
                axes[0].plot(X_max, alpha=0.7, label="accX_max {}".format(position) + ' ' + '{}'.format(pattern[position-1]))
                axes[1].plot(Y_max, alpha=0.7, label="accY_max {}".format(position) + ' ' + '{}'.format(pattern[position-1]))
                axes[2].plot(Z_max, alpha=0.7, label="accZ_max {}".format(position) + ' ' + '{}'.format(pattern[position-1]))

                for i in range(0, 3):
                    axes[i].legend()
            
            if(method[a] == 'add' or method[a] == 'all'):
                axes[0].plot(X_add, alpha=0.7, label="accX_add {}".format(position) + ' ' + '{}'.format(pattern[position-1]))
                axes[1].plot(Y_add, alpha=0.7, label="accY_add {}".format(position) + ' ' + '{}'.format(pattern[position-1]))
                axes[2].plot(Z_add, alpha=0.7, label="accZ_add {}".format(position) + ' ' + '{}'.format(pattern[position-1]))

                for i in range(0, 3):
                    axes[i].legend()

            if(method[a] == 'ara' or method[a] == 'all'):
                axes[0].plot(ARA, alpha=0.7, label="ARA {}".format(position) + ' ' + '{}'.format(pattern[position-1]))

                axes[0].legend()

    axes[0].set_title("Accel X" + methods)
    axes[1].set_title("Accel Y" + methods)
    axes[2].set_title("Accel Z" + methods)
    plt.show()



movement_v3_statistical_methods = pd.read_csv('./relevant_data/Test/Alexis/Backhand Tennis/WindowSize-10/statistics_data_WindowSize-10_Backhand Tennis_Alexis_3.csv')
movement_v4_statistical_methods = pd.read_csv('./relevant_data/Test/Alexis/Backhand Tennis/WindowSize-10/statistics_data_WindowSize-10_Backhand Tennis_Alexis_4.csv')


visualize_statistical_data([movement_v3_statistical_methods, movement_v4_statistical_methods],
 ['mean', 'std_deviation'], ['Backhand Tennis', 'Backhand Tennis'])

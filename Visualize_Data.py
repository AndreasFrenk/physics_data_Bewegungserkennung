import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def visualize_data(datasets, accPos,separate_data_visualization,show_3D, pattern, user): 
    fig, axes = plt.subplots(3, figsize=(10, 10))
    fig.tight_layout(pad=3) # add vertical spacing
    position = 0
    for dataset in datasets: 
        position += 1
        X = []
        Y = []
        Z = []
        acc_Total = []
        Position = []
        if not (accPos):
            # If not altered the position of accX is different compared to the others 
            # This could lead to problems if disregarded
            for element in range(0,len(dataset)):
                X.append(dataset[' X'][element])
                Y.append(dataset[' Y'][element])
                Z.append(dataset[' Z'][element])
                # acc_Total.append(dataset[ ' accTotal'][element])
                Position.append(element)
        else: 
            for element in range(0,len(dataset)):
                X.append(dataset['accX'][element])
                Y.append(dataset[' accY'][element])
                Z.append(dataset[' accZ'][element])
                # acc_Total.append(dataset[ ' accTotal'][element])
                Position.append(element)

        ## Shows graph of the accelerometer sensor data
        ## There are several ways to display the data
        ## Feel free to toggle with data

        if(separate_data_visualization):

            axes[0].plot(X, alpha=0.7, label="accX {}".format(position) + ' ' + '{}'.format(pattern[position-1]))
            axes[1].plot(Y, alpha=0.7, label="accY {}".format(position) + ' ' + '{}'.format(pattern[position-1]))
            axes[2].plot(Z, alpha=0.7, label="accZ {}".format(position) + ' ' + '{}'.format(pattern[position-1]))

            axes[0].set_title("Accel X "+ pattern[position-1] + ' ' + user)
            axes[1].set_title("Accel Y "+ pattern[position-1] + ' ' + user)
            axes[2].set_title("Accel Z "+ pattern[position-1] + ' ' + user)

            axes[0].legend()
            axes[1].legend()
            axes[2].legend()


        else:
            axes[0].plot(X, alpha=0.7, label="accX")
            axes[1].plot(Z, alpha=0.7, label="accZ")
            axes[0].legend()
            axes[1].legend()

            
        if(show_3D): 
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot(X,Y,Z)
            
    plt.show()


fulldatastream = pd.read_csv('./fulldatastream.csv')


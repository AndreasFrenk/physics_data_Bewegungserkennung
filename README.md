# physics_data_Bewegungserkennung

Es werden die Daten von https://github.com/makeabilitylab/signals/tree/master/Projects/GestureRecognizer/GestureLogs genutzt. Dabei geht es um die Erkennung der Bewegung.

Dieses Repository enthält bereits alle Test- und Trainingsdaten. Zunächst wurden die Daten geglättet bzw. bereinigt. Dabei wurden die Ruhephasen der Bewegung, d.h. in Zeitintervalle, in denen "nichts passiert", werden aussortiert (s. clean_raw_data_physics.py).

Dann wurden die Daten in 3 Kategorien unterteilt. Es gibt WindowSize 5,10 und 20. Dabei werden jeweils 5, 10 oder 20 Datensätze zusammengefasst. Die statistischen Methoden, die dabei verwendet worden sind, sind:

Durchschnittswert, Standardabweichung, Varianz, Median, Minimalwert, Maximalwert, Durchschnittliche Absolute Abweichung vom Mittelwert

Das Schreiben der Testdaten erfolgt in clean_data_to_statistical_methods_physics.py. Das Schreiben der Trainingsdaten erfolgt in create_training_data_physics_statistical_methods.py.

Es liegen insgesamt 5 Nutzer und 3 Bewegungen (Backhand Tennis, Midair-S, Shake) vor. Jeder Nutzer hat 5 Datensätze dieser Bewegungen. 3 von den 5 Datensätzen wurden für die Trainingsdaten und 2 für die Testdaten ausgewählt.

Mit Weka ließen sich gute Ergebnisse (größtenteils 80-90%) erzielen. Ausnahme dabei war Bryans Bewegung, wobei dies auch nur ein- bis zweimal vorkam.

Die Visualisierung der Daten kann auf 3 Weisen geschehen:

Visualize_Data.py

![Alt text](./images/cleaned_raw_data_backhand_tennis.png?raw=true "Title")

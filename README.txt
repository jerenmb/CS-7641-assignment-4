CS 7641 Assignment 4
Jeren Browning
jbrowning35

The code for this assignment can be found here: https://github.com/jerenmb/CS-7641-Assignment-4

This assignment was built using code taken from https://github.com/JonathanTay/CS-7641-assignment-4. Thanks jontay!

There are two subfolders in this project: 
1) Solution: contains the python/jython code needed to run the assignment
2) BURLAP: Contains the Java BURLAP project and its dependencies

This project was built with Java 1.8.0.121, Jython 2.7.0, and Python 3.5.2 (libraries include Pandas 0.18.0, numpy 1.11.3, matplotlib 1.5.1)

Begin by running the run.bat file in the Solution folder. This runs the jython code against the burlap.jar file.
If you need to recompile the burlap.jar file, go to the BURLAP subfolder and run "ant dist" and copy the executable burlap.jar file to the Solution folder.
The plotter.py file plots most of the charts. The policy maps are available when running the code easyGW, hardGW and varysizeGW scripts in Jython.


Within the Solution folder, there are the outputs from the jython script. These are named: 
1) Easy <solver name>.csv - results on easy grid world
2) Hard <solver name>.csv - results on hard grid world
3) Size <solver name>.csv - results on size experiments

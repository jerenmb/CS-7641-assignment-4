# Run python files in Spyder:
runfile('filepath/name.py')


#FOR ASSIGNMENT 3
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('large-qlearning.csv')
ax = df.plot(x=0,y=1, color="b", label='Steps')
ax.set_xlabel("Iterations")
ax.set_title("Steps per Iterations")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('large-qlearning.csv')
ax = df.plot(x=0,y=2, color="g", label='Reward')
ax.set_xlabel("Iterations")
ax.set_title("Reward per Iterations")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('large-qlearning.csv')
ax = df.plot(x=0,y=3, color="orange", label='Time')
ax.set_xlabel("Iterations")
ax.set_title("Time per Iterations")
plt.show()


#FOR ASSIGNMENT 2
#NN_OUTPUT
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('GA_50_20_10_LOG.csv')
ax = df.plot(x=0,y=1, color="r", label='MSE trg')
df.plot(x=0,y=2, color="g", label='MSE val', ax=ax)
df.plot(x=0,y=3, color="purple", label='MSE tst', ax=ax)
df.plot(x=0,y=4, color="b", label='Training', ax=ax)
df.plot(x=0,y=5, color="orange", label='Validation', ax=ax)
df.plot(x=0,y=6, color="yellow", label='Test', ax=ax)
ax.set_xlabel("Iterations")
ax.set_ylabel("Score")
ax.set_title("GA mating 20 mutating 10 NN")
plt.show()

#FITNESS FUNCTIONS

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('CONTPEAKS_RHC_1_LOG.txt')
dg = pd.read_csv('CONTPEAKS_RHC_2_LOG.txt')
dh = pd.read_csv('CONTPEAKS_RHC_3_LOG.txt')
di = pd.read_csv('CONTPEAKS_RHC_4_LOG.txt')
dj = pd.read_csv('CONTPEAKS_RHC_5_LOG.txt')

# Grab columns, then calculate and plot 
# Convert from dataframe to 1d array
iterations = df[['iterations']].values.flatten()
df_fit = df[['fitness']].values.flatten()
dg_fit = dg[['fitness']].values.flatten()
dh_fit = dh[['fitness']].values.flatten()
di_fit = di[['fitness']].values.flatten()
dj_fit = dj[['fitness']].values.flatten()
fit_array = [df_fit, dg_fit, dh_fit, di_fit, dj_fit]

fitness_scores_mean = np.mean(fit_array, axis=0)
fitness_scores_std = np.std(fit_array, axis=0)
plt.fill_between(iterations, fitness_scores_mean - fitness_scores_std, fitness_scores_mean + fitness_scores_std, alpha=0.1, color="r")
plt.plot(iterations, fitness_scores_mean, 'o-', color="r", label="Mean")
plt.legend(loc="lower right")
plt.xlabel("Iterations")
plt.ylabel("Fitness Score")
plt.title("Contpeaks RHC")
plt.show()



#WORKING
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('KNN_adult_reg.csv')
ax = df.loc[df['param_KNN__metric'] == 'manhattan'].loc[df['param_KNN__weights'] == 'uniform'].plot(kind="scatter", x=5,y=21, color="r", label='Manhattan Uniform')
df.loc[df['param_KNN__metric'] == 'manhattan'].loc[df['param_KNN__weights'] == 'distance'].plot(kind="scatter", x=5,y=21, color="g", label='Manhattan Distance', ax=ax)
df.loc[df['param_KNN__metric'] == 'euclidean'].loc[df['param_KNN__weights'] == 'uniform'].plot(kind="scatter", x=5,y=21, color="purple", label='Euclidean Uniform', ax=ax)
df.loc[df['param_KNN__metric'] == 'euclidean'].loc[df['param_KNN__weights'] == 'distance'].plot(kind="scatter", x=5,y=21, color="b", label='Euclidean Distance', ax=ax)
df.loc[df['param_KNN__metric'] == 'chebyshev'].loc[df['param_KNN__weights'] == 'uniform'].plot(kind="scatter", x=5,y=21, color="orange", label='Chebyshev Uniform', ax=ax)
df.loc[df['param_KNN__metric'] == 'chebyshev'].loc[df['param_KNN__weights'] == 'distance'].plot(kind="scatter", x=5,y=21, color="yellow", label='Chebyshev Distance', ax=ax)
ax.set_xlabel("# of Neighbors")
ax.set_ylabel("Accuracy")
ax.set_title("KNN Adult Train Accuracy")
plt.show()

######
# 3D attempt - WORKING
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('SVM_RBF_madelon_reg.csv')
# print(df)

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

for c, m in [('r', 'o')]:
# [:,4] to access column 4
    xs = df.to_numpy()[:,4]
    ys = df.to_numpy()[:,5]
    zs = df.to_numpy()[:,13]
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('Alpha')
ax.set_ylabel('Gamma Frac')
ax.set_zlabel('Accuracy')
ax.set_title("SVM Madelon Test Accuracy")

plt.show()

# WORKING
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(.1, 1.0, 5)
df = pd.read_csv('DT_adult_timing.csv')
dg = pd.read_csv('ANN_adult_timing.csv')
dh = pd.read_csv('Boost_adult_timing.csv')
di = pd.read_csv('KNN_adult_timing.csv')
dj = pd.read_csv('SVM_RBF_adult_timing.csv')

ax = df.plot(x=0,y=2, color="b", label="DT")
dg.plot(x=0,y=2, color="g", label="ANN", ax=ax)
dh.plot(x=0,y=2, color="r", label="Boost", ax=ax)
di.plot(x=0,y=2, color="orange", label="KNN", ax=ax)
dj.plot(x=0,y=2, color="purple", label="SVM", ax=ax)

ax.set_xlabel("Percentage data included in Test Split")
ax.set_ylabel("Time (seconds)")
ax.set_title("Adult Testing Time")
plt.show()

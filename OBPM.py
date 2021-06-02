import numpy as np
import matplotlib.pyplot as plt
import os

# load datasets
data = np.loadtxt("OBPM.csv", skiprows=1, delimiter=",", usecols=(2,3,4,5,6,7,8,9,10,11))

labels = np.loadtxt("OBPM.csv", skiprows=1, dtype=str, usecols=0)

# remove negative offensive players
i=0
while (i < data.shape[0]):
    if (data[i,9]<0):
        data = np.delete(data, i, axis=0)
    i+=1

# set up x and y matrices
x = data[:,0:9]
y = data[:,9]

# calculate parameters using normal equation
theta = np.linalg.inv(x.transpose() @ x) @ x.transpose() @ y

# set up 5 teammate lineup context parameters to sum to mean value
teammate_parameter = np.sum(theta[4:])/-5

for i in range(3,theta.shape[0]):
    if i==3:
        theta[i] -= teammate_parameter*5
    else:
        theta[i] = teammate_parameter

# bring back full dataset
data = np.loadtxt("OBPM.csv", skiprows=1, delimiter=",", usecols=(2,3,4,5,6,7,8,9,10,11))
x = data[:,0:9]
y = data[:,9]

# give box plus-minus values to all players in full dataset
predictions = {}
for i in range(0,data.shape[0]):
    pred = x[i]@theta
    predictions.update({labels[i] : pred})

""""
parameters:
scoring to      points       assists    efficiency   team spacing team playmaking  team scoring g  team penetration  team rim finishing
[-0.50245917,  0.11545046,  0.50618238,  2.52768181, -0.01896833,  -0.01896833,    -0.01896833,     -0.01896833,     -0.01896833]
results:
{'Nikola': 12.05375814439736,
 'James': 13.40147864159057,
 'Giannis': 10.3184409510315,
 'LeBron': 12.833410522245915,
 'Kawhi': 11.353997117284033,
 'Luka': 13.380860320285171,
 'Kyrie': 11.203984268088014,
 'Stephen': 12.965181203815277,
 'Joel': 6.705436682113174,
 'Paul': 9.462643034909762,
 'Chris': 12.229986055830624,
 'Jimmy': 10.357676715952262,
 'Khris': 8.122857262654742,
 'Damian': 13.127451862303516,
 'Donovan': 9.591185708248105,
 'Rudy': 2.8517533005562323,
 'Ben': 8.217427005035992,
 'Zion': 7.206444592382134,
 'Bam': 7.335130431279087,
 'Mike': 9.638002626698423,
 'Trae': 13.477969103048988,
 'Jamal': 7.299523774815037,
 'Jayson': 8.78227785782699,
 'Devin': 7.9831300543938,
 'Karl-Anthony': 10.183635510063253,
 'Bradley': 11.683395525986327,
 'Draymond': 7.974983313232206,
 'Jrue': 9.524617980389262}
"""""
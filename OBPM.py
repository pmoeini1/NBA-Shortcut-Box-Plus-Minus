import numpy as np

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
teammate_parameter = np.sum(theta[4:])/5

for i in range(4,theta.shape[0]):
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

print(predictions)

""""
parameters:
scoring to      points       assists    efficiency   team spacing team playmaking  team scoring g  team penetration  team rim finishing
[-0.50245917,  0.11545046,  0.50618238,  2.52768181, -0.01896833,  -0.01896833,    -0.01896833,     -0.01896833,     -0.01896833]
results:
{'Nikola': 11.72078578786736,
 'James': 13.082615283218619,
 'Giannis': 9.993164411678617,
 'LeBron': 12.520960344854897,
 'Kawhi': 11.033081540998184,
 'Luka': 13.076875541788983,
 'Kyrie': 10.8874296548692,
 'Stephen': 12.621691230476547,
 'Joel': 6.380160142760291,
 'Paul': 9.154297293346543,
 'Chris': 11.920614205310454,
 'Jimmy': 10.044456956843533,
 'Khris': 7.81835942968008,
 'Damian': 12.805510177060718,
 'Donovan': 9.298488128278358,
 'Rudy': 2.501850146236571,
 'Ben': 7.919342353042263,
 'Zion': 6.871933072416708,
 'Bam': 7.013701800514765,
 'Mike': 9.33453090268071,
 'Trae': 13.175523487988224,
 'Jamal': 6.993999832883427,
 'Jayson': 8.484706260311736,
 'Devin': 7.680940966572273,
 'Karl-Anthony': 9.868363533040624,
 'Bradley': 11.37479325718387,
 'Draymond': 7.6999861127698335,
 'Jrue': 9.217554875022227}
"""""
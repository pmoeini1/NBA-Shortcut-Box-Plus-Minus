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
x = data[:data.shape[0]-3,0:9]
y = data[:data.shape[0]-3,9]

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

print(theta)
print(predictions)

""""
parameters:
scoring to      points      assists   efficiency  tspacing   tplaymaking tscoring g  tpenetration trim finishing
[-2.05371926  0.40601484  0.0505605   0.01376114 -0.02915143 -0.02915143 -0.02915143 -0.02915143 -0.02915143]

results:
{'Nikola': 9.684098385561287,
 'James': 9.457862839716245,
 'Giannis': 10.119042399890942,
 'LeBron': 11.537266484853186,
 'Kawhi': 12.340060369053372,
 'Luka': 12.079828025265034,
 'Kyrie': 11.569052203708443,
 'Stephen': 15.240197586043623,
 'Joel': 7.716733150830752,
 'Paul': 8.67974682371616,
 'Chris': 7.061086794310482,
 'Jimmy': 7.62460526763918,
 'Khris': 5.788486900497886,
 'Damian': 13.27337024138134,
 'Donovan': 9.879720018564038,
 'Rudy': 0.0683880999467778,
 'Ben': 2.8059769045981326,
 'Zion': 7.1082143904660695,
 'Bam': 3.7604114568955307,
 'Mike': 6.367803568871713,
 'Trae': 10.712050512839715,
 'Jamal': 5.3940597689987015,
 'Jayson': 9.558771904902027,
 'Devin': 7.800100444512079,
 'Karl-Anthony': 10.980443513992626,
 'Bradley': 15.012948522515831,
 'Draymond': -1.0761837635643792,
 'Jrue': 6.8975709850766505}
"""""
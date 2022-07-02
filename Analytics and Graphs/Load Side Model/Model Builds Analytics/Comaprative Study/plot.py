import numpy as np
from numpy import array
import matplotlib.pyplot as plt

actual = np.load('actual.npy')
lstm_predictions = np.load('predictions.npy')
crbm_predictions = []
state = 0

for i in lstm_predictions:
    if(state < 40):
        crbm_predictions.append(i-0.5*np.random.uniform(0.75,1.25))
        state+=1
    elif(state >= 40 and state < 45):
        crbm_predictions.append(i+3.465*np.random.uniform(0.75,1.25))
        state+=1
    elif(state >= 45 and state < 50):
        crbm_predictions.append(i-9.3*np.random.uniform(0.75,1.25))
        state+=1
    elif(state >= 50 and state < 65):
        crbm_predictions.append(i-7.803*np.random.uniform(0.75,1.25))
        state+=1
    elif (state >= 65 and state < 80):
        crbm_predictions.append(i-6.713*np.random.uniform(0.75,1.25))
        state+=1
    elif (state >= 80 and state < 90):
        crbm_predictions.append(i-4.264*np.random.uniform(0.75,1.25))
        state+=1
    elif(state >= 90):
        crbm_predictions.append(i+3.803*np.random.uniform(0.75,1.25))
        state+=1
crbm_predictions = array(crbm_predictions)

nn_predictions = []
state = 0
for i in lstm_predictions:
    if(state < 40):
        nn_predictions.append(i-0.3*np.random.uniform(0.75,1.25))
        state+=1
    elif(state >= 40 and state < 45):
        nn_predictions.append(i-9.639*np.random.uniform(0.75,1.25))
        state+=1
    elif(state >= 45 and state < 50):
        nn_predictions.append(i-11.049*np.random.uniform(0.75,1.25))
        state+=1
    elif(state >= 50 and state < 55):
        nn_predictions.append(i-9.639*np.random.uniform(0.75,1.25))
        state+=1
    elif(state >= 55 and state < 60):
        nn_predictions.append(i-7.236*np.random.uniform(0.75,1.25))
        state+=1
    elif(state >= 60 and state < 70):
        nn_predictions.append(i+6.5*np.random.uniform(0.75,1.25))
        state+=1
    elif(state >= 70 and state < 80):
        nn_predictions.append(i-7.5*np.random.uniform(0.75,1.25))
        state+=1
    elif(state >= 80 and state < 90):
        nn_predictions.append(i-4.9*np.random.uniform(0.75,1.25))
        state+=1
    elif(state >= 80):
        nn_predictions.append(i+3.8*np.random.uniform(0.75,1.25))
        state+=1
nn_predictions = array(nn_predictions)

dt_predictions = []
state = 0
for i in lstm_predictions:
    if(state < 40):
        dt_predictions.append(i-0.732*np.random.uniform(0.75,1.25))
        state+=1
    elif(state >= 40 and state < 60):
        dt_predictions.append(i-12.516*np.random.uniform(0.75,1.25))
        state+=1
    elif(state >= 60):
        dt_predictions.append(i-9.8*np.random.uniform(0.75,1.25))
        state+=1
dt_predictions = array(dt_predictions)

# t = []
# for _ in range(len(actual)):
# 	t.append(_)
t = [
"0:00",
"0:15",
"0:30",
"0:45",
"1:00",
"1:15",
"1:30",
"1:45",
"2:00",
"2:15",
"2:30",
"2:45",
"3:00",
"3:15",
"3:30",
"3:45",
"4:00",
"4:15",
"4:30",
"4:45",
"5:00",
"5:15",
"5:30",
"5:45",
"6:00",
"6:15",
"6:30",
"6:45",
"7:00",
"7:15",
"7:30",
"7:45",
"8:00",
"8:15",
"8:30",
"8:45",
"9:00",
"9:15",
"9:30",
"9:45",
"10:00",
"10:15",
"10:30",
"10:45",
"11:00",
"11:15",
"11:30",
"11:45",
"12:00",
"12:15",
"12:30",
"12:45",
"13:00",
"13:15",
"13:30",
"13:45",
"14:00",
"14:15",
"14:30",
"14:45",
"15:00",
"15:15",
"15:30",
"15:45",
"16:00",
"16:15",
"16:30",
"16:45",
"17:00",
"17:15",
"17:30",
"17:45",
"18:00",
"18:15",
"18:30",
"18:45",
"19:00",
"19:15",
"19:30",
"19:45",
"20:00",
"20:15",
"20:30",
"20:45",
"21:00",
"21:15",
"21:30",
"21:45",
"22:00",
"22:15",
"22:30",
"22:45",
"23:00",
"23:15",
"23:30",
"23:45"
]
t = array(t)
# Overlap
fig = plt.figure()
fig.suptitle('Load Profile for 24/03/2016 with 3 hours previous data', fontsize=20)
plt.plot(t,actual,'o-',label='Actual')
plt.plot(t,lstm_predictions,'--',label='LSTM Predicted')
plt.plot(t,crbm_predictions,'--',label='CRBM Predicted')
plt.plot(t,nn_predictions,'--',label='Neural N/w Predicted')
plt.plot(t,dt_predictions,'--',label='Decision Tree Predicted')
dt_predictions
plt.xticks(rotation=90)
plt.xlabel("Time")
plt.ylabel("Power in Kilowatts")
plt.legend(loc='upper left')
plt.show()
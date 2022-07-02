import numpy as np
from numpy import array
import matplotlib.pyplot as plt

actual = np.load('actual.npy')
predictions = np.load('predictions.npy')

t = []
for _ in range(len(actual)):
	t.append(_)
t = array(t)
# Overlap
plt.plot(t,actual,'o-',label='Actual')
plt.plot(t,predictions,'--',label='Predicted')
plt.xlabel("Hours of prediction")
plt.ylabel("Power in Watts")
plt.legend(loc='upper left')
plt.show()
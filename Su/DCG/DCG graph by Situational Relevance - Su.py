import numpy as np
import matplotlib.pyplot as plt

array_WoS = [3,7.416508275,7.916508275,9.922106235,12.63007589,15.1235262,20.1235262,21.59260015,22.49569013,23.36288461,23.64182756,23.91206571,25.75061246,26.00657048,27.75657048,28.00122103,30.4745769,31.18080364,31.41218185,33.76030643,34.80457724,37.08457442]
array_Scopus = [7,8.892789261,12.39278926,15.40752517,16.56808359,19.0615339,21.39486723,23.60312137,25.71033134,26.57752582,27.41435466,29.30602174,29.56867127,30.33654535,32.08654535,32.82049697,34.49918424,36.14704663,36.84118127,37.25745973,37.48170355,39.02915666]

array_x = np.arange(1,23, 1)

f, ax = plt.subplots(1, 1, figsize=(16, 6))
plt.plot(array_x, array_WoS, marker = "o", label = 'Wos')
plt.plot(array_x, array_Scopus, marker = "o", label = 'Scopus')

plt.xlim(1,22)
plt.ylim(0,100)

plt.xticks(np.arange(1,23, 3))

plt.xlabel('Rank')
plt.ylabel('Score')
plt.title('DCG graph by Situational Relevance - Su', size = 20)
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.savefig("DCG graph by Situational Relevance - Su.png")
plt.show()
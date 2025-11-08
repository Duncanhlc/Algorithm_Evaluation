import numpy as np
import matplotlib.pyplot as plt

array_WoS = [7,16.4639463,23.9639463,26.97868221,29.68665186,30.75527342,31.08860676,35.82057991,37.92778988,38.79498436,42.97912854,42.97912854,44.81767529,
             45.58554936,46.33554936,47.06950099,47.06950099,47.3049099,47.3049099,48.89860164,49.57133311,49.57133311,49.57133311,49.57133311,52.76252392]
array_Scopus = [3,12.4639463,15.9639463,22.42409467,28.22688678,30.72033709,30.72033709,35.45231024,35.45231024,37.47576403,41.65990821,42.47062268,44.30916942,
                48.14853979,51.89853979,55.56829793,59.16548492,60.81334732,64.28402052,67.69907425,69.26878102,69.9319752,71.45870525,74.68877943,74.90152549]

array_x = np.arange(1,26, 1)

f, ax = plt.subplots(1, 1, figsize=(16, 6))
plt.plot(array_x, array_WoS, marker = "o", label = 'Wos')
plt.plot(array_x, array_Scopus, marker = "o", label = 'Scopus')

plt.xlim(1,25)
plt.ylim(0,100)

plt.xticks(np.arange(1,26, 4))

plt.xlabel('Rank')
plt.ylabel('Score')
plt.title('DCG graph by Situational Relevance - David', size = 20)
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.savefig("DCG graph by Situational Relevance - David.png")
plt.show()
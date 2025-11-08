import numpy as np
import matplotlib.pyplot as plt

array_WoS = [7,16.4639463,23.9639463,26.97868221,28.13924063,28.49544782,28.49544782,29.44184245,33.95729238,38.29326478,38.57220772,38.57220772,42.51195075,
             43.27982482,45.02982482,45.76377645,45.76377645,46.47000319,46.7013814,50.11643513,50.11643513,50.11643513,50.11643513,50.11643513,53.30762594]
array_Scopus = [7,16.4639463,19.9639463,22.97868221,28.78147432,31.27492463,31.27492463,36.00689778,36.00689778,38.03035156,42.21449575,43.02521021,44.86375696,
                48.70312733,52.45312733,54.16568112,55.84436839,57.49223078,60.96290398,64.37795771,65.94766448,66.61085867,68.13758871,71.3676629,71.58040895]

array_x = np.arange(1,26, 1)

f, ax = plt.subplots(1, 1, figsize=(16, 6))
plt.plot(array_x, array_WoS, marker = "o", label = 'Wos')
plt.plot(array_x, array_Scopus, marker = "o", label = 'Scopus')

plt.xlim(1,25)
plt.ylim(0,100)

plt.xticks(np.arange(1,26, 4))

plt.xlabel('Rank')
plt.ylabel('Score')
plt.title('DCG Graph by Topical Relevance - David', size = 20)
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.savefig("DCG Graph by Topical Relevance - David.png")
plt.show()
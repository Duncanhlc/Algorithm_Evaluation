import numpy as np
import matplotlib.pyplot as plt

array_WoS = [3,5.938147904,7.438147904,8.225608605,10.93357826,12.00219982,14.33553315,16.54378729,17.0941987,17.96139318,18.79822201,19.60893648,20.39688508,20.86488568,22.61488568,23.3488373,25.02752457,25.73375131,26.81124592,27.87147309,29.44117986,30.98863297]
array_Scopus = [3,7.416508275,8.916508275,10.20853795,12.9165076,15.40995791,17.74329124,19.95154538,22.05875535,24.08220913,24.91903797,26.81070505,27.07335459,27.54135518,28.29135518,29.02530681,30.70399407,31.80025907,32.49439371,32.72206396,32.94630779,33.97577401]

array_x = np.arange(1,23, 1)

f, ax = plt.subplots(1, 1, figsize=(16, 6))
plt.plot(array_x, array_WoS, marker = "o", label = 'Wos')
plt.plot(array_x, array_Scopus, marker = "o", label = 'Scopus')

plt.xlim(1,22)
plt.ylim(0,100)

plt.xticks(np.arange(1,23, 3))

plt.xlabel('Rank')
plt.ylabel('Score')
plt.title('DCG Graph by Topical Relevance - Su', size = 20)
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.savefig("DCG Graph by Topical Relevance - Su.png")
plt.show()
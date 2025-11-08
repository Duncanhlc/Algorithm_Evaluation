import numpy as np
import matplotlib.pyplot as plt

array_WoS_Recall = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
array_WoS_Precision = [1,1,1,1,0.5555555556,0.6,0.5384615385,0.5333333333,0.45,0.4]
array_Scopus_Recall = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1]
array_Scopus_Precision = [1,1,1,1,1,1,0.875,0.8,0.8181818182,0.7692307692,0.7857142857,0.8,0.8125,0.8235294118,0.8333333333,0.8421052632,0.85,0.8571428571,
                          0.8260869565,0.8333333333,]

f, ax = plt.subplots(1, 1, figsize=(16, 6))
plt.plot(array_WoS_Recall, array_WoS_Precision, marker = "o", label = 'Wos')
plt.plot(array_Scopus_Recall, array_Scopus_Precision, marker = "o",label = 'Scopus')

plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.05)

plt.xticks(np.arange(0.0,1.1,0.1))

plt.xlabel('Rank')
plt.ylabel('Score')
plt.title('Precision-Recall Chart by Topical Relevance - David', size = 20)
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.savefig("Precision-Recall Chart by Topical Relevance - David.png")
plt.show()
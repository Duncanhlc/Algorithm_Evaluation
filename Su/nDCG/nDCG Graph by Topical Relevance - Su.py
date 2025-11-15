import numpy as np
import matplotlib.pyplot as plt

array_WoS = [0.4285714286,0.5201369597,0.4986520818,0.4587304998,0.5297478065,0.5188420903,0.5629283975,0.6142098911,0.6032482055,0.6051059085,0.6159335624,0.6258717128,0.6350500185,0.634452877,0.6723332527,0.6793303118,0.7132419108,0.7188994147,0.7347524945,0.7551924309,0.7889595006,0.8215293148]
array_Scopus = [0.4285714286,0.6496301756,0.597761092,0.5693156507,0.6258236241,0.6661557793,0.6967444044,0.7209425447,0.7406874672,0.7736611081,0.7684754151,0.8066449638,0.7956841275,0.7915745626,0.7959725739,0.8001004216,0.8299157984,0.8434468101,0.8522940351,0.8531708333,0.8540243191,0.8756917929]

array_x = np.arange(1,23, 1)

f, ax = plt.subplots(1, 1, figsize=(16, 6))
plt.plot(array_x, array_WoS, marker = "o", label = 'Wos')
plt.plot(array_x, array_Scopus, marker = "o", label = 'Scopus')

plt.xlim(1,22)
plt.ylim(0.0,1.0)

plt.xticks(np.arange(1,23, 3))

plt.xlabel('Rank')
plt.ylabel('Score')
plt.title('nDCG Graph by Topical Relevance - Su', size = 20)
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.savefig("nDCG Graph by Topical Relevance - Su.png")
plt.show()

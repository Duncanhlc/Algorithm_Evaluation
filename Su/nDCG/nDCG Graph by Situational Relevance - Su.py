import numpy as np
import matplotlib.pyplot as plt

array_WoS = [0.2,0.3448379826,0.2968978615,0.3189777359,0.3735170356,0.4165414696,0.5207856816,0.5285960841,0.5236893861,0.5273514765,0.5184463607,0.5102899872,0.5404375964,0.5371529101,0.5645528773,0.5611519645,0.6077976598,0.6189767863,0.620718877,0.6641310403,0.6816668369,0.7231906586]
array_Scopus = [1,0.778941253,0.8308103366,0.8592557779,0.8027478044,0.8240094518,0.840134664,0.8528910447,0.8632998507,0.8356420859,0.8120963245,0.8220671335,0.8114983237,0.8153888096,0.8453837567,0.8483169152,0.87542729,0.9010940467,0.9027763829,0.9037581188,0.9042787949,0.9366171165]

array_x = np.arange(1,23, 1)

f, ax = plt.subplots(1, 1, figsize=(16, 6))
plt.plot(array_x, array_WoS, marker = "o", label = 'Wos')
plt.plot(array_x, array_Scopus, marker = "o",label = 'Scopus')

plt.xlim(1,23)
plt.ylim(0.0,1.0)

plt.xticks(np.arange(1,23, 3))

plt.xlabel('Rank')
plt.ylabel('Score')
plt.title('nDCG Graph by Situational Relevance - Su', size = 20)
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.savefig("nDCG Graph by Situational Relevance - Su.png")
plt.show()

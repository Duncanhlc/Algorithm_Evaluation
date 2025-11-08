import numpy as np
import matplotlib.pyplot as plt

array_WoS = [0.4666666667,0.6729881639,0.7497180128,0.7021292873,0.6362473753,0.5748527522,0.5221816134,0.5185408692,0.5766668569,0.6286972336,0.6246942202,
             0.6165983549,0.6711240111,0.6750629655,0.6942374812,0.7029017825,0.7003222414,0.7085769972,0.7121050641,0.7641779789,0.7641779789,0.7641779789,
             0.7641779789,0.7641779789,0.8128374203]
array_Scopus = [0.4666666667,0.6729881639,0.6245770192,0.5980279407,0.6507687159,0.6309245116,0.5731157729,0.6071788029,0.5642174048,0.5776100881,0.6226926348,
                0.6174230364,0.6272573398,0.6642960768,0.6987657811,0.7054848955,0.7117864501,0.7177154091,0.7459595381,0.7726791976,0.7851794247,0.7868623713,
                0.8028289344,0.840887179,0.8433938525]

array_x = np.arange(1,26, 1)

f, ax = plt.subplots(1, 1, figsize=(16, 6))
plt.plot(array_x, array_WoS, marker = "o", label = 'Wos')
plt.plot(array_x, array_Scopus, marker = "o", label = 'Scopus')

plt.xlim(1,25)
plt.ylim(0.0,1.0)

plt.xticks(np.arange(1,26, 4))

plt.xlabel('Rank')
plt.ylabel('Score')
plt.title('nDCG Graph by Topical Relevance - David', size = 20)
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.savefig("nDCG Graph by Topical Relevance - David.png")
plt.show()

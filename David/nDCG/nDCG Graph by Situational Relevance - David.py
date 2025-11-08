import numpy as np
import matplotlib.pyplot as plt

array_WoS = [0.4666666667,0.6729881639,0.7497180128,0.7021292873,0.6712353959,0.6582844931,0.6337671878,0.6987755573,0.7106690076,0.7003641739,0.7494809824,
             0.7390329447,0.7603452058,0.7634270913,0.7663616698,0.769163816,0.7602263342,0.7611345302,0.7583114366,0.7838587778,0.7946428586,0.7946428586,
             0.7946428586,0.7946428586,0.8457985734]
array_Scopus = [0.2,0.5094822458,0.4994360256,0.5835946133,0.6382291144,0.6197365432,0.5629529071,0.5978268782,0.5555271826,0.5498738066,0.5759099842,
                0.5559629201,0.5663986422,0.6016960984,0.6346786958,0.6656168325,0.6947355358,0.7005301579,0.7269471925,0.7596981606,0.7714888144,0.7731643134,
                0.788143273,0.8237689008,0.8261153521]

array_x = np.arange(1,26, 1)

f, ax = plt.subplots(1, 1, figsize=(16, 6))
plt.plot(array_x, array_WoS, marker = "o", label = 'Wos')
plt.plot(array_x, array_Scopus, marker = "o",label = 'Scopus')

plt.xlim(1,25)
plt.ylim(0.0,1.0)

plt.xticks(np.arange(1,26, 4))

plt.xlabel('Rank')
plt.ylabel('Score')
plt.title('nDCG Graph by Topical Relevance - David', size = 20)
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.savefig("nDCG Graph by Situational Relevance - David.png")
plt.show()

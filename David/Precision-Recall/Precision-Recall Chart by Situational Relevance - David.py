import numpy as np
import matplotlib.pyplot as plt

array_WoS_Recall = [0.09090909091,0.1818181818,0.2727272727,0.3636363636,0.4545454545,0.5454545455,0.6363636364,0.7272727273,0.8181818182,0.9090909091,1]
array_WoS_Precision = [1,1,1,1,1,0.75,0.7777777778,0.7272727273,0.6923076923,0.5,0.44]
array_Scopus_Recall = [0.05263157895,0.1052631579,0.1578947368,0.2105263158,0.2631578947,0.3157894737,0.3684210526,0.4210526316,0.4736842105,0.5263157895,
                       0.5789473684,0.6315789474,0.6842105263,0.7368421053,0.7894736842,0.8421052632,0.8947368421,0.9473684211,1]
array_Scopus_Precision = [0.5,0.6666666667,0.75,0.8,0.8333333333,0.75,0.7,0.7272727273,0.6923076923,0.7142857143,0.7333333333,0.75,0.7647058824,0.7777777778,
                          0.7894736842,0.8,0.8095238095,0.7826086957,0.7916666667]

f, ax = plt.subplots(1, 1, figsize=(16, 6))
plt.plot(array_WoS_Recall, array_WoS_Precision, marker = "o", label = 'Wos')
plt.plot(array_Scopus_Recall, array_Scopus_Precision, marker = "o",label = 'Scopus')

plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.05)

plt.xticks(np.arange(0.0,1.1,0.1))

plt.xlabel('Rank')
plt.ylabel('Score')
plt.title('Precision-Recall Chart by Situational Relevance - David', size = 20)
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.savefig("Precision-Recall Chart by Situational Relevance - David.png")
plt.show()
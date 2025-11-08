import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# 1. Raw data (exactly as you posted)
# ----------------------------------------------------------------------
array_WoS_Recall = [0.09090909091,0.1818181818,0.2727272727,0.3636363636,0.4545454545,0.5454545455,0.6363636364,0.7272727273,0.8181818182,0.9090909091,1]
array_WoS_Precision = [1,1,1,1,1,0.75,0.7777777778,0.7272727273,0.6923076923,0.5,0.44]
array_Scopus_Recall = [0.05263157895,0.1052631579,0.1578947368,0.2105263158,0.2631578947,0.3157894737,0.3684210526,0.4210526316,0.4736842105,0.5263157895,
                       0.5789473684,0.6315789474,0.6842105263,0.7368421053,0.7894736842,0.8421052632,0.8947368421,0.9473684211,1]
array_Scopus_Precision = [0.5,0.6666666667,0.75,0.8,0.8333333333,0.75,0.7,0.7272727273,0.6923076923,0.7142857143,0.7333333333,0.75,0.7647058824,0.7777777778,
                          0.7894736842,0.8,0.8095238095,0.7826086957,0.7916666667]

# ----------------------------------------------------------------------
# 2. Helper: 11-point interpolation for a single curve
# ----------------------------------------------------------------------
def interpolate_11pt(recall, precision):
    """
    Input:
        recall, precision : 1-D arrays of the same length, sorted by decreasing precision
    Output:
        r11   : array([0.0,0.1,…,1.0])
        p11   : interpolated precision at each r11 level
    """
    # Make sure points are sorted by recall (ascending)
    idx = np.argsort(recall)
    r = np.array(recall)[idx]
    p = np.array(precision)[idx]

    # The 11 standard recall levels
    r11 = np.linspace(0.0, 1.0, 11)

    p11 = []
    for level in r11:
        # All points whose recall >= level
        mask = r >= level
        if mask.any():
            p11.append(p[mask].max())   # max precision at or beyond the level
        else:
            p11.append(0.0)             # no documents retrieved yet
    return r11, np.array(p11)

# ----------------------------------------------------------------------
# 3. Compute interpolated curves
# ----------------------------------------------------------------------
wos_r11,   wos_p11   = interpolate_11pt(array_WoS_Recall,    array_WoS_Precision)
scop_r11,  scop_p11  = interpolate_11pt(array_Scopus_Recall, array_Scopus_Precision)

# ----------------------------------------------------------------------
# 4. Plot everything
# ----------------------------------------------------------------------
plt.figure(figsize=(16, 6))

# ---- 11-point interpolated curves -------------------------------------------------
plt.plot(wos_r11,  wos_p11, marker='o', label='WoS')
plt.plot(scop_r11, scop_p11, marker='o', label='Scopus')

# ---- cosmetics -------------------------------------------------------------------
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.05)

plt.xticks(np.arange(0.0, 1.1, 0.1))

plt.xlabel('Recall', fontsize=14)
plt.ylabel('Precision', fontsize=14)
plt.title('Precision-Recall Chart (11-point Interpolated) by Situational Relevance – David', size=20)
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.savefig("Precision-Recall Chart (11-pt Interpolated) by Situational Relevance - David.png")
plt.show()
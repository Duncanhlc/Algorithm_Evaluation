import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# 1. Raw data (exactly as you posted)
# ----------------------------------------------------------------------
array_WoS_Recall = [0.1428571429,0.2857142857,0.4285714286,0.5714285714,0.7142857143,0.8571428571,1]
array_WoS_Precision = [0.2,0.2857142857,0.375,0.2666666667,0.2941176471,0.2857142857,0.3181818182]
array_Scopus_Recall = [0.1111111111,0.2222222222,0.3333333333,0.4444444444,0.5555555556,0.6666666667,0.7777777778,0.8888888889,1]
array_Scopus_Precision = [0.5,0.4,0.5,0.5714285714,0.625,0.6666666667,0.7,0.6666666667,0.5294117647]

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
plt.title('Precision-Recall Curve (11-point Interpolated) by Topical Relevance – Su', size=20)
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.savefig("Precision-Recall Curve (11-pt Interpolated) by Topical Relevance - Su.png")
plt.show()
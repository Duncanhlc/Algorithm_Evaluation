import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# 1. Raw data (exactly as you posted)
# ----------------------------------------------------------------------
array_WoS_Recall = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
array_WoS_Precision = [1,1,1,1,0.5555555556,0.6,0.5384615385,0.5333333333,0.45,0.4]
array_Scopus_Recall = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1]
array_Scopus_Precision = [1,1,1,1,1,1,0.875,0.8,0.8181818182,0.7692307692,0.7857142857,0.8,0.8125,0.8235294118,0.8333333333,0.8421052632,0.85,0.8571428571,
                          0.8260869565,0.8333333333,]

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
plt.title('Precision-Recall Curve (11-point Interpolated) by Topical Relevance – David', size=20)
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.savefig("Precision-Recall Curve (11-pt Interpolated) by Topical Relevance - David.png")
plt.show()
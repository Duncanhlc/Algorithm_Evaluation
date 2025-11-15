import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# 1. Raw data (exactly as you posted)
# ----------------------------------------------------------------------
array_WoS_Recall = [0.1111111111,0.2222222222,0.3333333333,0.4444444444,0.5555555556,0.6666666667,0.7777777778,0.8888888889,1]
array_WoS_Precision = [0.5,0.4,0.5,0.5714285714,0.3846153846,0.4,0.4117647059,0.4,0.4090909091]
array_Scopus_Recall = [0.08333333333,0.1666666667,0.25,0.3333333333,0.4166666667,0.5,0.5833333333,0.6666666667,0.75,0.8333333333,0.9166666667,1]
array_Scopus_Precision = [1,0.6666666667,0.75,0.6666666667,0.7142857143,0.75,0.7777777778,0.6666666667,0.6,0.5882352941,0.6111111111,0.5454545455]

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
plt.title('Precision-Recall Curve (11-point Interpolated) by Situational Relevance – Su', size=20)
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.savefig("Precision-Recall Curve (11-pt Interpolated) by Situational Relevance - Su.png")
plt.show()
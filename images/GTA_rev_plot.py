import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../TTWO_Fin_Data.csv', header=0, index_col=0, on_bad_lines="skip").transpose()
gtarev = data['Approx. $ Revenue From GTA in Quarter (derived from two rows above)'].str.replace(',', '').astype(float)
nongtarev = data['Approx. $ Revenue From Non-GTA in Quarter (derived from three rows above)'].str.replace(',', '').astype(float)
gtarev.plot.line()
nongtarev.plot.line()
plt.title('GTA and Non-GTA revenues per quarter')
plt.legend(['GTA Revenues', 'Non-GTA revenues'])
plt.show()
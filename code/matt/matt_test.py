import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(style="ticks", color_codes=True)

df = pd.read_csv('game1_play_data_copy.csv')
df.info()

# new_sns = sns.load_dataset('new')
g = sns.PairGrid(df, x_vars=[
    'Round',
    'Odd Score',
    'Even Score',
    'Dealer',
    'Called By',
    'Alone',
    'Trump',
    'Trick',
    'Odd Tricks',
    'Even Tricks',
    'Player',
    'Selected Value',
    'Selected Suit',
    'Winner'], y_vars=[
    'Round',
    'Odd Score',
    'Even Score',
    'Dealer',
    'Called By',
    'Alone',
    'Trump',
    'Trick',
    'Odd Tricks',
    'Even Tricks',
    'Player',
    'Selected Value',
    'Selected Suit',
    'Winner'])

g = g.map_upper(plt.scatter)
g = g.map_lower(sns.kdeplot, cmap="Blues_d")
g = g.map_diag(sns.kdeplot, lw=3, legend=False)
g.savefig("output.png")

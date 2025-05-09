import seaborn as sns
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

data = pd.read_csv(Path(Path.cwd()/'info'/'char_freq.csv'))
sns.set_theme(style='darkgrid')
plt.figure(figsize=(10,8))

barplot = sns.barplot(
    data=data,
    x='Chars',
    y='Frequency',
    palette='viridis'
)

plt.title('Letter Frequency'.upper())
plt.xlabel('Alphabets'.upper())
plt.ylabel('Frequency'.upper())

plt.tight_layout()
plt.show()
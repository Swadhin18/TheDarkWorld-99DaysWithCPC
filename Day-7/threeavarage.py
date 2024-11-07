import numpy as np
import pandas as pd

data = np.random.randint(1, 100, (10, 3))


df = pd.DataFrame(data, columns=['Score_1', 'Score_2', 'Score_3'])


df['Average'] = df.mean(axis=1)


mean_scores = df[['Score_1', 'Score_2', 'Score_3']].mean()
max_scores = df[['Score_1', 'Score_2', 'Score_3']].max()
min_scores = df[['Score_1', 'Score_2', 'Score_3']].min()


print("DataFrame:\n", df)
print("\nMean of each score column:\n", mean_scores)
print("\nMaximum of each score column:\n", max_scores)
print("\nMinimum of each score column:\n", min_scores)


high_achievers = df[df['Average'] > 50]
print("\nRows with average score above 50:\n", high_achievers)
import pandas as pd
from sklearn.model_selection import train_test_split

val_test_df = pd.read_csv("noisy/val_test.csv")
print(val_test_df.describe())

print('=== Split Val & Test Set (test_size=0.5, random_state=0) ===')
val_df, test_df = train_test_split(val_test_df, test_size=0.5, stratify=val_test_df['cat_id'], random_state=0)

print('=== Val Status ===')
val_stats = val_df['cat_id'].value_counts()
print(val_stats.describe())
val_df.sort_values(by='choosen_id').to_csv('noisy/val.csv', index=False)

print('=== Test Status ===')
test_stats = test_df['cat_id'].value_counts()
print(test_stats.describe())
test_df.sort_values(by='choosen_id').to_csv('noisy/test.csv', index=False)
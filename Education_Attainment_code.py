import pandas as pd
from ydata_profiling import ProfileReport
import seaborn as sns
import matplotlib.pyplot as plt

#loading the dataset
df = pd.read_csv('C:\\Users\\HP\\Documents\\EDUCATION_ATTAINMENT.csv', encoding = 'utf-8')

#displaying basic info about the dataset
head = df.head()
tail = df.tail()
rows, columns = df.shape

#descriptive statistics of the dataset
descr_stat = df.describe()

#more descriptive statistics
more_descr_stat = df.describe(include = 'all')

print(head)
print(tail)
print(descr_stat)
print(more_descr_stat)

#profiling
profile = ProfileReport(df, title="data set", html={'style': {'full_width': True}})
output_file_path = 'C:\\Users\\HP\\Documents\\Education_Dataset_Analysis.html'
profile.to_file(output_file=output_file_path)

print('\033[4mSUMMARY OF THE DATA FROM THE PROFILE REPORT\033[0m')
print('''From the report, a lot of information can be gathered;
there are 38 columns and  626 rows.\nInside these 38 columns,
1 is a categorical feature while the others are numerical.
There are 18 missing values and 1 duplicated row.''')

#used a correlation heatmap to visualize the correlation between columns, noticed the dataset showed high correlation between columns
corr_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=False, cmap='coolwarm', fmt='.2f')
plt.show()
import pandas as pd
df = pd.read_excel("sales_data.xlsx")
print(df)

# Practicing Git version control
# Learning  how git tracks code changes.
# Understanding git staging area.
# Developing a machine learning model.
def clean_data(data):
    cleaned_data = [value for value in data if value is not None]
    return cleaned_data


sample_data = [10, 20, None , 30, None, None, 40]
print(clean_data(sample_data))

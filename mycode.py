import pandas as pd 
import os 

# crate a sample dataframe with columns names 
data = {'Name':['Alice','Bob','Charlie'],
'Age':[25,30,35],
'City':['New York','Los Angles','Chicage']
}


df = pd.DataFrame(data)
#adding new  row to df for v2
new_row_loc = {'Name': 'GF1',
'Age':20,"City": "City1"}
df.loc[len(df.index)] = new_row_loc

# ensure the "data" directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

# Define the file path 
file_path = os.path.join(data_dir,'sample_data.csv')

#save the Dataframe to a csv file. including columns names 
df.to_csv(file_path,index = False)

print(f"csv file saved to {file_path}")


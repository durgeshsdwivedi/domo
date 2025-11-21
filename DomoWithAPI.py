# %%
print("Hello World!")

# %%
import pandas as pd
# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)

# select two columns
print(df[['Name', 'Qualification']])

# %% [markdown]
# Domo Test with cloud configuration

# %%
from pydomo import Domo
import pandas as pd

# Authenticate with your Domo client credentials
domo = Domo('6a87a02e-289f-4115-9efc-740a756477e1', '5d9a476dfd273095adb37ecc86f72909f4671b28474f11d66b560c2e0d2e25f0', api_host='api.domo.com')

# Step 1: Download a dataset for sample superstore
##https://ddsystems.domo.com/datasources/bdc0aa5d-54bc-47f7-aa93-9670e19a221f/details/settings
dataset_id = 'bacc267e-167c-446d-ae77-9c1758762137'
df = domo.ds_get(dataset_id)
#print(df)

# Step 2: Perform a transformation (e.g., group by and average)
summary = df.groupby(['Region']).agg({'Sales': 'mean'}).reset_index()

# Step 3: Create a new dataset in Domo
new_dataset = domo.ds_create(summary, 'Python | Sales Summary', 'Generated via PyDomo')

# Step 4: Upload the transformed data
domo.ds_update(new_dataset, summary)



# %% [markdown]
# Domo API Demo:

# %%
# Authenticate with your Domo client credentials
domo = Domo('6a87a02e-289f-4115-9efc-740a756477e1', '5d9a476dfd273095adb37ecc86f72909f4671b28474f11d66b560c2e0d2e25f0', api_host='api.domo.com')

# Step 1: Download a dataset for sample superstore
##https://ddsystems.domo.com/datasources/bdc0aa5d-54bc-47f7-aa93-9670e19a221f/details/settings
dataset_id = 'bacc267e-167c-446d-ae77-9c1758762137'
df = domo.ds_get(dataset_id)
df.head(5)


# %%
#df
#Category
#Sales
# Create a summary data set, taking the mean of dollars by categroy and sales.
# Group by 'Category' and calculate the sum of 'Value' for each category
#sum
#grouped_data = df.groupby('Category')['Sales'].sum()
#mean
grouped_data = df.groupby(['City','Category']).agg({'Sales':'mean'}).reset_index()
print(grouped_data)


# %%
# Create a new data set in Domo with the result, the return value is the data set id of the new data set.
newds = domo.ds_create(df,'Row_ID | RowID','Order_Date | OrderDate')
#newds.show()
print(newds)

# %%
dataset_id = '24b2a63f-a2c1-4c47-a651-530667aa459f'
df1 = domo.ds_get(dataset_id)
#print(df)
df1.head(5)

# %% [markdown]
# Domo API Update Dataset

# %%
#Domo API Update Dataset
# Step 1: Download a dataset for sample superstore
dataset_id = '24b2a63f-a2c1-4c47-a651-530667aa459f'
df1 = domo.ds_get(dataset_id)
df1.head(2)


# %%
dd=df1

# %%
#errors='coerce' will convert bad values to NaN instead of crashing.
dd['Sales'] = pd.to_numeric(dd['Sales'], errors='coerce')
dd['Profit'] = pd.to_numeric(dd['Profit'], errors='coerce')

dd['Product Cost'] = dd['Sales'] - dd['Profit']
dd.head(2)

# %%
#Adding new column 'Product Cost' in existing Dataframe
#df1['Product Cost'] = df1.Sales - df1.Profit
df1['Product Cost'] = df1['Sales'] - df1['Profit']
df1.head(2)


# %%
#domo update column for the existing samplestore dataset id: '24b2a63f-a2c1-4c47-a651-530667aa459f'
#ds_update - updates an existing data set, only data sets created by the API can be updated
df1_update=domo.ds_update('24b2a63f-a2c1-4c47-a651-530667aa459f',df1)

# %%
df1_update

# %% [markdown]
# Domo API Data Set List and Meta Data

# %%
#Domo API Data Set List and Meta Data
#ds_list - downloads a list of data sets in your Domo instance
from pydomo import Domo
import pandas as pd

# Authenticate with your Domo client credentials
domo = Domo('2cb66264-2268-46e8-8922-e32f28c1fa4e', 'e00f7baa1ffd45de632dab3e8d6d257e4079819e787d00f70b63901bda426611', api_host='api.domo.com')

domo.ds_list()


# %%
#ds_meta - downloads meta data regarding a single data set
domo.ds_meta('24b2a63f-a2c1-4c47-a651-530667aa459f')

# %% [markdown]
# Domo Page list

# %%
###Domo Page list
from pydomo import Domo
import pandas as pd

# Authenticate with your Domo client credentials
domo = Domo('2cb66264-2268-46e8-8922-e32f28c1fa4e', 'e00f7baa1ffd45de632dab3e8d6d257e4079819e787d00f70b63901bda426611', api_host='api.domo.com')


# %%
pl=domo.page_list()
pl

# %%
page=domo.page_get('1524669750')
page



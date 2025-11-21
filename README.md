# DOMO BI with API's
#Generat ClientID and Secret Key
URL: https://developer.domo.com/new-client
API: myapi
Client ID :
6a87a02e-289f-4115-9efc-740a756477e1
Secret : 
5d9a476dfd273095adb37ecc86f72909f4671b28474f11d66b560c2e0d2e25f0
Scopes : data, workflow, audit, buzz, user, account, dashboard

#Import library

from pydomo import Domo
import pandas as pd

# Authenticate with your Domo client credentials
domo = Domo('6a87a02e-289f-4115-9efc-740a756477e1', '5d9a476dfd273095adb37ecc86f72909f4671b28474f11d66b560c2e0d2e25f0', api_host='api.domo.com')

# Step 1: Download a dataset for sample superstore
##https://ddsys.domo.com/datasources/bdc0aa5d-54bc-47f7-aa93-9670e19a221f/details/settings
dataset_id = 'bacc267e-167c-446d-ae77-9c1758762137'
df = domo.ds_get(dataset_id)
#print(df)

# Step 2: Perform a transformation (e.g., group by and average)
summary = df.groupby(['Region']).agg({'Sales': 'mean'}).reset_index()

# Step 3: Create a new dataset in Domo
new_dataset = domo.ds_create(summary, 'Python | Sales Summary', 'Generated via PyDomo')

# Step 4: Upload the transformed data
domo.ds_update(new_dataset, summary)


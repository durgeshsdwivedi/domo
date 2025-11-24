# Important Notes - Python 3 Compatibility
PyDomo is written for Python3, and is not compatible with Python2
Execute scripts via 'python3', and updates via 'pip3'

# About
The Domo API SDK is the simplest way to automate your Domo instance
The SDK streamlines the API programming experience, allowing you to significantly reduce your written code
This SDK was written for Python3, and is not compatible with Python2
PyDomo has been published to PyPI. The SDK can be easily installed via pip3 install pydomo, and can be updated via pip3 install pydomo --upgrade

# Features:
DataSet and Personalized Data Policy (PDP) Management
Use DataSets for fairly static data sources that only require occasional updates via data replacement
This SDK automates the use of Domo Streams so that uploads are always as fast as possible
Add Personalized Data Policies (PDPs) to DataSets (hide sensitive data from groups of users)
Docs: https://developer.domo.com/docs/domo-apis/data

# User Management
Create, update, and remove users
Major use case: LDAP/Active Directory synchronization
Docs: https://developer.domo.com/docs/domo-apis/users

# Group Management
Create, update, and remove groups of users
Docs: https://developer.domo.com/docs/domo-apis/group-apis

# Page Management
Create, update, and delete pages
Docs: https://developer.domo.com/docs/page-api-reference/page

# Setup
Install Python3: https://www.python.org/downloads/
Linux: 'apt-get install python3'
MacOS: 'brew install python3'
Windows: direct download, or use Bash on Windows 10
Install PyDomo and its dependencies via pip3 install pydomo

# Updates
Update your PyDomo package via pip3 install pydomo --upgrade
View the changelog

# Usage
Below are examples of how to use the SDK to perform a few common tasks. To run similar code on your system, do the following.
•	Create an API Client on the Domo Developer Portal
•	Use your API Client id/secret to instantiate pydomo 'Domo()'
•	Multiple API Clients can be used by instantiating multiple 'Domo()' clients
•	Authentication with the Domo API is handled automatically by the SDK
•	If you encounter a 'Not Allowed' error, this is a permissions issue. Please speak with your Domo Administrator.

# Create an API Client on the Domo Developer Portal
Use your API Client id/secret to instantiate pydomo 'Domo()'
Multiple API Clients can be used by instantiating multiple 'Domo()' clients
Authentication with the Domo API is handled automatically by the SDK
If you encounter a 'Not Allowed' error, this is a permissions issue. Please speak with your Domo Administrator.

**# DOMO BI with API's**
#Generat ClientID and Secret Key
URL: https://developer.domo.com/new-client
API: myapi
Client ID :
6a87a02e-289f-4115-9efc-740a756477e1
Secret : 
5d9a476dfd273095adb37ecc86f72909f4671b28474f11d66b560c2e0d2e25f0
Scopes : data, workflow, audit, buzz, user, account, dashboard

**#Import library**

from pydomo import Domo
import pandas as pd

#Authenticate with your Domo client credentials
domo = Domo('6a87a02e-289f-4115-9efc-740a756477e1', '5d9a476dfd273095adb37ecc86f72909f4671b28474f11d66b560c2e0d2e25f0', api_host='api.domo.com')

# Step 1: Download a dataset for sample superstore
#https://ddsys.domo.com/datasources/bdc0aa5d-54bc-47f7-aa93-9670e19a221f/details/settings
dataset_id = 'bacc267e-167c-446d-ae77-9c1758762137'
df = domo.ds_get(dataset_id)
#print(df)

# Step 2: Perform a transformation (e.g., group by and average)
summary = df.groupby(['Region']).agg({'Sales': 'mean'}).reset_index()

# Step 3: Create a new dataset in Domo
new_dataset = domo.ds_create(summary, 'Python | Sales Summary', 'Generated via PyDomo')

# Step 4: Upload the transformed data(Update the data existing dataset)
domo.ds_update(new_dataset, summary)


import os
from dasscostorageclient import DaSSCoStorageClient
from dasscostorageclient.exceptions import APIError

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client = DaSSCoStorageClient(client_id, client_secret)

# Get all institutions
institutions = client.institutions.list()

# Get a specific institution
institution = client.institutions.get('test-suite-institution-2')

# Create a new institution
try:
    new_inst = client.institutions.create('test-institution')
except APIError as e:
    # Institution might already exist
    pass

# Update the role restrictions on an institution
role_restrictions = [{ 'name': 'test-role' }]
up_inst = client.institutions.update('test-institution', role_restrictions)

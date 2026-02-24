import os
from dasscostorageclient import DaSSCoStorageClient
from dasscostorageclient.exceptions import APIError

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client = DaSSCoStorageClient(client_id, client_secret)

specimen_id = "specimen123"

body = {
    "institution": "test-institution",
    "collection": "test-collection",
    "specimen_pid": specimen_id,
    "barcode": "['123456', '3213123']",
    "preparation_types": ['pinned']
}

# Create or update specimen
specimen = client.specimens.populate(specimen_id, body)

# Get specimen
specimen = client.specimens.get(specimen_id)

# Get specimen preparation types
types = client.specimens.get_preparation_types()

# Delete specimen
client.specimens.delete(specimen_id)
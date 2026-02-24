import os
from dasscostorageclient import DaSSCoStorageClient
from dasscostorageclient.exceptions import APIError

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client = DaSSCoStorageClient(client_id, client_secret)

asset_guid = "test_asset"

# Create an asset
body = {
    "asset_pid": '1234',
    "asset_guid": asset_guid,
    "funding": ["some funding"],
    "institution": "test-suite-institution",
    "pipeline": "test-suite-pipeline",
    "collection": "test-suite-collection",
    "workstation": "test-suite-workstation",
    "status": "WORKING_COPY",
    "digitiser": "John Doe",
}

try:
    asset = client.assets.create(body, 10)
    print(asset.http_info)
except APIError as e:
    print(e)
    # Asset might already exist
    pass

# Get asset
asset = client.assets.get(asset_guid)

# Update asset
asset = client.assets.update(asset_guid, body)
print(asset)

# Get asset status
status = client.assets.get_status(asset_guid)
print(status)

# Delete asset
client.assets.delete(asset_guid)

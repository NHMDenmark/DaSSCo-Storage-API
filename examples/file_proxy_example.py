import os
from dasscostorageclient import DaSSCoStorageClient
from dasscostorageclient.exceptions import APIError

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client = DaSSCoStorageClient(client_id, client_secret)

filename = "file.tif"
institution = "test-suite-institution"
collection = "test-suite-collection"
guid = "test_asset24"

body = {
    "asset_pid": '1234',
    "asset_guid": guid,
    "funding": ["some funding"],
    "institution": institution,
    "pipeline": "test-suite-pipeline",
    "collection": collection,
    "workstation": "test-suite-workstation",
    "status": "WORKING_COPY",
    "digitiser": "John Doe",
}

# Create a new asset
asset = None
try:
    asset = client.assets.create(body, 10)
    print(asset.http_info)
except APIError as e:
    print(e)
    # Asset might already exist
    pass

# Upload file
client.files.upload_path(file_path=filename, path=asset.http_info.path, file_size_mb=10)
# Alternatively: client.files.upload(filename, institution, collection, guid, 10)

# List of files for a given asset with an open share
lst = client.files.list(institution, collection, guid)
print(lst)

# List of file metadata associated with an asset
info = client.files.list_info(guid)
print(info)

# Download file from an asset
file = client.files.download(institution, collection, guid, filename)
with open("downloaded_file.tif", "wb") as f:
    f.write(file)

#client.files.sync_erda(guid)

# Delete the specified file for an asset
#client.files.delete(institution, collection, guid, filename)

# Delete all files for an asset
#client.files.delete_all(institution, collection, guid)

files = client.files.list_files_in_erda(guid)
print(files)
# # Close share
# http_info = client.files.close_share(guid)
# print(http_info)
#
# # Open share
# http_info = client.files.open_share(institution, collection, guid, 10, ["John"])
# print(http_info)

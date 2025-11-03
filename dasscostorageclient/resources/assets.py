from dasscostorageclient.core.models import Asset, AssetStatus
from dasscostorageclient.resources.base import BaseResource

class AssetMetadataResource(BaseResource):
    def __init__(self, client):
        super().__init__(client, "/v1/assetmetadata")

    def get(self, guid: str) -> Asset:
        return Asset.model_validate(self._get(f"/{guid}").json())

    def create(self, body: dict, allocation_mb) -> Asset:
        res = self._post(f"?allocation_mb={allocation_mb}", body=body)
        return Asset.model_validate(res.json())

    def update(self, guid: str, body: dict) -> Asset:
        return Asset.model_validate(self._put(f"/{guid}", body).json())

    def delete(self, guid: str) -> None:
        self._delete(f"/{guid}/deleteMetadata")

class AssetResource(BaseResource):
    def __init__(self, client):
        super().__init__(client, "/v1/assets")
        self._metadata_resource = AssetMetadataResource(client)

    def get(self, guid: str) -> Asset:
        return self._metadata_resource.get(guid)

    def create(self, body: dict, allocation_mb) -> Asset:
        return self._metadata_resource.create(body, allocation_mb)

    def update(self, guid: str, body: dict) -> Asset:
        return self._metadata_resource.update(guid, body)

    def delete(self, guid: str) -> None:
        self._metadata_resource.delete(guid)

    def get_status(self, guid: str) -> AssetStatus:
        return AssetStatus.model_validate(self._get(f"/status/{guid}").json())
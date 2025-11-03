import zlib
import os
from typing import List
from pydantic import TypeAdapter
from .base import BaseResource
from ..core.models import FileInfo, HTTPInfo

class FileProxyResource(BaseResource):

    def __init__(self, client):
        super().__init__(client, "", True)

    def upload(self, file_path, institution: str, collection: str, asset_guid: str, file_size_mb: int) -> None:
        file = open(file_path, 'rb')
        file_data = file.read()
        file.close()
        # Calculate checksum
        crc = zlib.crc32(file_data)
        filename = os.path.basename(file_path)
        self._put(f"/assetfiles/{institution}/{collection}/{asset_guid}/{filename}?crc={crc}&file_size_mb={file_size_mb}", data=file_data)

    def delete_all(self, institution: str, collection: str, asset_guid: str) -> None:
        self._delete(f"/assetfiles/{institution}/{collection}/{asset_guid}")

    def delete(self, institution: str, collection: str, asset_guid: str, file_name: str) -> None:
        self._delete(f"/assetfiles/{institution}/{collection}/{asset_guid}/{file_name}")

    def download(self, institution: str, collection: str, asset_guid: str, file_name: str) -> bytes:
        return self._get(f"/assetfiles/{institution}/{collection}/{asset_guid}/{file_name}").content

    def list(self, institution: str, collection: str, asset_guid: str) -> list[str]:
        return self._get(f"/assetfiles/{institution}/{collection}/{asset_guid}").json()

    def list_info(self, asset_guid: str) -> List[FileInfo]:
        res = self._get(f"/assets/{asset_guid}/files").json()
        return TypeAdapter(List[FileInfo]).validate_python(res)

    def open_share(self, institution: str, collection: str, asset_guid: str, allocation_mb: int, users: List[str]) -> HTTPInfo:
        body = {
            "assets": [{
                "asset_guid": asset_guid,
                "institution": institution,
                "collection": collection
            }],
            "users": users,
            "allocation_mb": allocation_mb
        }
        return HTTPInfo.model_validate(self._post(f"/shares/assets/{asset_guid}/createShare", body).json())

    def close_share(self, asset_guid: str):
        return self._delete(f"/shares/assets/{asset_guid}/deleteShare").json()

    def sync_erda(self, asset_guid: str) -> None:
        self._post(f"/shares/assets/{asset_guid}/synchronize")

    def list_files_in_erda(self, asset_guid) -> List[str]:
        return self._get(f"/assetfiles/listfiles/{asset_guid}").json()




    # def change_allocation(self, asset_guid: str, new_allocation_mb: int):
    #     body = {
    #         "asset_guid": asset_guid,
    #         "new_allocation_mb": new_allocation_mb
    #     }
    #
    #     res = send_request_to_file_proxy(
    #         RequestMethod.POST,
    #         self.access_token,
    #         f"/shares/assets/{asset_guid}/changeAllocation",
    #         json=body
    #     )
    #     return res
    #
    # def list_shares(self):
    #     """
    #     List open shares and their information
    #     """
    #     res = send_request_to_file_proxy(
    #         RequestMethod.POST,
    #         self.access_token,
    #         f"/shares"
    #     )
    #     return res

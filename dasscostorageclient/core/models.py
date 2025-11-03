from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class ExternalPublisher(BaseModel):
    name: str

class HTTPInfo(BaseModel):
    path: str
    hostname: str
    total_storage_mb: int
    cache_storage_mb: int
    remaining_storage_mb: int
    allocated_storage_mb: int
    allocation_status_text: str | None
    http_allocation_status: str

class Issue(BaseModel):
    category: str
    name: str | None
    status: str | None
    description: str | None
    notes: str | None
    solved: bool
    timestamp: datetime = None

class Legality(BaseModel):
    copyright: str | None
    license: str | None
    credit: str | None

class Specimen(BaseModel):
    institution: str | None
    collection: str | None
    barcode: str
    pid: str = Field(alias='specimen_pid')
    preparation_types: list[str]
    asset_preparation_type: str | None
    specimen_id: int | None
    specify_collection_object_attachment_id: int | None
    asset_detached: bool

class Asset(BaseModel):
    asset_locked: bool
    asset_subject: str | None
    audited: bool
    camera_setting_control: str | None
    collection: str
    complete_digitiser_list: list[str]
    digitiser: str | None
    external_publishers: list[ExternalPublisher] | None
    file_formats: list[str]
    funding: list[str]
    guid: str = Field(alias='asset_guid')
    http_info: HTTPInfo | None = Field(alias='httpInfo')
    institution: str
    internal_status: str
    issues: list[Issue] | None
    legality: Legality | None
    make_public: bool
    metadata_source: str | None
    metadata_version: str | None
    # mime_type: str | None
    mos_id: str | None
    multi_specimen: bool
    parent_guids: list[str]
    payload_type: str | None
    pid: str | None = Field(alias='asset_pid')
    pipeline: str
    push_to_specify: bool
    restricted_access: list[str]
    specify_attachment_remarks: str | None
    specify_attachment_title: str | None
    specimens: list[Specimen]
    status: str
    tags: dict | None

class Event(BaseModel):
    user: str | None
    timestamp: datetime = Field(alias="timeStamp")
    event: str
    pipeline: str

class AssetStatus(BaseModel):
    guid: str = Field(alias='asset_guid')
    parent_guid: list[str]
    status: str
    error_timestamp: datetime | None
    error_message: str | None
    share_allocation_mb: int | None

class FileInfo(BaseModel):
    id: int = Field(alias='fileId')
    guid: str = Field(alias='assetGuid')
    path: str
    size_bytes: int = Field(alias='sizeBytes')
    crc: int
    delete_after_sync: bool = Field(alias='deleteAfterSync')
    sync_status: str = Field(alias='syncStatus')
    work_dir_filepath: str = Field(alias='workDirFilePath')

class RoleRestriction(BaseModel):
    name: str

class Institution(BaseModel):
    name: str
    roleRestrictions: List[RoleRestriction]

class Pipeline(BaseModel):
    name: str
    institution: str
    pipeline_id: int

class Collection(BaseModel):
    name: str
    institution: str

class Workstation(BaseModel):
    name: str
    status: str
    institution: str
    workstation_id: int
from typing import List
from dasscostorageclient.core.models import Specimen
from dasscostorageclient.resources.base import BaseResource

class SpecimenResource(BaseResource):

    def __init__(self, client):
        super().__init__(client, "/v1/specimens")

    def populate(self, specimen_pid: str, body: dict) -> Specimen:
        """
        Creates or updates the given specimen.

        :param specimen_pid: The PID of the specimen to be created/updated.
        :param body: The specimen payload.
        :return: The created/updated specimen.

        Example:

            .. code-block:: python

                specimen_pid = "specimen_pid"
                body = {
                    "institution": "test-institution",
                    "collection": "test-collection",
                    "barcode": "['ti-sp-00012']",
                    "specimen_pid": specimen_pid,
                    "preparation_types": ["pinned"],
                    "specimen_id": 0,
                    "role_restrictions": [
                        {
                            "name": "test-role"
                        }
                    ]
                }
                client.specimens.populate(specimen_pid, body)
        """
        return Specimen.model_validate(self._put(f"/{specimen_pid}", body).json())

    def get(self, specimen_pid: str) -> Specimen:
        """
        Gets the specimen with the given PID.
        :param specimen_pid: The PID of the specimen to be retrieved.
        :return: The retrieved specimen.
        """
        return Specimen.model_validate(self._get(f"/{specimen_pid}").json())

    def get_preparation_types(self) -> List[str]:
        """
        Gets the preparation types of specimens.
        :return: A list of preparation types.
        """
        return self._get("/preparationTypes").json()

    def delete(self, specimen_pid: str) -> None:
        """
        Deletes the specimen with the given PID.
        :param specimen_pid: The PID of the specimen to be deleted.
        :return: None
        """
        self._delete(f"/{specimen_pid}")

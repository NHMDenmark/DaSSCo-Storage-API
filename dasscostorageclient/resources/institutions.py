from typing import List
from dasscostorageclient.core.models import Institution, RoleRestriction
from dasscostorageclient.resources.base import BaseResource
from dasscostorageclient.utils import json_to_model

class InstitutionResource(BaseResource):

   def __init__(self, client):
       super().__init__(client, "/v1/institutions")

   def list(self) -> List[Institution]:
       """
       Gets a list of all institutions.
       :return: A list of institutions.
       """
       return json_to_model(List[Institution], self._get().json())

   def get(self, name: str) -> Institution:
       """
       Gets the institution with the given name.
       :param name: The name of the institution to be retrieved.
       :return: The retrieved institution.
       """
       return json_to_model(Institution, self._get(f"/{name}").json())

   def create(self, name: str, role_restrictions: List[RoleRestriction] = None) -> Institution:
       """
       Creates a new institution with the given name.
       :param name: The name of the institution to be created.
       :param role_restrictions: The roles needed to access assets within the institution.
       :return: The newly created institution.
       """
       if role_restrictions is None:
           role_restrictions = []

       body = {"name": name, "roleRestrictions": role_restrictions}
       return json_to_model(Institution, self._post(body=body).json())

   def update(self, name: str, role_restrictions: List[RoleRestriction]) -> Institution:
       """
       Update the role restrictions on the given institution.
       :param name: The name of the institution to be updated.
       :param role_restrictions: The roles needed to access assets within the institution.
       :return: The updated institution.
       """
       if role_restrictions is None:
           role_restrictions = []

       body = {"name": name, "roleRestrictions": role_restrictions}
       return json_to_model(Institution, self._put(f"/{name}", body).json())
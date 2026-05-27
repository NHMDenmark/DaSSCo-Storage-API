import os
import sys 
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) 
sys.path.append(project_root) 
import pytest 
from tests.dassco_test_client import client 
import json 

class SpecimenModel: 
   def __init__(self): 
       self.specimen_pid = "test_pid_654" 
       self.specimen = { "institution": "test-institution", "collection": "test-collection", "barcode": "test-barcode-654", "specimen_pid": self.specimen_pid, "preparation_types": ["pinned"], "specimen_id": None, "role_restrictions": [] }
       
@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
     # before
     
     yield 
      
     # after 
      
@pytest.mark.order(1) 
def test_can_create_specimen():

    specimen_model = SpecimenModel()
    institution = specimen_model.specimen["institution"]
    collection = specimen_model.specimen["collection"]
    catalogueNumber = specimen_model.specimen["barcode"]
    specimen = specimen_model.specimen
    
    res = client.specimens.create_or_update(institution, collection, catalogueNumber, specimen) 
    
    status_code = res.get('status_code') 
    specimen = res.get('data') 
    
    assert status_code == 200 
    assert specimen.barcode == specimen_model.specimen["barcode"] 
    
@pytest.mark.order(2) 
def test_can_get_specimen(): 
    
    specimen_model = SpecimenModel()
    specimen = specimen_model.specimen 
    
    res = client.specimens.get_specimen(institution=specimen["institution"], collection=specimen["collection"], catalogueNumber=specimen["barcode"]) 
    
    status_code = res.get('status_code') 
    specimen = res.get('data') 
    
    assert status_code == 200 
    assert specimen.barcode == specimen_model.specimen["barcode"] 

@pytest.mark.order(3) 
def test_can_delete_specimen():
    
    specimen_model = SpecimenModel()
    institution = specimen_model.specimen["institution"]
    collection = specimen_model.specimen["collection"]
    catalogueNumber = specimen_model.specimen["barcode"]

    res = client.specimens.delete_specimen(institution, collection, catalogueNumber)
    status_code = res.get('status_code') 
    
    assert status_code == 200
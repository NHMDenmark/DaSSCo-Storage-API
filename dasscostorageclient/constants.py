from dotenv import load_dotenv
import os

load_dotenv()

ARS_BASE_URL = os.getenv("ARS_BASE_URL") or "https://biovault.dassco.dk"
DASSCO_AUTH_URL = os.getenv("DASSCO_AUTH_URL") or "https://biovault.dassco.dk/keycloak"
DASSCO_REALM = os.getenv("DASSCO_REALM") or "dassco"


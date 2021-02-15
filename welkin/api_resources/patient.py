from welkin.api_resources.abstract import CreateableAPIResource
from welkin.api_resources.abstract import UpdateableAPIResource

class Patient(
    CreateableAPIResource,
    UpdateableAPIResource
):
    OBJECT_NAME = "patients"

    

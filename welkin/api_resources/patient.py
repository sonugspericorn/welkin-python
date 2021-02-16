from welkin.api_resources.abstract import CreateableAPIResource
from welkin.api_resources.abstract import GetableAPIResource
from welkin.api_resources.abstract import ListableAPIResource
from welkin.api_resources.abstract import UpdateableAPIResource


class Patient(
    CreateableAPIResource,
    GetableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource
):
    OBJECT_NAME = "patients"


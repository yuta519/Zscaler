import json
from typing import Dict
from typing import List
from typing import Union


import requests
from requests import api
from requests.models import Response

from auth import login
from auth import logout
from base import Base


base = Base()


def fetch_adminusers(search_query: str = None) -> str:
    """Get Zscaler's url catergories."""
    api_endpoint: str = f"{base.base_url}/adminUsers"
    if search_query is not None:
        api_endpoint = f"{api_endpoint}?search={search_query}"

    api_token: str = login()
    headers: dict[str, str] = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "cookie": api_token,
    }
    response: Response = requests.get(api_endpoint, headers=headers)
    logout(api_token)

    return response.text


def fetch_adminroles():
    api_token = login()
    pass


def create_adminuser(
    loginName: str,
    userName: str,
    email: str,
    password: str,
    rolename: str,
) -> str:
    api_token: str = login()
    role_api_endpoint: str = f"{base.base_url}/adminRoles/lite"
    user_api_endpoint: str = f"{base.base_url}/adminUsers"
    headers: Dict[str, str] = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "cookie": api_token,
    }

    role_response: Response = requests.get(role_api_endpoint, headers=headers)
    roles: List[Dict[str, Union[int, str]]] = role_response.json()
    role_id: int = None
    for role in roles:
        if rolename in role.values():
            role_id: int = role["id"]

    admin_user_information = {
        "loginName": loginName,
        "userName": userName,
        "email": email,
        "password": password,
        "role": {"id": role_id},
        "adminScopescopeGroupMemberEntities": [],
        "adminScopeType": "ORGANIZATION",
        "adminScopeScopeEntities": [],
        "isPasswordLoginAllowed": True,
        "name": "Yuta Kawamura",
    }
    user_response = requests.post(
        user_api_endpoint, json.dumps(admin_user_information), headers=headers
    )
    logout(api_token)

    message: str = "Success" if user_response.status_code == 200 else f"Failed"
    message += f": {user_response.status_code} {user_response.text}" if message == "Failed" else None
    return message

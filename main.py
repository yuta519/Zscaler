import argparse
import os

import zia
from admin import fetch_adminusers
from admin import create_adminuser
from base import Base


def main():
    # print(fetch_adminusers("yoshiyuki.ishii@softbank-demo-05.com"))
    create_adminuser(
        loginName="test1@zscaler.net",
        userName="Yuta Kawamura",
        email="test1@zscaler.net",
        password="P@ssw0rd",
        rolename="Admin",
    )


if __name__ == "__main__":
    main()

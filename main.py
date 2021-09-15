from admin import fetch_adminusers
from admin import create_adminuser
from url_filtering_rules import create_url_filering_rules
from url_filtering_rules import fetch_all_url_filering_rules 
from url_categories import get_url_categories 

def main():
    # create_adminuser(
    #     loginName="test1@zscaler.net",
    #     userName="Yuta Kawamura",
    #     email="test1@zscaler.net",
    #     password="P@ssw0rd",
    #     rolename="Admin",
    # )

    # print(fetch_all_url_filering_rules())

    # create_url_filering_rules(
    #     name="Test Filtering Rule",
    #     order=1,
    #     protocols=["HTTPS_RULE"],
    #     locations=[],
    #     groups=[],
    #     departments=[],
    #     users=[],
    #     url_categories=["GAMBLING"],
    #     state="DISABLED",
    #     rank=0,
    #     action="ALLOW",
    # )
    get_url_categories()

if __name__ == "__main__":
    main()

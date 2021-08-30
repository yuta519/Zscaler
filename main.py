import argparse
import os

import zia


def main():
    zlookup = zia.ZiaLookupUrl(
        cloud_name=os.environ.get("HOST_NAME"),
        api_key=os.environ.get("API_KEY"),
        admin_username=os.environ.get("USER_NAME"),
        admin_password=os.environ.get("PASSWORD"),
    )

    parser = argparse.ArgumentParser()
    parser.add_argument("function_name", type=str, help="set fuction name in this file")
    parser.add_argument(
        "-u",
        "--url",
        nargs="*",
        dest="url",
        help="set url to lookup by Zscaler",
        default=[],
    )
    parser.add_argument(
        "-m",
        "--mode",
        type=str,
        dest="mode",
        help="fetch url categories of Zscaler",
        default="",
    )
    args = parser.parse_args()

    if args.function_name:
        if args.function_name == "lookup":
            if args.url:
                z_url_lookup = zlookup.url_lookup(args.url)
                print(z_url_lookup)
            else:
                print("Please set url with -u or --url")
        elif args.function_name == "categories":
            if args.mode:
                z_url_categories = zlookup.get_url_categories(mode=args.mode)
            else:
                z_url_categories = zlookup.get_url_categories()
            print(z_url_categories)
        else:
            print("Please set property function name.")


if __name__ == "__main__":
    main()

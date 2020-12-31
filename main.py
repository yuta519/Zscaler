import argparse

import zia


def main():
    zlookup = zia.ZiaLookupUrl(
        cloud_name='zscaler.net', 
        api_key='xxxxxxxxxxxxxxxxxxxxxxxxx', 
        admin_username='xxxxxxxxxxxxxxx@xxxxxxxxxxxxxxx.co.jp',
        admin_password='xxxxxxxxxxxxxxxxxxxxxxx')

    parser = argparse.ArgumentParser()
    parser.add_argument('function_name', type=str,
                        help='set fuction name in this file')
    parser.add_argument('-u', '--url', nargs='*', dest='url',
                        help='set url to lookup by Zscaler', default=[])
    parser.add_argument('-m', '--mode', type=str, dest='mode',
                        help='fetch url categories of Zscaler', default='')
    args = parser.parse_args()

    if args.function_name:
        if args.function_name == 'lookup':
            if args.url:
                z_url_lookup = zlookup.url_lookup(args.url)
                print(z_url_lookup)
            else:
                print('Please set url with -u or --url')
        elif args.function_name == 'categories':
            if args.mode:
                z_url_categories = zlookup.get_url_categories(mode=args.mode)
            else:
                z_url_categories = zlookup.get_url_categories()
            print(z_url_categories)
        else:
            print('Please set property function name.')

if __name__ == "__main__":
    main()
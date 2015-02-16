#!/usr/bin/env python
import argparse
import requests


def main(api_key):
    s = requests.session()
    s.auth = (api_key, '')  # HTTP Authentication

    # List pushes
    cursor = None
    count  = 0
    while True:
        r_pushes = s.get('https://api.pushbullet.com/v2/pushes', params={'cursor': cursor, 'limit': 500})
        pushes = r_pushes.json()

        for push in pushes['pushes']:
            if push['active']:  # Push was not already deleted
                push_delete = s.delete(r_pushes.url + '/' + push['iden'])  # Delete push

                # Print progress
                count += 1
                print("Deleted %i pushes" % count)

        try:
            # Update cursor
            cursor = pushes['cursor']
        except KeyError:
            # Reached the end
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("API_KEY", help="Your PushBullet API key")
    args = parser.parse_args()

    main(args.API_KEY)
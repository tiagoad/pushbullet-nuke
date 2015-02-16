PushBullet Nuke
===============

One day I misconfigured a weechat pushbullet script and suddenly had 350 pushes in my account and no way to delete them.
My phone crashed when pushbullet started to display them, and through the website or the desktop application I could 
only delete them one by one.

I wrote this script to solve this issue, sharing it with the hope that it might help someone else with the same problem.

**WARNING**: This script will delete **every push** in your account.

Usage
-----

Simply run `python pushbullet_nuke.py <Your API key>`
You can find your API key [here](https://www.pushbullet.com/account)

This script works with both Python 2 and 3. Requires [requests](https://pypi.python.org/pypi/requests)
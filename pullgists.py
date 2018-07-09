#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Clone all gists of GitHub username given on the command line."""

import subprocess
import sys
import requests

gh_user = 'Wesalius'

req = requests.get('https://api.github.com/users/%s/gists' % gh_user)

for gist in req.json():
    ret = subprocess.call(['git', 'clone', gist['git_pull_url']])
    if ret != 0:
        print("ERROR cloning gist %s. Please check output." % gist['id'])

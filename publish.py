import writeas

import re
import os
import sys


token = os.environ.get('TOKEN')

c = writeas.client()
c.setToken(token)

with open('test.md', 'r') as f:
    lines = f.readlines()

# Extract title
title = re.sub('\n', '', lines[0].split("# ",1)[1])

# Extract body
body = sys.argv[0]

post = c.createCPost('actions', body)

print(post)
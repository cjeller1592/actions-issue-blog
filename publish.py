import writeas

import re
import os
import sys


token = os.environ.get('TOKEN')

c = writeas.client()
c.setToken(token)

# Extract body
body = sys.argv[1]

post = c.createCPost('actions', body)

print(post)
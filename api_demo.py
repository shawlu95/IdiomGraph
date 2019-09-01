import requests
from codecs import decode
import pandas as pd
import json

payload = {'idiom': '坚定不移', 'length': 2}
ret = requests.get("http://127.0.0.1:5000/find_next", params=payload)
content = decode(ret.text, 'unicode_escape')

print(pd.DataFrame(json.loads(content)))

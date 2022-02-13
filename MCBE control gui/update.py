import requests


url = 'https://minecraft.azureedge.net/bin-win/bedrock-server-1.18.11.01.zip'
r = requests.get(url, allow_redirects=True)

open('bedrock-server-1.18.11.01.zip', 'wb').write(r.content)

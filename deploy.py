import urllib.request
import json

token = "nfp_PfR3tTJC4NbWtnZhHuy8QXMtzHd7eXYU52db"
site_id = "96558610-34c3-43cb-85ed-f28cae6ccfa6"
zip_path = r"C:\Users\peter\Downloads\CC\websites\adventurets.com.au\site\deploy.zip"

url = f"https://api.netlify.com/api/v1/sites/{site_id}/deploys"

with open(zip_path, 'rb') as f:
    data = f.read()

print(f"Uploading {len(data) / (1024*1024):.1f} MB...")

req = urllib.request.Request(
    url,
    data=data,
    headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/zip',
    },
    method='POST'
)

resp = urllib.request.urlopen(req, timeout=300)
result = json.loads(resp.read())

print(f"Deploy ID: {result.get('id', '')}")
print(f"State: {result.get('state', '')}")
print(f"URL: {result.get('ssl_url', result.get('url', ''))}")
print(f"Deploy URL: {result.get('deploy_ssl_url', '')}")

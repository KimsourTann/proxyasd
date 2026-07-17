# api/proxy.py
import requests

def handler(request):
    url = request.args.get("url")
    if not url:
        return {"statusCode": 400, "body": "Missing 'url' parameter"}

    resp = requests.get(url)
    return {
        "statusCode": resp.status_code,
        "headers": {"Content-Type": resp.headers.get("Content-Type", "text/plain")},
        "body": resp.text
    }

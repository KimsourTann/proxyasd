# api/proxy.py
import requests

def handler(request):
    # Get target URL from query string
    url = request.args.get("url")
    if not url:
        return {
            "statusCode": 400,
            "body": "Missing 'url' parameter"
        }

    # Forward headers and method
    headers = {k: v for k, v in request.headers.items() if k.lower() != "host"}
    method = request.method

    try:
        if method == "GET":
            resp = requests.get(url, headers=headers, params=request.args)
        elif method == "POST":
            resp = requests.post(url, headers=headers, data=request.body)
        else:
            return {
                "statusCode": 405,
                "body": f"Method {method} not supported"
            }

        return {
            "statusCode": resp.status_code,
            "headers": dict(resp.headers),
            "body": resp.text
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }

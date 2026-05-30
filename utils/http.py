import requests

# def fetch(url):
#     try:
#         headers = {
#             "User-Agent": "Mozilla/5.0"
#         }
#         r = requests.get(url, timeout=8, headers=headers, allow_redirects=True)
#         return r
#     except Exception as e:
#         return None



def fetch(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        r = requests.get(url, timeout=8, headers=headers, allow_redirects=True)
        return r
    except Exception as e:
        print(f"[DEBUG] Request failed: {url} -> {e}")
        return None

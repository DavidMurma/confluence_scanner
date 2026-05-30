from utils.http import fetch

def detect_confluence(target):
    r = fetch(target + "/login.action")
    
    if r and "confluence" in r.text.lower():
        return True
    
    return False

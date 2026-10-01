import random
import string
import requests

BASE_URL = "https://api.mail.tm"










import requests

def sign_up(email, password):
    url = "https://api.rewind.ai/v1/auth/signup"
    
    headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzIiwiaXNBbm9ueW1vdXMiOnRydWUsImlhdCI6MTc5MDgzMTIwMSwiZXhwIjoxNzkzNDIzMjAxLCJzdWIiOiJjbXVwMm5xYXIwNHRybWswN2dsYm1zaGphIn0.M3Lc1z2fZcNAHh57CXuYd_XYearAhJaHNbFgBizWs34",
        "content-type": "application/json",
        "priority": "u=1, i"
    }

    payload = {
        "email": email,
        "password": password
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

# Example Usage:
# result = sign_up("vawegi1403@flakeian.com", "wdqaqad3qad")
# print(result)


def get_temp_email():
    """
    Fetches an available domain, creates a temporary user account,
    and returns (email, token).
    """
    try:
        # 1. Get list of available domains
        domain_resp = requests.get(f"{BASE_URL}/domains")
        domain_resp.raise_for_status()
        domains = domain_resp.json().get("hydra:member", [])
        
        if not domains:
            print("No domains available.")
            return None, None
            
        domain = domains[0]["domain"]
        
        # 2. Generate random username & password
        random_str = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
        email = f"user_{random_str}@{domain}"
        password = "TempPassword123!"

        # 3. Create account
        account_resp = requests.post(
            f"{BASE_URL}/accounts",
            json={"address": email, "password": password}
        )
        account_resp.raise_for_status()

        # 4. Get authentication token
        token_resp = requests.post(
            f"{BASE_URL}/token",
            json={"address": email, "password": password}
        )
        token_resp.raise_for_status()
        token = token_resp.json().get("token")

        return email, token

    except requests.RequestException as e:
        print(f"Error creating account on mail.tm: {e}")
        return None, None


def check_emails(token):
    """
    Checks for received messages on mail.tm using the authorization token.
    Returns a list of email message objects.
    """
    if not token:
        return []

    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(f"{BASE_URL}/messages", headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("hydra:member", [])
    except requests.RequestException as e:
        print(f"Error fetching inbox: {e}")
        return []


# Example Usage
if __name__ == "__main__":
    email, token = get_temp_email()
    print(f"Temporary Email: {email}")

    if email and token:
        messages = check_emails(token)
        print(f"Emails received: {len(messages)}")


    result = sign_up(email, "wdqaqad3qad")
    print(result)

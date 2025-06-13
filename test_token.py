import requests
import json

# Get token
response = requests.post(
    'http://localhost:8000/api/token/',
    json={
        'username': 'admin2',
        'password': 'admin2'  # Use the password you set
    }
)

print("Token Response:", response.status_code)
print(response.json())

if response.status_code == 200:
    token = response.json()['access']
    
    # Test the token with a protected endpoint
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    test_response = requests.get(
        'http://localhost:8000/api/snippets/',
        headers=headers
    )
    
    print("\nTest Response:", test_response.status_code)
    print(test_response.json()) 
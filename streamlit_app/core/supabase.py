import requests
import json


class AuthClient:

    def __init__(self):
        self.url = "https://vzefkdwuidkifnplavde.supabase.co"
        self.key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ6ZWZrZHd1aWRraWZucGxhdmRlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTUzMTAyMDcsImV4cCI6MjAzMDg4NjIwN30.2un9WhgPxBFALYou1yKwIbrvT28edFDLcReYpKr11F8"

    def registerRequest(self, email, password):
        register_url = f"{self.url}/auth/v1/signup"
        headers = {"apikey": self.key, "Content-Type": "application/json"}
        data = {"email": email, "password": password}
        response = requests.post(register_url,
                                 headers=headers,
                                 data=json.dumps(data))
        return response  # Mengambil respons dalam bentuk JSON

    def loginRequest(self, email, password):
        login_url = f"{self.url}/auth/v1/token?grant_type=password"
        headers = {"apikey": self.key, "Content-Type": "application/json"}
        data = {"email": email, "password": password}
        response = requests.post(login_url,
                                 headers=headers,
                                 data=json.dumps(data))
        return response

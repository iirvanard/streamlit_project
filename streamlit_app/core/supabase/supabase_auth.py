from .request_api import BaseApi
# from streamlit_local_storage import LocalStorage

# localS = LocalStorage()


class SupabaseAuth:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.client: BaseApi = BaseApi(
            base_url="https://vzefkdwuidkifnplavde.supabase.co",
            header={
                "apikey":
                "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ6ZWZrZHd1aWRraWZucGxhdmRlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTUzMTAyMDcsImV4cCI6MjAzMDg4NjIwN30.2un9WhgPxBFALYou1yKwIbrvT28edFDLcReYpKr11F8",
            })
        self.session = None

    def register_request(self, fname, email, password, phone):
        try:
            response = self.client._request(method="POST",
                                            endpoint="auth/v1/signup",
                                            body={
                                                "email": email,
                                                "password": password,
                                                "data": {
                                                    "fullname": fname,
                                                    "phone_number": phone
                                                }
                                            })

            return response
        except Exception as e:
            raise ValueError(e.response.json().get("msg"))

    def login_request(self, email, password):
        try:
            response = self.client._request(
                method="POST",
                endpoint="auth/v1/token?grant_type=password",
                body={
                    "email": email,
                    "password": password,
                })
            print(response.json())
            self.session = response.json()
            return response
        except Exception as e:
            raise ValueError(e.response.json().get('error_description'))

    def get_user(self):
        try:
            # print(self.client._cookies)
            response = self.client._request(
                method="GET",
                endpoint="auth/v1/user",
                headers={
                    "Authorization": f'Bearer {self.session["access_token"]}'
                })

            return response
        except Exception as e:
            return None

    def logout(self):
        try:
            # print(self.client._cookies)
            response = self.client._request(
                method="POST",
                endpoint="auth/v1/logout",
                headers={
                    "Authorization": f'Bearer {self.session["access_token"]}'
                })

            self.session = None
            return response
        except Exception as e:
            return str(e)

from supabase_auth import SupabaseAuth

auth = SupabaseAuth()

try:
    auth.login_request(email="t@t.com", password="123123")
    auth.get_user()
except Exception as e:
    print(str(e))

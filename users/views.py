from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url ="CALLBACK_URL_YOU_SET_ON_GITHUB"
    client_class = OAuth2Client


class GoogleLogin(SocialLoginView):
    """
    Retrive code (or token) By accessing Google’s endpoint, you can get code or token

If you’re using Authorization Code Grant, you can get code from following URL

https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=<CALLBACK_URL_YOU_SET_ON_GOOGLE>&prompt=consent&response_type=code&client_id=<YOUR CLIENT ID>&scope=openid%20email%20profile&access_type=offline

If you’re using Implicit Grant, you can get token from following URL

https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=<CALLBACK_URL_YOU_SET_ON_GOOGLE>&prompt=consent&response_type=token&client_id=<YOUR CLIENT ID>&scope=openid%20email%20profile

POST code or token to specified URL(/dj-rest-auth/google/)

    """
    adapter_class = GoogleOAuth2Adapter
    callback_url = "CALLBACK_URL_YOU_SET_ON_GOOGLE"
    client_class = OAuth2Client
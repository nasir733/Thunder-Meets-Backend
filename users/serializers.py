
from rest_framework import serializers

from django.contrib.auth import get_user_model
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.urls.base import reverse
from allauth.account import app_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import user_pk_to_url_str, user_username
from allauth.utils import build_absolute_uri
from dj_rest_auth.forms import AllAuthPasswordResetForm
from dj_rest_auth.serializers import PasswordResetSerializer
from django_countries.serializers import CountryFieldMixin
from django_countries.serializer_fields import CountryField
from dj_rest_auth.registration.serializers import RegisterSerializer



User = get_user_model()
class CustomRegisterSerializer(RegisterSerializer, ):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', '')
        }


class CustomAllAuthPasswordResetForm(AllAuthPasswordResetForm, CountryFieldMixin):
    def save(self, request, **kwargs):
        current_site = get_current_site(request)
        email = self.cleaned_data['email']
        token_generator = kwargs.get('token_generator',
                                     default_token_generator)

        for user in self.users:

            temp_key = token_generator.make_token(user)

            # save it to the password reset model
            # password_reset = PasswordReset(user=user, temp_key=temp_key)
            # password_reset.save()

            # send the password reset email
            path = reverse(
                'password_reset_confirm',
                args=[user_pk_to_url_str(user), temp_key],
            )

            # PASS NONE INSTEAD OF REQUEST
            url = build_absolute_uri(None, path)

            context = {
                'current_site': current_site,
                'user': user,
                'password_reset_url': url,
                'request': request,
            }
            if app_settings.AUTHENTICATION_METHOD != app_settings.AuthenticationMethod.EMAIL:
                context['username'] = user_username(user)
            get_adapter(request).send_mail('account/email/password_reset_key',
                                           email, context)
        return self.cleaned_data['email']

class CustomPasswordResetSerializer(PasswordResetSerializer):
    @property
    def password_reset_form_class(self):
        return CustomAllAuthPasswordResetForm


class Dj_Rest_Auth_Custom_User_Serializer(CountryFieldMixin, UserDetailsSerializer):
    country = CountryField(name_only=True)

    class Meta:
        extra_fields = []
        # see https://github.com/iMerica/dj-rest-auth/issues/181
        # UserModel.XYZ causing attribute error while importing other
        # classes from `serializers.py`. So, we need to check whether the auth model has
        # the attribute or not
        if hasattr(User, "USERNAME_FIELD"):
            extra_fields.append(User.USERNAME_FIELD)
        if hasattr(User, "EMAIL_FIELD"):
            extra_fields.append(User.EMAIL_FIELD)
        if hasattr(User, "first_name"):
            extra_fields.append("first_name")
        if hasattr(User, "last_name"):
            extra_fields.append("last_name")
        model = User

        exclude = [
            "password",
            "is_staff",
            "is_superuser",
            "user_permissions",
            "groups",
        ]
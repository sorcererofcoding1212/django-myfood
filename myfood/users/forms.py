from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields


class UserRegisterForm(UserCreationForm):
    email = fields.EmailField()
    description = fields.CharField(max_length=500)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'description']

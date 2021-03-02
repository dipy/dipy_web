from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


class UsersLoginForm(forms.Form):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput,)

    def __init__(self, *args, **kwargs):
        super(UsersLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
                    'class': 'form-control input-sm',
                    'name': 'email',
                    'placeholder': 'email'})
        self.fields['password'].widget.attrs.update({
                    'class': 'form-control input-sm',
                    'name': 'password',
                    'placeholder': 'password'})

    def clean(self, *args, **keyargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                # This user does not exists
                raise forms.ValidationError("Please enter a correct email and password. Note that both fields may be case-sensitive")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("User is no longer active")

        return super(UsersLoginForm, self).clean(*args, **keyargs)


class UsersRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "confirm_email", "password",
                  "confirm_password"]
    username = forms.CharField()
    email = forms.EmailField(label="Email")
    confirm_email = forms.EmailField(label="Confirm Email")
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput,
                                       label="Confirm Password")

    def __init__(self, *args, **kwargs):
        super(UsersRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control',
                                                     'name': 'username',
                                                     'placeholder': 'username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control',
                                                  'name': 'email',
                                                  'placeholder': 'email'})
        self.fields['confirm_email'].widget.attrs.update({
            'class': 'form-control',
            'name': 'confirm_email',
            'placeholder': 'confirm email'})
        self.fields['password'].widget.attrs.update({'class': 'form-control',
                                                     'name': 'password',
                                                     'placeholder': 'password'})
        self.fields['confirm_password'].widget.attrs.update({
            'class': 'form-control',
            'name': 'confirm_password',
            'placeholder': 'confirm password'})

    def clean(self, *args, **keyargs):
        email = self.cleaned_data.get("email")
        confirm_email = self.cleaned_data.get("confirm_email")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if email != confirm_email:
            raise forms.ValidationError("Email must match")

        if password != confirm_password:
            raise forms.ValidationError("Password must match")

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email is already registered")

        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("User with this username already registered")

        # you can add more validations for password
        if len(password) < 8:
            raise forms.ValidationError("Password must be greater than 8 characters")

        return super(UsersRegisterForm, self).clean(*args, **keyargs)

from django import forms


class RegisterForm(forms.Form):
    image = forms.ImageField()
    email = forms.EmailField()
    age = forms.IntegerField()
    username = forms.CharField()
    password = forms.CharField()
    password_confirm = forms.CharField()


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match")
        if password and password_confirm:
            return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

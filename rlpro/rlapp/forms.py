from django import forms

class RegistrationForm(forms.Form):
    fname=forms.CharField(
        label="Enter first name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'firstname'
            }
        )
    )

    lname = forms.CharField(
        label="Enter last name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'lastname'
            }
        )
    )

    uname = forms.CharField(
        label="Enter user name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'username'
            }
        )
    )
    pword = forms.CharField(
        label="Enter password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }
        )
    )

    mobile = forms.IntegerField(
        label="Enter Mobile number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'mobile'
            }
        )
    )

    email = forms.EmailField(
        label="Enter email",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }
        )
    )



class LoginForm(forms.Form):
    uname = forms.CharField(
        label="Enter user name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'username'
            }
        )
    )
    pword = forms.CharField(
        label="Enter password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }
        )
    )
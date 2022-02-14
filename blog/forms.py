
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import mCreatepost


class fUserCreate(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
            'required': ''
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password',
            'required': ''
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Password',
            'required': ''
        })
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'First name',
            'required': ''
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Last name',
            'required': ''
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email',
            'required': ''
        })

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2"]
class fCreatepost(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={"rows":2,"placeholder":"title"}))
    discription = forms.CharField(widget=forms.Textarea(attrs={"rows":3,"placeholder":"discripion"}))
    body = forms.CharField(widget=forms.Textarea(attrs={"rows":8,"placeholder":"body"}))
    class Meta:
        model = mCreatepost
        fields = "__all__"

    
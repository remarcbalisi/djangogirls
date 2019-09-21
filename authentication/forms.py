from django import forms


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.PasswordInput(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
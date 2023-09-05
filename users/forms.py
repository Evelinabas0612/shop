
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin,UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({"placeholder": 'Введите свой email'})
        self.fields['first_name'].widget.attrs.update({"placeholder": 'Ваше имя'})
        self.fields["last_name"].widget.attrs.update({"placeholder": 'Ваша фамилия'})
        self.fields["avatar"].widget.attrs.update({"placeholder": 'Ваша автарка'})
        self.fields['password'].widget = forms.HiddenInput()


class UserForgotPasswordForm(StyleFormMixin, PasswordResetForm):
    """Запрос на восстановление пароля"""

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class UserSetNewPasswordForm(StyleFormMixin, SetPasswordForm):
    """Изменение пароля пользователя после подтверждения"""

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

""" Definition of forms. """

import email
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.db import models
from .models import Comment
from .models import Blog


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))
    
""" Description of the contents of the form """

class PollForm (forms.Form):
    genre = forms.CharField(label='Какой жанр музыки вы предпочитаете слушать?', min_length=2, max_length=100)
    faveartist = forms.CharField(label='Какие три исполнителя (группы) являются вашими любимыми?', min_length=2, max_length=100)
    where = forms.CharField(label='Вы предпочитаете слушать музыку в дороге, на работе/учебе, дома или на больших мероприятиях?', min_length=2, max_length=100)
    important = forms.CharField(label='Что для вас важнее в музыке: мелодия, тексты песен или исполнение?', min_length=2, max_length=100)
    memoryalbum = forms.CharField(label='С каким альбомом или песней у вас связаны самые яркие музыкальные воспоминания?', min_length=2, max_length=100)
    notice = forms.BooleanField(label='Получать новости сайта?', required=False)
    
class CommentForm (forms.ModelForm):

    class Meta:

        model = Comment # используемая модель

        fields = ('text',) # требуется заполнить только поле text

        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}
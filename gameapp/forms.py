from django import forms
from .models import GameSearch, Game, Membership, FreeGame, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class GameSearchForm(forms.ModelForm):
    name_of_game = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control search-input", 'placeholder': 'Search Game',
    }))
    class Meta:
        model = GameSearch
        fields = ['name_of_game',]


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'form-control', 'placeholder': 'Username',  
    }))

    email = forms.CharField(max_length = 100, widget = forms.EmailInput(attrs={
        'class' : 'form-control', 'placeholder': 'Email Address', 
    }))

    password1 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs={
        'class' : 'form-control', 'placeholder': 'At least eight characters',
    }))
    password2 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs={
        'class' : 'form-control', 'placeholder': 'Confirm Password',
    }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Create a Game form
class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'slug', 'cover_image', 'banner', 'video', 'description', 'ram', 'game_size', 'category', 'file', 'show_in_banner',
                    'top_games', 'recently_added', 'popular', 'recommended', 'allowed_memberships')


# Create a FreeGame form
class FreeGameForm(ModelForm):
    class Meta:
        model = FreeGame
        fields = ('title', 'slug', 'cover_image', 'banner', 'video', 'description', 'ram', 'game_size', 'category', 'file1', 'file2',
                    'file3', 'file4', 'file5', 'free_games')


# Create a Game form
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class MembershipForm(ModelForm):
    class Meta:
        model = Membership
        fields = ('name', 'slug', 'cover_image', 'membership_type', 'duration', 'duration_period', 'price')
        

       
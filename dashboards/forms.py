from django import forms
from blogs.models import Category, Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','category','featured_image','short_description','blog_body','status','is_featured')


class UserAddingForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','username','first_name','last_name','is_staff','is_superuser','groups','user_permissions')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','username','first_name','last_name','is_staff','is_superuser','groups','user_permissions')

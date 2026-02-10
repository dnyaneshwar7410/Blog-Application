from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, BlogPostForm
from django.template.defaultfilters import slugify
from django.contrib import messages
# Create your views here.


@login_required(login_url='login/')
def dashboard(request):
    blogs_count = Blog.objects.all().count()
    context = {
        'blogs_count':blogs_count,
    }
    return render(request,'dashboard/dashboard.html', context)


#  category CRUD operations
def categories(request):
    return render(request,'dashboard/categories.html')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context ={
        'form':form
    }
    return render(request, 'dashboard/add_category.html', context)


def edit_category(request,pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return redirect('categories')
    
    if request.method == 'POST':
        form =  CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')   
    form = CategoryForm(instance=category)
    context = {
        'form':form,
        'category':category,
    }
    return render(request, 'dashboard/edit_category.html',context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')


# blogs CRUD operations

def posts(request):
    posts = Blog.objects.all().order_by('-created_at')
    context = {
        'posts':posts
    }
    return render(request, 'dashboard/posts.html',context)


def add_post(request):
   if request.method == 'POST':
       form = BlogPostForm(request.POST, request.FILES)
       if form.is_valid():
            post = form.save(commit=False)   # temporarily saving the form
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')     
   form = BlogPostForm()
   context = {
       'form':form
   }
   return render(request,'dashboard/add_post.html', context)


def edit_post(request, pk):
    try:
        post = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return redirect('posts')
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context = {
        'form':form,
        'post':post,
        }
    return render(request, 'dashboard/edit_post.html', context)


def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')
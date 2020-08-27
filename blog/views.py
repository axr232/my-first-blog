from django.shortcuts import render
from .models import Post
from .models import CV
from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from .forms import PostForm
from .forms import CVForm
from django.shortcuts import redirect
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,instance = post)
        if form.is_valid():
            post =form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
            form = PostForm(instance = post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
    print("TEST")
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def cv_page(request):
    cvForms = CV.objects.get()
    print("!!!!")
    print(cvForms.profile)
    print("!!!!")
    return render(request,'blog/cv_page.html',{'cvForms':cvForms})

def cv_edit(request):
    #print("DONE!")
    if request.method == "POST":
        form = CVForm(request.POST)
        if form.is_valid():
            #print("TEST2")
            CV.objects.all().delete()
            form.save()
            return redirect('cv_page')
    else:
        #print("TEST")
        form = CVForm()
    return render(request, 'blog/cv_edit.html', {'form': form})


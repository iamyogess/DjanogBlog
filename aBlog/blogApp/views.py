from django.shortcuts import render, redirect
from . models import AddBlogModel


def HomeView(request):
    blog_elements = AddBlogModel.objects.all()
    context = {
        'blog_elements': blog_elements,
    }
    return render(request, 'blogApp/index.html', context)


def AddPostView(request):
    if request.method == 'POST' or request.FILES:
        title = request.POST.get('title')
        addBlog = request.POST.get('add_post_input')
        if request.FILES:
            img = request.FILES.get('image')
        blog_contents = AddBlogModel(
            title=title, blog_content=addBlog, blog_img=img)
        blog_contents.author = request.user
        blog_contents.save()
        return redirect('blog_details')
    blog_obj = AddBlogModel.objects.all()
    return render(request, 'blogApp/add_post.html', {'blog_obj': blog_obj})


def UpdatePostView(request, id):
    UpdatePostId = AddBlogModel.objects.get(id=id)
    if request.method == 'POST':
        UpdatePostId.title = request.POST.get('title')
        UpdatePostId.blog_content = request.POST.get('add_post_input')
        UpdatePostId.save()
        return redirect('home')
    return render(request, 'blogApp/add_post.html', {'UpdatePostId': UpdatePostId})


def DeletePostView(request, id):
    DeletePostId = AddBlogModel.objects.get(id=id)
    DeletePostId.delete()
    return redirect('home')


def BlogDetailsView(request):
    blog_elements = AddBlogModel.objects.all()
    context = {
        'blog_elements': blog_elements,
    }

    return render(request, 'blogApp/blog_details.html', context)

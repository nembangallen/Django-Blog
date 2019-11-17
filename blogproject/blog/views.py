from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm
from django.views.generic import View, ListView, DetailView
# Create your views here.
# @login_required
# def blog_list(request):
#     blogs_list = Blog.objects.all()
#     return render(request, 'home.html',{'blogs_list':blogs_list}) 

class BlogListView(ListView):
    model = Blog
    # content_object_name = 'blogs_list'    
    template_name = 'home.html'

'''
Function Based View create_blog

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog_form.html',{'form':form})
'''

# Class Based View for create new blog
class CreateBlogView(View):
    def post(self,request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
        return render(request, 'blog_form.html',{'form':form})
    def get(self, request):
        form = BlogForm()
        return render(request, 'blog_form.html',{'form':form})

'''
Function Based View
@login_required
def blog_detail(request,pk):
    blog = Blog.objects.get(pk=pk)
    return render(request,'blog_detail.html',{'blog':blog})
'''
class BLogDetailView(DetailView):
    template_name = 'blog_detail.html'
    # queryset = Blog.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Blog, pk=pk_)

class UpdateBlogView(View):
    def post(self,request,pk):
        blog = Blog.objects.get(pk=pk)
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
        return render(request, 'blog_form.html',{'form':form})

    def get(self,request,pk):
        blog = Blog.objects.get(pk=pk)
        form = BlogForm(instance=blog)
        return render(request, 'blog_form.html',{'form':form})
        
# @login_required
# def blog_update(request, pk):

#     blog = Blog.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = BlogForm(request.POST, request.FILES, instance=blog)
#         if form.is_valid():
#             form.save()
#             return redirect('blog_list')
#     else:
#         form = BlogForm(instance=blog)

#     # if form.is_valid():
#     #     form.save()
#     #     return redirect('blog_list')
#     # if request.method == 'POST':
#     #     form = BlogForm(request.POST, request.FILES)
#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('blog_list')
#     # else:
#     #     blog = Blog.objects.get(pk=pk)
#     #     form = BlogForm(request.POST or None, instance=blog)
#     return render(request, 'blog_form.html',{'form':form})

@login_required
def blog_delete(request, pk):
    blog = Blog.objects.get(pk=pk).delete()
    return redirect('blog_list')
    pass

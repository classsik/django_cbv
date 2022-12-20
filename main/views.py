from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

from django.views.generic import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {
            'posts': Post.objects.all(),
        })


class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'create.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return self.get(request)


class PostEditView(View):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form': form})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

        return self.get(request, pk)


class PostDeleteView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('home')

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from blog.models import Post
from blog.forms import PostForm


# Create your views here.
class PostListView(generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(date_publish__isnull=False).order_by('date_publish')


class PostListDraftView(generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(date_publish__isnull=True).order_by('id')


class CreatePostView(generic.CreateView):
    model = Post
    form_class = PostForm


class PostDetailView(generic.DetailView):
    model = Post
    form_class = PostForm


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish_post()
    return redirect('blog:detail_post', pk=pk)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('blog:post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

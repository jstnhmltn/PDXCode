from django.shortcuts import render

from blog.forms import CommentForm
from blog.models import Post, Comment

# Create your views here.
def journal_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {"posts": posts}
    return render(request, "journal_index.html", context)

def journal_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "journal_detail.html", context)
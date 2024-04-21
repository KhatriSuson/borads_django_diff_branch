from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm
from django.http import HttpResponse, Http404


# Create your views here.


def home(request):
    boards = Board.objects.all()

    return render(request, "home.html", {"boards": boards})


def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)

    except Board.DoesNotExist:
        raise Http404
    return render(request, "topics.html", {"board": board})


def question(request, pk):
    return HttpResponse(f"Question:{pk}")


def post(request, slug):
    return HttpResponse(f"Slub :{slug}")


def blog_post(request, slug, pk):
    return HttpResponse(f"Blog_Post : {slug} and PK: {pk}")


def user_profile(request, username):
    return HttpResponse(f"User name:  {username}")


def year_archive(request, year):
    return HttpResponse(f"Year : {year}")


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        subject = request.POST["subject"]
        message = request.POST["message"]

        user = User.objects.first()
        topic = Topic.objects.create(subject=subject, board=board, starter=user)

        post = Post.objects.create(message=message, topic=topic, created_by=user)

        return redirect("board_topics", pk=board.pk)

    return render(request, "new_topic.html", {"board": board})

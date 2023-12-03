from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Board, Post
from .forms import TopicForm
from django.contrib.auth.decorators import login_required

#home views 
def home(request):
    boards = Board.objects.all()

    return render(request, 'board/home.html', {'boards':boards})


# This views open boards ditals
def topic(request, board_id):
    
    board = get_object_or_404(Board, pk=board_id)
    post = Post.objects.all()

  
    return render(request, 'board/topic.html', {'board':board, 'post':post})


@login_required
def new_topic(request, board_id):

    board = Board.objects.get(pk=board_id)
    user = User.objects.first()

    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            topic=form.save(commit=False)
            topic.board=board
            topic.created_by=user
            topic.save()
        
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user,
            )
            return redirect('topic', board_id)
    else:
        form = TopicForm()                  
    
    return render(request, 'board/new_topic.html', {'form':form})


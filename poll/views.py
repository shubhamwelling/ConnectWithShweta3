from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreatePollForm
from .models import Poll
from .forms import CommentForm
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test


def home(request):
    polls = Poll.objects.order_by('-dt')[:5]
    context = {
        'polls': polls
    }
    return render(request, 'poll/home.html', context)

def instructions(request):
    return render(request, 'poll/instructions.html')

def how(request):
    return render(request, 'poll/how.html')

def privacy(request):
    return render(request, 'poll/privacy.html')


def date(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll': poll
    }

    return render(request, 'poll/date.html', context)


def suggestions(request,poll_id):
    poll=Poll.objects.get(pk=poll_id)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.poll=poll
            comment.save()

            return redirect('suggestions',poll_id)
    else:
        form=CommentForm()

    return render(request,'poll/suggestions.html',{'poll':poll, 'form':form})



def create(request):
 if request.user.is_superuser:
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {
        'form': form
    }
    return render(request, 'poll/create.html', context)
 if not request.user.is_superuser:
        return HttpResponse('Access Denied')

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        elif selected_option == 'option4':
            poll.option_four_count += 1
        elif selected_option == 'option5':
            poll.option_five_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('home')

    context = {
        'poll': poll
    }
    return render(request, 'poll/vote.html', context)


def results(request, poll_id):
 if request.user.is_superuser:
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll': poll
    }

    return render(request, 'poll/results.html', context)
 if not request.user.is_superuser:
        return HttpResponse('Access Denied')


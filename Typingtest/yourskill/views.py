import random

from django.shortcuts import render,redirect

from .models import Paragraph,Score

from .forms import RegisterForm

from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


@login_required
def typing_test(request):
    if request.method == 'POST':
        wpm = int(request.POST.get('wpm', 0) or 0)
        accuracy = float(request.POST.get('accuracy', 0.0) or 0.0)
        Score.objects.create(user=request.user, wpm=wpm, accuracy=accuracy)
        return redirect('dashboard')

    paragraphs = Paragraph.objects.all()
    text = random.choice(paragraphs)
    leaderboard = Score.objects.order_by('-wpm')[:10]
    return render(request, 'typing.html', {
        'text': text,
        'leaderboard': leaderboard
    })


def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    else:

        form = RegisterForm()

    return render(request,'register.html',{'form':form})


@login_required
def dashboard(request):

    scores = Score.objects.filter(user=request.user)

    return render(request,'dashboard.html',{
        'scores':scores
    })
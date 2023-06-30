from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models


@login_required
def feed(request):
    tickets = models.Ticket.objects.all()
    return render(request, 'feed.html')


@login_required
def create_ticket(request):
    return render(request, 'create_ticket.html')


@login_required
def update_ticket(request):
    return render(request, 'update_ticket.html')


@login_required
def create_review(request):
    return render(request, 'create_review.html')


@login_required
def update_review(request):
    return render(request, 'update_review.html')


@login_required
def my_posts(request):
    return render(request, 'my_posts.html')


@login_required
def subscription(request):
    return render(request, 'subscription.html')

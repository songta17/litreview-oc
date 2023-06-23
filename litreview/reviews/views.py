from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models


@login_required
def feed(request):
    tickets = models.Ticket.objects.all()
    return render(request, 'home.html')


@login_required
def create_ticket(request):
    # manage form
    pass

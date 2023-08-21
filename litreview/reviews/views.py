from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from reviews.models import Ticket, Review
from reviews.form import NewTicketForm, NewReviewForm, FollowUserForm
from django.views.decorators.csrf import csrf_protect
from django.db import IntegrityError
# from django.urls import reverse
import ipdb
from itertools import chain
from django.db.models import Value, CharField


@login_required
def feed(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    tickets_and_reviews_sorted = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True)

    context = {
        "tickets_and_reviews_sorted": tickets_and_reviews_sorted
    }
    return render(request, 'feed.html', context)


@login_required
def my_posts(request):
    user = request.user
    tickets = Ticket.objects.filter(user=user)
    reviews = Review.objects.filter(user=user)

    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    tickets_and_reviews_owner_sorted = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True)
    context = {
        "tickets_and_reviews_owner_sorted": tickets_and_reviews_owner_sorted
    }
    return render(request, 'my_posts.html', context)


@ login_required
@ csrf_protect
def create_ticket(request):
    if request.method == 'POST':
        form = NewTicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            # ipdb.set_trace()
            ticket.user = request.user
            try:
                ticket.save()
                return redirect('feed')
            except IntegrityError as e:
                form.add_error(
                    None, 'Une erreur s\'est produite lors de la création du ticket.')
        else:
            print(form.errors)
    else:
        form = NewTicketForm()
    return render(request, 'create_ticket.html', {'form': form})


@login_required
def update_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    update_form = NewTicketForm(instance=ticket)
    if request.method == 'POST':
        update_form = NewTicketForm(
            request.POST, request.FILES, instance=ticket)
        if update_form.is_valid():
            update_form.save()
            return redirect('my_posts')
    context = {
        'update_form': update_form,
        'ticket': ticket
    }
    return render(request, 'update_ticket.html', context)


@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':
        ticket.delete()
        return redirect('my_posts')

    context = {
        'ticket': ticket
    }
    return render(request, 'delete_ticket.html', context)


@login_required
@csrf_protect
def create_review(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    form = NewReviewForm()
    if request.method == 'POST':
        form = NewReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = get_object_or_404(Ticket, id=ticket_id)
            review.ticket.has_review = True
            review.ticket.save()
            try:
                review.save()
                return redirect('feed')
            except IntegrityError as e:
                form.add_error(
                    None, 'Une erreur s\'est produite lors de la création de la critique.')
        else:
            print(form.errors)
    else:
        form = NewReviewForm()
    return render(request, 'create_review.html', {'form': form, 'ticket': ticket})


@login_required
@csrf_protect
def create_review_and_ticket(request):
    ticket_form = NewTicketForm()
    review_form = NewReviewForm()
    if request.method == 'POST':
        ticket_form = NewTicketForm(request.POST, request.FILES)
        review_form = NewReviewForm(request.POST)
        if review_form.is_valid() and ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.has_review = True
            try:
                ticket.save()
            except IntegrityError as e:
                review_form.add_error(
                    None, 'Une erreur s\'est produite lors de la création du ticket.')
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = get_object_or_404(Ticket, id=ticket.id)

            try:
                review.save()
                return redirect('feed')
            except IntegrityError as e:
                review_form.add_error(
                    None, 'Une erreur s\'est produite lors de la création de la critique et du ticket.')
        else:
            print(ticket_form.errors)
            print(review_form.errors)

    return render(request, 'create_review_and_ticket.html', {'ticket_form': ticket_form, 'review_form': review_form})
    # else:
    #     form = NewReviewForm()
    # return render(request, 'create_review.html', {'form': form})


@login_required
def update_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    update_form = NewReviewForm(instance=review)
    ticket = review.ticket
    if request.method == 'POST':
        update_form = NewReviewForm(request.POST, instance=review)
        if update_form.is_valid():
            update_form.save()
            return redirect('my_posts')
    context = {
        'update_form': update_form,
        'review': review,
        'ticket': ticket,
    }
    return render(request, 'update_review.html', context)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        review.delete()
        return redirect('my_posts')

    context = {
        'review': review
    }
    return render(request, 'delete_review.html', context)


@login_required
def subscription(request):
    follow_form = FollowUserForm()

    context = {
        'follow_form': follow_form
    }
    return render(request, 'subscription.html', context)

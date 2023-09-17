from django import forms

from .models import Ticket, Review


class NewTicketForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(widget=forms.FileInput, required=True)

    class Meta:
        model = Ticket
        # , 'user']  # , 'has_review']
        fields = ['title', 'description', 'image']


class NewReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(widget=forms.RadioSelect(
        attrs={'class': 'vertical-radio'}), choices=Review.RATING_CHOICES)

    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        labels = {
            'rating': 'Note',
        }


class FollowUserForm(forms.Form):
    follow_user = forms.CharField(
        label="Suivre d'autres utilisateurs", max_length=100, widget=forms.TextInput(attrs={'value': ''}))

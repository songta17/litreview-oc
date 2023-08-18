from django import forms

from .models import Ticket, Review


class NewTicketForm(forms.ModelForm):
    update_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(widget=forms.FileInput, required=True)

    class Meta:
        model = Ticket
        # , 'user']  # , 'has_review']
        fields = ['title', 'description', 'image']


class NewReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(widget=forms.RadioSelect(
        attrs={'class': 'radio-input'}), choices=Review.RATING_CHOICES)

    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']

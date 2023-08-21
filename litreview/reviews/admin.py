from django.contrib import admin
from reviews.models import Ticket, Review, UserFollows


class TicketAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "time_created", "has_review")


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("ticket", "rating", "headline", "body", "time_created")


class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ("user", "followed_user")


admin.site.register(Ticket, TicketAdmin)
# ajouter dans admin un barre de recherche, voir vidéo Nbe

admin.site.register(Review, ReviewAdmin)

admin.site.register(UserFollows, UserFollowsAdmin)

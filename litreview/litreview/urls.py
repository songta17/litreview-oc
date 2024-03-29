"""
URL configuration for litreview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
# dosssier pour les static et staticfile
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.urls import path

import authentication.views
from reviews.views import feed, create_ticket, subscription, create_review, create_review_and_ticket, my_posts, update_ticket, update_review, delete_ticket, delete_review, unsubscribe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'
    ), name='password_change'),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'
    ), name='password_change_done'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('feed/', feed, name='feed'),
    path('create-ticket/', create_ticket, name='create_ticket'),
    path('update-ticket/<int:ticket_id>/', update_ticket, name='update_ticket'),
    path('delete-ticket/<int:ticket_id>/', delete_ticket, name='delete_ticket'),
    path('create-review/<int:ticket_id>/', create_review, name='create_review'),
    path('create-review/', create_review_and_ticket,
         name='create_review_and_ticket'),
    path('update-review/<int:review_id>/', update_review, name='update_review'),
    path('delete-review/<int:review_id>/', delete_review, name='delete_review'),
    path('my-posts/', my_posts, name='my_posts'),
    path('subscription/', subscription, name='subscription'),
    path('unsubscribe/<int:subscription_id>/',
         unsubscribe, name='unsubscribe'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

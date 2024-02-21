from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("home/", views.Home.as_view(), name="home"),
    path("about/", views.About.as_view(), name="about"),
    path("contact/", views.Contact.as_view(), name="contact"),

    path("cart/", login_required(views.Cart.as_view()), name="cart"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("dashboard/", views.dashborad, name="dashboard"),

    
]

htmx_patterns = [
    path('check_username', views.check_username, name='check_username'),
]

urlpatterns += htmx_patterns


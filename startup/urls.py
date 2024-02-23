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
    path('check_username/', views.check_username, name='check_username'),
    path('check_email/', views.check_email, name='check_email'),
    path('check_password/', views.check_password, name='check_password'),
    path('check_mobile_number/', views.check_mobile_number, name='check_mobile_num'),
    # path('check_username_password/', views.check_username_password, name='check_username_password'),
]

urlpatterns += htmx_patterns


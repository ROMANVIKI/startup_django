from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.About.as_view(), name="about"),
    path("contact", views.Contact.as_view(), name="contact"),

   
    path("signin", views.signin, name="signin"),
    path("logout", views.logout_view, name="logout"),

    path("signup", views.signup, name="signup"),
    path("dashboard", views.dashborad, name="dashboard"),
  



    path('get_username', views.get_username, name='get-username'),
    path('product-list', views.ProductListView.as_view(), name='product-list'),
    path('product-detail/<str:slug>', views.product_detail, name='product-detail'),
    path('payment-process/', views.payment_process, name='payment-process'),

    path('invoice', views.invoice, name='invoice'),
    
]

htmx_patterns = [
    path('check_username/', views.check_username, name='check_username'),
    path('check_email/', views.check_email, name='check_email'),
    path('check_password/', views.check_password, name='check_password'),
    path('check_mobile_number/', views.check_mobile_number, name='check_mobile_num'),
    # path('check_username_password/', views.check_username_password, name='check_username_password'),
]

urlpatterns += htmx_patterns


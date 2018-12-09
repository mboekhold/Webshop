from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as account_views

urlpatterns = [
    # path("login/", views.LoginView.as_view(), name="login"),
    # path('logout/', views.LogoutView.as_view()),
    # path('signup/',views.SignUp.as_view(), name="signup"),

    path('signup/', account_views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('change_profile/', account_views.changeProfile, name='change_profile')
]

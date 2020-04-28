from django.urls import path
from . import views
# Create your views here.

urlpatterns = [
    #path('signup/', views.Signup),
    path('signup/', views.SignUp),
    path('confirmation/', views.SignUp),
    path('match/', views.matches),
]

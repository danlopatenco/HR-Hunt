from django.urls import path
from core.views import (
    home,
    login_view,
    logout_view
)

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('books/', views.book_list, name='book_list'),
    path('issue/<int:book_id>/', views.issue_book, name='issue_book'),
    path('logout/', views.logout_view, name='logout'),
]

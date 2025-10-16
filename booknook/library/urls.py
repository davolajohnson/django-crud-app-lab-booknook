from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    # Books
    path('books/', views.BookList.as_view(), name='book_list'),
    path('books/new/', views.BookCreate.as_view(), name='book_create'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('books/<int:pk>/edit/', views.BookUpdate.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),

    # Notes
    path('books/<int:book_id>/notes/new/', views.NoteCreate.as_view(), name='note_create'),
    path('notes/<int:pk>/edit/', views.NoteUpdate.as_view(), name='note_update'),
    path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='note_delete'),

    # Tags
    path('tags/', views.TagListCreate.as_view(), name='tag_list_create'),
    path('tags/<int:pk>/edit/', views.TagUpdate.as_view(), name='tag_update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tag_delete'),

    # Tag attach/detach
    path('books/<int:book_id>/add_tag/<int:tag_id>/', views.add_tag_to_book, name='add_tag_to_book'),
    path('books/<int:book_id>/remove_tag/<int:tag_id>/', views.remove_tag_from_book, name='remove_tag_from_book'),
]

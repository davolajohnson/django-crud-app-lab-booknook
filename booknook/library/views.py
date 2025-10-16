from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book, Note, Tag

class HomeView(TemplateView):
    template_name = 'home.html'

# Books
class BookList(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/index.html'
    context_object_name = 'books'
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user).order_by('title')

class BookDetail(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/detail.html'
    context_object_name = 'book'
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'published_year']
    template_name = 'books/form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'published_year']
    template_name = 'books/form.html'
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/confirm_delete.html'
    success_url = reverse_lazy('library:book_list')
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

# Notes
class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['text']
    template_name = 'notes/form.html'
    def form_valid(self, form):
        book = get_object_or_404(Book, pk=self.kwargs['book_id'], user=self.request.user)
        form.instance.book = book
        return super().form_valid(form)
    def get_success_url(self):
        return self.object.book.get_absolute_url()

class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['text']
    template_name = 'notes/form.html'
    def get_queryset(self):
        return Note.objects.filter(book__user=self.request.user)
    def get_success_url(self):
        return self.object.book.get_absolute_url()

class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/confirm_delete.html'
    def get_queryset(self):
        return Note.objects.filter(book__user=self.request.user)
    def get_success_url(self):
        return self.object.book.get_absolute_url()

# Tags
class TagListCreate(LoginRequiredMixin, ListView, CreateView):
    model = Tag
    fields = ['name']
    template_name = 'tags/list_create.html'
    context_object_name = 'tags'
    success_url = reverse_lazy('library:tag_list_create')

class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ['name']
    template_name = 'tags/form.html'
    success_url = reverse_lazy('library:tag_list_create')

class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = 'tags/confirm_delete.html'
    success_url = reverse_lazy('library:tag_list_create')

@login_required
def add_tag_to_book(request, book_id, tag_id):
    book = get_object_or_404(Book, pk=book_id, user=request.user)
    tag = get_object_or_404(Tag, pk=tag_id)
    book.tags.add(tag)
    return redirect(book.get_absolute_url())

@login_required
def remove_tag_from_book(request, book_id, tag_id):
    book = get_object_or_404(Book, pk=book_id, user=request.user)
    tag = get_object_or_404(Tag, pk=tag_id)
    book.tags.remove(tag)
    return redirect(book.get_absolute_url())

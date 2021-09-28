from django.shortcuts import render
from main.models import Book, Bolg, Projects, Team
from django.views.generic import ListView


class BookList(ListView):
    model = Book
    template_name = 'main/index.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs["book"] = Book.objects.all()
        kwargs["blog"] = Bolg.objects.all()
        kwargs["pro"] = Projects.objects.all()
        kwargs["team"] = Team.objects.all()

        return super().get_context_data(**kwargs)





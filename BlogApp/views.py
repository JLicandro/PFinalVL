from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from BlogApp.models import BlogModel
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.models import User


class BlogList(ListView):

    model = BlogModel
    template_name = "Blogapp/blog_list.html"


class BlogDetail(DetailView):

    model = BlogModel
    template_name = "Blogapp/blog_detail.html"


class BlogCreate(LoginRequiredMixin, CreateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo", "subtitulo", "imagen", "cuerpo"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class BlogUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo", "subtitulo", "imagen", "cuerpo"]

    def test_func(self):
        exist = BlogModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False
        


class BlogDelete(LoginRequiredMixin,UserPassesTestMixin, DeleteView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")

    def test_func(self):
        exist = BlogModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False


class BlogLogin(LoginView):
    template_name = 'Blogapp/blog_login.html'
    next_page = reverse_lazy("blog_list")


class BlogLogout(LogoutView):
    template_name = 'Blogapp/blog_logout.html'

def photo(request):
    imagen = BlogModel.objects.imagen()
    return render("blog_list.html", {"imagen": imagen})

def index(request):
    num_blogs = BlogModel.objects.all().count()
    num_user = User.objects.all().count()

    context = {'numblogs':num_blogs, 'numuser':num_user}
    return render(request, 'BlogApp/index.html', context=context)

def autores(request):
    num_blogs = BlogModel.objects.all().count()
    num_user = User.objects.all().count()

    context = {'numblogs':num_blogs, 'numuser':num_user}
    return render(request, 'BlogApp/autores.html', context=context)
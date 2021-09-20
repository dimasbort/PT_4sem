import logging
import asyncio
from django.contrib import messages
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import *
from .async_methods import *

logger = logging.getLogger('django')


class BaseView(ListView):
    paginate_by = 5
    model = Post
    template_name = 'home.html'

    queryset = asyncio.run(get_earlier_posts('-publication_date'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = asyncio.run(get_categories())
        return context


class CreateProduct(CreateView):
    model = Post
    template_name = 'prod_new.html'
    fields = ['title', 'categories', 'price', 'info']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)


class CreateUser(CreateView):
    model = Profile
    template_name = 'profile.html'
    fields = ['phone_number', 'email', 'inform']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)


class ProductCategory(ListView):
    paginate_by = 5
    template_name = 'prod_of_category.html'

    def get_queryset(self):
        return asyncio.run(get_filter_posts_by_category(self.kwargs['slug']))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_name'] = asyncio.run(get_category_title(self.kwargs['slug']))
        return context


class ProductDetail(DetailView):
    model = Post
    template_name = 'prod_detail.html'


class UserDetail(DetailView):
    model = Profile
    template_name = 'profile_detail.html'


class ProductUpdate(UpdateView):
    model = Post
    template_name = 'prod_edit.html'
    fields = ['title', 'categories', 'price', 'info']

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            messages.error(self.request, "You can't edit this post")
            logger.error("Attempt to get an access to update function")
            raise Http404("You don't own this object")
        return obj


class ProductDelete(DeleteView):
    model = Post
    template_name = 'prod_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            messages.error(self.request, "You can't edit this post")
            logger.error("Attempt to get an access to delete function")
            raise Http404("You don't own this object")
        return obj
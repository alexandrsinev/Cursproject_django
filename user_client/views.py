from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from user_client.models import Users, Clients


class Main(ListView):
    model = Users


class FeedBackView(View):

    def post(self, request):
        name = request.post.get('name')
        phone = request.post.get('phone')
        message = request.post.get('message')
        print(f'{name} {phone} {message}')
        return render(request, 'user_client/feedback.html')

    def get(self, request):
        return render(request, 'user_client/feedback.html')


class CreateUserView(CreateView):
    model = Users
    fields = ('user_first_name', 'user_last_name', 'company_name', 'email')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save()
        return HttpResponseRedirect(
            reverse('user_client:user_profile', args=[new_user.pk]))


class UpdateUser(UpdateView):
    model = Users
    fields = ('user_first_name', 'user_last_name', 'company_name', 'email')

    def get_success_url(self):
        return reverse('user_client:user_profile', args=[self.kwargs.get('pk')])


class DeleteUser(DeleteView):
    model = Users
    success_url = reverse_lazy('user_client:main')


class UserProfile(DetailView):
    model = Users


class CreateClientView(CreateView):
    model = Clients
    fields = ('client_first_name', 'client_last_name', 'client_email', 'company_name')
    success_url = reverse_lazy('user_client:clients_list')

    def form_valid(self, form):
        if form.is_valid():
            new_client = form.save()
            new_client.slug = slugify(new_client.client_last_name)

        return super().form_valid(form)



class ClientsListView(ListView):
    model = Clients

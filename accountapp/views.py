from accountapp.forms import AccountCreationForm
from accountapp.models import NewModel
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




# Create your views here.


def hello_world(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            temp = request.POST.get('input_text')

            new_model = NewModel()
            new_model.text = temp
            new_model.save()

            return HttpResponseRedirect(reverse('accountapp:hello_world'))

        else:
            data_list = NewModel.objects.all()
            return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # reverse_lazy 를 쓰는 이유: 함수에서는 reverse를 바로 불러오면 되지만 클래스에서는 추후에 부를 때 값을 되돌려 달라는 의미의 reverse_lazy를 사용한다.
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
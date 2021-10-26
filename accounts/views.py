from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from .forms import SignUpForm

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView

"""
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
"""


class UserSignupView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return HttpResponseRedirect(self.success_url)

    """
    다른 방법
    def get_success_url(self):
        return resolve_url('home')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())
    """


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'my_account.html'
    success_url = reverse_lazy('accounts:my_account')

    def get_object(self):
        return self.request.user


class UserPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_url = reverse_lazy('accounts:password_reset_done')


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('accounts:password_change_done')


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'password_change_done.html'


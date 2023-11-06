from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from .forms import LoginForm
# Create your views here.


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True
    success_url = '/todo/'


    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})
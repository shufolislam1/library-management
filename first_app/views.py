from django.shortcuts import render,  redirect
from django.views.generic import FormView, View
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserUpdateForm
from .models import Book, Catagory

# Create your views here.

class UserRegistrationView(FormView):
    template_name =  'user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')
    
    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'user_login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    

class UserProfileUpdateView(View):
    template_name = 'profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})
    
    
def home(request, catagory_slug = None):
    books = Book.objects.all()
    if catagory_slug is not None:
        catagorys = Catagory.objects.get(slug = catagory_slug)
        books = Book.objects.filter(catagory = catagorys)
    catagorys = Catagory.objects.all()
    
    return render(request, 'home.html', {'catagorys': catagorys, 'books': books})

def all_books(request):
    books = Book.objects.all()
    catagorys = Catagory.objects.all()

    return render(request, 'home.html', {'catagorys': catagorys, 'books': books})
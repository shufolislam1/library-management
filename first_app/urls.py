from django.urls import path
from .views import UserRegistrationView,UserLoginView, UserLogoutView, UserProfileUpdateView, home, all_books
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileUpdateView.as_view(), name='profile' ),
    path('', home, name='home'),
    path('catagory/<slug:catagory_slug>/', home, name='catagory'),
    path('all_books/', all_books, name='all_books'),
    # path('details/<int:pk>/', carDetails.as_view(), name='carDetails'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
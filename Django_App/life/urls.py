from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    RegistView, HomeView, CustumLoginView, CustumLogoutView, BarcodeView, BookAddView
)

app_name = 'life'

urlpatterns = [
    path('regist/', RegistView.as_view(), name='regist'),
    path('login/', CustumLoginView.as_view(), name='login'),
    path('logout/', CustumLogoutView.as_view(), name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    path('barcode/', BarcodeView.as_view(), name='barcode'),
    path('add/', BookAddView.as_view(), name='add'),
    path('social-auth/', include('social_django.urls', namespace='social')), # googlelogin
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
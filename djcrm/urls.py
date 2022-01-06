from django.contrib import admin
from django.urls import path, include
from .views import HomepageView

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('', include('leads.urls', namespace='leads')),
    path('admin/', admin.site.urls),
]

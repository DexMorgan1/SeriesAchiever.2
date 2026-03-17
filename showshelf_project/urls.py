from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # This is the secret door to your admin panel
    path('admin/', admin.site.urls),
    
    # This sends all normal visitors to your TV show tracker
    path('', include('tracker.urls')),
]

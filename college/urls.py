from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('join/', include('admissions.urls')),
    path('dept/', include('departments.urls')),
    path('tandp/', include('placements.urls')),
    path('other/', include('other_areas.urls'))
]

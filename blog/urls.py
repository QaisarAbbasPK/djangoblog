
from django.contrib import admin
from django.urls import path, include


admin.site.site_header = 'QA IT Agency'                    # default: "Django Administration"
admin.site.index_title = 'QA IT Agency'                 # default: "Site administration"
admin.site.site_title = 'QA IT Agency' # default: "Django site admin"




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('deshboard.urls')),
]

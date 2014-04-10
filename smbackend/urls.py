from django.conf.urls import patterns, include, url
from services.api import all_resources
from rest_framework import routers

# from django.contrib import admin
# admin.autodiscover()

router = routers.DefaultRouter()
for res_name, view_set in all_resources.items():
    router.register(res_name, view_set)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smbackend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^', include(v1_api.urls)),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/', include(router.urls))
)

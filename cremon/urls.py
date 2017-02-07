from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from registration.backends.default.views import RegistrationView
from myproject import views, models


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cremon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('myproject.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/logout/$', 'accounts.views.logout_view', name='auth_logout'),
    url(r'^accounts/login/$', 'accounts.views.login_view', name='auth_login'),
    #url(r'^accounts/register/$', 'accounts.views.registration_view', name='auth_register'),
    #url(r'^accounts/password/reset/$', 'accounts.views.password_reset', name='password_reset'),
    url(r'^accounts/address/add/$', 'accounts.views.add_user_address', name='add_user_address'),
    url(r'^ajax/add_user_address/$', 'accounts.views.add_user_address', name='ajax_add_user_address'),
    url(r'^accounts/activate/(?P<activation_key>\w+)/$', 'accounts.views.activation_view', name='activation_view'),
    url(r'^accounts/password/reset/$', include('registration.backends.default.urls')),

)


if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )

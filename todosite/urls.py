from django.conf.urls import patterns, include, url
from todo import views
from rest_framework import viewsets, routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'todos', views.TodoViewSet)

urlpatterns = patterns('',

    # For admin
    url(r'^data/', include(router.urls)),

    # Registration of new users
    url(r'^registration/$', views.RegistrationView.as_view()),

    # Todos endpoint
    url(r'^user/todos/$', views.TodosView.as_view()),
    url(r'^user/$', views.UserView.as_view()),
    url(r'^user/todos/(?P<todo_id>[0-9]*)$', views.TodosView.as_view()),

    # API authentification
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)


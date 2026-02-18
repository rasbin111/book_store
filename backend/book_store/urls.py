from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql/v1/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

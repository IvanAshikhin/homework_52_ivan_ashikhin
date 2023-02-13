from django.urls import path


from webapp.views import base

urlpatterns = [
    path("", base.index_view),
]


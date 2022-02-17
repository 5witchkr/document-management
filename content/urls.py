from django.conf.urls import url
from django.urls import path
from .views import Main, CreateDoc, Detail, AllPrint, Delete

urlpatterns = [
    path('main<int:page>', Main.as_view(), name='main'),
    path('create', CreateDoc.as_view(), name='create'),
    path('detail<int:titleNum>', Detail.as_view(), name='detail'),
    path('allprint', AllPrint.as_view(),name='allprint'),
    path('delete', Delete.as_view(),name='delete')
]
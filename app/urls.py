from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('sniffScript.js',views.serveScript),
    path('cf.js',views.serveCf),
    path('getDates',views.getDates),
    path('getID',views.getID),
    path('track',views.track),
    path('sniff',views.sniff)
]
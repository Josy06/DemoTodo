# This is Todoapp urls

from django.urls import path
from . import views

urlpatterns = [

    path('', views.open, name='open'),
    # path('details/',views.details,name='details') this path was used to display details at details.html (a new page)
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbview/',views.tasklistview.as_view(),name='cbview'),
    path('cbdetail/<int:pk>/',views.taskdetails.as_view(),name='cbdetail')
]

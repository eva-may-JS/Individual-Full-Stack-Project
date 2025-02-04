from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventList.as_view(), name='events'),
    path('<slug:slug>/', views.event_detail, name='event_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]

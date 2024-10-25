from django.urls import path
from .views import LinkListView, LinkCreateView,LinkUbdate,Linkdelet,profile_view

urlpatterns = [
    path('', LinkListView.as_view(), name='Link_View'),
    path('link/create/', LinkCreateView.as_view(), name='Create_View'),
    path('link/update/<int:pk>/', LinkUbdate.as_view(), name='update-view'),
    path('link/delet/<int:pk>/', Linkdelet.as_view(), name='delet-view'),
    path('<slug:profile_slug>/', profile_view, name="profile"),
]


from django.urls import path
from .views import cloth_view, update_cloth, about_cloth, delete_cloth

urlpatterns = [
    path('clothes/', cloth_view,name='clothes'),
    path('<int:pk>/about-cloth/',about_cloth,name='about-cloth'),
    path('update/<int:pk>/',update_cloth,name='update'),
    path('delete/<int:pk>/',delete_cloth,name='delete')
]
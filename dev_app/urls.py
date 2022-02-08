from django.urls import path  
from dev_app import views  

urlpatterns = [
	path('',views.help,name='help'),
	path('social/',views.social,name='social'),
	path('blog/',views.blog,name='blog'),
	path('portfolio/',views.portfolio,name='portfolio'),
	path('store/',views.store,name='store'),
]
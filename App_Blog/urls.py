from django.urls import path, re_path


from App_Blog import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<slug:slug>/', views.blog_details, name='blog_details')
    #re_path(r'^details/(?P<slug>[\w’\-"]+)/$', views.blog_details, name='blog_details')
]

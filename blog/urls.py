from django.conf.urls import url
from blog import views


app_name = 'blog'

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name="post_list"),
    url(r'^post/draft/$',views.PostListDraftView.as_view(),name="post_list_draft"),
    url(r'^post/new/$',views.CreatePostView.as_view(),name="create_post"),
    url(r'^post/detail/(?P<pk>\d+)$',views.PostDetailView.as_view(),name="detail_post"),
    url(r'^post/update/(?P<pk>\d+)$',views.PostUpdateView.as_view(),name="update_post"),
    url(r'^post/delete/(?P<pk>\d+)$',views.PostDeleteView.as_view(),name="delete_post"),
    url(r'^post/publish(?P<pk>\d+)$',views.post_publish,name="publish_post"),
]
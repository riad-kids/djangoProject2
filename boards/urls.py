from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'boards'

urlpatterns = [
    path('boards/<int:pk>/', views.TopicListView.as_view(), name='board_topics'),
    path('boards/<int:pk>/topics/<int:topic_pk>/', views.PostListView.as_view(), name='topic_posts'),
    path('boards/<int:pk>/new/', login_required(views.TopicCreateView.as_view()), name='new_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>/reply/',
         login_required(views.ReplyTopicView.as_view()),
         name='reply_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/',
         views.PostUpdateView.as_view(),
         name='edit_post'),
]

__author__ = 'yang'
__date__ = '2019/9/5 20:24'
from django.urls import path
from django.conf.urls import url, include

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView, VideoPlayView


urlpatterns = [
    # 课程列表页
    path('list/', CourseListView.as_view(), name="course_list"),

    # 课程详情页
    # path('detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),
    path('detail/<int:course_id>/', CourseDetailView.as_view(), name="course_detail"),


    # path('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name="course_info"),
    path('info/<int:course_id>/', CourseInfoView.as_view(), name="course_info"),

    # 课程评论
    # path('comments/(?P<course_id>\d+)/', CommentsView.as_view(), name="course_comments"),
    path('comments/<int:course_id>/', CommentsView.as_view(), name="course_comments"),

    # 添加课程评论
    path('add_comment/', AddCommentsView.as_view(), name="add_comment"),

    # 播放
    # path('video/(?P<video_id>\d+)/', VideoPlayView.as_view(), name="video_play"),
    path('video/<int:course_id>/', VideoPlayView.as_view(), name="video_play"),
]

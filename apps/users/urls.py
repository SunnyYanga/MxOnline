__author__ = 'yang'
__date__ = '2019/9/20 11:51'
from django.urls import path

from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView, MyCourseView
from .views import MyFavOrgView, MyFavTeacherView, MyFavCourseView, MyMessageView

urlpatterns = [
    # 用戶信息
    path('info/', UserInfoView.as_view(), name="user_info"),
    # 用戶頭像上傳
    path('image/upload/', UploadImageView.as_view(), name="image_upload"),
    # 用戶個人中心修改密碼
    path('update/pwd/', UpdatePwdView.as_view(), name="update_pwd"),
    # 發送郵箱驗證碼
    path('sendemail_code/', SendEmailCodeView.as_view(), name="sendemail_code"),
    # 修改郵箱
    path('update_email/', UpdateEmailView.as_view(), name="update_email"),
    # 我的課程
    path('my_course/', MyCourseView.as_view(), name="my_course"),
    # 我收藏的課程機構
    path('myfav/org/', MyFavOrgView.as_view(), name="myfav_org"),
    # 我收藏的授課講師
    path('myfav/teacher/', MyFavTeacherView.as_view(), name="myfav_teacher"),
    # 我收藏的公開課
    path('myfav/course/', MyFavCourseView.as_view(), name="myfav_course"),
    # 我的消息
    path('mymessage/', MyMessageView.as_view(), name="mymessage"),
]

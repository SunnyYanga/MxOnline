"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
# from django.urls import include, path
from django.urls import path
from django.views.generic import TemplateView
from django.views.static import serve
from DjangoUeditor.models import UEditorField
import xadmin

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogOutView
from users.views import IndexView
from MxOnline.settings import MEDIA_ROOT
# from MxOnline.settings import STATIC_ROOT

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogOutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('forget/', ForgetPwdView.as_view(), name="forget_pwd"),
    path('modify_pwd/', ModifyPwdView.as_view(), name="modify_pwd"),
    # 课程机构url配置
    path('org/', include(('organization.urls', 'organization'), namespace="org")),
    # url(r'^org/', include(('organization.urls', 'organization'), namespace="org")),

    # 课程相关url配置
    path('course/', include(('courses.urls', 'courses'), namespace="course")),

    path('users/', include(('users.urls', 'users'), namespace="users")),

    # 课程机构url配置
    # url(r'^org/', include(('organization.urls', 'organization'), namespace="org")),

    # path('captcha/', include('captcha.urls'))
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    # path('active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active")
    # url('^$', TemplateView.as_view(template_name="index.html"), name="index")

    # 富文本相关url
    url(r'^ueditor/', include(('DjangoUeditor.urls', 'ueditor'), namespace="ueditor")),
]

# 全局404頁面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'

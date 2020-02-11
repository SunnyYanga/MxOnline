from datetime import datetime
from django.db import models

from organization.models import CourseOrg, Teacher
from DjangoUeditor.models import UEditorField

# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="课程机构", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name="课程名")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="讲师", null=True, blank=True)
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    # detail = models.TextField(verbose_name="课程详情")
    detail = UEditorField(verbose_name=u"课程详情", width=600, height=300, imagePath="courses/ueditor/",
                 filePath="courses/ueditor/", default='')
    degree = models.CharField(verbose_name="难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="封面图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    category = models.CharField(default='后端开发', max_length=20, verbose_name="课程类别")
    tag = models.CharField(default='', verbose_name="课程标签", max_length=10)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    you_need_know = models.CharField(default='后端开发', max_length=300, verbose_name="课程须知")
    teacher_tell = models.CharField(default='后端开发', max_length=300, verbose_name="老师告诉你")
    is_banner = models.BooleanField(default=False, verbose_name="是否輪播")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        # 获取课程章节数
        return self.lesson_set.all().count()
    get_zj_nums.short_description = "章節數"

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.baidu.com'>跳轉</a>")
    go_to.short_description = "章節數"

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        # 获取课程所有章节
        return self.lesson_set.all()

    def get_course_course_resource(self):
        return self.courseresource_set.all()

    def __str__(self):
        return self.name


class BannerCourse(Course):
    class Meta:
        verbose_name = "輪播課程"
        verbose_name_plural = verbose_name
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    name = models.CharField(max_length=50, verbose_name="章节名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def get_lesson_video(self):
        # 获取章节视频
        return self.video_set.all()

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="章节")
    name = models.CharField(max_length=50, verbose_name="视频名称")
    url = models.CharField(max_length=200, default="", verbose_name="访问地址")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    name = models.CharField(max_length=50, verbose_name="名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
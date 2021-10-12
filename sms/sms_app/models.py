from django.db import models

# Create your models here.
class AdminHOD(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    created_at = models.CharField(auto_new_add = True)
    updated_at = models.CharField(auto_new_add = True)
    objects = models.manager()


class Stuffs(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    address = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    object = models.manager ( )


class Courses(models.Model):
    id = models.AutoField(primary_key = True)
    course_name = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add=True)
    object = models.manager ( )


class Subjects(models.Model):
    id = models.AutoField(primary_key = True)
    subject_name = models.CharField(max_length=225)
    course_id = models.ForeignKey(Courses, on_delete= models.CASCADE)
    staff_id = models.ForeignKey(Stuffs, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    object = models.manager ( )


class Students(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)
    profile_pic = models.FileField()
    address = models.TextField()
    object = models.manager()
    course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Attendance(models.Model):
    id = models.AutoField(primary_key = True)
    subject_id = models.ForeignKey(Subjects)
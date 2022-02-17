from django.db import models

# Create your models here.

class Doc(models.Model):
    titleNum = models.IntegerField(unique=True)  # 유니크(관리코드)
    type = models.CharField(max_length=10)#구분
    depart = models.CharField(max_length=20)#상세업무명
    date = models.DateField(auto_now=True)#접수일자
    title = models.CharField(max_length=60)
    docNum = models.IntegerField()##문서구분번호
    docSubject = models.CharField(max_length=80)##문서글내용제목
    adminName = models.CharField(max_length=10)#결재권자
    name = models.CharField(max_length=10)#기안자
    sendName = models.CharField(max_length=40)#수신자/발신자
    elec = models.BooleanField()#문서구분2
    openDoc = models.BooleanField()#공개여부 불리언타입
    other = models.TextField(null=True)#비고
    file = models.FileField(null=True)
    yearNum = models.IntegerField()
    ##Todo 첨부파일


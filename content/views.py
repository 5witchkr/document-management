from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import Doc
from rest_framework.response import Response
from django.db.models import Max
from django.core.paginator import Paginator


# Create your views here.

class Main(APIView):
    def get(self, request, page):

        Docs = Doc.objects.all().order_by('-id')

        ##TODO 페이징처리
        pageNumber = page
        if page > 0:
            prepage = page-1
        else:
            prepage = 0
        nextpage = page+1

        isLastPage = True
        if pageNumber is not None and pageNumber >= 0:
            if Docs.count() <= 10:
                pass
            elif Docs.count() <= (1 + pageNumber) * 10:
                Docs = Docs[pageNumber * 10:]
            else:
                isLastPage = False
                Docs = Docs[pageNumber * 10:(1 + pageNumber) * 10]
        else:
            pass

        DocList = []
        for i in Docs:
            DocList.append(dict(
                docID=i.id,
                title=i.title,
                docSubject=i.docSubject,
                titleNum=i.titleNum
            ))

        return render(request, "content/main.html", context=dict(DocList=DocList, isLastPage=isLastPage, page=page, prepage=prepage, nextpage=nextpage))


class CreateDoc(APIView):
    def get(self, request):
        return render(request, "content/create.html")

    def post(self, request):

        obj = Doc.objects.aggregate(titleNum=Max('titleNum'))
        obj2 = Doc.objects.aggregate(yearNum=Max('yearNum'))
        titleNum = obj['titleNum']+1
        yearNum = obj2['yearNum'] + 1
        # titleNum = 20227777
        # yearNum = 50
        type = request.data.get('type')
        depart = request.data.get('depart')
        title = "미국골프지도자연맹-"+str(yearNum)
        docNum = request.data.get('docNum')
        docSubject = request.data.get('docSubject')
        adminName = request.data.get('adminName')
        name = request.data.get('name')
        sendName = request.data.get('sendName')
        elec = request.data.get('elec')
        openDoc = request.data.get('openDoc')
        other = request.data.get('other')


        Doc.objects.create(titleNum=titleNum,
                           type=type,
                           depart=depart,
                           title=title,
                           docNum=docNum,
                           docSubject=docSubject,
                           adminName=adminName,
                           name=name,
                           sendName=sendName,
                           elec=elec,
                           openDoc=openDoc,
                           other=other,
                           yearNum=yearNum
                           )

        return Response(status=200, data=dict(resultCode=0, resultMsg="success"))



class Detail(APIView):
    def get(self, request, titleNum):

        detailDoc = Doc.objects.filter(titleNum=titleNum)

        DocList = []
        for i in detailDoc:
            DocList.append(dict(
                docID=i.id,
                titleNum=i.titleNum,
                type=i.type,
                depart=i.depart,
                date=i.date,
                title=i.title,
                docNum=i.docNum,
                docSubject=i.docSubject,
                adminName=i.adminName,
                name=i.name,
                sendName=i.sendName,
                elec=i.elec,
                openDoc=i.openDoc,
                other=i.other,
            ))

        return render(request, "content/detail.html", context=dict(DocList=DocList))




class AllPrint(APIView):
    def get(self, request):
        return render(request, "content/allprint.html")

    def post(self, request):
        startdate = request.POST.get('startdate')
        enddate = request.data.get("enddate")
        allDoc = Doc.objects.filter(date__range=[startdate, enddate])
        allDocList = []
        for i in allDoc:
            allDocList.append(dict(
                titleNum=i.titleNum,
                yearNum=i.yearNum,
                date=i.date,
                title=i.title,
                docSubject=i.docSubject,
                other=i.other,
            ))
        return render(request, "content/allprint.html", context=dict(allDocList=allDocList))


class Delete(APIView):
    def post(self, request):
        DocId = request.data.get('DocId', '')
        doc = Doc.objects.get(id=DocId)
        if doc:
            doc.delete()
            return Response(status=200, data=dict(resultCode=0, resultMsg="success"))
        else:
            print("err")

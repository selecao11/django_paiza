from django.shortcuts import render
from django.views.generic import TemplateView
from .C039 import C039
from .C086 import C086
from .C081 import C081
from .C049 import C049

class IndexViewC039(TemplateView):
# Create your views here.
    
    def get(self,request):
        params = {"message":"クラスベースView：Get処理"}
        return render(request,"paizac039.html",params)

    def post(self,request):
        params = {'in_data': 0,'add_r': 0,}
        params['in_data'] = request.POST['in_data']
        c039 = C039()
        r = c039.c036_start(params['in_data'])
        params['add_r'] = r['total']
        return render(request,"paizac039.html",params)

class IndexViewC086(TemplateView):
    def get(self,request):
        params = {"message":"クラスベースView：Get処理"}
        return render(request,"paizac086.html",params)

    def post(self,request):
        params = {'in_data': 0,'add_r': 0,'msg': ""}
        params['in_data'] = request.POST['in_data']
        c086 = C086()
        r = c086.c086_start(params['in_data'])
        params['msg'] = r['e']
        params['add_r'] = r['anser']
        return render(request,"paizac086.html",params)

import io
import csv
class IndexViewC081(TemplateView):
    def get(self,request):
        params = {"message":"クラスベースView：Get処理"}
        return render(request,"paizac081.html",params)

    def post(self,request):
        params = {'file_name': "",'add_r': 0,'msg': "正常におわりました。"}
        params['file_name'] = request.FILES['file_name'] 
#
        data = io.TextIOWrapper(request.FILES['file_name'].file, encoding='utf-8')
        params['csv_data'] = csv.reader(data)
        csv_data = []
        for e in params['csv_data']:
            csv_data.append(e)
            print('1回目 ='+ str(e))
#       params['csv_data'] = csv_data
        c081 = C081()
        r = c081.c081_start(csv_data)
        in_data=  r['in_data']
        print('2_1回目')
        print("r['count'] " + str(r['count']))
        for e in in_data:
            print('2回目 ='+ str(e))
        if r['Error'] == ValueError:
            params['msg']=e
#        params['msg'] = params['file_name']
        params['add_r'] = r['count']
        params['lists'] = r['in_data']
        return render(request,"paizac081.html",params)


class IndexViewC049(TemplateView):
    def get(self,request):
        params = {"message":"クラスベースView：Get処理"}
        return render(request,"paizac049.html",params)

    def post(self,request):
        params = {'file_name': "",'add_r': 0,'msg': "異常終了です。"}
        params['file_name'] = request.FILES['file_name'] 
        data = io.TextIOWrapper(request.FILES['file_name'].file, encoding='utf-8')
        csv_content = csv.reader(data)
        subject_data = []
        for d in csv_content:
            subject_data.append(d)
            print('csv_content = '+ str(d))
        c049 = C049()
        r = c049.c049_start(subject_data)
        in_data=  r['subject_data']
        for e in in_data:
            print('2回目 ='+ str(e))
        if r['Error'] == None:
            params['msg']='正常終了です'
        params['move_total'] = r['move_total']
        params['lists'] = r['subject_data']
        return render(request,"paizac049.html",params)

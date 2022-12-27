import unicodedata
import re

class C049():

    def c049_indata_int_validation(self,d):
        if isinstance(d,float):#少数点判定
            d = int(d)
        if int(d)>=1001 or int(d)<=0:#範囲判定
            raise ValueError('対象範囲を超えています 1以上1000以下')
        return int(d)

    def c049_indata_str_validation(self,d):
        if len(d) <= 0:
            raise ValueError('未入力です。')
        if d.isspace():#半角判定
            raise ValueError('全角空白です')
        d = d.strip()
        if len(re.findall(r"[A-Z]", d)) >= 1:
            raise ValueError('数字ではありません。')
        if len(re.findall(r"[a-z]", d)) >= 1:
            raise ValueError('数字ではありません。')
        if len(re.findall(r"[-\\.,/\"'>*()&;:]", d)) >= 1:
            raise ValueError('特殊文字か混入しています。')
        w = list(d)
        for s  in w:
            if unicodedata.east_asian_width(s) =="W":
                raise ValueError('適切な半角文字ではありません。')
            if unicodedata.east_asian_width(s) =="F":
                raise ValueError('適切な半角文字ではありません。')
        if int(d)>=1001 or int(d)<=0:
            raise ValueError('対象範囲を超えています 1以上1000以下')
        return int(d)

    def Floor_mobe_total(self,d,data):#エレベータの移動距離産出
        if d >= data['position']:#移動階が上の場合
            k = d - data['position']
        else:#移動階が下の場合
            k = data['position'] - d 
        data['move_total'] += k
        data['position'] = d
        return data
        
    def c049_validation(self,data,in_data):
        subject_data = []#チェック済入力データ
        print('start c049_validation')
        for dl in in_data:
            print('c049_validation d = ' + str(dl))
            d = dl[0]
            try:
                s =str(d) 
                if s.isalpha():
                    d = self.c049_indata_str_validation(d)
                else:
                    d = self.c049_indata_int_validation(d)
            except ValueError as e:
                data['Error']= ValueError   
                data['e'] = e
            subject_data.append(d)
        data['subject_data']=subject_data
        return data

    def c049_init(self):
        data = {}
        total_init = 0
        start_position = 1
        data['move_total'] = total_init
        data['subject_data'] = None
        data['position'] = start_position
        data['Error'] = None
        data['e']=""
        return data
            
    def c049_start(c049,subject_data):
        print('c049_start')
        in_data = []
        in_data = subject_data
        data = c049.c049_init()
        data = c049.c049_validation(data,in_data)
        for d in data['subject_data']:
            print('d = ' + str(d))
            if data['Error']:
                print(data['e'])
                return data 
            data = c049.Floor_mobe_total(d,data)
        return data
        

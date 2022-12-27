import sys
import re

class C039():

    def data_add(self,data):
        anser = data["anser"]
        total = 0
        for a in anser:
            total += a
        data["total"] = total
        return data

    def data_keta_count(self,data):
        ds =data['d']
        anser=[]
        for index,d in enumerate(ds):
            k10 = d.count('<')
            k1 = d.count('/')
            w = 0
            if k10 >=1:
                w = k10 * 10
            if k1 >=1:
                w = w + k1 * 1
            anser.append(w)
        data["anser"]=anser    
        return data 
    
    def data_split(self,in_data,data):
        d =[]
        d = in_data.split('+')
        data['d'] = d
        return data

    def data_check(self,in_data):
        err_data = re.findall("[^+/<]", in_data)
        if err_data != None:
            err_count = len(err_data)
        else:
            err_count = (0,0)
        plass_count_min = 2
        plass_count = in_data.count('+')
        try:
            if err_count >= 1:
                raise ValueError('正しい値が入っていません')
            if plass_count >= plass_count_min:
                raise Exception('+ が多い')
        except ValueError as e:
            raise           # 呼び出し元に送信
        except Exception as e:
            raise           # 呼び出し元に送信

    def c036_start(self,in_data):
        data ={}
        data['e']=None
        try:
            self.data_check(in_data)
            data = self.data_split(in_data,data)
            data = self.data_keta_count(data)
            data = self.data_add(data)
        except ValueError as e:
            print('ValueError ng')
            print(e)
            raise           # 呼び出し元に送信
        except Exception as e:
            print('Exception ng')
            raise           # 呼び出し元に送信
#            data['e'] = e            
#            return data
        return  data

    # def test_c039_01(self,operand_1):
    #     with self.assertRaises(Exception, msg=anser):
    #             c039.c036_start(operand_1)

operand_1 = '<'
#operand_2 = "<"
#in_data= operand_1 + "+" + operand_2
in_data=operand_1
c039 = C039()
data = c039.c036_start(in_data)
if data["e"]!=None:
    print(data['e'])
else:
    print(data['total'])

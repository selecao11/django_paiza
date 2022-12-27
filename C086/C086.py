import sys
import re

class C086():

    def data_vowel_del(self,in_data,data):
        del_vowel_data = re.findall("[^aiueo]", in_data)
        r = "".join(del_vowel_data)
        data['anser'] = r  
        return data
    
    def data_check(self,in_data):
        if len(in_data) <= 0:
                raise ValueError('データが入力されていません')                
        if in_data in(' '):
                raise ValueError('正しい文字が入っていません')
        if in_data in('　'):
                raise ValueError('正しい文字が入っていません')
        if in_data.isalpha() == False:
                raise ValueError('正しい文字が入っていません')
        if len(in_data) <= 4 or len(in_data) >= 21:
                raise ValueError('文字の長さが適切ではありません')
        return in_data

    def c086_start(self,in_data):
        data ={}
        data['e']=""
        try:
            self.data_check(in_data)
        except ValueError as e:
            data['anser'] = ''
            data["e"]=e
            return data
        except Exception as e:
            raise           # 呼び出し元に送信
        data = self.data_vowel_del(in_data,data)
        return  data

#in_data = '1'
in_data = 'Trv'
c086 = C086()
data = c086.c086_start(in_data)
if data["e"]!=None:
    print(data['e'])
else:
    print(data['anser'])

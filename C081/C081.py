import unicodedata

class C081():

    def RL_Non_hit(self,d,iRL,data):
        w = []
        w.append(d[1])
        data[iRL]=w
        del w
        return data            

    def RL_Duplicate_check(self,d,iRL,data):
        dw = data[iRL]
        if d[1] in dw :
            return True

    def RL_hit(self,d,iRL,data):
        if self.RL_Duplicate_check(d,iRL,data):
            return data 
        w = data[iRL]
        w.append(d[1])
        data['count']+=1 #そろった合計                
        del data[iRL]
        del w
        return data 
    
    def dict_index_hit(self,d,data):
        iRL = d[0]
        Non_iRL = data.get(iRL)
        if Non_iRL == None:
            self.RL_Non_hit(d,iRL,data)
        else:
            self.RL_hit(d,iRL,data)
        return data

    def c081_indata_validation(self,d):
        if d[0]=="" or d[1]=="": #空白
            raise ValueError('文字が入力されていません')
        if d[1]=="": #空白
            raise ValueError('ＲもしくはＬ文字が入力されていません')
        if d[0].isalpha() == False or d[1].isalpha() == False: #英字以外
            raise ValueError('適切な文字ではありません。')
        if d[0].isupper() ==False or d[1].isupper() ==False: #大文字以外
            raise ValueError('適切な文字ではありません。')
        if len(d[0])>=2 or len(d[1])>=2:#連続文字
            raise ValueError('適切な文字ではありません。')
        if  unicodedata.east_asian_width(d[0]) == 'F' or \
            unicodedata.east_asian_width(d[1]) == 'F':#全角以外
            raise ValueError('適切な文字ではありません。')
        
    def c081_start(c081,in_data):
        data = {}
        data['count'] = 0
        data['in_data'] = in_data
        data['Error'] = None
        for d in in_data:
            try:
                c081.c081_indata_validation(d)
            except ValueError as e:
                data['Error']= ValueError   
                data['e'] = e
                return data
#                raise           # 呼び出し元に送信
            data = c081.dict_index_hit(d,data)
        return data
        
# c081=C081()
# data = c081.dict_index_hit()
# print(data['count'])

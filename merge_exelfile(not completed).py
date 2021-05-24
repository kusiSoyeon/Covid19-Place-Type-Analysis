import pandas as pd  
import sys

#엑셀 파일 이름 입력

excel_names = ['file.xlsx', 'file2.xlsx', 'file3.xlsx']  
excels = [pd.ExcelFile(name) for name in excel_names]  
frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]  
frames[1:] = [df[1:] for df in frames[1:]]  
combined = pd.concat(frames)

#파일저장

combined.to\_excel("C:/Users/KUSHY/장소유형.xlsx", header=False, index=False)
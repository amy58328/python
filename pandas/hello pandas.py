import pandas as pd 


# 準備傳入 DataFrame 的資料
data_1 = {
    'name': ['王小郭', '張小華', '廖丁丁', '丁小光'],
    'email': ['min@gmail.com', 'hchang@gmail.com', 'laioding@gmail.com', 'hsulight@gmail.com'],
    'grades': [60, 77, 92, 43]
}

data_2 = {
    'name': ['王小郭', '張小華', '廖丁丁', '丁小光'],
    'age': [19, 20, 32, 43]
}

# 建立 DataFrame 物件
student_df_1 = pd.DataFrame(data_1)
student_df_2 = pd.DataFrame(data_2)


print(student_df_1,end="\n=============\n\n")
print(student_df_2,end="\n=============\n\n")


student_fg_3 = pd.merge(student_df_1, student_df_2)

# merge結果
print(student_fg_3,end="\n=============\n\n")

# 輸出特定行列值
print(student_fg_3.loc[:,["name","age"]],end="\n=============\n\n")
print(student_fg_3.iloc[:,[0,2]],end="\n=============\n\n")
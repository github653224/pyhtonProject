# urls = ["page1", "page2" ...]

urls  = [f"page{i}" for i in range(0, 10)]
print(urls)

temp_dic = dict()
for index, j in enumerate(urls):
    print(index, j)
    temp_dic[index] = j
print(temp_dic)

文件名=input("请输入文件名（不含拓展名）：")
拓展名=input("请输入拓展名（不含点）：")
if ((拓展名=="txt") or (拓展名=="")):
	输入文件=open(文件名+".txt","r",encoding="shift_JIS")
	输出文件=open(文件名+"_utf-8.txt","w",encoding="utf-8")
else:
	输入文件=open(文件名+"."+拓展名,"r",encoding="shift_JIS")
	输出文件=open(文件名+"."+拓展名+"_utf-8.txt","w",encoding="utf-8")
输出文件.write(输入文件.read())
输出文件.close()
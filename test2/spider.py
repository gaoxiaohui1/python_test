#coding:utf-8
import urllib.request
import re
from urllib import parse

# 获取网页字符串
def get_html(page):
	url='http://search.sina.com.cn/?q=%C3%C0%B9%FA&c=blog&from=index&col=&range=&source=&country=&size=&match=&a=&dpc=1&page='+str(page)
	html = urllib.request.urlopen(url)
	htmlBytes = html.read()
	htmlStr=htmlBytes.decode('gb2312','replace')
	print ('原始长度：',len(htmlStr))
	return htmlStr
# 写入txt文件
def write_file(data):
	file=open('html.txt','a',encoding='utf-8')
	file.write("\r")
	# file.write("\n")
	file.write(data)
	file.close()
# 获取主内容	
def get_content(htmlStr):
	# 内容分割的标签
	str = '<div class="result-boxes">'
	content = htmlStr.partition(str)[2]
	print ('第一次截取后长度：',len(content))
	str = '<div class="filterzz">'
	content = content.partition(str)[0]
	print ('第二次截取后长度：',len(content))
	content=content.replace("\r","")
	print ('替换r后长度：',len(content))
	content=content.replace("\n","")
	print ('替换n后长度：',len(content))
	content=content.replace(" ","")
	print ('替换空格后长度：',len(content))
	content=content.replace("	","")
	print ('替换空格后长度：',len(content))
	content=content.strip()
	print ('strip后长度：',len(content))
	content=content.replace('<spanstyle="color:#C03">美国</span>','美国')
	print ('替换美国后长度：',len(content))
	return content # 得到网页的内容
# 获取单条数据
def get_datalist(htmlStr):
	reg = r'<!--0422博主新模板--><divclass="box-resultclearfix"data-sudaclick=(.+?)</div><!--0422博主新模板-->'#正则表达式
	reg_str = re.compile(reg)#编译一下，运行更快
	matchList = reg_str.findall(htmlStr)#进行匹配
	# for match in matchList:
		# print (match)
	return matchList
	print ('时间 end----------------------')
# 获取时间
def get_time(htmlStr):
	# print ('获取时间时长度：',len(htmlStr))
	# print (type(htmlStr))
	reg = r'<spanclass="fgray_time">(.+?)</span>'#正则表达式
	reg_str = re.compile(reg)#编译一下，运行更快
	matchList = reg_str.findall(htmlStr)#进行匹配
	# for match in matchList:
		# print (match)
	return matchList
	print ('时间 end----------------------')
# 获取标题		
def get_title(htmlStr):
	# <ahref="http://blog.sina.com.cn/u/edc55d8f0102yop5"target="_blank">四年之后美国终于造出和同款反隐身雷达</a> 
	reg = r'<h2class=\'r-info-blog-tit\'>(.+?)</h2>'#正则表达式
	reg_str = re.compile(reg)#编译一下，运行更快
	matchList = reg_str.findall(htmlStr)#进行匹配
	reg=r'target="_blank">(.+?)</a>'
	reg_str = re.compile(reg)#编译一下，运行更快
	list=[]
	for match in matchList:
		newMatchList = reg_str.findall(match)
		list.append(newMatchList[0])
		# print(newMatchList[0])
	return list
	print ('标题 end----------------------')
# 获取标题链接	
def get_titlelink(htmlStr):
	reg = r'<h2class=\'r-info-blog-tit\'><ahref="(.+?)"target="_blank">'#正则表达式
	reg_str = re.compile(reg)#编译一下，运行更快
	matchList = reg_str.findall(htmlStr)#进行匹配
	# for match in matchList:
		# print (match)
	return matchList
	print ('标题链接 end----------------------')
# 获取内容	
def get_bref(htmlStr):
	reg = r'<pclass="content">(.+?)</p>'#正则表达式
	reg_str = re.compile(reg)#编译一下，运行更快
	matchList = reg_str.findall(htmlStr)#进行匹配
	# for match in matchList:
		# print (match)
	return matchList
	print ('内容 end----------------------')
# 获取博主	
def get_author(htmlStr):
	reg = r'class=\'rib-author\'>(.+?)</a>'#正则表达式
	reg_str = re.compile(reg)#编译一下，运行更快
	matchList = reg_str.findall(htmlStr)#进行匹配
	# for match in matchList:
		# print (match)
	return matchList
	print ('博主 end----------------------')
# 获取博主链接
def get_authorlink(htmlStr):
	reg = r'博主：</span><ahref="(.+?)"target=\'_blank\'class=\'rib-author\'>'#正则表达式
	reg_str = re.compile(reg)#编译一下，运行更快
	matchList = reg_str.findall(htmlStr)#进行匹配
	# for match in matchList:
		# print (match)
	return matchList
	print ('博主链接 end----------------------')
def get_bypage(page):
	htmlStr=get_html(page)
	htmlStr=get_content(htmlStr)
	# write_file(htmlStr)
	datahtmllist=get_datalist(htmlStr)
	for datastr in datahtmllist:
		timelist=get_time(datastr)
		if len(timelist)>0:
			write_file('时间：'+timelist[0][0:10]+' '+timelist[0][10:])
		else:
			write_file('时间：')
		titlelist=get_title(datastr)
		if len(titlelist)>0:
			write_file('标题：'+titlelist[0])
		else:
			write_file('标题：')
		titlelinklist=get_titlelink(datastr)
		if len(titlelinklist)>0:
			write_file('标题链接：'+titlelinklist[0])
		else:
			write_file('标题链接：')
		breflist=get_bref(datastr)
		if len(breflist)>0:
			write_file('简介：'+breflist[0])
		else:
			write_file('简介：')
		authorlist=get_author(datastr)
		if len(authorlist)>0:
			write_file('博主：'+authorlist[0])
		else:
			write_file('博主：')
		authorlinklist=get_authorlink(datastr)
		if len(authorlinklist)>0:
			write_file('博主链接：'+authorlinklist[0])
		else:
			write_file('博主链接：')
		write_file('-----------------------------------------------我是分割线-------------------------------------------------')
		write_file('\n')
		print('处理了一条数据')

keyword=input('输入要搜索的关键词：')
print(keyword,parse.quote_plus(keyword))		
pagestart=input("输入要获取的开始页码：")
pageend=input("输入要获取的结束页码：")		
page=int(pagestart)
while (page<int(pageend)+1):
	msg='第'+str(page)+'页-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
	write_file(msg)
	get_bypage(page)
	print('第'+str(page)+'页')
	page=page+1
# for index in range(len(timelist)):
	# write_file(timelist[index])
	# write_file(titlelist[index])
	# write_file(titlelinklist[index])
	# write_file(breflist[index])
	# write_file(authorlist[index])
	# write_file(authorlinklist[index])
	# write_file('----------------------------')
#write_file(htmlStr)
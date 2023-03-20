import re
import requests
import time
import json
import csv


with open(r'C:\Users\Administrator\Desktop\python\taobao.csv',mode='a',encoding='utf-8',newline='') as f:
		csv_writer=csv.writer(f)
		csv_writer.writerow(['raw_title','detail_url','view_price','item_loc','view_sales','shopName'])


# # url = 'www.baidu.com'
# datas = '搞事情'
# bytedatas = datas.encode('UTF-8')  #转换编码格式
# # res = requests.post(url, data=bytedatas, headers=headers)



# # https://www.1ting.com/player/d3/player_103969.html

# #https://music.163.com/#/discover/toplist


# agent1="Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
# agent2="Mozilla/5.0 (Linux; Android 8.1; EML-AL00 Build/HUAWEIEML-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.143 Crosswalk/24.53.595.0 XWEB/358 MMWEBSDK/23 Mobile Safari/537.36 MicroMessenger/6.7.2.1340(0x2607023A) NetType/4G Language/zh_CN"
# agent3="Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36"
# agent4="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
# agent5="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
# list1=[agent1,agent2,agent3,agent4,agent5]

# agent=random.choice(list1)

#构造请求头信息
header={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
'referer':'https://www.taobao.com/',	
'Cookie':'t=ceeab96c379b520a782c21f7b8dd6ca1; thw=cn; _tb_token_=e41498f5734be; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; cookie2=16694790496c209ed8ac0b9b8665575b; _samesite_flag_=true; xlly_s=1; cna=vxZ+HLI3g3UCAXABPo61/Ufw; _m_h5_tk=5b928c7201455b332994e6c7ff0dcd69_1679051477254; _m_h5_tk_enc=f7d8ea62af609f70e0bec3d41ce6e67c; sgcookie=E100ALplt1Nceu4inV10y9n17qpoIVVkvPS4DTSTRBs+VvkaJdzWCWgluEYXh3xahjVd3bxs4WkVqn4l35asCO2roRWkxrlf1IgpXJeyVMsE2E8=; unb=1105878105; uc3=vt3=F8dCsfeav76rW53agC4=&lg2=VT5L2FSpMGV7TQ==&id2=UoCJjWwdenCk8w==&nk2=FPa0K9pDGtG9BpU=; csg=7a03da55; lgc=wojichunyin; cancelledSubSites=empty; cookie17=UoCJjWwdenCk8w==; dnk=wojichunyin; skt=3a741ce0ed42e906; existShop=MTY3OTA0Mjg2OQ==; uc4=nk4=0@Fn13DW+poQ1MvYetbaHDdqj8zrUV7g==&id4=0@UOg1xaXn613Zn0fX9zY48g5SG4NI; tracknick=wojichunyin; _cc_=VT5L2FSpdA==; _l_g_=Ug==; sg=n52; _nk_=wojichunyin; cookie1=ACJfoKk5vcfCXxSdTOBtKOWoz2QCf7JPRsrg7eNmEqw=; mt=ci=4_1; uc1=pas=0&cookie21=U+GCWk/7pY/F&cookie14=UoezRmbxjfsXLg==&cookie15=V32FPkk/w0dUvg==&cookie16=VFC/uZ9az08KUQ56dCrZDlbNdA==&existShop=false; JSESSIONID=201FB504F9BDCCF15F9CA2424607BA2D; tfstk=cxPfB20Ctnxfx0CMim_P7yznYxl1ZMLI5ti0limy4ToO8D4fi0REAi73IhhZW41..; l=fBL_NNUcNOOsxHHCBOfwPurza77OSIRAguPzaNbMi9fPOyfp5SwAW1M-RiT9C3GVFs6kR3uCdsmHBeYBqIv4n5U62j-la_kmnmOk-Wf..; isg=BJOTxDMn8674IL_qrnopdDoFIhe9SCcKoXwbMkWw77LpxLNmzRi3WvEW_jSq5H8C'
}


for page in range(1,99):
	print(f'-----------------------正在爬取第{page}页------------------------')
	url=f'https://s.taobao.com/search?q=大红袍&suggest=history_2&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&_input_charset=utf-8&wq=&suggest_query=&source=suggest&bcoffset=1&ntoffset=1&p4ppushleft=2,48&s={page*44}'

	response=requests.get(url,headers=header)  



	html_data=response.text


	pat1='g_page_config = (.*);'

	json_str=re.findall(pat1,html_data)[0]

	json_dict=json.loads(json_str)

	auctions=json_dict['mods']['itemlist']['data']['auctions']
	for auction in auctions:
		try:
			raw_title=auction['raw_title']
			detail_url=auction['detail_url']
			view_price=auction['view_price']
			item_loc=auction['item_loc']
			view_sales=auction['view_sales']
			shopName=auction['shopName']

			print(raw_title,detail_url,view_price,item_loc,view_sales,shopName)
			with open(r'C:\Users\Administrator\Desktop\python\大红泡.csv',mode='a',encoding='utf-8',newline='') as f:
				csv_writer=csv.writer(f)
				csv_writer.writerow([raw_title,detail_url,view_price,item_loc,view_sales,shopName])

		except:
			pass

# 	strr=html.text

# 	pat1=r'<a href="/music/(.*?)"'
# 	pat2=r'data-v-17805956><img alt="(.*?)"'


# 	idlist=re.findall(pat1,strr)
# 	titlelist=re.findall(pat2,strr)


# 	songID.extend(idlist)
# 	songName.extend(titlelist)


# print(len(songID))
# print(len(songName))

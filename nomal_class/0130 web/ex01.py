import requests
from bs4 import BeautifulSoup


url ="https://search.naver.com/search.naver"

params = {
    "sm" :"tab_hty.top",
    "where" :"nexearch",
    "ssc" :"tab.nx.all",
    "query" :"손흥민",
    "oquery" :"ㅅ",
    "tqi" :"jUxZqsqpulossBXXBns-104381",
    "ackey" : "qk8zy7tl"
}

res = requests.get(url, params=params)
res.raise_for_status()
html = BeautifulSoup(res.content,"lxml")
target= html.select_one(
    "#main_pack > section.sc_new.cs_common_module.case_normal._au_people_content_wrap.color_14._cs_sports_people"
)
real_target= target.select_one("div.cm_info_box")

all_dts= real_target.select("dt")
for x in all_dts :
    print(x.get())
all_dds= real_target.select("dd")
for x in all_dds :
    print(x)


# print(res.text)
#main_pack > section.sc_new.cs_common_module.case_normal._au_people_content_wrap.color_14._cs_sports_people
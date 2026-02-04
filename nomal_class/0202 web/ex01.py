import requests
from bs4 import BeautifulSoup,Tag, ResultSet

url ="https://blog.naver.com/PostView.naver"

payload = {
 "blogId" : "pororin_hamong",
    "logNo" : "224162984703",
    "redirect" : "Dlog",
    "widgetTypeCall" : "true",
    "trackingCode": "external&directAccess=false"
}

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "NAC=eKfHEwDs0RnID; NNB=EY64JUDSDR2WS; ba.uuid=0fdb1a78-7bc5-49d5-b944-43ddd8f47ebc; BA_DEVICE=2476fcd6-9705-48f6-9ab2-07a6434bfc03; loungesRecentlyVisited=Terraria; NACT=1; SRT30=1769994640; SRT5=1769994640; BUC=WdvvNSeo3hsLxvqZIgcfDllD_qrcJuR7Mzl4uU9IGvU=; JSESSIONID=4669E28E74F99DDFBEC362830B1BDC02.jvm1",
    "priority": "u=0, i",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}

res = requests.get(url, params=payload, headers=headers)
res.raise_for_status()
html = BeautifulSoup(res.text, "lxml")

outer_target = html.find("div", {"class": "se-main-container"})
blocks : list[Tag] = outer_target.find_all("div", {"class": "se-component"})

comp_text_list = []
comp_img_list = []

for comp in blocks :
    comp : Tag

    class_list = comp.get("class")
    if "se-text" in class_list :
        comp_text_list.append(comp.get_text(strip=True))

    elif "se-image" in class_list :
        img_tag = comp.select_one("img")
        img_src = {
            img_tag.get("data-lazy-src").strip()
            if img_tag.get("data-lazy-src")
            else img_tag.get("src").strip()
        }
        comp_img_list.append(img_src)

    elif "se-imageStrip" in class_list :
        img_tag = comp.find_all("img")
        img_srcs = {img.get("data-lazy-src") or img.get("src") or img.get("src") for img in img_tag}
        comp_img_list.extend(img_srcs)

print(comp_img_list)
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup,Tag, ResultSet
from pygments.formatters import img
from io import StringIO

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

tables = html.select("table.se-table-content")
# print(len(tables))

for idx, table in enumerate(tables):
    print(f"==================={idx} 번째 테이블 출력======================")
    df = pd.read_html(StringIO(str(table)))[0]
    df.to_csv(f"{idx}.csv", index=False, encoding="utf-8-sig")
    df.to_excel(f"{idx}.xlsx", index=False, sheet_name="itineray")

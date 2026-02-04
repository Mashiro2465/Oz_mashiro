import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search"

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.coupang.com/?src=1042016&spec=10304903&addtag=900&ctag=HOME&lptag=%EC%BF%A0%ED%8C%A1&itime=20260202133705&pageType=HOME&pageValue=HOME&wPcid=17699524732348139215876&wRef=www.google.com&wTime=20260202133705&redirect=landing&gclid=Cj0KCQiAkPzLBhD4ARIsAGfah8jMFhdkGIt9t5GjXmr3LPYv8ELVCedVGkkO30Jji85gNLcqZgSaNTkaAkS2EALw_wcB&mcid=71d9998efbbb46c48a69a777d154d2c8&campaignid=8704277940&adgroupid=86483039646&network=g',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    # 'cookie': 'PCID=17699524732348139215876; MARKETID=17699524732348139215876; x-coupang-target-market=KR; sid=d849a4500ad244c997f733609a499c585d3709b4; gd1=Y; CSID=DUM_eNx520chtJPCNtm3eJp.5fphh5hm0; CUPT=DUM_-2dsCTMP1FJY_iJBStK7lsTYp0AKj-MdCdJyoMC0_a0; x-coupang-accept-language=ko-KR; ISAPP=N; viewType=Vertical; baby-isWide=wide; trac_src=1042016; trac_spec=10304903; trac_addtag=900; trac_ctag=HOME; trac_lptag=%EC%BF%A0%ED%8C%A1; trac_itime=20260202133705; bm_ss=ab8e18ef4e; bm_so=0ADAA02D45B76A2537364379E5B20A90EBBD5FA0610DC1A4D86B98C178C05415~YAAQZnXTF157zPqbAQAAbNmjHAYlfgjPjjTy1fqAtXqS6t/HY+zLBVJgKEQdOwzRGiXKEPHuhsRwIYk3YrtZtlfCxXi4mdedRiM6UqIKXW4M9mfm+H6bDXSwEtt/o6fL4MXKOOryJjvghimuer6zLAoxOGXs4aAgDhcyQ6vD0c9+PlplgGDCTUq2d4xgSl7yOZyBdYwOgpfR6KwA7XaBHWQ36l8f1PuB3CysZgwOsJIhI71MzwIybPec2TophVT11GO4N5PItZKU7ymxQXT+Zhy4KT4f9GK8EsTepceexqmxKczyRy99RQ2bNkVQgs/iGSupfzBY46Nc4fFIDIJejB4PwAI7RYIGjFk3Fs/YfGpFCtqcfFw4l0xDnFgqj6s/nCJrMMCJhNZDLa7iTyqxrcNtY/pubEmAxTpu5J/BIhToAm3RfW1HXm2Oj8cmTFQhLfWES4U3iLCur5lRnmeL; ak_bmsc=03C4588BB127406CB46291E87A58F175~000000000000000000000000000000~YAAQZnXTF+N7zPqbAQAA4tyjHB6WS6BfVXBF/YmbpCwefnjIqHqPhfMsoc6kv6vlzShoJI/Pp7LazahYxQXliGI5fqPwGhJhk98DkIHFzWBQuNe95ya3uqUHmwurd4CBPvJn/fdCICyJxs/z5jz2fXPo6EBAfR0gwcbbQSKBLvs16DwqOTjRl4jgLvygdBdxtgLuC+pB+Vy8F3YypO/qgUXzQiy1zV9ieOtdOarqFlXlKrw55WW5TnQwLTmsIf4ziPICPPXR22L5oq8l3xJ1mWvgdcZAesh9L4NiL5BPGeyGE7+saGHvHdWhNiCSqeYckYqHwzYeEEHP6rENS/YDTUyfxzVbi+RgFdhtaYcS01UNJeMtsSOt2WBww9uKJhh4UekQzlouzgu3zEMWAXARgE3OWAna8vlyWjzczkYShA5JgJ4OWxcne3H1t3wsG7iJ71ErzTlt3vvhBei8wDo=; bm_lso=0ADAA02D45B76A2537364379E5B20A90EBBD5FA0610DC1A4D86B98C178C05415~YAAQZnXTF157zPqbAQAAbNmjHAYlfgjPjjTy1fqAtXqS6t/HY+zLBVJgKEQdOwzRGiXKEPHuhsRwIYk3YrtZtlfCxXi4mdedRiM6UqIKXW4M9mfm+H6bDXSwEtt/o6fL4MXKOOryJjvghimuer6zLAoxOGXs4aAgDhcyQ6vD0c9+PlplgGDCTUq2d4xgSl7yOZyBdYwOgpfR6KwA7XaBHWQ36l8f1PuB3CysZgwOsJIhI71MzwIybPec2TophVT11GO4N5PItZKU7ymxQXT+Zhy4KT4f9GK8EsTepceexqmxKczyRy99RQ2bNkVQgs/iGSupfzBY46Nc4fFIDIJejB4PwAI7RYIGjFk3Fs/YfGpFCtqcfFw4l0xDnFgqj6s/nCJrMMCJhNZDLa7iTyqxrcNtY/pubEmAxTpu5J/BIhToAm3RfW1HXm2Oj8cmTFQhLfWES4U3iLCur5lRnmeL~1770007023889; bm_sz=04D26DA55BFAD9C82875CD50CAFD12E5~YAAQZnXTF8d9zPqbAQAAW+qjHB5B6P83ZGBfIH5p/ub7hGdo4lhHyX5CEx35Q5WJGgaHkLa1nsqvogEPBDIs9XF8YsVEgeQn9yWrlDhutZ43vaIndBvlbD+VNvpdsmpza9aOEgaD8uVO++yArdqFAq23TQirkKbTFpeX0cM8oRc3hQQprmSKxO9OSKenj3UsUmXd8K3cBOwjc7R+Ecy3iiF+R6us2lT2Z0nny8fmwxgYZinps8jMKvy2BKZyNdKV1N9m3oB9OwUuYyAsUblwSDdv+8CjQv63ilm8S2THZXy4yMA1PUcqOqBtrjhUdb+on6WcDruArbAlqmBZzpXJrJca3eVWNDFL7FSL9Idy3yiS8kp5ti666wLYX8B3ugAEiVSbmCrg+cOlHKOOuSshr/ehHvn/9XAyjg==~3487044~3687728; _abck=930D276F262ED3ACA8F127317F34E544~0~YAAQZnXTF899zPqbAQAAvOqjHA+yStZSInfjh6tHZr3K+Wz2KJq8oLhTrWfPJzbKh8uMg/wvPjcweXvwAS2XjyUhR4+VHSZ0eGJkFPtbXB+GftVG5kGa2wzQ+8R78agJR9+eJPOmDkTG9aDrFHsmIihj7KdquZP0H3iO2VjRBSp4Hx3E5rlM/ihYjTrSquNhJu1MKQmQSA8TmVvIdEyF719FUiBPojmV7e4XVFEN0tg54USCzLbDLUq+lWqzukSsSPlF9AM5pXqERrD3pdAdRvMPaaLJIEJ+mrcxENE72jJ3B0T1jpFtwb5wU4rX9ApnN/YnVl2tVZT/rftsUxvKAqBkKB9nsQatbR8a+E4FsQ5RtJKKNEiQwrB/XZKTfg6jcPVuZeFfimZLxB18d+B8Q52UcqDiwRaIauLD+dcad6aOkcMKE3HMEvnv35jw/F2vGvMWQhAk5+lMqQGNdRa34YoGiyoLGRh943qnPvBfo6rxn8r+eDDDjp57OQvOnYbaZ1tg0MnGK+VcWT5VmDXHAxQuurvEkzCqbVJ7rbJx2dYDx3Fb+oms6t4rvFGPmPojbk0JMdlbvekdCjhBV8TAmTa5MyJ9G/sD6jbLn5tonZ9em5FcsebkSUPIvDwPxuBN8SHtBJkeRd+PMh+RA6v88SSzGo0HizW+5Ro4yzUa4RM9bk/NV1OOxsJffZWghVgKlRsHcuMt6fvwWxsJZ97ZjaK+hRzMPGh2ONNwQr9aM37O8vOXkXkynNr9BSaJb3UBZrqQyKxV6v0MKTQ8+GKN4bRAq3Fl0ty0+q2/CmmnQa47~-1~-1~1770010626~AAQAAAAF%2f%2f%2f%2f%2f3Kgwh%2fok+TQHy2tvW0Sc58yrab5%2fchkZpOoqow0caNzi3RF0X55%2fCesvOSa9QDt+CjpL2vtc0aBxEl6Z6kvuBVGiIWe8UvmJsxN~-1; bm_sv=1ADF4B39788EC68513E5A969CFA7A160~YAAQZnXTF1N+zPqbAQAAbvKjHB6ww2HHoToWArjB8DCE1gdix9CKs8zrlVsssUGqtPxdPMcpSg79XiG4ELYAcUJwx2bXMhY9EbIi0HHikZ79zbOqZsgZQ0FDMUgKPj1GP9rNQXwQqCjdufP2L1FpqjEIBYY3t2TC+5JyHda8FtZQPCLYrlvQ/HXpPFSQJFOfKdm4ldW+3MkEz2QAhoQixsnYWxVRGE/vFq2rEYUy4tzXmNopL8YCvBhIK4E122MEgw==~1; bm_s=YAAQZnXTF21+zPqbAQAAZ/OjHAQo8j5SwQAKfQZRKWdl3FcptAHB1q2l/jOuk9HTkiwVWKRysRYFiFmjq5eSuMJncYCtcrG9tr7BLb1wG5QWEXb+u5o5dEOXuxZF58dWLle+B65YaFTkOursxfkijt6KLou1bryB7GuppQL+w39lwxhMJ5H3Y0dR3CNKP6v2ZbIV6lpX6o2PCfaolcOwJrwmoWk3j3r+VJc3lqDufwpH9+7bRnxw0DTArutGgSB7BQKS9sfOJg15k4zcXcJsIu8OVGvCBjDqQIGiUHm43RWjgDElM7p+m15Sddsp8KCAQ9WAopezwWJOAzCFD/SLBgWfqMq9AYnePykTy3Tw4vtLbyJdYDidR0dztv5ei4tQlwQxrrbGkYJcX6gcyEKDFSTo65LR7NVBzZ79y0UF+PMv2Q5bicxRGsfaf+8TQFyxeZofCm/Oc7KmNRdrHJVcqMc2ya5nnrrzVt/DNyFaX2Su2WRsB1iSOCK0Dylc5ikuTGEVg3D70vtSIrOmSecUuIeTzXYrFSebKcNPFNigFQRIULbUFb/SuTNJoV3Ao97yeSUjUkynPV5AGxbLkw==',
}

payload = {
    "q" : "페브리즈",
    "traceId" : "ml4ohcxa",
    "channel" : "user"
}

res = requests.get(url, data=payload, headers=headers)
html = BeautifulSoup(res.content, "lxml")
print(html)
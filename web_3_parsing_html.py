import bs4,requests,sys

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}
address=sys.argv[1:]
#address='https://www.amazon.in/Epson-EcoTank-L3150-Wi-Fi-Printer/dp/B07JXYQK82?pd_rd_w=m1Mxf&pf_rd_p=e6322eff-fb5e-4cc4-8cef-e41c114df71b&pf_rd_r=S0QR5KFN6YR1Y9H61FDG&pd_rd_r=81c4f1a2-fa5f-419d-b827-209c3d0f4d5c&pd_rd_wg=wcwGF&ref_=pd_gw_cr_simh'
res=requests.get(address[0],headers=headers)
#print(res)
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text,'html.parser')
elem=(soup.select('#priceblock_ourprice'))
print(elem[0].text)



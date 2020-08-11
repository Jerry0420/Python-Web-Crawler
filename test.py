from bs4 import BeautifulSoup
import requests

# rnye2e55tff1jm45n4johz55
# 5its2455xcq3xovzr50izvqp
cookies = {
    'ASP.NET_SessionId': 'ltcxfh55eimywaun0tvf5nbq',
}


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://www.ip2.sg/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.ip2.sg',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

data = {
  'MSOWebPartPage_PostbackSource': '',
  'MSOTlPn_SelectedWpId': '',
  'MSOTlPn_View': '0',
  'MSOTlPn_ShowSettings': 'False',
  'MSOGallery_SelectedLibrary': '',
  'MSOGallery_FilterString': '',
  'MSOTlPn_Button': 'none',
  'MSOSPWebPartManager_DisplayModeName': 'Browse',
  'MSOSPWebPartManager_ExitingDesignMode': 'false',
  '__EVENTTARGET': 'ctl00$PlaceHolderMain$uclSimpleSearch$PagerIP$ddlTopSelect',
  '__EVENTARGUMENT': '',
  'MSOWebPartPage_Shared': '',
  'MSOLayout_LayoutChanges': '',
  'MSOLayout_InDesignMode': '',
  'MSOSPWebPartManager_OldDisplayModeName': 'Browse',
  'MSOSPWebPartManager_StartWebPartEditingName': 'false',
  'MSOSPWebPartManager_EndWebPartEditing': 'false',
  '__LASTFOCUS': '',
  '__VIEWSTATE': 'O8r2WFfty/OC+bXzaQ7OdYHhI3aSCjXd051UsU3jndy5qCSf/X8IryWKU4U9npb86cn3VsrhpypEhhZUQoUA/apvhXaLyz92GbMj8P8cjo4iTIRuWwUe5+UOCHj0bSaKzLofQosIGIX/PDRt3ERsw+97qQlCVyqnSjhIFgfSdFca9SkTOtxdLrIZsR2PxzvnYpl4Y4MkJD/KE9ddN1cgbKwjftEZPHBvKxL1yNlWQEIfngDOC+720Y3lZYqHSEPRoJPZ7k/X8NL2kAtXhAH5GdHD7tJyJ5i9mSwqRPWGJKkuAGlEG7sfG98jdY9ffzt8/A1dFDryxA3yTK8+X1kQsr6mhQf0eHg7rUhCq1KwqWWq3Y4l5EGMxFV9FPHC7PzfzcTDvYzOk/FSs8D/H7QHKCL3suCVfhJuBsTLmGdS4//1jDQSHwudocX3BXfWv7KpBC9RnUU49XVL4Wee2N+3lf+QrCHFGwojkxmzQfap6VBuFEeXeEfw9ubSfLv8rqISAFjZsVgv0plFRCpObP1CAIyfT9E26k3tSDHz7DCvfVWy0mxZvSg7kuDeDLt5+IlnfnagG1q75YtaraJPoEV6u1/uZ9dfztC6bN6OgySlEDI/XDq9Y13hNmd3Cjx5pbjinps7M47JCOuhPcHGjacFPFKyqppRgItaDcfgldEOThjaxR8+CZTwzVt5tpuoN3AO912h2EcrPIvQgzUuOfZQegfhNbdklFghfULFW9sjrEodnH3XDtQTHczZedjU4P02nV7L1oE6J2mFaZx3LKNCHCcDyfQ/QvKGOjeL8nTxJ5E+bz3pgKZbCiH/DPD8LMLrpk0CYghUReeceys9pap6rVYBLL4uY1A4dI2D+iwFdW5LWIQH5SJ2VFRQHDef/+5G7waoKzxjVW6ZX1mxrood1Z9vnbxp6Boxlh3o14h5XbJkr3+UQYMr4pVzLJUFMVUcodBr6QCHgDJ7xTDTvo+XCHx3unQF5IfWSx/HQ2bnctT1E0TlEsNaBISWyGh3+qPab2rPUIxw3VTs7STRrWHAqjK0phbxA4R0KRmlUyaTCtUJDsKeMAUhfuH7Jxx+QLFLgBlXN5r+banM5sEDi9EE7AZ+HOhYFDz3zhPLwb5Cm7kNOj853Wu9k74Ycc1S9u7ptmDO6+HBuNAU2y6MM3oEynmuKnA71x8f2IpHn2OILGw53bTbD7msjTL2neF6YXdUXAb0Macsn0/GDZqQl1dY8SI6MAj5oKWI1cLLhPOaSNhYx/WAM+3kbE+6WdmRXY0T9MaJMHBVqBS438JD7jDbvlHSWygYlNoELiu+5BaAXKBOGgu24G2FS6ENKBbY/14ulk2X07F1Vwp7gDwhDMUscW3jGN+5Q1agIspghutiiWNz8odYqnV1FxtUig9gWrSkQZYWu8JdhVvYTw7wQ75fiyJ8wg5OI4JDy6Lr/pWWSp2T29kyJ8qA43DaGD1yoJSTHmV0Q3L9KDNcHmLnZBUvDQBj/PyB1fbdt/Z0LkA9nzpA/z13CHmT1eYOc4XSCNzvcJm3eg181cRYT6CkADYsNpnOJwDSgWbPOsc76ricKucxhj06KqewOubWz64I6nz1SR7i3f1GXRf4ymUbGgJg7D97iEljiBBW8VJ9I4V4IIbTLghQZOlye56De0ez3nN01wUegTh/2JE5EQDzGbpdjab7Ecv19PHXbwiDu84D1rkNq7bMqosuicY4NhX6KqowbSecKLK07zmDn/POo8eN7DMIL+5ypLX3ApVHY0h+cen6eQTII4ZpFGxVMoubN9HFjnmIZb91uGpiOEY3Qsj4RL4GZgu+IrSrJIZ+ZkyKgfxxslziwR4TPRpSBtN//QqcM0lxw09YwHzueSuk6YqZ/XJpwoprP1YWNQ0xRsQ3P3JBntaixPtL1MtnJRd+5HayNvErxEUjTMhrXa5VnfbjLmnasG55JS5K388s0hwGziRY/7CrWUIpS4mlOPflHy+kkc9PvqVaoBOtRg9ZbOYkrxkOd5v6tSVm+sd8kWnSJymlf3tLVFwRgGLbISjwfh6/ACUsw9bSi12TcP2M+qpAFPkHXBTAxIB7ckQBevH1YgOUpmkNjrKMBVO/6SLAiJSJsdQcs4RbzRTI8fyXaI3CXJmxipo9x8224fQF1oF7coOSN7k46PnAJPQEBERU6Th18or/hRRW0OGpy/IhRCzONtHNOcboNqebOadUzgdJxpwVkgfqZYbo39uicIBnQq0VmBo6rwUkbPxmt2h2ILyJXwInOvyqKkZOfpLBYh7v9JmpcgHzWy4AOcKQp9QRCgOJBu1d7QEO2rRfzKGTUuPN37sg1iwzrmgwQ2H8cukpS45FdNFMl+dI4RF/LA6PYTFz5QWaww0Ag5g86xRRhFLRHlXaqILlsdUx2qbskMHLwcwH8tRUk7Izzd1RDb0BjdHj33n01TmRxDNrzNTlvhYO4YtjPn+lubhJ3+XQzSGOcuhEJ5BzsuZLOLun2E8cbfxLtmBCtibRm+w0Nih0zbdzP641YwKhBSARqLl4/LxEOlzmjRCMbXlWQACH1IDx4pg2HAP8SjU6HzlIkiE+uKRym27KqWUuB3elMwhaeXoivtxCyL7r/YueaQDsoLcvtSv1+V6xLwgpYjWGUVPqjWEj5vxaLXJ/4fkmfqLF6d8usIQa1mO8lDvzYTyzDXERwQC/BnPuuVqghB/gsKGrRlsLvYoX9wK5jjBanH3jdkgnweFlfKzjnVNUk/fyvTLXbVbJsLBiloEbIHVqJXVDdNmhX4sHBOwtj1hF9zJ8O/CfYbEQYZ0PM0RmamB+UL1Lpuzuh2sidZQHkQtWVJTCiy7EEHzYc4VSbJHoyCKLu+mIsDtYP8uMHCJPTR43I/Q3CyFv4j80X19lR5HRIUW/ZivlC+tt7eDiRKntX7s6OcJcVDHPxOcXy6ffVzQixa6kAEiQ2uDjsGeKGh1efF/tu4vQL7+siXmpWMKug0MDgNfes4AC64TLeOEgpoxhlxiXA7Ga09gtRrXizQpISiQnWcL9nf4WQliaIu+V6LTjHiMwHpDT6JXadT8mzcrHvPzaC7vWDQMe/rNA9jiisOTAObcW6XyGrexQ0xZ60LHT4Eb4AccfOxQ1b3VD8isiFNERWBO4xjXcOWDMUWy2RJ0HVhWdYYstKI34VbW9FD8cwHaouERUscGleAJ4zZhE9PPAUTeV+n3KAFUjG1qlbanwYUuJzsxdrMhstKTDxSouYLzq8RKdlgN2q7XOgejCpsvW6YhWTML5BWNnauWiia4bvo9m8j+0bbViYBOKW8dvKodAY7t9u/+e1Lzh9LhHO9EbdRgRze6o3IAfhhgxdKqLwmoiT0zRDZ6mi2I0HB7oCor4GGTYgahLKXvjVGNP6sJWtKtgMsH1hp9D02TSCoQq7z1g/fyAepNKri1Oy2ZP5PhICcOKN6IOz1jdd10rXjs9FiponSQwIS94IxOIncYl32PhLjlj1AzhOSDFK3ueePha4s8D9DlnYgE7ZLV4FezbKOsPdO3BuZ4pO8iyClxF8JbThpHYEUfUqO1arO9Cb0SttKAViG7kaQM7/terzrQYrxsiuXwQDpI8WYzEBt+d7w0RgxkHMke38R1wBhu2X9qc/90XkGes5Hh0iVLAnN3chl+IcuyyqsCgzIeSBtLKhp/krqjEJsig2JF/LVU7KiI2bJrWT1B+ixb9gSH5G0SI2/xT+1GCvq/q0QD4X65Wj1GvXet8fZdp08FWxKoUFFKoBNDPxKY5TgAwTaxuNcFs97e0C4zb1ciydDqv6hpt6G2zGhGvr4HkJXTD6AF94lEseQPbyiPvFx20Fbd+3VzETZHl3g43AzgIg00aaHQRRBf/UAifuo2/qBPj18xQd9ythfwISwwFqZvFdCMIF576i4y9zX5wjDhK/Jty6SwiTPpFzNQVmkod5fSSa+ZpngvCjLVmssrkewZPpyCD/aCsnMHlK76MB+MAVbWrG5/ztojXlTddnMxKa8KcCwaheNMCGSUS6aq2ZPRIpiDSoQuqwC49I3+QhJD+XewGkEIu54c6b/y53eAa16Bwrp0F3M/QmjRqW0vM8ccmmKycFFsBNwdDn+76iWzUhgWTrjTe+1VWMv5ZzOVj16h8MexCYoKrw6taNWlvj2p93WmWQK0YNGpTOrxHpfYyCtiuTF9aOKhykhiW3XPhanRoX9F81SdzWjzamJIsArAluOMcY/K64v7RIImLP1MUi+X5pGK9bJITVtMT3i9rrBEApTl0aEP9yx+B9XJfEVQnGlXVP+p/0EGkqU2riyZqmE5Ua6pbtL2W2rQo6FEEeRGYZApmejGJmRhS3+ynRyYGc1fVHjGB4W57miXkSrowEcnHYpgbTpSUEV0mUkd5OqbqLC4qeF9uNYnX5Z0F6hXRVbf81k+bO+LT12LEIhFLM3XPfFLKJDa/mQS7kRiQfjazCzMNLRSn0Yn2BUKYwM/DjgTzq88FZ0smc+PRIfj3uhUk+BW5iV/0+Dd3n45xl4gV0/pOy5DjwHrXTWkugzf0W8rl9QVxZqhreDZe4slJwv6+EVBsbESl56Y9l2j1uEnkToMiZJn/ip/UAtxB7YjD2777UFOiGyM9Fkk8um2LMJuh40FfDd3/JJK9bP1zGxu9FqAw6Aigebf293XRUcrfvlApMcLOlXiheahXxeby5Wxy7sU0MQ4Py4i404PSxwp39gQX1AiwBORl5PXvONXqNUQ3vGW/SZ7/yUnXxq9TJGwZ7JGoN+lXnLp2vFx3+zXb1BnCkr2MIvNDOwhiJJL55hX0wpNEVK7ZeThjXn6pfCNy83JRP4Ku4Efvlu0kR2HjC5rhV9yUBZJ3F3+GJRLn0dHuJ3/qM0PlZOguFgy+UBQQ6sKmX5sG0uymGRXW5oCGm0bEBdFGO1R37oj60QHGhoe7zqFtr3B9qZCM9SbMElxj1t2jL4DPAXAOjLK5wYl+lSy2RROH1d74aZiflC0Lcz5oeVtLjEa1U0KivU9+ybbIEOZ7c5QmbTNaNqPHVajeap65cnnN405xT2OO0OK4/goe9qcUyzTVTR822iTQ+5IaVnm3QtC4SeJchrGWxrrT3BWceWpF5LEBXBAquR4mDZ+ylVBtkZYagHxnu3Ypl3jlHfnpO68f/zIpgeN3kAPn8Ffd6c/R1SkRme8iRdLC7j6HIvrdGbOYUG4AoU2SyWTJimK9m+UtNiSPLZPgneDD3sFW/6UThzsmmcm1EXUyYmK7E1UdWtiRS8nogMi2UOxYSqleOATDjUJGwNBrgfb3pIj5/Ae6oK6LKveypGagV5OHKMqI0gvnjmZ7HZQ0grVoe+U7w5hAR2t/LzicP0v0E3ofcPfLDk54wGfpzmRI6nltbTLwcle+n5eatb/xAWPyKQvvv2bEf8s9RgNyCdU3VuHHOaZO9yDWXiLnWDCl6PZxdrvUOpEEd5i/JthOewXOyjBbXQDT0Ah1TDZp76shG2RQO5NcUlwOf9scCuh/DHe0nv6yrQCnazv7e70h5hzloDZK9mInHUah8w4V0qqxdOw/tzPyHHOupAavlvk9LrK5Mx/1GmgvbddBTvfJQgJ0VYYdyb7Kvnf6Sdd5nHxCkfBSu6KB8XwoX46BjM4uWWRVbeqc3qYvlCUTDwNnT/jq6odzYQkj/yLF4blJBB3lVsWrPxPAzbBJW+mHUx45BfH+lCNL9iJIyNbrI8alsca62tErBalOGvaEj3WEZWiINBlugpp7E0QpDZtIRgU+gf0R31pU4FW5ij9sHfS2CKh+ae0FqPIMCJX3ejOVQ8GcBkiQUSIote15BtgP6vgwZgQoe1ukT2iWyJHm+0cqQk82BU0tyzD81IpbhxumuHjoKsrrR+emxf1D/gnAtAt/oaT75Y3+CTCmIEJcXLQgYqBopmn5UmjtAvX8WoAL8Igijdwwd9f/xhyof+YryAX3ClxVX6OimqIMStJdftmqlZncvAzr6pNotkZi+Y4Kz/Y9opxUX6sZ7QbmablD7x4kjYIzZsrPnGXPSANwFbkED26n5sb9LdAyHFmgTkgqBBfmxLq7FRSmX2il+OycuNgP1lNSth6+/DHfqSsAzX8HlQK2mA9ZuQXzVu76FrUunrbJGzgbZsIfCZI87Qo8x8nxjU0cuLqTIgMGuAL8/Y69tJy3tuYWmBAont3gVwB71jDxQvCtQ/3h2qVR3l+2oZEPLuaTZ0wnM95RhM0ILrk1iiLnaprd5vYU4KfAB5/tTBWnqAb/r48zzt6zWvAfRKsmUY891YsDZkfNZtxC/jaXtdWNqAwt3IXboCdmdXkqF3c86Y5mlKvXjN8zf4g1RuacYO18NWQIPt4cp6p2Vk2ipjIiG0lwnYaa1Z33tb7vN36foIX5dFt+6yPIoJANuFD/1jGa7iqu1cOsrpMklcXH6htkwbp96NWNnauQ2VyxjrAko1jHDlxYYb9VJ1E1FJEgNfUEpOMyhOeJtAacd5dwoKaMZ3zuvh4V32SpWIlkJ5VYAHjcH7s+Iq+b9SG7JKUhnmuUuikoPBihccHr+az9VshkHRVXcZn7ZPFViaZeHNnWHIZ/DOG3XVsZjIlGV82kU3C8lzDA8OwIeOajRMcKPSbqvRhwBeeb87qoqS+p7lUWWxeWHMW/COjZZl+L5yiWPneQEunNm3xnFekoxftP5Wgdfu9UIUyV0wNyBo8RpdJmebvRyFc9msAQih/dJcoIUaQzp1qtO/eenice5dt5ErAJfDcikkTAgDUVjHbrFb4yMWl+NUplACSvrnJN/usB0JtyRBdRWg3US+hCEPb/rnsmD2YWzmBp98jMKrTnFtGiKMwj9EUk6FBuEY2YWH/pTUeIrp4nZIrsQm0fSYSiG3O+4Fn4tzFvSW96dZwyAgz+Vh+HL9mQ162kTTdonHU5SZGxepWH3WUU2QySMNT1wme6a6eIjczEyf/woYLG72V3XHd5uuF3zt/WFsOwuZHMCKkUekk5NnPg29IMppwmNwJBSmLexhbP/0Ieiw3cRIoEileZvykSDHNeDlC3dw11x/YaQmuHpIVhI8KIxLhoTCvbCqiaE4QLLjtedyVJpunWFYlF/7GFbiy5NEpdUar4dYjH9DSP0XbNlWL/CUf1pmkiKMnNPT8pjoKrHlIMRj+ONGyPc7k+8ch1qJO7DsEWE63swVIcEWJVkv1cDR++4sGoSqccfwC4rSQEiCu/txRThOSDTM3EkMAWZkefLGsdYY6LqYO4frVA/P/jaAt6C6rvv6rOiEt9PVV0Tasa8kNImIxscAoXWOd6POqQSf4Qqjx8Aeuxf1bEPl+U3Oc29j4IGdildfXXdmSTptQ+c06Pb9duHPitDmQViXDsD0rimwetlyrRIjiswsTZZae3xp7c6+KQknas+HdhAyXAlVWqATB8oRXxhP12clNw9rb/2uIhDZXQpOlHEkPsrUEr67gWj/DfE5LnYtSp7JvASMj4l+tWcKZ4oHpUx0JL1e191INhRxfXKbOLd0svplqTzvd3npn54wOCBVkKQcKrIx+vmzRzH2EFfj+I/oW6oRV2nnEhGxxKosQdpCuv/t5kvPJ4cGpytD7FZJ7LxKmdCAKbkVCWwA+u7AP7K+ID/ta/kVaI5oLr1ycawTk+6dR1iMA9M5u9Tz7GKsNYxmGB6DH6MpBE5INKDdq9X4iamjxwP1GMJ4mdp/kAznPqmRxW140dHzRJiIZRVv2yeOsKUHKtmI8Ug7rVCp3KcywUdrpEjaUrBmL8htfTC3uBZzZmZMzvjItfSLzZwj1HhXDXfm1JpoStL4MsB3gKrzcyYSOdFP2ApWjnRdhF8h9opMYWAjENEPjKI2NNTe/LJZIb55PMv8fbLV5E680EtetIOBxDnDTI6TBkJpoxxHNJkMbksuOso4uhEgGfL8QtIs6NhdVUXa92TkZdj/no0ck3xcNZozcOdi3aviLE0moMu3qOUWYz1jPYlxyvx2INLXP1JzKozpC8FZrbGALZDiVt4draI15uJjF1dq6U5pQetwLdmUboGXNnl9YIpNmg3HtrzkeDUvPLB78Es+v1ElV3a5y/I6HeY+hm7GyC86cXwLWKWtmjDPu2xsQ3VWss+b/bZZUhWunZOcOU8UwIErtQiXdWHPEeapt2AqS5wN8ktyfRRUDMdbqCOjGV+sAeU1/0gM5EzqAvIR1eRLixRrakRFCIvA44mEbIHu4CXmm/Kj88JF9bf2FiAMTS8jkZAmQhnodHs/kWghTRfImWYrqiW32LDL3ws1aV3hYd1qqLv13WcuG/yKMumFDRdGwzqKl/g3nk8xdb/WC703GacjAOdnjVZVTNEFJQFSD47To9Y5sgWKwp9tQA+ayhpskfzqNHYD+7n/0tTzwJBqAeeiFnn40GFmcGpDjEUL9GYJEgYcHosuNNFNB8K7amXwPMQW+t7fqsIh6mVZhKWNiI/tfT4JGwvK9a6b5eDSwRSEXA2cBYa43k9EdbGd5gfm/ftWBfWrJTkn3QUWJ4jwdF5oPH3RNMYG+n/xz6o1cgmNNwoOTzXcwdFV/cbDWLq5JFWgJAHl706PM3Z1QooFCTG+WTZYZVfULjcxL8BVx7Z8BzrpVHBX+TG0S9rVpUWJeAuIvTGZq8keJW8MdBhIN1tO6OzxeZdnlAimhWtrND0pPeCSMixZIRw6qAha0RuuLmJD+r34LuCoPSXV6mq97XBQqq4qPX33FTUMDSpu8X/Puh/tHJ2yRLyM7opf4T/YpRXs8cyq9apRTNCJvkevPFioxZxfQUGvWrDD5dCd+AKNt6IDNu1Ag4rt2Dn6na2A3ci3tzFuv9k2GQEV1J1J94+SUuCDOmPEovAWeCOuhimwo/hpwLhvHLjdkEWJFT5j4pXaE30aPPdFWwO/yebZ7YlF3ucqALG5bYKCSMESmwCW3xPFbwA97rIsliQNCB3j2NAtl5cJT2xL7GncEFZkOgDLGwplYM1Agt3ePQ2hmHqEHOGUvQzYmA/hRaMaVE2xyNGKMNgbHE6+59woSNxl04CdpxCUr9OHqz/P1GGWOcqUQ+qAryrpO6BXe8W/lYpgn5Okkmm5DXIcClCJ7DCL3XPEtpGm9zVvZQLAiF82RlKhIfQxpRfgfUCT6b5AuXSn4ttRrxbDD/sC2hVRjzN4q+5YYCFf7NHvUxMGDULZRCjukuHAwc9JOpGznDti2OjhPXt1OrwX5/dXCspgQQnKjmyWQDtPx4TjwJZ5NRxgn5yUdgDUJG4R5x+/i7N/8EHhOT7AXcCAEWGD+xK710enwYQpK0JL16kxe2TE706Z9IJipC40s0lQyDgEb6hgzImeJKS1oO/uIAqOUd34sCr+leyM7sJ/txecvYo+kEX/2SC4Ykj1Riof99W0y1Shg3WF9dFJuzVpsfabqD7KHMELzP32oSEcuBF8nmRJRO39qsLq3r4QDlPPhYWT+4EQ+Uu9Ez1ubOopXY6SbhGXLzqR2mshoTlCRqo/SvFHE0DlH/grfWzb5Q0alUNeSiACvTlQHWc+hQuCKTMHYulAODf4TOx6Te7pl+aAjW8r1jVjfl93BaLkQcHh0VyN+SVCUDzD6PmtzKbVm4xC0FnldthCENZEdZNEdxaAa85MC1kLWn2ViBD2KoDhHXgCV6KWhPq1eqVwoizpNwDy4P4aB91RY22CJTmrbbmZPWrCbLtFGzWrOpt1P9e0b7veOZGafkoFIGLPfWRoRQOnhT1UjwGXKxKINkKII8T62xpHHJ+b55GuoEwmO+wENWS6FGVWQYAK1240lb4EWgHYudyb396UXeFzweI1v9H9iDoymOyY/+8NkCXFD+lv8Grtz2HF07iFyd4+e9Q/s+ocJtcwk1Ot42wxcj1hpPE0gZzDj0Mw7FsWbDdoFepTzy5GBQbhdtoG3kCm8u4/wnqt+X0proKaUMAT/Ppw3Gwx2EKtF5v2V1kBfHKmjqvmUw7aA/L11DNPWe3V/BLcSL9GVTS7svpuKbD/Xgo/y9Sjr8qA8Yq27Yljyjg4Fegj0JtXChg1XK7NQT8/bGSVhFglt38CVXbzrwMzRzTTD2G/BRlagx41yvg/pJheNfqVlJbi/7sPpORzVojAb8xXJ67Kyv4wp1uw+kriQubDl1V6LVLIKuuFK97jqzmgZ+zNVJD5D6gBCrEKw0Pg+bu2ugvoS7N7PqcPo7iiVhnBrrltB0vRPKJ7HVnG1hFTUwngUN0i1x1AwI+hTpcr0Aw8ykCtR5ZevdefqT5dy22lQOr+RpMQskkfd/OtZzRrukCB2R5+3940wgbZX3/6PzoebUYvlXJCqOgHbi4zd22LusRjevm49YexDtz8IB3U/Hk1V2WOCpHDBq3a4s6qmgCPusbmkHn09n2gdtR0YhHJss5QztFCOROu8lPhmKgdbE2EteOOl9KzoTaLIj/150unISVnLtmcH2V9QDH0HYcR51CuWLBTLm4t/vFaoz3rJlg4X2dVvOt99W3FApcWjxKHbzVWS3pnknw66wVShPem8QwKIqusMJe7CSV3C5ebPZjm8lDXI4/w+m0EluGZpbFs2hKmZ6iCUojdyxQ71S7z/dNMuqQnxU6S8O0/QtJdGZg16KaingiJkwh5SpcdblM65AXkwyWwm2IsOjlFCWlHJJi2R8YvL8Jy0RPSF9r8CY0SOAf3/Iy+KVhjMPDkzx6diElohgsvSDWmpYtD8U2UFCS4b3CwoMS+gG5oAs9pDvhwx7Z0jFcNfG28qajwy/2vbduCwoo15/UAtu39m1hjxo6qN1m3ecIJfktd+slvkvkDihl3Oj/JVySECIvN4mctAf/n9LUtH19ky6NKW1CdeSUx8V8Zra8r3b4H0fUBe1SINNWeMyJZbxX/i9YywGdvTgyo/qTJRhLqpC2kfHIEWDZiX4O+w2fexLhSomFpgMZGdel5J7EYxINtC0TsmilgCeVSK/8TrymFYz2+RVyLS37EQQ9lfoYJ+qqFurM79zsF8gIv/jRK6MLLfbYj1ICaMkiwBM2efmuH5lB8AUAxPsa+mIopqZYX5vbxYOpLWbSWaOS1uuwhVwQN3zMPAQ2wiTRAhynohAbqurewc1jn3L7qXJ760n2ASqHsOLxKKDfvj7GtdYRMkTXue4u/tcvMz1oCW5JYfoyopM77cFHcYFeC6DuY3nZ20oS+qBmWf3Os5ywIeCcUW7Q4jcIHkC8hUGXGvx+C/cTdzcqwF/GMGEzJWzDqeA2HfENbmHXUyERuqfZJNRNL4JpXGHdTwi6rfJcUgVLM8Jg5LDTa8N+3lY2kQHqVVqumsq5x8ypZaL0MgtE6hA6td5LCfddmnm8i9GBC18LARiF6dYXbXLPDMuv755swVQkGRree8s+cTrYj5/tNLDbdKS5CLcbM+XqRO2UVSzE/+XtEOJrh2zvTEvwvElcQDOOjXuHDMxtKUbQhmcWWsyD4NE0THs+Pj0HqxJ5Lw2ynA3FFxfoNf0ebpyFqDLLbGLeqN60VQFz+6ak4I0w0CaO5RMS06Qjtkal5GNaDouRgUyql9iaPSgC6M5Zkwg/FMmR1r8dtakiJaHbSM7v9T/AzOZA16cjNf2fJkdQvc6vSCxht3FQz3nRQ8H6gU8EugahPQDbJjdLffho3bkpeDVJfyWONmMBFS9P4rVsyEATDWBsV1lOYkmo3M4Av/+o8A7R88RVf1YNaITkYlGDhRaQRYbh+lVlA2xPOhRAbEKGAoFLxW8J8PSVWjDszxyd2DrEmqSqT0RYEIyYVluyMDY0SmqfS4ra0caD3t8ZwZ6YrXDLlM/a0aY6FMFH6Wk7ceZf0iANL6kl3LO/Zvl4bIdU8JyigNqRzbc9x7zSdBM750ANtV4zTwE',
  '__VIEWSTATEGENERATOR': 'CCB3C644',
  '__SCROLLPOSITIONX': '0',
  '__SCROLLPOSITIONY': '1823',
  '__VIEWSTATEENCRYPTED': '',
  '__EVENTVALIDATION': 'zdEvo0qnCWa6iX52wo9YTAA2iDiNSpBCN85IowRj1ky0t40QHR8jENu5P9sHx5oJUgor79MirqMjPB1bVhpd/WBLxbjfHMtgqfEGkpYGwIu2UkaHUrJwFglAM9h1jXMl7c+Xvgt3LVb6C92hlnlQfpPog6fW7QiSnLuwQTUd5a6gH01Gx8Ood9gjYJJPsS0+1QJ1E3x2PRucxQTMmWkdlcIREf6OXSzD+ux9CoygxdQjtyQC340iazWidFSRITcFsBEumzZ033KIc/lQflF389CjCwzTBxDkif/bxb6cpJ7P2gJmxeszme6fO7wMKpA1NFJdN+GeZBMU92UCdbG/oM0bwd4QDmBvvNOtVJRvpQ/qp+dqb3jfGEs/ObPoVe+Ij5orUxAQE4IzqC6tFG247S6EyeU47EPUeTCPdxZTR8/HFw0Ewiu7g/8wBbADSowCVOKA2x8/wEU7MsYpjSD6Ndqea5rxR4JQD3FWzFPseg3GupyH',
  'ctl00$PlaceHolderMain$uclSimpleSearch$txtSearchText': 'math',
  'ctl00$PlaceHolderMain$uclSimpleSearch$PagerIP$ddlTopSelect': '100'
}

import requests


response1 = requests.get('https://www.ip2.sg/RPS/WP/CM/SearchFastP.aspx', headers={
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
})
print(response1.cookies)

response1 = requests.get('https://www.ip2.sg/RPS/WP/CM/SearchFastP.aspx', headers={
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}, cookies=response1.cookies)

response = requests.post(url='https://www.ip2.sg/RPS/WP/CM/SearchFastP.aspx', headers=headers, cookies=cookies, data=data)
document = BeautifulSoup(response.content, 'lxml')
odds = document.select('tr.odd')
evens = document.select('tr.even')
print(len(odds) + len(evens))
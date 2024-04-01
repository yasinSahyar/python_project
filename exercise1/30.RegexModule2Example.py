import re
#https://www.youtube.com/watch?v=6yQQJBV1RpE&list=PLWctyKyPphPiul3WbHkniANLqSheBVP3O&index=32
"""
GSM operatörleri:

#54 ....              -> Vodafone
#501,505,506 ....     -> AVEA
#53 ....              -> Turkcell

"""

def gsm_operator_bul(tel_no):
    patern = r"(\d{3})-(\d{7})"                             # (\d{3})-- o ci index, (\d{7})--1 index
    eslesme = re.search(patern, tel_no)

    if eslesme:
        gsm_kod = eslesme.groups()[0]                        #0 inci gurubundan bul
        if gsm_kod.startswith('54'):
            return "Vodafone"
        elif gsm_kod.startswith('501') or gsm_kod.startswith('505') or gsm_kod.startswith('506'):
            return "AVEA"
        elif gsm_kod.startswith('53'):
            return "Turkcell"
        else:
            return "Numra dogru degil"

    else:
        return "eslesme bulunamadi"

tel_no = input("")
print(gsm_operator_bul(tel_no))
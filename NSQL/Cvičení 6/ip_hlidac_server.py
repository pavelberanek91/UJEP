import datetime
import ipaddress
import redis

cerna_listina = set()
MAX_NAVSTEV = 15

ip_hlidac = redis.Redis(db=5)

while True:
    
    #blpop vrati seznam klient
    _, bytova_ip_adresa = ip_hlidac.blpop("klient")

    #prevede IP adresu v bytove podobne do IP adresy ve vhodne podobe do stringu
    ip_adresa = ipaddress.ip_address(bytova_ip_adresa.decode("utf-8"))

    #vytvori par klic-hodnota z IP adresy a aktualni minuty navstevy
    aktualni_datumcas = datetime.datetime.utcnow()
    adresa_cas = f"{ip_adresa}:{aktualni_datumcas.minute}"

    #inkrementuje par IP adresa-minuta navstevy o 1 (novy pozadavek)
    pocet_navstev = ip_hlidac.incrby(adresa_cas, 1)

    #pokud prekrocil pocet dvojic IP adresa-minuta maximalni pocet navstev za minutu, tak je to bot
    if pocet_navstev >= MAX_NAVSTEV:
        print(f"Bot detekovan!:  {ip_adresa}")
        cerna_listina.add(ip_adresa)
    #v opacnem pripade nastavime experaci ze seznamu za 60 sekund at ma pozadavek navic
    else:
        print(f"{aktualni_datumcas}:  pozadavek od {ip_adresa}")
        ip_hlidac.expire(adresa_cas, 60)
    


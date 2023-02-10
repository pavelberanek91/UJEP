#zakladni obraz, ktery stahneme z docker hubu pro nas vlastni obraz
FROM node

#vytvor a prejdi do pracovniho adresare, vsechny dalsi Docker prikazy se odehravaji relativne vuci nemu
WORKDIR /usr/src/app

#zkopiruj npm balicky do pracovniho adresare pro npm instalaci
COPY ./src/package*.json ./

#spust v terminale npm a nainstaluj json balicky
RUN npm install

#zkopiruj veskery obsah lokalniho adresare do pracovniho adresare v obrazu (cache optimalizace)
COPY ./src .

#odkryj port 8080, pres ktery budeme komunikovat s hostem
EXPOSE 8080

#vytvor mount, kam se budou nahravat data ze specifikovaneho lokalniho adresare
#VOLUME ./src .

#pokud je jiz obraz vytvoren a bezi v kontajneru, tak spust tento prikaz pro spusteni node serveru
CMD ["node", "server.js"]

#instrukce pro vytvoreni obrazu
#docker build -t "phaser:game" .

#instrukce pro kontrolu vytvorenych obrazu
#docker images

#instrukce pro spusteni obrazu do kontejneru
#docker run -dp 3000:8080 phaser:game 

#vypis bezicich kontajneru (nalezne id)
#docker container ls 

#zastaveni kontejneru
#docker stop ID_konteiner

#odstraneni obrazu
#docker image rmi phaser:game -f

#pokud nejaky obraz visi a nelze odstranit (nazev <none>)
#docker container prune
#docker image prune -f
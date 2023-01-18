#zakladni obraz, ktery stahneme z docker hubu pro nas vlastni obraz
FROM node

#vytvor a prejdi do pracovniho adresare, vsechny dalsi Docker prikazy se odehravaji relativne vuci nemu
WORKDIR /app

#spust v terminale npm a nainstaluj json balicky
RUN npm install http-server
RUN npm install phaser

#zkopiruj veskery obsah lokalniho adresare do pracovniho adresare v obrazu
COPY . .

#vytvor mount, kam se budou nahravat data ze specifikovaneho lokalniho adresare
VOLUME ./src .

#pokud je jiz obraz vytvoren a bezi v kontajneru, tak spust tento prikaz pro spusteni node serveru
CMD ["node", "http-server"]

#instrukce pro vytvoreni obrazu
#docker build -t "phaser_game:Dockerfile"

#instrukce pro kontrolu vytvorenych obrazu
#docker images

#instrukce pro spusteni obrazu do kontejneru
#docker run -dp 3000:80 phaser_game 
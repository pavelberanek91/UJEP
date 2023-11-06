# NoSQL databázové systémy

## Cvičení 6 - Asynchronní úlohy pomocí Redis fronty:

V tomto cvičení budete realizovat na serveru pomocí modulu Redis Queue (nebo Celery) frontu pro asynchronní úlohy. Jednodušší řešení je využít Redis Queue, ale v praxi se více používá celery. Následující odkazy vás zavedou na příslušné tutoriály, které jsou alternativy:
* Redis Queue: [ZDE](https://testdriven.io/blog/asynchronous-tasks-with-flask-and-redis-queue/)
* Celery: [ZDE](https://testdriven.io/blog/flask-and-celery/)

### Zadání

Naprogramujte frontový systém pomocí Redis + Redis Queue nebo Celery, který koná pro uživatele asynchronní úlohu se zajímavým algoritmem. Nechám to zcela na vás.
1. Připravite si projekt se všemi závislostmi (flask, redis, redis queue, celery) pomocí docker-compose.yml.
2. Napište si kód služby do nějakého souboru (např.: service.py nebo jako v tutoriály tasks.py)
3. Pomocí formuláře nebo javascriptové události nad webovým prvkem zadejte serveru žádost o úlohu.
4. Zachyťte na serveru žádost o úlohu, zařaďte ji do fronty a vraťte uživateli přiřazené ID jeho žádosti.
5. Přiřaďte do systému Redis Workera aby žádosti o úlohu z fronty vyzvedával a vykonal žádosti.
6. Zprovozněte si monitorovací Dashboard pro Redis Queue.


## Materiály k samostudiu

Projděte si následující tutoriál, který vám ukáže všechny možné příkazy Redisu. Vyzkoušejte si je volat z redis-py: [ZDE](https://www.tutorialspoint.com/redis/index.htm). Tím budete mít zásobu příkazů, které můžete pro vaše aplikace s Redis využít. Dalším zajímavým tutoriálem je tutoriál na využití specializovaného modulu om-redis, vytvářející abstrakci nad redisem pro práci s objektovým modelem: [ZDE](https://redis.io/docs/stack/get-started/tutorials/stack-python/)


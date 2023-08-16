# RSS Reader
## 2016.08.16
### https://github.com/NA-rsstestuser/rsstask
___

Used framwork: django 4.2.4, Docker 20.10.25,, Python 3.11.4  ~20h
## How to
Just use
> docker build --name=rss rsstask . 
> docker run --name=kacsa1 -p 8000:8000 rsstask  
Will make a running website with admin:admin  
losalhost:8000/admin

One of the main obstacle was that python changing and dont have backward compatibility.  
Until the last hours everyting went fine until something broke somwhere in the python modules so docker compose and external database was dropped.  
Used this basic docker + postgres:  
https://github.com/docker/awesome-compose/tree/master/official-documentation-samples/django/  


For de RSS first idea was own inplemention, but went too many hours into it, instead using:  
Unluckily dont have a ui to see what we can add and how....   
https://github.com/xurble/django-feed-reader


All in all it's a working djungo backend without any kind of security or proper struct, in its current state its can not reach the desired minimal usecase.
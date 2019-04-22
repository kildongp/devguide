# devguide
development environment setting

Server OS : Ubuntu 18.04
## Apache Install 

```
sudo apt-get install apache2
sudo a2enmod proxy
sudo a2enmod proxy_http
```

vi /etc/apache2/sites-available/000-default.conf
```
<VirtualHost *:80>
    ServerAdmin     {ADMIN_EMAIL}
    ServerName      {SERVER_NAME}
    ServerAlias     {SERVER_ALIAS}
    ErrorLog        logs/error_log
    CustomLog       logs/access_log common
    ProxyRequests   off
    <Proxy *>
        Order       deny,allow
        Allow       from all
    </Proxy>
    <Location />
        ProxyPass           http://localhost:{PORT}/
        ProxyPassReverse    http://localhost:{PORT}/
    </Location>
</VirtualHost>
```
* apache config test
```
apachectl -t
```

apache restart
```
sudo service apache2 restart
```
## Maria Db Install

```
sudo apt-get update
sudo apt-get install mariadb-server mariadb-client
```

mysql connect, use sudo, if not , connection fail.

```
sudo mysql -u root -p
```

    + user1 계정 생성

    create user '계정아이디'@'접속위치' identified by '패스워드';
    ```
create user 'user1'@'%' identified by 'user!@#$';
    ```

    * user1 권한 주기
    grant all privileges on DB이름.테이블 to '계정아이디'@'접속위치';

    '''
grant all privileges on testDB.* to 'user1'@'localhost';
'''

* user 권한보기

'''
grant select on testDB.* to 'user1'@'%';
'''

* 권한 확인

'''
show grants for 'user1'@'접속위치';
'''

* 계정 삭제
'''
drop user '계정아이디'@'접속위치';
'''

'''
drop user 'user1'@'%';
'''

** 권한 삭제

'''
revoke all on DB이름.테이블 FROM '계정아이디'@'접속위치';
'''

## Install Node

```
curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -
sudo apt-get install -y nodejs
```



공식문서 - https://github.com/nodesource/distributions/blob/master/README.md

## java8 설치

openjdk 는 안된다. ninja -C 할때 sun 툴을 찾는다. 

After adding PPA repository we can move to installing java on Ubuntu. Executing apt search oracle-java command should now show multiple java versions available for install. 

Namely they are java8 and java10.


* Java version 8
```
sudo add-apt-repository ppa:webupd8team/java
sudo apt update
sudo apt install oracle-java8-set-default
```

* Java version 10
```
sudo add-apt-repository ppa:linuxuprising/java
sudo apt update
sudo apt install oracle-java10-set-default
```


* Set default Java Version Manually

In case you need to manually switch between installed Java version start by listing your current java environment variable settings:

```
sudo update-alternatives --get-selections | grep ^java
```


# python 설치
```
sudo easy_install pip
```

설치확인
```
pip
```

bs4 install
```
sudo pip install bs4
```

```
# -*- coding: utf-8 -*- 
# parser.py
import requests
from bs4 import BeautifulSoup

req = requests.get('https://beomi.github.io/beomi.github.io_old/')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'h3 > a'
    )
# my_titles는 list 객체
for title in my_titles:
    # Tag안의 텍스트
    print(title.text)
    # Tag의 속성을 가져오기(ex: href속성)
    print(title.get('href'))
```

Selenium을 설치하는 것은 기본적으로 pip를 이용한다.
```
pip install selenium
```

크롬을 사용하려면 로컬에 크롬이 설치되어있어야 한다.

그리고 크롬 드라이버를 다운로드 받아주자.
크롬 드라이버를 받을 때 내 크롬 버전과 같아야 한다.


https://sites.google.com/a/chromium.org/chromedriver/downloads

```
wget https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_mac64.zip
unzip chromedriver_mac64.zip
```


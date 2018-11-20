# devguide
development environment setting

Server OS : Ubuntu 18.04

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




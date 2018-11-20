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




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





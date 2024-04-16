# PostgresPro_tt
Test task for PostgresPro Internship
### Задача

Реализовать консольное приложение, которое будет устанавливать PostgreSQL на удаленный хост

---

Реализация должна включать:
* подключение к удаленному хосту по ssh
* инсталляцию PostgreSQL на удаленный хост
* настройку PostgreSQL для приема внешних соединений, т.е. БД должна отвечать на внешние sql запросы.

Требования
* приложение принимает один параметр - ip или адрес удаленного хоста
* приложение должно сообщать статус выполнения инсталляции
  
Будет плюсом
* приложение выполняет проверку работы БД, выполняя sql запрос (SELECT 1)

Требования к коду
* язык разработки: python, golang, rust
* библиотеки можно использовать любые
* код должен быть выложен на Github с Readme файлом с инструкцией по запуску и примерами. Важно, чтобы по инструкции можно было запустить код и он работал
* при возникновении вопросов по ТЗ оставляем принятие решения за тобой.
  
Желательно отразить в Readme, какие вопросы возникали и какие решения были приняты

---
### Решение задачи

#### Запуск из терминала
python connect_to_host.py XXX.XXX.XXX.XXX или
python connect_to_host.py HOST_NAME

#### После запуска
Выводится список команд:
```
Список доступных команд:
  1 - Команда test_connection
  2 - Команда setup_postgres
  3 - Команда get_status
  4 - Команда set_open
  5 - Команда send_select_1
  exit - Выход из программы
Введите номер команды:
```
При вводе номера запускается соответствующая функция, результат выполнения отображается в терминале.

#### Пример работы

```Список доступных команд:
  1 - Команда test_connection
  2 - Команда setup_postgres
  3 - Команда get_status
  4 - Команда set_open
  5 - Команда send_select_1
  exit - Выход из программы
Введите номер команды: 1
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"

Список доступных команд:
  1 - Команда test_connection
  2 - Команда setup_postgres
  3 - Команда get_status
  4 - Команда set_open
  5 - Команда send_select_1
  exit - Выход из программы
Введите номер команды: 2
Установка PostgreSQL...

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Get:1 file:/etc/apt/mirrors/debian.list Mirrorlist [30 B]
Get:5 file:/etc/apt/mirrors/debian-security.list Mirrorlist [39 B]
Get:2 https://deb.debian.org/debian bookworm InRelease [151 kB]
Get:3 https://deb.debian.org/debian bookworm-updates InRelease [55.4 kB]
Get:4 https://deb.debian.org/debian bookworm-backports InRelease [56.5 kB]
Get:7 https://packages.cloud.google.com/apt google-compute-engine-bookworm-stable InRelease [5146 B]
Get:6 https://deb.debian.org/debian-security bookworm-security InRelease [48.0 kB]
Get:8 https://packages.cloud.google.com/apt cloud-sdk-bookworm InRelease [6406 B]
Get:9 https://packages.cloud.google.com/apt google-compute-engine-bookworm-stable/main amd64 Packages [1917 B]
Get:10 https://deb.debian.org/debian bookworm-backports/main Sources.diff/Index [63.3 kB]
Ign:10 https://deb.debian.org/debian bookworm-backports/main Sources.diff/Index
Get:11 https://deb.debian.org/debian bookworm-backports/main amd64 Packages.diff/Index [63.3 kB]
Get:12 https://deb.debian.org/debian bookworm-backports/main Translation-en.diff/Index [63.3 kB]
Get:14 https://deb.debian.org/debian bookworm-backports/main amd64 Packages T-2024-04-16-1405.22-F-2024-03-13-0824.19.pdiff [22.2 kB]
Get:14 https://deb.debian.org/debian bookworm-backports/main amd64 Packages T-2024-04-16-1405.22-F-2024-03-13-0824.19.pdiff [22.2 kB]
Get:15 https://deb.debian.org/debian bookworm-backports/main Translation-en T-2024-04-05-2005.03-F-2024-03-13-0824.19.pdiff [22.7 kB]
Get:13 https://deb.debian.org/debian bookworm-backports/main Sources [200 kB]
Get:15 https://deb.debian.org/debian bookworm-backports/main Translation-en T-2024-04-05-2005.03-F-2024-03-13-0824.19.pdiff [22.7 kB]
Get:16 https://deb.debian.org/debian-security bookworm-security/main Sources [89.8 kB]
Get:17 https://deb.debian.org/debian-security bookworm-security/main amd64 Packages [151 kB]
Get:18 https://deb.debian.org/debian-security bookworm-security/main Translation-en [91.7 kB]
Get:19 https://packages.cloud.google.com/apt cloud-sdk-bookworm/main amd64 Packages [477 kB]
Fetched 1569 kB in 1s (1405 kB/s)
Reading package lists...
Building dependency tree...
Reading state information...
16 packages can be upgraded. Run 'apt list --upgradable' to see them.

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Reading package lists...
Building dependency tree...
Reading state information...
The following additional packages will be installed:
libc-l10n libcommon-sense-perl libjson-perl libjson-xs-perl libllvm14 libpq5
libsensors-config libsensors5 libtypes-serialiser-perl libxslt1.1 libz3-4
locales postgresql-15 postgresql-client-15 postgresql-client-common
postgresql-common ssl-cert sysstat
Suggested packages:
lm-sensors postgresql-doc postgresql-doc-15 isag
The following NEW packages will be installed:
libc-l10n libcommon-sense-perl libjson-perl libjson-xs-perl libllvm14 libpq5
libsensors-config libsensors5 libtypes-serialiser-perl libxslt1.1 libz3-4
locales postgresql postgresql-15 postgresql-client-15
postgresql-client-common postgresql-common postgresql-contrib ssl-cert
sysstat
0 upgraded, 20 newly installed, 0 to remove and 16 not upgraded.
Need to get 53.7 MB of archives.
After this operation, 221 MB of additional disk space will be used.
Get:1 file:/etc/apt/mirrors/debian.list Mirrorlist [30 B]
Get:19 file:/etc/apt/mirrors/debian-security.list Mirrorlist [39 B]
Get:2 https://deb.debian.org/debian bookworm/main amd64 libjson-perl all 4.10000-1 [87.5 kB]
Get:3 https://deb.debian.org/debian bookworm/main amd64 postgresql-client-common all 248 [35.1 kB]
Get:4 https://deb.debian.org/debian bookworm/main amd64 ssl-cert all 1.1.2 [21.1 kB]
Get:5 https://deb.debian.org/debian bookworm/main amd64 postgresql-common all 248 [179 kB]
Get:6 https://deb.debian.org/debian bookworm/main amd64 libc-l10n all 2.36-9+deb12u4 [674 kB]
Get:7 https://deb.debian.org/debian bookworm/main amd64 locales all 2.36-9+deb12u4 [3902 kB]
Get:8 https://deb.debian.org/debian bookworm/main amd64 libcommon-sense-perl amd64 3.75-3 [23.0 kB]
Get:9 https://deb.debian.org/debian bookworm/main amd64 libtypes-serialiser-perl all 1.01-1 [12.2 kB]
Get:10 https://deb.debian.org/debian bookworm/main amd64 libjson-xs-perl amd64 4.030-2+b1 [92.1 kB]
Get:11 https://deb.debian.org/debian bookworm/main amd64 libz3-4 amd64 4.8.12-3.1 [7216 kB]
Get:12 https://deb.debian.org/debian bookworm/main amd64 libllvm14 amd64 1:14.0.6-12 [21.8 MB]
Get:13 https://deb.debian.org/debian bookworm/main amd64 libsensors-config all 1:3.6.0-7.1 [14.3 kB]
Get:14 https://deb.debian.org/debian bookworm/main amd64 libsensors5 amd64 1:3.6.0-7.1 [34.2 kB]
Get:15 https://deb.debian.org/debian bookworm/main amd64 libxslt1.1 amd64 1.1.35-1 [242 kB]
Get:16 https://deb.debian.org/debian bookworm/main amd64 postgresql all 15+248 [10.1 kB]
Get:17 https://deb.debian.org/debian bookworm/main amd64 postgresql-contrib all 15+248 [10.1 kB]
Get:18 https://deb.debian.org/debian bookworm/main amd64 sysstat amd64 12.6.1-1 [596 kB]
Get:20 https://deb.debian.org/debian-security bookworm-security/main amd64 libpq5 amd64 15.6-0+deb12u1 [188 kB]
Get:21 https://deb.debian.org/debian-security bookworm-security/main amd64 postgresql-client-15 amd64 15.6-0+deb12u1 [1697 kB]
Get:22 https://deb.debian.org/debian-security bookworm-security/main amd64 postgresql-15 amd64 15.6-0+deb12u1 [16.8 MB]
debconf: unable to initialize frontend: Dialog
debconf: (Dialog frontend will not work on a dumb terminal, an emacs shell buffer, or without a controlling terminal.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (This frontend requires a controlling tty.)
debconf: falling back to frontend: Teletype
dpkg-preconfigure: unable to re-open stdin:
Fetched 53.7 MB in 1s (85.4 MB/s)
Selecting previously unselected package libjson-perl.
(Reading database ... 66761 files and directories currently installed.)
Preparing to unpack .../00-libjson-perl_4.10000-1_all.deb ...
Unpacking libjson-perl (4.10000-1) ...
Selecting previously unselected package postgresql-client-common.
Preparing to unpack .../01-postgresql-client-common_248_all.deb ...
Unpacking postgresql-client-common (248) ...
Selecting previously unselected package ssl-cert.
Preparing to unpack .../02-ssl-cert_1.1.2_all.deb ...
Unpacking ssl-cert (1.1.2) ...
Selecting previously unselected package postgresql-common.
Preparing to unpack .../03-postgresql-common_248_all.deb ...
Adding 'diversion of /usr/bin/pg_config to /usr/bin/pg_config.libpq-dev by postgresql-common'
Unpacking postgresql-common (248) ...
Selecting previously unselected package libc-l10n.
Preparing to unpack .../04-libc-l10n_2.36-9+deb12u4_all.deb ...
Unpacking libc-l10n (2.36-9+deb12u4) ...
Selecting previously unselected package locales.
Preparing to unpack .../05-locales_2.36-9+deb12u4_all.deb ...
Unpacking locales (2.36-9+deb12u4) ...
Selecting previously unselected package libcommon-sense-perl:amd64.
Preparing to unpack .../06-libcommon-sense-perl_3.75-3_amd64.deb ...
Unpacking libcommon-sense-perl:amd64 (3.75-3) ...
Selecting previously unselected package libtypes-serialiser-perl.
Preparing to unpack .../07-libtypes-serialiser-perl_1.01-1_all.deb ...
Unpacking libtypes-serialiser-perl (1.01-1) ...
Selecting previously unselected package libjson-xs-perl.
Preparing to unpack .../08-libjson-xs-perl_4.030-2+b1_amd64.deb ...
Unpacking libjson-xs-perl (4.030-2+b1) ...
Selecting previously unselected package libz3-4:amd64.
Preparing to unpack .../09-libz3-4_4.8.12-3.1_amd64.deb ...
Unpacking libz3-4:amd64 (4.8.12-3.1) ...
Selecting previously unselected package libllvm14:amd64.
Preparing to unpack .../10-libllvm14_1%3a14.0.6-12_amd64.deb ...
Unpacking libllvm14:amd64 (1:14.0.6-12) ...
Selecting previously unselected package libpq5:amd64.
Preparing to unpack .../11-libpq5_15.6-0+deb12u1_amd64.deb ...
Unpacking libpq5:amd64 (15.6-0+deb12u1) ...
Selecting previously unselected package libsensors-config.
Preparing to unpack .../12-libsensors-config_1%3a3.6.0-7.1_all.deb ...
Unpacking libsensors-config (1:3.6.0-7.1) ...
Selecting previously unselected package libsensors5:amd64.
Preparing to unpack .../13-libsensors5_1%3a3.6.0-7.1_amd64.deb ...
Unpacking libsensors5:amd64 (1:3.6.0-7.1) ...
Selecting previously unselected package libxslt1.1:amd64.
Preparing to unpack .../14-libxslt1.1_1.1.35-1_amd64.deb ...
Unpacking libxslt1.1:amd64 (1.1.35-1) ...
Selecting previously unselected package postgresql-client-15.
Preparing to unpack .../15-postgresql-client-15_15.6-0+deb12u1_amd64.deb ...
Unpacking postgresql-client-15 (15.6-0+deb12u1) ...
Selecting previously unselected package postgresql-15.
Preparing to unpack .../16-postgresql-15_15.6-0+deb12u1_amd64.deb ...
Unpacking postgresql-15 (15.6-0+deb12u1) ...
Selecting previously unselected package postgresql.
Preparing to unpack .../17-postgresql_15+248_all.deb ...
Unpacking postgresql (15+248) ...
Selecting previously unselected package postgresql-contrib.
Preparing to unpack .../18-postgresql-contrib_15+248_all.deb ...
Unpacking postgresql-contrib (15+248) ...
Selecting previously unselected package sysstat.
Preparing to unpack .../19-sysstat_12.6.1-1_amd64.deb ...
Unpacking sysstat (12.6.1-1) ...
Setting up postgresql-client-common (248) ...
Setting up libc-l10n (2.36-9+deb12u4) ...
Setting up libsensors-config (1:3.6.0-7.1) ...
Setting up libpq5:amd64 (15.6-0+deb12u1) ...
Setting up libcommon-sense-perl:amd64 (3.75-3) ...
Setting up postgresql-client-15 (15.6-0+deb12u1) ...
update-alternatives: using /usr/share/postgresql/15/man/man1/psql.1.gz to provide /usr/share/man/man1/psql.1.gz (psql.1.gz) in auto mode
Setting up locales (2.36-9+deb12u4) ...
debconf: unable to initialize frontend: Dialog
debconf: (Dialog frontend will not work on a dumb terminal, an emacs shell buffer, or without a controlling terminal.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (This frontend requires a controlling tty.)
debconf: falling back to frontend: Teletype
Generating locales (this might take a while)...
Generation complete.
Setting up libz3-4:amd64 (4.8.12-3.1) ...
Setting up ssl-cert (1.1.2) ...
debconf: unable to initialize frontend: Dialog
debconf: (Dialog frontend will not work on a dumb terminal, an emacs shell buffer, or without a controlling terminal.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (This frontend requires a controlling tty.)
debconf: falling back to frontend: Teletype
Setting up libsensors5:amd64 (1:3.6.0-7.1) ...
Setting up libllvm14:amd64 (1:14.0.6-12) ...
Setting up libtypes-serialiser-perl (1.01-1) ...
Setting up libjson-perl (4.10000-1) ...
Setting up libxslt1.1:amd64 (1.1.35-1) ...
Setting up sysstat (12.6.1-1) ...
debconf: unable to initialize frontend: Dialog
debconf: (Dialog frontend will not work on a dumb terminal, an emacs shell buffer, or without a controlling terminal.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (This frontend requires a controlling tty.)
debconf: falling back to frontend: Teletype

Creating config file /etc/default/sysstat with new version
update-alternatives: using /usr/bin/sar.sysstat to provide /usr/bin/sar (sar) in auto mode
Created symlink /etc/systemd/system/sysstat.service.wants/sysstat-collect.timer → /lib/systemd/system/sysstat-collect.timer.
Created symlink /etc/systemd/system/sysstat.service.wants/sysstat-summary.timer → /lib/systemd/system/sysstat-summary.timer.
Created symlink /etc/systemd/system/multi-user.target.wants/sysstat.service → /lib/systemd/system/sysstat.service.
Setting up libjson-xs-perl (4.030-2+b1) ...
Setting up postgresql-common (248) ...
debconf: unable to initialize frontend: Dialog
debconf: (Dialog frontend will not work on a dumb terminal, an emacs shell buffer, or without a controlling terminal.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (This frontend requires a controlling tty.)
debconf: falling back to frontend: Teletype

Creating config file /etc/postgresql-common/createcluster.conf with new version
Building PostgreSQL dictionaries from installed myspell/hunspell packages...
Removing obsolete dictionary files:
Created symlink /etc/systemd/system/multi-user.target.wants/postgresql.service → /lib/systemd/system/postgresql.service.
Setting up postgresql-15 (15.6-0+deb12u1) ...
debconf: unable to initialize frontend: Dialog
debconf: (Dialog frontend will not work on a dumb terminal, an emacs shell buffer, or without a controlling terminal.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (This frontend requires a controlling tty.)
debconf: falling back to frontend: Teletype
Creating new PostgreSQL cluster 15/main ...
/usr/lib/postgresql/15/bin/initdb -D /var/lib/postgresql/15/main --auth-local peer --auth-host scram-sha-256 --no-instructions
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "C.UTF-8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /var/lib/postgresql/15/main ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... posix
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting default time zone ... Etc/UTC
creating configuration files ... ok
running bootstrap script ... ok
performing post-bootstrap initialization ... ok
syncing data to disk ... ok
update-alternatives: using /usr/share/postgresql/15/man/man1/postmaster.1.gz to provide /usr/share/man/man1/postmaster.1.gz (postmaster.1.gz) in auto mode
Setting up postgresql-contrib (15+248) ...
Setting up postgresql (15+248) ...
Processing triggers for man-db (2.11.2-2) ...
Processing triggers for libc-bin (2.36-9+deb12u4) ...
Список доступных команд:
  1 - Команда test_connection
  2 - Команда setup_postgres
  3 - Команда get_status
  4 - Команда set_open
  5 - Команда send_select_1
  exit - Выход из программы
Введите номер команды: 3
Получение статуса PostgreSQL...
● postgresql.service - PostgreSQL RDBMS
     Loaded: loaded (/lib/systemd/system/postgresql.service; enabled; preset: enabled)
     Active: active (exited) since Tue 2024-04-16 15:09:10 UTC; 1min 7s ago
   Main PID: 3586 (code=exited, status=0/SUCCESS)
        CPU: 1ms

Apr 16 15:09:10 instance-20240416-150806 systemd[1]: Starting postgresql.service - PostgreSQL RDBMS...
Apr 16 15:09:10 instance-20240416-150806 systemd[1]: Finished postgresql.service - PostgreSQL RDBMS.

Список доступных команд:
  1 - Команда test_connection
  2 - Команда setup_postgres
  3 - Команда get_status
  4 - Команда set_open
  5 - Команда send_select_1
  exit - Выход из программы
Введите номер команды: 4
Executing echo "listen_addresses = '*'" | sudo tee -a /etc/postgresql/15/main/postgresql.conf...
Done
Executing echo "host all all 0.0.0.0/0 md5" | sudo tee -a /etc/postgresql/15/main/pg_hba.conf...
Done
Executing sudo systemctl restart postgresql...
Done
Список доступных команд:
  1 - Команда test_connection
  2 - Команда setup_postgres
  3 - Команда get_status
  4 - Команда set_open
  5 - Команда send_select_1
  exit - Выход из программы
Введите номер команды: 5
 ?column? 
----------
        1
(1 row)


Список доступных команд:
  1 - Команда test_connection
  2 - Команда setup_postgres
  3 - Команда get_status
  4 - Команда set_open
  5 - Команда send_select_1
  exit - Выход из программы
Введите номер команды: exit
Программа завершает работу.
```
---
#### Какие вопросы возникали и какие решения были приняты
Первое же предупреждение при установке Postgres:
```
WARNING: apt does not have a stable CLI interface. Use with caution in scripts.
```
предупредило, что не стабильно работает, собственно что и привело к трем дням ковыряния SOF в поисках ответа и решения, но видимо не достаточно моих знаний и понимания работы apt для полноценного решения данной задачи и вывода полностью всего, что отображается в терминале при установке. Строка состояния так и не появилась, видимо она отображается в каком-то отдельном потоке.




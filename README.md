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

Список доступных команд:<br>
  1 - Команда test_connection<br>
  2 - Команда setup_postgres<br>
  3 - Команда get_status<br>
  4 - Команда set_open<br>
  5 - Команда send_select_1<br>
  exit - Выход из программы<br>
Введите номер команды:

При вводе номера запускается соответствующая функция, результат выполнения отображается в терминале.

#### Пример работы
```
python connect_to_host.py 35.228.49.141<br>
Список доступных команд:<br>
  1 - Команда test_connection<br>
  2 - Команда setup_postgres<br>
  4 - Команда set_open<br>
  5 - Команда send_select_1<br>
  exit - Выход из программы<br>
Введите номер команды: 1<br>

NAME="Ubuntu"
VERSION="20.04.6 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.6 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal

Список доступных команд:
  1 - Команда test_connection
  2 - Команда setup_postgres
  3 - Команда get_status
  4 - Команда set_open
  5 - Команда send_select_1
  exit - Выход из программы
Введите номер команды: 2
Установка PostgreSQL...
Hit:1 http://europe-north1.gce.archive.ubuntu.com/ubuntu focal InRelease
Hit:2 http://europe-north1.gce.archive.ubuntu.com/ubuntu focal-updates InRelease
Hit:3 http://europe-north1.gce.archive.ubuntu.com/ubuntu focal-backports InRelease
Hit:4 http://security.ubuntu.com/ubuntu focal-security InRelease
Reading package lists... Done
Building dependency tree       
Reading state information... Done
6 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree       
Reading state information... Done
postgresql is already the newest version (12+214ubuntu0.1).
postgresql-contrib is already the newest version (12+214ubuntu0.1).
The following packages were automatically installed and are no longer required:
  libatasmart4 libblockdev-fs2 libblockdev-loop2 libblockdev-part-err2
  libblockdev-part2 libblockdev-swap2 libblockdev-utils2 libblockdev2
  libmbim-glib4 libmbim-proxy libmm-glib0 libnspr4 libnss3 libnuma1
  libparted-fs-resize0 libqmi-glib5 libqmi-proxy libudisks2-0 libxmlb2
  usb-modeswitch usb-modeswitch-data
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 6 not upgraded.
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
     Loaded: loaded (/lib/systemd/system/postgresql.service; enabled; vendor preset: enabled)
     Active: active (exited) since Mon 2024-04-15 11:01:25 UTC; 42s ago
    Process: 37523 ExecStart=/bin/true (code=exited, status=0/SUCCESS)
   Main PID: 37523 (code=exited, status=0/SUCCESS)

Apr 15 11:01:25 instance-20240415-040606 systemd[1]: Starting PostgreSQL RDBMS...
Apr 15 11:01:25 instance-20240415-040606 systemd[1]: Finished PostgreSQL RDBMS.

Список доступных команд:
  1 - Команда test_connection
  2 - Команда setup_postgres
  3 - Команда get_status
  4 - Команда set_open
  5 - Команда send_select_1
  exit - Выход из программы
Введите номер команды: 4
Executing echo "listen_addresses = '*'" | sudo tee -a /etc/postgresql/12/main/postgresql.conf...
Done
Executing echo "host all all 0.0.0.0/0 md5" | sudo tee -a /etc/postgresql/12/main/pg_hba.conf...
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
```


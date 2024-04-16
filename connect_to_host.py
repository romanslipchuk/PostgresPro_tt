# Импортируем библиотеки
import paramiko
import argparse

# Создаём SSH клиент
def connect_ssh(host, username, key_file):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, username=username, key_filename=key_file)
    return ssh_client

# Запуск команд
def ssh_command(ssh_client, command):
    stdin, stdout, stderr = ssh_client.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()
    error_status = stderr.channel.recv_stderr_ready()
    if exit_status == 0:
        return stdout.read().decode("utf-8")
    if error_status:
        raise Exception(stderr.read().decode("utf-8"))

# Отправка тестового запроса для проверки соединения, проверяем какая ОС стоит на сервере
def test_connection(ssh_client):
    out = ssh_command(ssh_client, "cat /etc/os-release") # подразумевается что стоит linux
    print(out,'\n')

# Устанавливаем PostgreSQL
def setup_postgres(ssh_client):
    print("Установка PostgreSQL...")
    command = 'sudo apt update && sudo apt install -y postgresql postgresql-contrib'
    stdin, stdout, stderr = ssh_client.exec_command(command)
    stdout.channel.set_combine_stderr(True)
    # читаем stdout и выводим в консоль
    for line in stdout:
        print(line.strip())
    print("Done\n")
    
# Проверяем статус PostgreSQL
def get_status(ssh_client):
    print("Получение статуса PostgreSQL...")
    status = ssh_command(ssh_client, 'systemctl status postgresql')
    print(status,'\n')

# Открываем для приема внешних соединений
def set_open(ssh_client):
    output = ssh_command(ssh_client, 'psql --version')
    version_line = output.strip().split(' ')[2] 
    version = version_line.split('.')[0] # получили номер версии чтобы поменять файлы настроек в нужной папке
    pg_config_path = f"/etc/postgresql/{version}/main"
    commands = [
        f"echo \"listen_addresses = '*'\" | sudo tee -a {pg_config_path}/postgresql.conf",
        f"echo \"host all all 0.0.0.0/0 md5\" | sudo tee -a {pg_config_path}/pg_hba.conf",
        "sudo systemctl restart postgresql"
    ]

    for command in commands:
        print(f"Executing {command}...")
        ssh_command(ssh_client, command)
        print("Done\n")

# Выполняем "SELECT (1);" на хосте
def send_select_1(ssh_client):
    command = 'sudo -u postgres psql -c "SELECT (1);"'
    output = ssh_command(ssh_client, command)
    print(output,'\n')

# Парсим аргументы
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('host', help='IP адрес или имя хоста удаленного сервера')
    return parser.parse_args()

# Список команд
commands = {
    '1': test_connection,
    '2': setup_postgres,
    '3': get_status,
    '4': set_open,
    '5': send_select_1
}

def print_commands():
    print("Список доступных команд:")
    for cmd in commands:
        print(f"  {cmd} - Команда {commands[cmd].__name__}")
    print("  exit - Выход из программы")

# main
def main():
        
    USER = 'roma_sl'
    KEY_FILE = '/home/romasl/.ssh/google'
    
    args = parse_arguments()
    ssh_client = connect_ssh(args.host, USER, KEY_FILE)
    
    while True:
        print_commands()
        user_input = input("Введите номер команды: ")
        if user_input == 'exit':
            print("Программа завершает работу.")
            if ssh_client:
                ssh_client.close()
            break
        elif user_input in commands:
            try:
                commands[user_input](ssh_client)
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        else:
            print("Неправильная команда, попробуйте снова.")

if __name__ == "__main__":
    main()

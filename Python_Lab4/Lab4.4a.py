ignore = ['duplex', 'alias', 'Current configuration']

def check_ignore(command, ignore):
    """
    Функция проверяет, содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    """
    return any(word in command for word in ignore)

def config_to_dict(config_file):
    """
    config_file - имя конфигурационного файла
    """
    config_dict = {}
    with open(config_file) as file:
        current_command = None
        for line in file:
            line = line.rstrip()
            if not line or line.startswith('!') or check_ignore(line, ignore):
                continue
            if not line.startswith(' '):
                current_command = line
                config_dict[current_command] = {}
            else:
                sub_command = line.strip()
                if sub_command.startswith(' '):
                    sub_sub_command = sub_command.strip()
                    if isinstance(config_dict[current_command], dict):
                        config_dict[current_command][sub_command].append(sub_sub_command)
                    else:
                        config_dict[current_command] = {sub_command: [sub_sub_command]}
                else:
                    if isinstance(config_dict[current_command], dict):
                        config_dict[current_command][sub_command] = []
                    else:
                        config_dict[current_command] = {sub_command: []}

    return config_dict

config_dict = config_to_dict('config_r1.txt')

for command, subcommands in config_dict.items():
    print(f"{command}:")
    if isinstance(subcommands, dict):
        for subcommand, subsubcommands in subcommands.items():
            print(f"  {subcommand}:")
            for subsubcommand in subsubcommands:
                print(f"    {subsubcommand}")
    else:
        for subcommand in subcommands:
            print(f"  {subcommand}")

import os
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from utils.file import abs_path_from_project


def to_driver_options(context):
    options = UiAutomator2Options()

    # Определение пути к файлу .env в зависимости от контекста
    if context == 'local_emulator':
        env_file = '.env.local_emulator'
    elif context == 'local_real_device':
        env_file = '.env.local_real_device'
    elif context == 'bstack':
        env_file = '.env.bstack'
    else:
        raise ValueError(f"Unsupported context: {context}")

    print(f"Loading environment from {env_file}")  # Отладка

    # Загрузка переменных окружения из указанного файла
    load_dotenv(dotenv_path=env_file)

    remote_url = os.getenv('REMOTE_URL_LOCAL') if context == 'local_emulator' else os.getenv('REMOTE_URL_BS')
    device_name = os.getenv('DEVICE_NAME_EMU') if context == 'local_emulator' else os.getenv('DEVICE_NAME_BS')
    app = os.getenv('APP') if context in ['local_emulator', 'local_real_device'] else os.getenv('BS_APP')

    print(f"Remote URL from environment: {remote_url}")  # Отладка
    print(f"Device Name from environment: {device_name}")  # Отладка
    print(f"App Path from environment: {app}")  # Отладка

    options.set_capability('remote_url', remote_url)
    options.set_capability('deviceName', device_name)
    options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
    options.set_capability('app', abs_path_from_project(app))

    if context == 'bstack':
        options.set_capability(
            'bstack:options', {
                'projectName': 'Wikipedia project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack test',
                'userName': os.getenv('BROWSERSTACK_USER'),
                'accessKey': os.getenv('BROWSERSTACK_KEY'),
            }
        )

    return options

import random
import subprocess
import time
import os

# Базовые символы для пароля
#base58_chars = "12359ABCEGHKMNPQRSabcjfvwd"
base58_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
# Количество символов в пароле S идёт неизменная
password_length = 21

# Время работы 
run = 220000

# Программа
program_path = r"./keyhunt"


def run_auto():
    while True:
        password_str = ''.join(random.choices(base58_chars, k=password_length))

        params = [
            "-m", "minikeys",
            "-C", f"S{password_str}",
            "-f", "good.txt",
            "-s", "0",
            "-t", "5",
            "-n", "0x1000000"
        ]

        try:
            command = [program_path] + params
            process = subprocess.Popen(command)
            time.sleep(run)
            process.terminate()
        except subprocess.CalledProcessError as e:
            print(f"Произошла ошибка при выполнении программы: {e}")
        except Exception as e:
            print(f"Произошла неизвестная ошибка: {e}")

run_auto()

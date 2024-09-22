import random
import subprocess
import time
import os

def run_keyhunt():
    # начало
    Ns = 0x40000000000000000
    # конец
    N =  0x7ff00000000000000
    
    r_start = Ns
    program_path = r"keyhunt.exe"

    #время работы диапазона (в секундах) 
    run = 33
    
    #шаг увеличения
    step = 10000000000000000
    
    #делаем список рядом лежащих файлов
    folder_path = os.getcwd()
    old_files = set(os.listdir(folder_path))
    
    clear = lambda: os.system('cls')

    while True:
        #начало бесконечного цикла
        new_files = set(os.listdir(folder_path))
        diff = new_files - old_files

        #если список изменился напишем сообщение и остановим цикл
        if diff:
           print(f"ЧТО ТО ИЗМЕНИЛОСЬ,ВОЗМОЖНО НАШЛИ!!!")
           break


        if r_start > N:
           #когда пройдёт весь диапазон , уменьшит шаг
           step = step/10
           r_start = Ns
           
        r_end = r_start + step
        r = f"{hex(int(r_start))[2:]}:{hex(int(r_end))[2:]}"
        params = [
            "-m", "rmd160",
            "-f", "unsolvedpuzzles.rmd",
            "-r", r,
            "-l", "compress",
            "-R",
            "-t", "4",
            "-s", "0",
            "-n", "0x1000000",
            "-q",
        ]
        r_start = r_end
        try:
            #составление парметров запуска(как в батнике)
            command = [program_path] + params
            #запуск программы с параметрами
            process = subprocess.Popen(command)
            #ждём указаное время
            time.sleep(run)
            #закрываем программу
            process.terminate()
            clear()
        except subprocess.CalledProcessError as e:
            print(f"Произошла ошибка при выполнении программы: {e}")
        except Exception as e:
            print(f"Произошла неизвестная ошибка: {e}")

run_keyhunt()
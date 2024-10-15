"""
Class for assembling logs
"""
from time import time, localtime, sleep
import os
from threading import Thread, active_count, current_thread
from configuracoes import DEBUG, SALVAR_LOG

if not "logs§" in os.listdir():
    os.mkdir("logs§")

def time_now():
    data = localtime()
    d = data.tm_mday
    mt = data.tm_mon
    y = data.tm_year
    h = data.tm_hour
    m = data.tm_min
    s = data.tm_sec
    return [d, mt, y, h, m, s]

class Log:
    """
    Creates a txt log that stores information along with the machine's local time
    """
    def __init__(self, file:str = "logs§/log"):
        """
        file: File name next to directory
        """
        if file == "logs§/log":
            t = time_now()
            file += f"_{t[2]}_{t[1]:02}_{t[0]:02}-{t[3]:02}:{t[4]:02}:{t[5]:02}"
        if file.find(".txt") == -1:
            file += ".txt"
        self.file = file
        self.name = id(self)
        self.time_initial = time_now()
        self.create_file()

    def create_file(self):
        """
        Create txt file if file does not exist
        """
        if not os.path.isfile(self.file):
            with open(self.file, 'w') as arq:
                t = self.time_initial
                arq.write(f"<log creation> {t[0]:02}/{t[1]:02}/{t[2]} - {t[3]:02}:{t[4]:02}:{t[5]:02}")

        else:
            self.add(text = f"connecting to the log", description = "action")

    def add(self, text:str, description:str = "information"):
        """
        Add the requested text next to the time
        """
        if os.path.isfile(self.file):
            with open(self.file, 'r') as arq:
                old = arq.read()
        else:
            print("The log has been lost!")

        if os.path.isfile(self.file):
            with open(self.file, 'w') as arq:
                t = time_now()
                arq.write(f"{old}\n<{description}> {t[0]:02}/{t[1]:02}/{t[2]} - {t[3]:02}:{t[4]:02}:{t[5]:02} | {text}")
        else:
            print("The log has been lost!")

    def backup(self, new_log:str = "backup_log"):
        """
        Back up the specified log
        new_log: Backup txt name
        """
        if new_log.find(".txt") == -1:
            new_log += ".txt"
        self.add(text = f"Make copy to '{new_log}'", description = "backup")
        with open(self.file, 'r') as arq:
            old = arq.read()
        if not os.path.isfile(new_log):
            with open(new_log, 'w') as arq:
                arq.write(old)

    def read(self):
        """
        Reads the log and returns a dictionary
        """
        self.add(text = f"getting log", description = "action")
        
        with open(self.file, 'r') as arq:
            old = arq.read()
        all_log = old.split("\n")
        
        all_log_dict = {}
        for i in range(len(all_log)):
            all_log[i] = all_log[i].replace("<","").split(">")
            if not all_log[i][0] in all_log_dict:
                all_log_dict[all_log[i][0]] = [all_log[i][1][1:]]
            else:
                all_log_dict[all_log[i][0]].append(all_log[i][1][1:])

        all_log_dict["all"] = old.split("\n")        
        return all_log_dict

    def clean(self):
        """
        Clear the log
        """
        if os.path.isfile(self.file):
            with open(self.file, 'w') as arq:
                t = time_now()
                arq.write(f"<log creation> {t[0]:02}/{t[1]:02}/{t[2]} - {t[3]:02}:{t[4]:02}:{t[5]:02}")
        else:
            print("The log has been lost!")

    def __repr__(self):
        log = self.read()
        t = self.time_initial
        text = f"Log: {self.file}\nCreation Log: {log['log creation'][0]}\nOpen log: {t[0]:02}/{t[1]:02}/{t[2]} - {t[3]:02}:{t[4]:02}:{t[5]:02}\nLines Log: {len(log['all'])}"
        return text

def print_log(texto:str, end:str = "\n") -> None:
    """
    Printa e salva o log
    """
    if DEBUG:
        print(texto, end = end)
    if SALVAR_LOG:
        log.add(texto)

if SALVAR_LOG:
    log = Log()

if __name__ == "__main__":
    my_log = Log()
    log = my_log.read()

from datetime import datetime


class Logger:
    logfile = None

    def __init__(self, file) -> None:
        self.logfile = file

    def log(self, s: str) -> None:
        with open(self.logfile, "a", encoding="utf-8") as lf:
            cur_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
            lf.write(f"{cur_datetime}: {s}\n")

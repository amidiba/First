import json, sys, logging, time
def get_logger(x):
	x=logging.getLogger("x")
	x.setLevel(logging.DEBUG)
	if x.handlers:
		return x
	return x
l=get_logger("l")
h1=logging.StreamHandler(sys.stdout)
h1.setLevel(logging.INFO)
l.addHandler(h1)
h1.setFormatter(logging.Formatter("\033[94m%(asctime)s - %(message)s", datefmt= "%H::%M"))


class JF(logging.Formatter):
    def format(self, record):
        data = {
            "name": record.name,
            "message": record.getMessage(),
            "time": self.formatTime(record, datefmt="%H-%M / %y")
        }
        return json.dumps(data)

h2=logging.FileHandler("m.json")
h2.setFormatter((JF()))
l.addHandler(h2)
l.debug("j")
l.info("info")
l.error("er")

from os import listdir, path
from random import randint
from time import sleep


_ROOT_DIR = ".."
_TEMP_DIR = path.join(_ROOT_DIR, "temp")


def producer(next_coroutine):
	_INPUT_DIR = path.join(_TEMP_DIR, "input")
	files = listdir(_INPUT_DIR)
	for file in files:
		next_coroutine.send(file)
	next_coroutine.close()


def parse(next_coroutine=None):
	print("parse: start")
	try:
		while True:
			file = (yield)
			print("processing {} file".format(file))
			sleep(randint(5, 10))
			next_coroutine.send(file)
	except GeneratorExit:
		print("parse: end")


def load():
	print("load: start")
	try:
		while True:
			file = (yield)
			print("loading {} file".format(file))
			sleep(randint(5, 10))
	except GeneratorExit:
		print("load: end")


pt = load()
pt.__next__()
pf = parse(next_coroutine = pt)
pf.__next__()

producer(pf)

from threading import Thread
from threading import Lock
import time

t_lock = Lock()
db = []

def timer(name, delay, repeat):
	print('start ' + name + '\n')
	
	while repeat > 0:
		time.sleep(delay)
		print(name + ': ' + str(time.ctime()))
		db.append(name + ': ' + str(time.ctime()))
		
		repeat -= 1
	print(name + 'is done')
		
if __name__ == "__main__":
	t1 = Thread(target=timer, args=('timer_1', 2, 5))
	t2 = Thread(target=timer, args=('timer_2', 4, 5))

	t1.start()
	t2.start()
	print('...this is last line of code...')


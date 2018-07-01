import threading
import time 
class AsyncWrite(threading.Thread):
	def __init__(self, text, out):
		threading.Thread.__init__(self)
		self.text = text
		self.out = out

	def run(self):
		f = open(self.out, 'a')
		f.write(self.text + '\n')
		f.close()
		time.sleep(2)
		print('finished background file write to'+self.out)
def main():
	message = input('enter a string to store')
	background = AsyncWrite(message, 'out.txt')
	background.start()
	print('the program can contiune whilel it writes in another thread')
	background.join()
	print('wait until thread was complete')

if __name__ == "__main__":
	main()

import asyncio
from codetiming import Timer
import aiohttp

"""
Anything with the "async" prefix is a "coroutine" (Cooperative sub-routine function) which is an awatable.
Other awaitales are like "task" which is created when you use asyncio.create_task() and "future" object.
You will be then able to use the "await" keyword for these awaitables.

The awaitables can be gathered as a group by using them as a list argument to "asyncio.gather(awaitables)".
They have to be prefixed with await.

-When all gathered tasks are completed, their aggregated return values are returned as a list ordered in accordance with the awaitables list order.
-You can cancel any task in the gather, or even cancel the gather as whole.

"""


async def task(name, work_queue):
	timer = Timer(text=f'Task {name} elasped time: {{:.1f}}')
	while not work_queue.empty():
		# this is needed otherwise it won't work. It seems for queue get/put you always have to use await
		delay = await work_queue.get()
		print(f'Task {name} running')

		timer.start()
		await asyncio.sleep(delay)
		timer.stop()

async def main():
	work_queue = asyncio.Queue()

	for work in [15, 10, 5, 2]:
		await work_queue.put(work) # this is needed otherwise it won't work!

    # Run the tasks
	with Timer(text="\nTotal elapsed time: {:.1f}"):
		# The gather() will do two things, one is to gather the tasks that you create using asyncio.create_task
		# second is it will wait until all these tasks are completed before proceeding
		await asyncio.gather(
			asyncio.create_task(task("one", work_queue)),
			asyncio.create_task(task("two", work_queue)),
			asyncio.create_task(task("three", work_queue)),
			asyncio.create_task(task("four", work_queue)),
		)

	print("I am all done!")  # this should be executed after the asyncio.gather is all done


#----------------------------------------------------------
# A more real world example calling http

async def get_data(name, work_queue):
	timer = Timer(text=f'Task {name} elapsed time: {{:.1f}}')
	async with aiohttp.ClientSession() as session:
		data = []
		while not work_queue.empty():
			url = await work_queue.get()
			print(f'Task {name} getting URL: {url}')
			timer.start()
			async with session.get(url) as response:
				contents = await response.text()
				data.append(contents[:100])
			timer.stop()
		return data

async def get_data_async():
	work_queue = asyncio.Queue()

	for url in [
	"http://google.com",
    "http://yahoo.com",
    "http://linkedin.com",
    "http://apple.com",
	]:
		await work_queue.put(url)

	# Run tasks
	with Timer(text='\nTotal elapsed time: {:.1f}'):
		all_data = await asyncio.gather(
			asyncio.create_task(get_data("One", work_queue)),
			asyncio.create_task(get_data("Two", work_queue)),
		)

	print("All done getting all URLs")
	print(all_data)
if __name__ =='__main__':
	#asyncio.run(main())
	asyncio.run(get_data_async())

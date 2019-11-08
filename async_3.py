"""Now assuming you can only work with blocking code"""

import asyncio
from requests import get
import functools

def legacy_blocking_func(url):
	res = get(url)
	content = res.text
	return content


def run_in_executor(f):
	@functools.wraps(f)
	def inner(*args, **kwargs):
		loop = asyncio.get_running_loop()
		return loop.run_in_executor(None, lambda: f(*args, **kwargs))
	return inner


async def get_url(url):
	return legacy_blocking_func(url)

async def cor_get_url(name, work_queue):
	while not work_queue.empty():
		url = await work_queue.get()
		print(f'{name} getting {url}...')
		resp = await get_url(url)
		print(f"{len(resp)} lines")

	
async def main():
	work_queue = asyncio.Queue()
	for url in [
       "http://google.com",
       "http://yahoo.com",
       "http://linkedin.com",
       "http://apple.com",
       "http://apple.com",
       "http://apple.com",
    ]:
		await work_queue.put(url)	
	# Run task
	await asyncio.gather(
		asyncio.create_task(cor_get_url("One", work_queue)),
		asyncio.create_task(cor_get_url("Two", work_queue)),
	)

if __name__ == '__main__':
	asyncio.run(main())

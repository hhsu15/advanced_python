import asyncio

async def count ():
	print("hello")
	await asyncio.sleep(1)
	print("world")
	return "hello world"

async def main():
	t = asyncio.create_task(count())
	t2 = asyncio.create_task(count())
	res = await asyncio.gather(t, t2) # gather will put the return into a list
	# await asyncio.gather(*(count() for i in range(3)))
	return res

if __name__ == '__main__':
	import time
	s = time.perf_counter()
	result = asyncio.run(main())
	elapsed = time.perf_counter() - s
	print(f'excuted in {elapsed:0.2f} seconds')
	print(result)

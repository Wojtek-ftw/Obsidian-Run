import asyncio



async def fetch1():
    await asyncio.sleep(4)
    return 1




async def main():
    print("Hello")
    task1 = asyncio.create_task(fetch1())   # Starts coroutines
    task2 = asyncio.create_task(fetch1())
    task3 = asyncio.create_task(fetch1())


    results = asyncio.gather(fetch1(),fetch1(),fetch1(),fetch1())   # Note, doesnt cancel other coroutines if one fails.
    print(results)


    r1 = await task1
    r2 = await task2
    r3 = await task3        # Syncs


    print(r1,r2,r3)

# async def foo1():     # ONLY PYTHON 3.11+
#     tasks = []
#     async with asyncio.TaskGroup() as tg:
#         for i, sleeptime in enumerate([1,1,1],start=1):
#             task = tg.create_task(fetch1())
#             tasks.append(task)
#     results = [task.result() for task in tasks]
#     print(results)

async def future_result(future, value):
    await asyncio.sleep(2)  # simulate program doing something
    future.set_result(value)
    print(f"Future value value {value}")

async def foo2():
    loop =  asyncio.get_running_loop()
    future = loop.create_future()

    asyncio.create_task(future_result(future,"Hell Yeah"))

    result = await future   # Note. This will run once the future value is set. This means that the task (e.g. future_result) could still be running.
    print(result)

shared_resource = 0
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock:
        print(f"Start: {shared_resource}")
        shared_resource += 1
        await asyncio.sleep(1)
        print(f"End: {shared_resource}")
        
async def foo3():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))


async def access_resource(semaphore, rid):
    async with semaphore:
        print(f"Acc {rid=}")
        await asyncio.sleep(1)
        print(f"Rel {rid=}")
async def foo4():
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))


async def waiter(event):
    print("Waiting for event to be set")
    await event.wait()
    print("Event has been set")

async def setter(event):
    await asyncio.sleep(2)
    event.set()
    print("Evnet set at setter")

async def foo5():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))


if __name__ == "__main__":
    # asyncio.run(main())     # main() -> Coroutine object -> needs to be awaited.
    # asyncio.run(foo2())
    # asyncio.run(foo3())
    # asyncio.run(foo4())
    asyncio.run(foo5())

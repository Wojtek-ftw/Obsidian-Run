import asyncio
import json
import datetime
import redis.asyncio as redis
import csv

MODEL_WORKER_FLAG = True
DELETE_OLD = True

async def run_model(name, duration, item):
    """Simulate model runtime based on guestimates provided by assessment"""
    await asyncio.sleep(duration)
    item[name] = datetime.datetime.now().isoformat()
    return item

async def model_worker(name, duration, queue, output_queue):
    while MODEL_WORKER_FLAG:
        item = await queue.get()
        processed = await run_model(name, duration, item)
        await output_queue.put(processed)

async def redis_subscriber(input_queue):
    r = redis.Redis(host="redis", port=6379)
    pubsub = r.pubsub()
    await pubsub.subscribe('firehose')

    async for message in pubsub.listen():
        if message['type'] == 'message':
            data = json.loads(message['data'])
            await input_queue.put(data)

async def dispatcher(input_queue, model_queues):
    """Adds the datapackets for each model to analyze"""
    counter = 0
    while True:
        item = await input_queue.get()
        await model_queues['model1'].put(dict(item))
        if DELETE_OLD and model_queues['model1'].qsize() > 2: await model_queues['model1'].get()

        await model_queues['model2'].put(dict(item))
        if DELETE_OLD and model_queues['model2'].qsize() > 2: await model_queues['model2'].get()

        await model_queues['model3'].put(dict(item))
        if DELETE_OLD and model_queues['model3'].qsize() > 2: await model_queues['model3'].get()

        counter += 1

async def output_writer(output_queue):
    with open("output.csv", "w", newline='') as csvfile:
        fieldnames = ["timestamp", "index", "model1", "model2", "model3"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        while True:
            item = await output_queue.get()
            writer.writerow(item)
            csvfile.flush()

async def main():
    input_queue = asyncio.Queue()
    model_queues = {
        "model1": asyncio.Queue(),
        "model2": asyncio.Queue(),
        "model3": asyncio.Queue()
    }
    output_queue = asyncio.Queue()

    await asyncio.gather(
        redis_subscriber(input_queue),
        dispatcher(input_queue, model_queues),
        model_worker("model1", 0.003, model_queues["model1"], output_queue),
        model_worker("model2", 0.25, model_queues["model2"], output_queue),
        model_worker("model3", 1.0, model_queues["model3"], output_queue),
        output_writer(output_queue)
    )

if __name__ == "__main__":
    asyncio.run(main())

import time
import redis
import json
from datetime import datetime
import random

r = redis.Redis(host='redis', port=6379)

index = 0
start_time = time.time()

while time.time() - start_time < 300:  # Run for 5 minutes
    message = {
        "timestamp": datetime.utcnow().isoformat(),
        "index": f"pat{str(index).zfill(9)}"
    }
    r.publish('firehose', json.dumps(message))
    index += 1
    time.sleep(random.uniform(0.002, 0.003))

from prefect import flow, task

@task
def clean_data(data):
    return [d for d in data if d is not None]

@flow
def pipeline():
    return clean_data([1, None, 3])

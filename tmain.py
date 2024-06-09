# poetry run python tmain.py

from tworker import celery_app
import redis

def handle_result(task_id, result):
    print(f"Task {task_id} completed with result: {result}")

if __name__ == '__main__':

    try:
        r = redis.Redis(host='redis', port=6379, db=0)
        r.ping()
        print("Redis connection successfully established.")
    except redis.exceptions.ConnectionError as e:
        print(f"Redis connection error: {e}")


    task = celery_app.send_task('hello_world')
    result = task.get()     # timeout=10

    # task = celery_app.apply_async('hello_world', args=[123, 456], callback=handle_result)
    
    print(f'Result: {result}')

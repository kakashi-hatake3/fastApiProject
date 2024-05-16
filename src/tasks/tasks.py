from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379')


@celery.task
def background_func(username: str = "User"):
    print(f"Hello {username}!!!")


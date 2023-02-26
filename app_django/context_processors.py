from . import models


def task_count(request):
    try:
        count = models.Task.objects.all().count()
    except Exception as error:
        count = 0
        print(f"context_processors.py task_count {error}")

    return dict(task_count=count)


def post_count(request):
    try:
        count_post = models.Post.objects.all().count()
    except Exception as error:
        count_post = 0
        print(f"context_processors.py post_count {error}")

    return dict(count_post=count_post)

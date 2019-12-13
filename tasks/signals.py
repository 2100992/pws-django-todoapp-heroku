from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from tasks.models import TodoItem, Category
from collections import Counter

# def new_count(model, ):

@receiver(m2m_changed, sender=TodoItem.category.through)
def print_signal_info(sender, instance, action, model, **kwargs):
    print()
    print(f'sender = {sender}')
    print(f'instance = {instance}')
    print(f'action = {action}')
    print(f'model = {model.__name__}')
    print(f'kwargs')
    for key, value in kwargs.items():
        print(f'    key = {key}, value = {value}')
    print()


# @receiver(m2m_changed, sender=TodoItem.category.through)
# def task_cats_added(sender, instance, action, model, **kwargs):
#     if action == "post_add":
#         for cat in instance.category.all():
#             slug = cat.slug

#             new_count = 0
#             for task in TodoItem.objects.all():
#                 new_count += task.category.filter(slug=slug).count()

#             Category.objects.filter(slug=slug).update(todos_count=new_count)


@receiver(m2m_changed, sender=TodoItem.category.through)
def task_cats_removed(sender, instance, action, model, **kwargs):
    if action in ["post_remove", "post_add"]:
        cat_counter = Counter()
        
        for cat in Category.objects.all():
            cat_counter[cat.slug] = 0

        for t in TodoItem.objects.all():
            for cat in t.category.all():
                cat_counter[cat.slug] += 1

        for slug, new_count in cat_counter.items():
            Category.objects.filter(slug=slug).update(todos_count=new_count)
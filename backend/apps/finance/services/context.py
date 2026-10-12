from django.db.models import QuerySet

from apps.finance.models import Context
from apps.users.models import User


def get_all_contexts() -> QuerySet[Context]:
    """ FOR DEV Возвращает все контексты из базы данных"""
    return Context.objects.all()


def get_contexts(*, user: User) -> QuerySet[Context]:
    # Возвращает все контексты конкретного пользователя
    return Context.objects.filter(
        user=user,
        is_archived=False,
    )


def get_context(*, user: User, context_id: int) -> Context:
    # Возвращает конкретный контекст конкретного пользователя по ID
    return Context.objects.get(
        id=context_id,
        user=user,
        is_archived=False,
    )


def create_context(*, user: User, data: dict) -> Context:
    # Создаёт контекст для конкретного пользователя
    return Context.objects.create(
        user=user,
        **data,
    )


def update_context(*, context: Context, data: dict) -> Context:
    # Обновляет переданные поля контекста
    for field, value in data.items():
        setattr(context, field, value)

    context.save()
    return context


def archive_context(*, context: Context) -> Context:
    # Архивирует контекст, не удаляя его из бд
    context.is_archived = True
    context.save(update_fields=["is_archived", "updated_at"])
    return context

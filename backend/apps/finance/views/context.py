from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.finance.models import Context
from apps.finance.serializers.context import ContextSerializer
from apps.finance.services.context import (
    archive_context,
    create_context,
    get_all_contexts,
    get_context,
    update_context,
)
from apps.users.models import User

"""Временно возвращает первого пользователя для тестирования."""
def get_first_user_development():
    return User.objects.first()


# Просмотр списка контекстов и создание нового
class ContextListCreateView(APIView):

    def get(self, request):
        contexts = get_all_contexts()
        serializer = ContextSerializer(contexts, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ContextSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_first_user_development()

        if user is None:
            return Response(
                {"detail": "Сначала необходимо создать пользователя."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        context = create_context(
            user=user,
            data=serializer.validated_data,
        )

        return Response(
            ContextSerializer(context).data,
            status=status.HTTP_201_CREATED,
        )


# Получение, обновление и архивирование одного контекста
class ContextDetailView(APIView):

    def get_context_object(self, context_id):
        user = get_first_user_development()

        if user is None:
            return None

        try:
            return get_context(user=user, context_id=context_id)
        except Context.DoesNotExist:
            return None

    def get(self, request, context_id):
        context = self.get_context_object(context_id)

        if context is None:
            return Response(
                {"detail": "Контекст не найден."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ContextSerializer(context)
        return Response(serializer.data)

    def patch(self, request, context_id):
        context = self.get_context_object(context_id)

        if context is None:
            return Response(
                {"detail": "Контекст не найден."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ContextSerializer(
            context,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        context = update_context(
            context=context,
            data=serializer.validated_data,
        )

        return Response(ContextSerializer(context).data)

    def delete(self, request, context_id):
        context = self.get_context_object(context_id)

        if context is None:
            return Response(
                {"detail": "Контекст не найден."},
                status=status.HTTP_404_NOT_FOUND,
            )

        archive_context(context=context)

        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import serializers

from apps.finance.models import Context


class ContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Context
        fields = [
            "id",
            "name",
            "description",
            "color",
            "icon",
            "is_archived",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "is_archived",
            "created_at",
            "updated_at",
        ]

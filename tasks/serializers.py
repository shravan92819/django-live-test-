from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    title = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Title is required",
            "blank": "Title cannot be empty",
        }
    )

    status = serializers.CharField(required=False)

    def validate_title(self, value):
        raw_value = self.initial_data.get("title")

        if not isinstance(raw_value, str):
            raise serializers.ValidationError("Title must be a string")

        return value

    def validate_status(self, value):
        valid_statuses = ["Pending", "Completed"]
        if value not in valid_statuses:
            raise serializers.ValidationError(
                "Status must be either Pending or Completed"
            )
        return value

    class Meta:
        model = Task
        fields = "__all__"

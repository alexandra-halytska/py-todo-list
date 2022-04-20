from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "tag"

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        ordering = [
            "status",
            "-created_at"
            ]
        db_table = "task"

    def __str__(self):
        return f"{self.tag.name} - {self.content}"

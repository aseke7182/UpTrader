from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children', on_delete=models.CASCADE
    )

    def to_json_without_child(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'parent_id': self.parent.id if self.parent else 'orphan_id',
            'parent_name': self.parent.name if self.parent else 'orphan',
            'children': [
                i.to_json_without_child() for i in self.children.all()
            ]
        }

    def __str__(self):
        return self.name

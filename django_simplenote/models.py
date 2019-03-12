from django.db import models
from .settings import get_setting


class Note(models.Model):
    """Represents a note."""
    content = models.TextField()

    def save(self, *args, **kwargs):
        max_length = get_setting('SIMPLENOTE_MAX_NOTE_LENGTH')
        max_notes = get_setting('SIMPLENOTE_MAX_NOTES')
        if len(self.content) > max_length:
            self.content = self.content[:max_length]
        notes = list(Note.objects.all())
        excess_notes = len(notes) + 1 - max_notes
        if self in notes:
            excess_notes -= 1
        if excess_notes >= 0:
            for n in notes[0:excess_notes]:
                n.delete()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

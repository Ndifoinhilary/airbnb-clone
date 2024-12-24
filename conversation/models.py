from django.db import models
from core import  models as core_models
# Create your models here.



class Conversation(core_models.TimeStampedModel):
    """
    Conversation model Definition
    """
    participants = models.ManyToManyField("users.User")





class Message(core_models.TimeStampedModel):
    """
    Message model Definition
    """
    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("conversation.Conversation", on_delete=models.CASCADE)

    def __str__(self):
        return self.message

from django.db.models.signals import post_save
from django.dispatch import receiver
from firstapp.models import Profile
from django.contrib.auth.models import User

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('profile created')

@receiver(post_save,sender=User)
def update_profile(sender,instance,created,**kwargs):
    if created==False:
        instance.profile.save()
        print('profile updated')
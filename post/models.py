from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    content = models.TextField()

    image = models.ImageField(upload_to='blog', 
            null=True, 
            blank=True, 
            )
    # height_field = models.IntegerField(default=0)
    # width_field = models.IntegerField(default=0)
 
    # draft = models.BooleanField(default=False)

    
    # read_time =  models.IntegerField(default=0) # models.TimeField(null=True, blank=True) #assume minutes
    # updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)
from django.db import models
from services.mixin import SlugMixin, DateMixin
from services.generator import Generator
from services.uploader import Uploader
from django.contrib.auth import get_user_model 
from services.extract import extract_google_maps_url_from_iframe


SOCIAL_CHOICES = (
    ("insta", "Instagram"),
    ("fb", "Facebook"),
    ("wp", "WhatsApp"),
    ("twitter", "Twitter"),
    ("linkedin", "Linkedin"),
    ("tiktok", "Tiktok")
)

User = get_user_model()



COUNTRY_CHOICES = (
    ("usa", "Amerika"),
    ("az", "Azerbaijan"),
    ("eu", "Europa"),
    ("as", "Asia"),
    
    
)

# User = get_user_model()


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 255,verbose_name = 'adi')


    def __str__(self):
        return self.name


    class Meta:
     ordering = ('-created_at',)
     verbose_name = 'category'
     verbose_name_plural = 'categories'








class Color(models.Model):
      name = models.TextField(verbose_name = 'mehsulun rengi')


      def __str__(self):
        return self.name

      class Meta:
       ordering = ('-created_at',)
       verbose_name = 'reng'
       verbose_name_plural = 'rengler'


        

class Size(models.Model):
      name = models.TextField(verbose_name = 'mehsulun olcusu')

      def __str__(self):
        return self.name

      class Meta:
       ordering = ('-created_at',)
       verbose_name = 'olcu'
       verbose_name_plural = 'olculer'

 


class Product(SlugMixin, DateMixin):
     category = models.ForeignKey(Category,on_delete = models.SET_NULL,null = True,blank = True)
     name = models.CharField(max_length = 255,verbose_name = 'mehsulun adi')
     price = models.FloatField(verbose_name ='mehsulun qiymeti')
     description_L = models.TextField(verbose_name = 'kicik movzu')
     description_B = models.TextField(verbose_name = 'boyuk movzu')
     rating = models.FloatField(verbose_name = 'reyting')
     information = models.TextField(verbose_name = 'mehsul haqqinda')
     color = models.ManyToManyField(Color,verbose_name='reng')
     size = models.ManyToManyField(Size,verbose_name= 'olcu')
     is_seen = models.BooleanField(default = False)

     def __str__(self):
        return self.name

     class Meta:
       ordering = ('-created_at',)
       verbose_name = 'mehsul'
       verbose_name_plural = 'mehsullar'

    

    # partniors model yalniz image fild 
    # contact modeli form ve istifadeci yalniz 20 den az yaza bilr subject
    # chekout modeli
    # base.html
        
class Partniors(DateMixin):
      image = models.ImageField(upload_to=Uploader.upload_photo_partniors,null=True,blank=True)
      
      def __str__(self):
        return f'{self.created_at}'

      class Meta:
       ordering = ('-created_at',)
       verbose_name = 'partnior sekil'
       verbose_name_plural = 'partnior sekiller'


class Contact(SlugMixin, DateMixin):
       
    name = models.CharField(max_length=255,verbose_name='ad ve soyad')
    email = models.CharField(max_length=255,verbose_name='email adress')
    subject = models.CharField(max_length=255,verbose_name='movzu')
    mesage = models.TextField(verbose_name='mesaj')
    
    
   
    def __str__(self):
        return self.name
    
    class Meta:

     ordering = ('name',)
     verbose_name = 'contact'
     verbose_name_plural = 'contactlar'



class Checkout(SlugMixin, DateMixin):
       name = models.CharField(max_length = 255,verbose_name = 'ad')
       surname = models.CharField(max_length = 255,verbose_name = 'soyad')
       email = models.CharField(max_length = 255,verbose_name = 'email')
       phone = models.CharField(max_length = 255, verbose_name = 'telefon')
       adress1 = models.CharField(max_length = 255, verbose_name = 'adress 1')
       adress2 = models.CharField(max_length = 255, verbose_name = 'adress 2')
       country = models.CharField(max_length=255,verbose_name='olke adlari',choices=COUNTRY_CHOICES)
       city = models.CharField(max_length = 255,verbose_name = 'sheher adi')
       state  = models.CharField(max_length = 255,verbose_name = 'dovlet')
       zipcode = models.CharField(max_length = 255, verbose_name = 'olke kodu')

       def __str__(self):
         return self.name
    
       class Meta:
        ordering = ('name',)
        verbose_name = 'checkout'
        verbose_name_plural = 'checkout'
        

 

class ProductImage(SlugMixin, DateMixin):
       product = models.ForeignKey(Product,on_delete = models.SET_NULL,null = True,blank = True)

       def __str__(self):
         return self.product.name
    
       class Meta:
        ordering = ('-created_at',)
        verbose_name = 'mehsul shekili'
        verbose_name_plural = 'mehsul shekilleri'




class Comment(DateMixin):
    text = models.TextField(verbose_name="User's comment")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.text[:10]

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Rey"
        verbose_name_plural = "Reyler"

   

class SpecialOffer(SlugMixin, DateMixin):
    text = models.TextField(verbose_name="metn")
    discount = models.TextField(verbose_name = 'endirim')
    image = models.ImageField(upload_to=Uploader.upload_photo_special_offer,null=True,blank=True)

    def __str__(self):
        return self.discount

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "xususi teklif"
        verbose_name_plural = "xususi teklifler"

    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=SpecialOffer)
        super(SpecialOffer, self).save(*args, **kwargs)


class Slider(SlugMixin, DateMixin):
       image = models.ImageField(upload_to=Uploader.upload_photo_slider,null=True,blank=True)
       title = models.CharField(max_length = 255, verbose_name = 'basliq')
       text = models.TextField(verbose_name="metn")

       def __str__(self):
         return self.title
    
       class Meta:
        ordering = ('-created_at',)
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'

       def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=Slider)
        super(Slider, self).save(*args, **kwargs)


class Basket(SlugMixin, DateMixin):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True, blank=True)
    count = models.IntegerField()
    total_price = models.FloatField(null=True, blank=True)

    def __str__(self):
          return self.user.first_name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "sebet"
        verbose_name_plural = "sebetler"

    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=Basket)
        super(Basket, self).save(*args, **kwargs)

   
        
class SignUp(DateMixin):
    email = models.CharField(max_length = 255,verbose_name = 'email')

    def __str__(self):
        return self.email
    


class SosialMedia(SlugMixin, DateMixin):
    sosial_name = models.CharField(max_length=255,verbose_name='sosial media hesabi',choices=SOCIAL_CHOICES)
    sosial_link = models.TextField(verbose_name='sosial media linki')

    def __str__(self):
        return self.sosial_name

    class Meta:
        ordering = ("sosial_name", )
        verbose_name = "sosial media hesabi"
        verbose_name_plural = "sosial media hesablari"

    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=SosialMedia)
        super(SosialMedia, self).save(*args, **kwargs)




class MainDetails(SlugMixin, DateMixin):
    email = models.EmailField(verbose_name='Email')
    adresss = models.CharField(max_length=255,verbose_name='adress' )
    phones = models.CharField(max_length=255,verbose_name='phones')
    locations = models.TextField(verbose_name='locations',null=True,blank=True)
    
  
    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "elaqe melumati"
        verbose_name_plural = "elaqe melumatlari"


    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=MainDetails)
        super(MainDetails, self).save(*args, **kwargs)
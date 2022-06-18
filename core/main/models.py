from django.db import models

# Create your models here.

class Home(models.Model):
    name = models.CharField('Home name', max_length=50)
    about = models.TextField('Home about')
    img1 = models.ImageField('Home img1', upload_to='media')
    img2 = models.ImageField('Home img2', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'



class HomeProduct(models.Model):
    name = models.CharField('HomeProduct name', max_length=50)
    name2 = models.CharField('HomeProduct name2', max_length=50, null=True)
    price = models.IntegerField('HomeProduct price')
    price2 = models.IntegerField('HomeProduct price2', null=True)
    img = models.ImageField('HomeProduct img', upload_to='media')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeProduct'
        verbose_name_plural = 'HomeProducts'




class HomeProduct1(models.Model):
    img = models.ImageField('HomeProduct1 img', upload_to='media')
    name = models.CharField('HomeProduct1 name', max_length=50)
    price = models.IntegerField('HomeProduct1 price')
    
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeProduct1'
        verbose_name_plural = 'HomeProducts1'




class HomeProduct2(models.Model):
    img = models.ImageField('HomeProduct2 img', upload_to='media')
    name = models.CharField('HomeProduct2 name', max_length=50)
    price = models.IntegerField('HomeProduct2 price')
    
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeProduct2'
        verbose_name_plural = 'HomeProducts2'




class Eror404(models.Model):
    img1 = models.ImageField('Eror 404 img1', upload_to='media',null=True)
    img2 = models.ImageField('Eror 404 img2', upload_to='media', null=True)
    name1 = models.CharField('Eror 404 name1', max_length=50)
    about = models.TextField('Eror 404 about')
    name2 = models.CharField('Eror 404 name2', max_length=50)
    

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'Eror 404'
        verbose_name_plural = 'Erors 404'



class Checkout(models.Model):
    about = models.TextField('Checkout about')
    img1 = models.ImageField('Checkout img1', upload_to='media')
    img2 = models.ImageField('Checkout img2', upload_to='media')
    img3 = models.ImageField('Checkout img3', upload_to='media')
    
    

    def __str__(self):
        return self.about

    class Meta:
        verbose_name = 'Chekcout'
        verbose_name_plural = 'Chekcouts'



class Footer(models.Model):
    about = models.TextField('Footer about')
    img = models.ImageField('Footer img', upload_to='media')
    name1 = models.CharField('Footer name1', max_length=50)
    name2 = models.CharField('Footer name2', max_length=50)

    
    

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footers'
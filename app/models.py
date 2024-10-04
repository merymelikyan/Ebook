from django.db import models


class HeaderText (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    
 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Header Text"
        verbose_name_plural = "Header Texts"
 
class PhonImage(models.Model):
    image = models.ImageField(upload_to="phon_image")

    def __str__(self):
        return str(self.image)
    

class FooterText(models.Model):
    text1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.CharField(max_length=255, blank=True, null=True)
    link_url = models.URLField(max_length=200, blank=True, null=True) 

    def __str__(self):
        return f"{self.text1} {self.text2}"

    class Meta:
        verbose_name = "Footer Text"
        verbose_name_plural = "Footer Text"


  
class Avatars(models.Model):
    image = models.ImageField(upload_to="avatars")

    def __str__(self):
        return str(self.image)
 
    
    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatars"

class Reviews(models.Model):
    stars = models.CharField(max_length=40, blank=True, null=True)
    reviews_class1  = models.CharField(max_length=40, blank=True, null=True)
    reviews_class2  = models.CharField(max_length=40, blank=True, null=True)
    reviews_class3 = models.CharField(max_length=40, blank=True, null=True)
    reviews_class4  = models.CharField(max_length=40, blank=True, null=True)
    reviews_class5  = models.CharField(max_length=40, blank=True, null=True)
    total = models.CharField(max_length=40, blank=True, null=True) # To store the total number of reviews (e.g., 2,564)

    def __str__(self):
        return self.total
    
    class Meta:
        verbose_name = "Reviews"
        verbose_name_plural = "Reviews"


class Modern(models.Model):
    image = models.ImageField(upload_to="tablet")
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text1 = models.CharField(max_length=255, blank=True, null=True)
    link_url = models.URLField(max_length=200, blank=True, null=True) 
    link_name = models.CharField(max_length=255)
    text2 = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Modern"
        verbose_name_plural = "Modern"


class Inside(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Inside"
        verbose_name_plural = "Inside"



class Charters(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255) 
    html_url = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Charters"
        verbose_name_plural = "Charters"


class Introducing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    quastion = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    blockquote = models.TextField(max_length=255)
    note = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.title} - {self.blockquote}"

    class Meta:
        verbose_name = "Introducing"
        verbose_name_plural = "Introducing"


class Winback(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.TextField(max_length=255, blank=True, null=True)
    description2 = models.TextField(max_length=255, blank=True, null=True)
    description3 = models.TextField(max_length=255, blank=True, null=True)
    image1 = models.ImageField(upload_to="winback", blank=True, null=True)
    image2 = models.ImageField(upload_to="winback", blank=True, null=True)
    note = models.TextField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Winback"
        verbose_name_plural = "Winback"

class Workless(models.Model):
    title = models.CharField(max_length=255)
    text1 = models.CharField(max_length=255)
    link_url = models.URLField(max_length=200, blank=True, null=True) 
    link_name = models.CharField(max_length=255)
    text2 = models.CharField(max_length=255)
    description1 = models.TextField(max_length=255, blank=True, null=True)
    description2 = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="tablet")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Workless"
        verbose_name_plural = "Workless"


class Modernebook(models.Model):
    title= models.TextField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Modernebook"
        verbose_name_plural = "Modernebook"


class Delegate(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.TextField(max_length=255)
    description2 = models.TextField(max_length=255, blank=True, null=True)
    description3 = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="bloks")
    note = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Delegate"
        verbose_name_plural = "Delegate"

class Habits(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.TextField(max_length=255, blank=True, null=True)
    description2 = models.TextField(max_length=255, blank=True, null=True)
    quastion = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    blockquote = models.TextField(max_length=255)
    note = models.TextField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Habits"
        verbose_name_plural = "Habits"

class MeetAuther(models.Model):
    image = models.ImageField(upload_to="auther")
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description1 = models.TextField(max_length=255, blank=True, null=True)
    description2 = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Meet Auther"
        verbose_name_plural = "Meet Auther"


      
class AllReviews(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "All Reviews"
        verbose_name_plural = "All Reviews"


class ReviewsMembers(models.Model):   
    name = models.CharField(max_length=45)
    position = models.CharField(max_length=60)
    image = models.ImageField(upload_to="reviews_members")
    stars = models.CharField(max_length=40, blank=True, null=True)
    reviews_class1  = models.CharField(max_length=40, blank=True, null=True)
    reviews_class2  = models.CharField(max_length=40, blank=True, null=True)
    reviews_class3 = models.CharField(max_length=40, blank=True, null=True)
    reviews_class4  = models.CharField(max_length=40, blank=True, null=True)
    reviews_class5  = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name}{self.stars}"
    
    class Meta:
        verbose_name = "Reviews Members"
        verbose_name_plural = "Reviews Members"


class ContactsName(models.Model):
    tag = models.CharField(max_length=255,blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Contacts Name"
        verbose_name_plural = "Contacts Name"


class Contact(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
   

    def __str__(self):
        return f"{self.address} | {self.email} | {self.phone}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class SocialsName(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Socials Name"
        verbose_name_plural = "Socials Name"


class Socials(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=255, blank=True)
    html_class = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"



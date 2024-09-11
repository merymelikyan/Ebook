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
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

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
    stars = models.FloatField()  # To store the average star rating (e.g., 4.5)
    total = models.FloatField()  # To store the total number of reviews (e.g., 2,564)

    def __str__(self):
        return f"{self.stars} | {self.total} reviews"
    
    class Meta:
        verbose_name = "Reviews"
        verbose_name_plural = "Reviews"


class Modern(models.Model):
    image = models.ImageField(upload_to="tablet")
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text1 = models.CharField(max_length=255)
    link_url = models.URLField(max_length=200, blank=True, null=True) 
    link_name = models.CharField(max_length=255)
    text2 = models.CharField(max_length=255)
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


class ContentBlock(models.Model):
    title = models.CharField(max_length=255)  # Title of the block (e.g., Introduction, Chapter 1)
    url = models.URLField(max_length=200, blank=True, null=True)  # Optional URL for the content
    order = models.PositiveIntegerField(default=0)  # Order of the block
    description = models.TextField(blank=True, null=True)  # Optional description or content

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Content Block"
        verbose_name_plural = "Content Block"


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
    note = models.TextField(max_length=255)

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
        verbose_name = "MeetAuther"
        verbose_name_plural = "MeetAuther"


      
class AllReviews(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "AllReviews"
        verbose_name_plural = "AllReviews"


class ReviewsMambers(models.Model):   
    name = models.CharField(max_length=45)
    position = models.CharField(max_length=60)
    image = models.ImageField(upload_to="reviews_mambers")
    stars = models.FloatField()  # To store the average star rating (e.g., 4.5)
    description = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.name}{self.stars}"
    
    class Meta:
        verbose_name = "ReviewsMemrers"
        verbose_name_plural = "ReviewsMembers"


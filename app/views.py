from django.shortcuts import render

from .models import (
    HeaderText,
    PhonImage,
    FooterText, 
    Avatars,
    Reviews,
    Modern,
    Inside,
    ContentBlock,
    Introducing,
    Winback,
    Workless,
    Modernebook,
    Delegate,
    Habits,
    MeetAuther,
    AllReviews,
    ReviewsMambers
)    

def index(request):
    context = {
          "header_text": HeaderText.objects.all(),
          "phon_image": PhonImage.objects.all().first(),
          "footer_text": FooterText.objects.all().first(),
          "avatars": Avatars.objects.all(),
          "reviews": Reviews.objects.all().first(),
          "modern": Modern.objects.all().first(),
          "inside": Inside.objects.all().first(),
          "content_block": ContentBlock.objects.all(),
          "introducing": Introducing.objects.all().first(),
          "winback": Winback.objects.all().first(),
          "workless": Workless.objects.all().first(),
          "modernebook": Modernebook.objects.all().first(),
          "delegate": Delegate.objects.all().first(),
          "habits": Habits.objects.all().first(),
          "meetauther": MeetAuther.objects.all().first(),
          "allreviews": AllReviews.objects.all().first(),
          "reviews_mambers": ReviewsMambers.objects.all()
      }      

    return render(request,"base.html" , context)


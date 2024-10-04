from django.shortcuts import render

from .models import (
    HeaderText,
    PhonImage,
    FooterText, 
    Avatars,
    Reviews,
    Modern,
    Inside,
    Charters,
    Introducing,
    Winback,
    Workless,
    Modernebook,
    Delegate,
    Habits,
    MeetAuther,
    AllReviews,
    ReviewsMembers,
    ContactsName,
    Contact,
    SocialsName,
    Socials
)    
 
def index(request):
    context = {
          "header_text": HeaderText.objects.all(),
          "phon_image": PhonImage.objects.all().first(),
          "footer_text": FooterText.objects.all().first(),
          "avatars": Avatars.objects.all(),
          "reviews": Reviews.objects.all(),
          "modern": Modern.objects.all().first(),
          "inside": Inside.objects.all().first(),
          "charters" : Charters.objects.all(),
          "introducing": Introducing.objects.all().first(),
          "winback": Winback.objects.all().first(),
          "workless": Workless.objects.all().first(),
          "modernebook": Modernebook.objects.all().first(),
          "delegate": Delegate.objects.all().first(),
          "habits": Habits.objects.all().first(),
          "meetauther": MeetAuther.objects.all().first(),
          "allreviews": AllReviews.objects.all().first(),
          "reviews_members": ReviewsMembers.objects.all(),
          "contactsname" : ContactsName.objects.all().first(),
          "contact" : Contact.objects.all().first(),
          "socialsname" : SocialsName.objects.all().first(),
          "socials" : Socials.objects.all()
      }      

    return render(request,"home.html" , context)




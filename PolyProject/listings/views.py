from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from listings.models import Listing
from django.core.urlresolvers import reverse
from django.core.mail import EmailMessage

def getEmbed(url):
    videoID = url.partition("=")[2]
    if(videoID != ""):
        embedVideo = "<iframe width=\"560\" height=\"315\" src=\"//www.youtube.com/embed/" + videoID + "\" frameborder=\"0\" allowfullscreen></iframe>"
    else:
        embedVideo = ""
    return embedVideo

def index(request):
    listing_list = Listing.objects.order_by('-dateAdded')
    context = {'listing_list': listing_list}
    return render(request, 'listings/index.html', context)

def detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    listing.video = getEmbed(listing.video)
    return render(request, 'listings/detail.html', {'listing':listing})

def edit(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, 'listings/edit.html', {'listing':listing})

def editPost(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    if('delete' in request.POST):
        listing.delete()
        return redirect(reverse('index'))
    elif('edit' in request.POST):
        listing.firstname = request.POST['firstname']
        listing.lastname = request.POST['lastname']
        listing.title = request.POST['title']
        listing.description = request.POST['description']
        listing.skillsNeeded = request.POST['skills']
        listing.email = request.POST['email']
        editedImage = request.FILES.get('image')
        if(editedImage):
            listing.image = editedImage
        listing.video = request.POST.get('video')
        listing.save()
    return redirect(reverse('detail', args=(listing.id,)))
    
def createlisting(request):
    userEmail = request.POST['email'];
    listingTitle = request.POST['title'];

    l = Listing(firstname=request.POST['firstname'],lastname=request.POST['lastname'],
        title=listingTitle, description=request.POST['description'], 
        skillsNeeded=request.POST['skills'], dateAdded=timezone.now(),
        email=userEmail, image=request.FILES.get('image'), 
        video=request.POST.get('video'))
    l.save()

    email = EmailMessage(listingTitle+" Listing",
     "Use the following link to edit or delete your listing: http://127.0.0.1:8000/listings/edit/"+str(l.id),
     to=[userEmail])
    email.send()

    return redirect(reverse('detail', args=(l.id,)))

def create(request):
    return render(request, 'listings/create.html')

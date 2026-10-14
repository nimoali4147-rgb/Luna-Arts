from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import PhotoReaction
from .forms import UserProfileForm
from .models import UserProfile
# Create your views here.


from .models import Photo, Tag


def home(request):
    photos = Photo.objects.all().order_by('-created_at')
    tags = Tag.objects.all()

    return render(
        request,
        'home.html',
        {
            'photos': photos,
            'tags': tags,
        }
    )


@login_required(login_url='login')
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        user_form = ProfileUpdateForm(
            request.POST,
            instance=request.user
        )

        bio_form = UserProfileForm(
            request.POST,
            instance=profile
        )

        if user_form.is_valid() and bio_form.is_valid():
            user_form.save()
            bio_form.save()

            messages.success(
                request,
                'Your profile has been updated successfully!'
            )
            return redirect('profile')

    else:
        user_form = ProfileUpdateForm(instance=request.user)
        bio_form = UserProfileForm(instance=profile)

    return render(
        request,
        'profile.html',
        {
            'form': user_form,
            'bio_form': bio_form,
        }
    )


def change_password_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = PasswordChangeForm(
            request.user,
            request.POST
        )

        if form.is_valid():
            user = form.save()

            update_session_auth_hash(request, user)

            messages.success(
                request,
                'Your password has been changed successfully.'
            )

            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)

    return render(
        request,
        'change_password.html',
        {'form': form}
    )


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                'Welcome to Luma Art! Your account has been created.'
            )
            return redirect('home')
    else:
        form = RegisterForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Welcome back to Luma Art!')
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(
        request,
        'login.html',
        {'form': form}
    )


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have logged out successfully.')

    return redirect('login')


def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)

    likes_count = photo.reactions.filter(
        reaction='like'
    ).count()

    dislikes_count = photo.reactions.filter(
        reaction='dislike'
    ).count()

    return render(
        request,
        'photo_detail.html',
        {
            'photo': photo,
            'likes_count': likes_count,
            'dislikes_count': dislikes_count,
        }
    )

def filter_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)

    photos = Photo.objects.filter(
        tags=tag
    ).order_by('-created_at')

    tags = Tag.objects.all()

    return render(
        request,
        'home.html',
        {
            'photos': photos,
            'tags': tags,
            'selected_tag': tag,
        }
    )



@login_required(login_url='login')
@require_POST
def photo_reaction_view(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)

    reaction = request.POST.get('reaction')

    if reaction not in [
        PhotoReaction.LIKE,
        PhotoReaction.DISLIKE,
    ]:
        messages.error(request, 'Invalid reaction.')
        return redirect('photo_detail', photo_id=photo.id)

    existing_reaction = PhotoReaction.objects.filter(
        user=request.user,
        photo=photo,
    ).first()

    if existing_reaction:
        if existing_reaction.reaction == reaction:
            # Clicking the same reaction removes it
            existing_reaction.delete()
        else:
            # Switch from like to dislike, or vice versa
            existing_reaction.reaction = reaction
            existing_reaction.save()
    else:
        # Create a reaction only if one does not exist
        PhotoReaction.objects.create(
            user=request.user,
            photo=photo,
            reaction=reaction,
        )

    return redirect('photo_detail', photo_id=photo.id)

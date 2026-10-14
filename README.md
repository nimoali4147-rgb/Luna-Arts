# Luma Art – Photo Gallery

Luma Art is a Django photo gallery website where users can browse photos, view photo details, filter photos by tags, and like or dislike photos. Users can also register, log in, and manage their profiles.

## Features
- User registration and login
- User profiles with bio
- Photo gallery and photo details
- Filter photos by tags
- Like and dislike photos
- Upload and manage photos through Django Admin

## Project Structure

```text
photo_gallary/
├── manage.py
├── photo_gallary/
│   ├── settings.py
│   └── urls.py
├── photoapp/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
├── static/
│   └── css/
├── media/
└── README.md
```

## How It Works

- **Models:** Store photos, tags, user profiles, and reactions.
- **Views:** Handle gallery display, authentication, filtering, and photo reactions.
- **Forms:** Handle user registration and profile updates.
- **URLs:** Connect website pages to their views.
- **Templates:** Display the website interface using HTML and Tailwind CSS.
- **Admin:** Allows administrators to upload and manage photos and tags.
- **Static and Media:** Store CSS files and uploaded photos.

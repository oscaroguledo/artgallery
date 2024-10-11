
# Art Gallery App

## Overview

The **Art Gallery App** is a Django-based application designed to showcase and manage different forms of artwork. It allows users to upload and view various types of art, including paintings, drawings, and NFTs. The platform also features user profile management, search functionality, and an art gallery interface for viewing and organizing artwork.

## Features

- **User Profiles**: Users can create and edit profiles with details such as name, email, phone number, country, and profile picture.
- **Art Upload**: Users can upload artwork, including images, titles, and types of art (painting, drawing, NFTs, etc.).
- **Attachments**: Additional images or attachments can be added to existing artworks.
- **Art Gallery**: View, filter, and search artwork by type, name, artist, or upload date.
- **Search Functionality**: Users can search the gallery by keywords related to the artwork or artist.
- **Pagination**: Supports paginated browsing of artwork.

## Technologies Used

- **Backend**: Django 4.x
- **Frontend**: HTML, CSS (Django Templates)
- **Database**: SQLite (default, can be switched to PostgreSQL or MySQL)
- **Authentication**: Custom user model with Django's built-in authentication
- **Media Handling**: Django's ImageField for uploading and storing images

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/art-gallery.git
   cd art-gallery
   ```

2. **Set up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

## Usage

### 1. **Access the App**:
   - Open your browser and go to `http://127.0.0.1:8000/`.

### 2. **User Profiles**:
   - Register an account or log in.
   - Access and edit your profile.

### 3. **Uploading Artwork**:
   - Go to the upload section and submit your artwork along with an image.
   - Add attachments to existing artwork.

### 4. **Viewing the Gallery**:
   - Explore different categories like paintings, drawings, and NFTs.
   - Use the search bar to find specific art by artist name, title, or type.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

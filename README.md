# Bitesize-Church-Colshaw

## Project Prompt

Create a single page website for Bitesize Church, a friendly and welcoming community church based in Colshaw. The site should have the following sections: a warm hero section with a tagline and call to action, an about section explaining what Bitesize Church is, a Bitesize Brunch section explaining their monthly get-together events, an events section showing upcoming 2026 brunch dates, a visit us section with location and what to expect when you arrive, and a contact section with a simple enquiry form. The tone should be friendly, warm and inclusive. The brand colours are red, golden yellow and white.

## Website Technology and Content Management

This project is designed to create a single-page website for Bitesize Church, a friendly and welcoming community church based in Colshaw.

### Why use Python and Django?

- **Django** is a powerful Python web framework that includes a built-in admin interface, making it easy for non-coders to update website content (such as events, about info, and brunch details) through a user-friendly dashboard.
- You can learn web development and Python by building the site and defining models for each content type (e.g., events, brunches, about section).
- The church owner or other team members can log in to the Django admin panel to update content without touching any code.
- The website automatically updates to show new or changed content, so no coding is required for regular updates.
- This approach is robust, customizable, and future-proof, combining a great learning experience with easy content management for the future.

### Workflow Summary

1. Build the website using Django and Python.
2. Define models for each content section (events, brunches, about, etc.).
3. Use the Django admin panel to manage and update content.
4. The site updates automatically as content is changed in the admin area.

This setup ensures the site is both a valuable learning project and easy to maintain for non-technical users.

## Latest Updates (21 March 2026)

- Added `home/models.py` with Django/Wagtail models for all homepage sections (hero, about, brunch, events, location, contact, brunch dates, etc.)
- Created `home/templates/home/home_page.html` to render all dynamic content sections using template variables and Wagtail tags
- Ran `python manage.py makemigrations` and `python manage.py migrate` to apply database changes
- Committed and pushed all changes to GitHub

The homepage is now fully dynamic and editable via the Django/Wagtail admin interface, allowing non-coders to update all content easily.
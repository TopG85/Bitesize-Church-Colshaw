# Bitesize-Church-Colshaw

## Project Overview

This is a single-page website for Bitesize Church, a friendly and welcoming community church based in Colshaw. The site is built with Django, Wagtail, and Tailwind CSS, and is fully editable via the Wagtail admin interface.

## Key Features & Recent Updates (March 2026)

- **Favicon:** Added a favicon using the church logo (`382980107_153910111126206_2093967587040039248_n.webp`).
- **Logo:** The logo is now used in the navbar and as the favicon for consistent branding.
- **Hero Section:** Features a large hero image, lowercase h1, and a call-to-action button.
- **About Section:** Explains what Bitesize Church is and what makes it unique.
- **Why Bitesize? Section:** Added a new section explaining the name and approach, with a yellow background matching the contact section.
- **Calendar Section:**
	- Main header uses the "Luckiest Guy" font for a playful look.
	- Calendar cards have rounded corners, 3D drop shadows, and yellow paper-strip backgrounds (SVG) for a desk calendar effect.
	- Calendar dates update automatically for any year (second Sunday of each month).
- **Contact Section:**
	- Styled with a yellow background and red accents.
	- Includes a contact form, mobile and email info with icons, and a Facebook link with icon.
- **Facebook Integration:**
	- Facebook link and icon added to contact section.
	- Three latest Facebook posts embedded manually for demo purposes.
- **Color & Font Consistency:**
	- Brand colors: red (#d32f2f), golden yellow (bg-yellow-400), and white.
	- Fonts: "Luckiest Guy" for headers, "Special Elite" for body text.
- **Mobile Responsive:**
	- Layout and typography are responsive for all devices.
- **Wagtail Admin:**
	- All content is editable via the Wagtail admin interface. No coding required for regular updates.

## How to Edit Content

Wagtail provides a user-friendly admin interface for editing all website content. You do **not** need to be a superuser to edit content. Site owners and editors can be assigned to groups with specific permissions (CRUD: Create, Read, Update, Delete) per page type or section.

To enable editing for non-superusers:
1. Create a user and assign them to a group (e.g., “Editors”).
2. In Wagtail admin, go to Settings → Groups and set the desired permissions for that group.
3. Editors can then log in at `/admin/` to manage content without superuser access.

This setup allows safe, flexible content management for owners and team members.

## Project Prompt (Original)

Create a single page website for Bitesize Church, a friendly and welcoming community church based in Colshaw. The site should have the following sections: a warm hero section with a tagline and call to action, an about section explaining what Bitesize Church is, a Bitesize Brunch section explaining their monthly get-together events, an events section showing upcoming 2026 brunch dates, a visit us section with location and what to expect when you arrive, and a contact section with a simple enquiry form. The tone should be friendly, warm and inclusive. The brand colours are red, golden yellow and white.
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



## Latest Updates (27 March 2026)

- **Sticky Navbar:** The main navigation bar is now sticky and always visible at the top of the page as you scroll.
- **Smooth Scrolling:** Anchor links (navbar/footer) now smoothly scroll to their sections for a better user experience.
- **Scroll Offset for Anchors:** Section anchors (About, Dates, Location, Contact) have a scroll offset so headers are not hidden behind the sticky navbar.
- **Clickable Logo:** The logo in the navbar is now clickable and returns you to the top of the homepage.
- **Footer & Navbar Links:** Footer links match the navbar, are right-aligned, and have a unified hover underline animation.
- **Admin-Editable Content:** All homepage content (except the calendar) is now editable via the Wagtail admin, including flexible extra sections and footer text.
- **Dynamic Events Section:** The events heading and intro in the Dates section are now dynamic and fully editable from the Wagtail admin panel.
- **Code/Template Changes:** All changes are reflected in `home/templates/home/home_page.html` and the Wagtail `HomePage` model.


- Updated the calendar main header to use the "Luckiest Guy" font from Google Fonts (closest free match to Wak by Rodrigo Typo)
- Calendar cards now feature rounded corners, a strong 3D drop shadow, and yellow paper-strip backgrounds for a playful desk calendar look
- All non-header text uses the "Special Elite" typewriter-style font for extra character
- Navbar size increased for better visual impact
- Tailwind CSS is now loaded via CDN for rapid UI development
- Google Fonts (Baloo 2, Luckiest Guy, Special Elite) are integrated for custom typography
- All changes are reflected in `home/templates/home/home_page.html`



The homepage remains fully dynamic and editable via the Django/Wagtail admin interface, allowing non-coders to update all content easily. All UI/UX improvements from 27 March 2026 are now live and committed to GitHub.

## Content Editing and Permissions in Wagtail

- Wagtail provides a user-friendly admin interface for editing all website content.
- You do **not** need to be a superuser to edit content. Site owners and editors can be assigned to groups with specific permissions.
- Permissions can be set per page type or section, allowing for fine-grained control (CRUD: Create, Read, Update, Delete) over different parts of the site.
- To enable editing for non-superusers:
	1. Create a user and assign them to a group (e.g., “Editors”).
	2. In Wagtail admin, go to Settings → Groups and set the desired permissions for that group.
	3. Editors can then log in at `/admin/` to manage content without superuser access.
- This setup allows safe, flexible content management for owners and team members.

### Section/Area-Specific CRUD Permissions

- You can grant CRUD permissions for specific sections of the site tree or for specific page types.
- For example, a user can be allowed to manage only the “Events” section, or only “Blog” pages, etc.
- This is managed via the Wagtail Groups and Permissions system in the admin interface.

**Summary:**
- Owners/editors do not need to be superusers.
- Use Wagtail’s Groups and Permissions to control who can edit what.
- Each section/page type can have its own CRUD permissions for safe, flexible content management.
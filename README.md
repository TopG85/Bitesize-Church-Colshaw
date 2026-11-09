# ⛪ Bitesize Church Colshaw - Brand Architecture Rollout

This repository hosts the production web platform for Bitesize Church Colshaw, engineered using Python, Django 6.0+, Wagtail CMS, and Tailwind CSS. The platform is fully responsive and leverages an intuitive, role-based administrative content network to empower non-technical editors to control core features safely.

## 🏗️ Technical Foundation

- **Core Framework:** Python / Django web architecture for robust, scalable data persistence.
- **Content Management Engine:** Wagtail CMS, utilizing customized block models for fluid content editing.
- **UI Styling Pipeline:** Tailwind CSS utility classes running a multi-branch token configuration matrix.

## 🎨 Q4 Rebrand Deployment Objectives (Meeting Imogen)

- [ ] Conduct Design-to-Engineering asset alignment sync with Marketing Director.
- [ ] Audit existing Wagtail block components against upcoming brand guidelines.
- [ ] Consolidate the experimental Git design branches (`design/navy-gold-palette`, `design/professional-church-theme`) into a unified styling system matching the new rollout.
- [ ] Migrate static asset tokens (Logos, Fonts, Hex Palettes) into the core `tailwind.config.js` layer.

### 🗣️ Non-Technical Translator Cheat Sheet

_Use these plain-English summaries to explain the technical system architecture to Imogen or church stakeholders._

| Technical Component  | What It Actually Means (The Analogy) | How to Explain It to Imogen                                                                                                                                                                                                          |
| :------------------- | :----------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Wagtail CMS**      | **The Modular Lego Set**             | "I've built the backend like a structured Lego set. You don't need code to change text or images; you just log into a clean dashboard, type into the boxes, and the site layouts arrange themselves perfectly."                      |
| **Tailwind Config**  | **The Global Brand Control Panel**   | "Instead of painting every single page by hand, the site reads from a master brand control panel. The moment you give me your new color codes and fonts, I plug them into this panel, and the entire site changes colors instantly." |
| **Git Branches**     | **The Parallel Mockup Universes**    | "I've engineered the prototype inside multiple 'parallel design universes'. This means I can show you a Navy-and-Gold layout version or a minimalist version side-by-side without breaking the core system."                         |
| **Django Framework** | **The Deep Structural Foundation**   | "Under the hood, this runs on Python and Django—the same high-security framework used by Instagram. It ensures the site is incredibly fast, perfectly secure, and won't crash if thousands of people load it on a Sunday morning."   |

---

## 📋 Client Discovery Sync Agenda (Meeting Imogen)

_Bring this up on screen or reference these notes during the session to guide the design-to-engineering handoff._

### 1. Discovery Core Questions (Ask Imogen)

- [ ] **Brand Kit Hex Codes:** "Can you provide the exact hexadecimal strings (e.g., `#0A2540`) for the primary, accent, and neutral tones of the rebrand?"
- [ ] **Typography Fonts:** "What are the typography rules for headings vs. body text? Are they accessible via Google Fonts, or do we have custom `.woff2` files?"
- [ ] **Vector Assets:** "Do you have the new logo variants exported as SVGs or high-res transparent PNGs for both light-mode and dark-mode sticky navbars?"
- [ ] **Content Node Map:** "What is the structural breakdown of the new main navigation menu layout? (e.g., Home, Events, Media, Contact?)"

### 2. Wagtail CMS Live Demonstration Checklist

- [ ] Open local environment baseline viewport at `http://localhost:8003`.
- [ ] Show the scroll-reveal sticky navigation bar functionality to prove responsiveness.
- [ ] Log into `/admin` to demonstrate how non-technical marketing editors can update content blocks independently.
- [ ] Switch Git layout branches to show structural multi-branch palette flexibility.

### 3. Deployment, Ownership & SEO Logistics (Ask Imogen)

- [ ] **Domain Name & Billing:** "Who currently owns the `bitesizechurch...` domain registrar account (e.g., GoDaddy, Namecheap)? We will need to set up direct billing so the church pays for the yearly renewal directly."
- [ ] **Legal Ownership:** "Who is the official legal owner or trustee signed to the domain and hosting accounts for Bitesize?"
- [ ] **Google Visibility & Search (SEO):** "Once the site is built, I will need access to the church's master Google account to hook up **Google Search Console** and **Google Analytics**. This ensures the rebrand maps properly, maps indexing requests, and can be discovered on Google searches seamlessly."

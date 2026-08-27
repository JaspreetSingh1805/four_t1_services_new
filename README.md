# 4T1 Services — Truck & 4x4 Tyre Specialist Website (Django)

A bold, rugged, heavy-duty Django website built for **4T1 Services**, an Australian specialist company for truck, heavy vehicle, 4WD, and 4x4 tyres.

---

## 🛠️ Tech Stack & Features

- **Framework**: Django 4.2+ / 6.1
- **App Name**: `core`
- **Template Inheritance**: `base.html` shared layout containing header navigation, 24/7 hotline banner, messages container, floating action call button, and industrial footer.
- **Design System**: Industrial dark background (`#0D0D0D` / `#141414`), gold accent (`#E7B11B`), Google Fonts (`Anton`, `Oswald`, `Montserrat`), and Font Awesome 6 icons.
- **Form Handling**: Working Django `ContactForm` on `/contact/` with POST validation and success alert state.
- **Static Assets**: Configured with `STATICFILES_DIRS` serving CSS, JS, SVG logo, and high-resolution automotive imagery.

---

## 📂 Project Structure

```text
Fortione_services/
├── manage.py
├── requirements.txt
├── README.md
├── fortione_services/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/
│   ├── __init__.py
│   ├── apps.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── images/
│   │       ├── logo.svg
│   │       ├── hero-truck.jpg
│   │       ├── truck-tyre-change.jpg
│   │       ├── 4x4-vehicle.jpg
│   │       ├── night-callout.jpg
│   │       ├── fleet-trucks.jpg
│   │       └── tyre-brands-wall.jpg
│   └── templates/
│       └── core/
│           ├── base.html
│           ├── home.html
│           ├── services.html
│           ├── callout_maintenance.html
│           └── contact.html
```

---

## 🚀 How to Run the Website

### Step 1: Open Terminal in Project Directory
Ensure you are in the project folder:
```bash
cd c:\Users\VIRENDER\OneDrive\Desktop\Fortione_services
```

### Step 2: Install Dependencies
Install Django and required packages:
```bash
pip install -r requirements.txt
```

### Step 3: Run Database Migrations
Run initial Django migrations:
```bash
python manage.py migrate
```

### Step 4: Start Development Server
Start the Django local development server:
```bash
python manage.py runserver
```

### Step 5: View in Browser
Open your browser and navigate to:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 📞 Contact & Business Information

- **SAMMIE**: `0421 191 220`
- **ROBIN**: `0450 480 043`
- **Email**: `4t1services@gmail.com`
- **Service Area**: Servicing Melbourne & Surrounding Areas
- **QR Code Scanner**: Scan to save contact directly to mobile devices (stored in `core/static/images/qr-code.png`)

- `/` — **Home Page** (`templates/core/home.html`)
  - Full-width hero banner, core services icon bullet grid, 5 feature cards, CTA banner.
- `/services/` — **Our Tyre Services** (`templates/core/services.html`)
  - Truck & Heavy Vehicle Tyres section, 4WD & 4x4 Tyres (HT/AT/MT breakdown), Fitting CTA block.
- `/callout-maintenance/` — **24/7 Callout & Yard Maintenance** (`templates/core/callout_maintenance.html`)
  - Emergency 24/7 callout assistance & commercial yard fleet servicing.
- `/contact/` — **Tyre Brands & Contact** (`templates/core/contact.html`)
  - Major brand showcase (Michelin, Bridgestone, Goodyear, etc.), 6 feature blocks, working contact form, quick action buttons (`CALL NOW`, `REQUEST A QUOTE`, `CONTACT US`).

---

## 🖼️ Static Image Assets & Where to Drop Images

All site images are stored inside:
`core/static/images/`

To replace or update images, drop new files into `core/static/images/`:
- `hero-truck.jpg` — Home hero background image
- `truck-tyre-change.jpg` — Truck tyre fitting section image
- `4x4-vehicle.jpg` — 4WD & 4x4 section image
- `night-callout.jpg` — 24/7 Callout section image
- `fleet-trucks.jpg` — Fleet maintenance section image
- `tyre-brands-wall.jpg` — Major brands background image
- `logo.svg` / `logo.png` — Company brand logo

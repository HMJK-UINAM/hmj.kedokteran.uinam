# HMJ Kedokteran UINAM Website - AI Coding Guidelines

## Project Overview
Static website for **HMJ Kedokteran UIN Alauddin Makassar** (Student Organization of Medical Faculty). The site showcases 9 academic departments, each with structured information about leadership, members, and organizational goals.

## Architecture & Key Components

### Data-Driven HTML Generation
- **Single Source of Truth**: [generate_departments.py](generate_departments.py) defines all department metadata
- **Departments Dictionary**: Contains 10 departments (HubLu, DANUS, JARKOM, PMB, PENGMAS, KASTRAD, P2, PSDM, PIKIS)
- **Template System**: Universal HTML template with placeholder format (`{title}`, `{name}`, `{profil1}`, etc.)
- **Automation**: Running the script generates/updates all 9 department HTML files from this single configuration
- **Do NOT** manually edit generated department pages (hublu.html, danus.html, jarkom.html, etc.) - edit [generate_departments.py](generate_departments.py) instead

### File Organization
```
Root HTML files:          Department pages (regenerated):
├─ index.html             ├─ hublu.html
├─ admin.html             ├─ danus.html
├─ navbar.html            ├─ jarkom.html
└─ p2.html (legacy)       ├─ pmb.html
                          ├─ pengmas.html
                          ├─ kastrad.html
                          ├─ p2.html (regenerated)
                          ├─ psdm.html
                          └─ pikis.html
```

## Development Workflow

### Updating Department Information
1. Modify department data in [generate_departments.py](generate_departments.py) (lines 1-170)
2. Run: `python generate_departments.py`
3. Script outputs: "✓ Created: [filename]" for each updated page
4. All 9 department HTML files regenerate automatically

### Example: Adding a Department Member
In `departments` dict, update `anggota` list:
```python
"anggota": [
    ("Existing Member", "Anggota"),
    ("New Member Name", "Anggota"),  # ← Add here
]
```
Then regenerate with Python script.

## Design & Styling Patterns

### Consistent Visual Language
- **Color Scheme**: Brown (#8B7355) for primary brand, neutral grays for text
- **Font**: Montserrat (Google Fonts) with weights 400, 600, 700, 800
- **Layout**: Bootstrap 5.3.3 + custom CSS with Flexbox
- **Navbar**: Sticky, scroll-sensitive shadow effect, dropdown animations
- **Icons**: Bootstrap Icons (v1.11.3) via CDN

### Reusable Components
- `.navbar-custom` - Modern navbar with hover effects
- `.anggota-card` - Team member profile cards (image placeholder, name, position)
- `.ketua-card` - Department leader card (larger, featured position)
- Intersection Observer animation - Cards fade-in on scroll

### Localization
All content is Indonesian (lang="id"). Site uses Bahasa Indonesia throughout.

## Critical Dependencies
- **Bootstrap 5.3.3**: CSS framework (CDN link in every HTML)
- **Bootstrap Icons 1.11.3**: Icon library (CDN)
- **Google Fonts/Montserrat**: Typography (CDN)
- **Python 3**: For [generate_departments.py](generate_departments.py) automation

## Common Tasks

### Styling Updates
- Edit CSS in `<style>` block within HTML templates
- For department pages: Update `template` variable in [generate_departments.py](generate_departments.py) (lines 168-850)
- Regenerate department pages after CSS changes

### Adding Contact Information
Located in footer sections - consistent across all pages:
- Email: `hmjk.uinam@gmail.com`
- Instagram: `@hmjkuinam`
- TikTok: `@hmjkuinam`

### Backup Strategy
- [BACKUP_2026-01-25_103418/](BACKUP_2026-01-25_103418/) contains snapshot of department pages
- Use for reference or recovery if needed

## Best Practices

1. **Always regenerate after Python edits**: Changes to [generate_departments.py](generate_departments.py) require running the script
2. **Preserve structure**: Template placeholders are intentional - maintain `{field_name}` pattern
3. **CSS before JS**: Solve styling with CSS before adding JavaScript
4. **Accessibility**: Use semantic HTML, meaningful icon labels, sufficient color contrast
5. **Indonesian content**: All user-facing text should be in Bahasa Indonesia

# Querencia Linux Website

Landing page and documentation for [Querencia Linux](https://github.com/endegelaende/querencia-linux) — *Where Linux Feels at Home*.

**Live:** [querencialinux.org](https://querencialinux.org)

Querencia Linux is an atomic, immutable Linux desktop built on AlmaLinux 10 with MATE Desktop.

## Structure

```
querencia-web/
├── index.html                  ← Landing page (HTML + CSS + JS, single file)
├── privacy.html                ← Privacy policy (GDPR)
├── assets/
│   ├── querencia-logo.svg      ← Logo (SVG vector paths)
│   ├── og-image.png            ← Social media preview (1200×630)
│   ├── og-image.svg            ← OG image source
│   ├── screenshot-lightdm.png  ← LightDM login screenshot (1920×1080)
│   └── screenshot-desktop.png  ← MATE desktop screenshot (1920×1080)
├── docs/
│   ├── index.html              ← Documentation overview
│   ├── getting-started.html    ← First login, Welcome Center, desktop
│   ├── installing-software.html← Flatpak, Micromamba, Distrobox
│   ├── updates.html            ← Automatic updates, rollback, ZRAM
│   ├── hardware.html           ← GPU (AMD/NVIDIA), audio, printing, WiFi
│   └── faq.html                ← Frequently asked questions
├── fonts/
│   ├── inter-variable.woff2    ← Inter (self-hosted, GDPR)
│   └── jetbrains-mono-variable.woff2  ← JetBrains Mono (self-hosted)
├── generate-og-image.py        ← Regenerate OG image (Python + Pillow)
├── CNAME                       ← Legacy (unused by Cloudflare)
└── .gitignore
```

## Hosting

The site is deployed via **Cloudflare Pages** — every push to `master` goes live within ~60 seconds.

- **Custom domain:** `querencialinux.org` (DNS managed via Cloudflare)
- **SSL:** Automatic (Full strict)
- **Build command:** None (static files served directly)

## Local Preview

No build step required:

```bash
python -m http.server 8000
# or: npx serve .
# or: just open index.html in your browser
```

## Design

Warm, inviting design language with Terracotta accent colors:

| Token | Hex | Usage |
|---|---|---|
| Terracotta | `#C75230` | Primary accent, logo |
| Terracotta Dark | `#A33D1E` | Hover states |
| Gold | `#D4A853` | Secondary accent |
| Cream | `#FFFBF5` | Page background |
| Sand | `#F5EDE4` | Card backgrounds |
| Text Primary | `#3D2E1F` | Headings, body |
| Text Secondary | `#6B5B4D` | Descriptions |
| Text Muted | `#9C8B7A` | Labels, captions |

Terminal mockups use the Dracula color scheme (`#282A36` background).

Self-hosted fonts: **Inter** (sans-serif) and **JetBrains Mono** (monospace).

## No Tracking

- **No cookies** — none at all
- **No analytics** — no Google Analytics, no Matomo, no Plausible
- **No external requests** — fonts are self-hosted, zero CDN dependencies
- **No JavaScript frameworks** — vanilla JS for tabs, accordion, and lightbox

## Documentation

The `docs/` directory contains 6 user-facing documentation pages with a shared sidebar layout. Content is sourced from the Markdown files in the [main repository](https://github.com/endegelaende/querencia-linux/tree/main/Documentation) and hand-converted to HTML.

| Page | Content |
|---|---|
| [Overview](/docs/) | Guide cards, quick reference, links |
| [Getting Started](/docs/getting-started.html) | First login, Welcome Center, desktop, keyboard, apps |
| [Installing Software](/docs/installing-software.html) | Flatpak, Micromamba, Distrobox |
| [Updates & Maintenance](/docs/updates.html) | Automatic updates, rollback, ZRAM, system info |
| [Hardware Support](/docs/hardware.html) | GPU (AMD/NVIDIA), audio, printing, scanning, Bluetooth, WiFi |
| [FAQ](/docs/faq.html) | 23 questions across General, Software, and System |

## License

[MIT](https://github.com/endegelaende/querencia-linux/blob/main/LICENSE)
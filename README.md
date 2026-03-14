# Querencia Linux Website

Static website for [Querencia Linux](https://github.com/endegelaende/querencia-linux) — "Where Linux Feels at Home".

**Live:** [querencialinux.org](https://querencialinux.org)

## Structure

```
querencia-web/
├── index.html          ← Main landing page (single-page, no build step)
├── privacy.html        ← Privacy policy (GDPR)
├── CNAME               ← Custom domain for GitHub Pages
├── assets/
│   └── querencia-logo.svg  ← Project logo
├── fonts/
│   ├── inter-variable.woff2          ← Inter font (self-hosted, no Google CDN)
│   └── jetbrains-mono-variable.woff2 ← JetBrains Mono (self-hosted)
└── README.md           ← This file
```

## Setup

### 1. Download fonts (required)

Fonts are self-hosted to avoid GDPR issues with Google Fonts CDN. Download them into `fonts/`:

```bash
# Inter (variable weight, Latin subset)
curl -L -o fonts/inter-variable.woff2 \
  "https://fonts.gstatic.com/s/inter/v18/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuLyfAZ9hiJ-Ek-_EeA.woff2"

# JetBrains Mono (variable weight, Latin subset)
curl -L -o fonts/jetbrains-mono-variable.woff2 \
  "https://fonts.gstatic.com/s/jetbrainsmono/v21/tDbY2o-flEEny0FZhsfKu5WU4zr3E_BX0PnT8RD8yKxjPVmUsaaDhw.woff2"
```

Or get them from:
- **Inter:** https://rsms.me/inter/ → Download → extract `.woff2`
- **JetBrains Mono:** https://www.jetbrains.com/lp/mono/ → Download → extract `.woff2`

### 2. Preview locally

No build step needed — just open the HTML file:

```bash
# Python
python3 -m http.server 8000 --directory .

# Node
npx serve .

# Or just open index.html in your browser
```

### 3. Deploy to GitHub Pages

#### Option A: Dedicated repo (recommended)

1. Create repo `endegelaende/querencia-web` (or `endegelaende.github.io` for the org page)
2. Push this directory to `main`
3. Go to **Settings → Pages → Source: Deploy from a branch → Branch: main / root**
4. GitHub Pages will serve `index.html` automatically
5. Add custom domain `querencialinux.org` in Pages settings

#### Option B: Subdirectory of main repo

1. Copy this directory to `docs/` in the `querencia-linux` repo
2. Go to **Settings → Pages → Source: Deploy from a branch → Branch: main / docs**

### 4. DNS Setup (Ionos → GitHub Pages)

Add these DNS records at your domain registrar (Ionos):

| Type | Name | Value |
|---|---|---|
| `A` | `@` | `185.199.108.153` |
| `A` | `@` | `185.199.109.153` |
| `A` | `@` | `185.199.110.153` |
| `A` | `@` | `185.199.111.153` |
| `CNAME` | `www` | `endegelaende.github.io` |

GitHub Pages provides free HTTPS automatically after DNS propagation (up to 24h).

## Design

Warm, inviting design language inspired by the admin-panel "Warm Theme 2026":

| Token | Hex | Usage |
|---|---|---|
| Terracotta | `#C75230` | Primary accent (from logo) |
| Terracotta Dark | `#A33D1E` | Hover states |
| Gold | `#D4A853` | Secondary accent |
| Cream | `#FFFBF5` | Page background |
| Sand | `#F5EDE4` | Card backgrounds, code blocks |
| Text Primary | `#3D2E1F` | Headings, body text |
| Text Secondary | `#6B5B4D` | Descriptions |
| Text Muted | `#9C8B7A` | Labels, captions |
| Linux Gray | `#888780` | From logo "LINUX" text |

## No Tracking

- **No cookies** — none at all
- **No analytics** — no Google Analytics, no Matomo, no Plausible
- **No external requests** — fonts are self-hosted, no CDN dependencies
- **No JavaScript frameworks** — vanilla JS for tabs/accordion only

## Adding Screenshots

When screenshots are available, add them to `assets/` and reference in `index.html`:

```
assets/screenshot-desktop.webp    ← MATE desktop
assets/screenshot-terminal.webp   ← Terminal with ujust
assets/screenshot-warehouse.webp  ← Warehouse app store
assets/screenshot-lightdm.webp    ← Login screen
```

Use WebP format for best size/quality ratio. Recommended size: 1200×800px.

## License

[MIT](https://github.com/endegelaende/querencia-linux/blob/main/LICENSE)
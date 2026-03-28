# BERENT.AI — Unternehmenswebsite

## Projektübersicht

Offizielle Website von BERENT | Beratung + Entwicklung. Präsentiert Dienstleistungen, Anwendungen, Leitfäden und Kontaktmöglichkeiten.

**Deployment:** Vercel — https://berent.ai
**Repository:** https://github.com/peerendees/berent.ai.git
**Domain:** berent.ai (+ www.berent.ai)

## Architektur

- **Multi-Page Website:** Einzelne HTML-Seiten pro Bereich
- **CSS:** Tailwind CSS (Build via PostCSS) + Custom Properties für CI
- **Kein Framework:** Vanilla HTML/CSS/JS
- **Deployment:** Vercel (Static)

## Seiten

| Seite | Datei | Inhalt |
|-------|-------|--------|
| Startseite | `index.html` | Hero, Services, CTA |
| Anwendungen | `apps.html` | Links zu Sub-Apps (Textschmiede, Startrampe, VAaaS, ROI-Rechner, Obsidian Gen) |
| Leitfaden | `guides.html` | Relaunch-Guide, Launch-Lotse, Hacks |
| Buch | `buch.html` | Buchprojekt |
| Über mich | `profil.html` | Profil Marcus Berent |
| Kontakt | `kontakt.html` | Kontaktformular |
| Vorträge | `vortraege.html` | Vortragsangebote |
| Impressum | `impressum.html` | Rechtliches |
| Datenschutz | `datenschutz.html` | DSGVO |
| Showcase | `showcase.html` | Projektgalerie |
| Termin | `termin.html` | Terminbuchung |

## Sub-Domains und Projekte

| App | URL | Repo |
|-----|-----|------|
| Textschmiede | textschmiede-5tc.berent.ai | peerendees/textschmiede-5TC |
| Startrampe | startrampe.berent.ai | peerendees/startrampe |
| Launch-Lotse | launch-lotse.berent.ai | peerendees/launch-lotse |
| Hacks | hacks.berent.ai | peerendees/hacks |
| VAaaS | vaaas.berent.ai | peerendees/vaaas |
| ROI-Rechner | roi.berent.ai | peerendees/vaaas-roi-calculator |
| BelegChat | belegchat.berent.ai | peerendees/belegchat-landing |

## Corporate Identity

Folgt der BERENT.AI CI (siehe Skill `berent-ci`):
- **Dark Mode** ist Standard, Light Mode über Toggle
- **Fonts:** Bebas Neue (Headlines), Lora (Fließtext), JetBrains Mono (Labels)
- **Farben:** Kupfer-Akzentsystem, Gold nur für Plus-Symbol
- **Kein Ampersand** als Konjunktion — immer „und"

## Navigation

Alle App-Links öffnen in neuem Tab (`target="_blank" rel="noopener"`), damit die Hauptseite im Hintergrund bleibt.

### Smart Back-Navigation (Pflicht für alle Subdomains)

Jede Subdomain MUSS einen sichtbaren „← berent.ai" Back-Button mit 3-stufiger Logik haben:

1. `window.close()` — wenn Tab via `window.opener` geöffnet wurde (Tab schließt sich)
2. `history.back()` — wenn `document.referrer` den String `berent.ai` enthält
3. **Fallback** — Navigation zur konkreten Herkunftsseite (NICHT generisch zu berent.ai)

**Referenz-Implementierung (HTML):**
```html
<a href="https://berent.ai/apps" class="header-back"
   onclick="event.preventDefault();
     if(window.opener) { window.close(); }
     else if(document.referrer.includes('berent.ai')) { history.back(); }
     else { window.location.href='https://berent.ai/apps'; }">
  ← berent.ai
</a>
```

**Fallback-Zuordnung nach Herkunft:**

| Subdomain | Verlinkt von | Fallback-URL |
|-----------|-------------|-------------|
| textschmiede-5tc.berent.ai | Anwendungen | `https://berent.ai/apps` |
| startrampe.berent.ai | Anwendungen | `https://berent.ai/apps` |
| vaaas.berent.ai | Anwendungen | `https://berent.ai/apps` |
| roi.berent.ai | Anwendungen | `https://berent.ai/apps` |
| belegchat.berent.ai | Anwendungen | `https://berent.ai/apps` |
| launch-lotse.berent.ai | Leitfaden | `https://berent.ai/guides` |
| hacks.berent.ai | Leitfaden | `https://berent.ai/guides` |
| relaunch-guide.berent.ai | Leitfaden | `https://berent.ai/guides` |

**Regel:** Neue Subdomains erhalten die Fallback-URL der Seite, von der sie primär verlinkt werden. Diese Zuordnung wird in dieser Tabelle gepflegt.

## Theme-System

- Dark/Light Toggle in Navigation (Desktop + Mobile)
- SVG-Icons: Sonne (Dark aktiv) / Mond (Light aktiv)
- Zustand in localStorage gespeichert

## Konventionen

- **Sprache:** Deutsche UI
- **Commit-Sprache:** Englisch
- **CSS:** Tailwind + Custom Properties in `output.css`
- **Kein Ampersand** in UI-Texten

## Dateien

```
index.html          # Startseite
apps.html           # Anwendungen (Links zu Sub-Apps)
guides.html         # Leitfaden (Relaunch-Guide, Launch-Lotse, Hacks)
buch.html           # Buchprojekt
profil.html         # Über mich
kontakt.html        # Kontakt
vortraege.html      # Vorträge
termin.html         # Terminbuchung
showcase.html       # Projektgalerie
impressum.html      # Impressum
datenschutz.html    # Datenschutz
output.css          # Tailwind Build Output
tailwind.config.js  # Tailwind Konfiguration
vercel.json         # Vercel Config (Rewrites)
images/             # Logos, Bilder
public/             # Statische Assets
src/                # Source CSS für Tailwind
```

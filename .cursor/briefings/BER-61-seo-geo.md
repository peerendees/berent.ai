# Cursor-Briefing: SEO/GEO Maßnahmenpaket
**Datum:** 11.04.2026
**Linear-Issue:** [BER-61](https://linear.app/berent/issue/BER-61)
**Projekt:** berent.ai
**Komplexität:** Mittel
**Repo:** `peerendees/berent.ai`

## Cursor-Prompt (kopieren und einfügen)

```
Lies das Briefing .cursor/briefings/BER-61-seo-geo.md und setze es vollständig um.

Kurzfassung: SEO/GEO-Optimierung der gesamten Website.

1. Meta Description auf ALLEN HTML-Seiten ergänzen (index, profil, apps, buch, guides, kontakt, termin, qualifikationen, vortraege, showcase, datenschutz, impressum). Jede Seite braucht eine individuelle, max. 160 Zeichen.
2. Schema.org LD+JSON auf index.html einfügen (ProfessionalService + Person).
3. Google Fonts durch lokale Font-Dateien ersetzen. Die Fonts liegen bereits unter assets/fonts/ (siehe Blog-Repo als Referenz). Entferne die Google-Fonts-Links und füge @font-face-Deklarationen ein.
4. sitemap.xml: Alle URLs auf https://www.berent.ai/... ändern (mit www, weil Vercel dorthin redirected).
5. Sitemap-Index erstellen: sitemap-index.xml im Root, verweist auf eigene sitemap.xml + https://blog.berent.ai/sitemap.xml.
6. robots.txt: Sitemap-Verweis auf sitemap-index.xml ändern.

Geräte-Label: gerät:m2
Werkzeug-Label: werkzeug:cursor

git add -A
git commit -m "[BER-61] done: SEO/GEO — Meta Descriptions, Schema.org, lokale Fonts, Sitemap-Index"
git push
```

---

## Aufgabe 1: Meta Description

Jede HTML-Seite braucht `<meta name="description" content="...">` — individuell, max. 160 Zeichen.

Vorschläge (Cursor darf anpassen):

| Seite | Description |
|---|---|
| index.html | KI-Strategieberatung und Transformation für den Mittelstand. TÜV-zertifizierter KI-Strategieberater und Hedy-Trainer. |
| profil.html | Marcus Kunkel — KI-Strategieberater, Hedy-Trainer und Begleiter für Digitalisierung im Mittelstand. |
| apps.html | KI-Werkzeuge von BERENT: Textschmiede, ROI-Rechner, Obsidian Properties Generator und mehr. |
| buch.html | KI für Einsteiger — das Buch von Marcus Kunkel für den praxisnahen Einstieg in Künstliche Intelligenz. |
| guides.html | Leitfaden und Anleitungen für KI-Transformation, Webseiten-Relaunch und Automatisierung im Mittelstand. |
| kontakt.html | Kontakt zu BERENT — Erstgespräch kostenfrei. E-Mail, Threema oder Terminbuchung. |
| termin.html | Kostenloses Erstgespräch buchen — KI-Beratung für den Mittelstand. |
| qualifikationen.html | Zertifikate und Qualifikationen: TÜV KI-Strategieberater, MCR, Hedy-Trainer, AITI Trainer. |
| vortraege.html | Vorträge und Workshops zu KI-Transformation, Automatisierung und Telefonassistenz. |
| showcase.html | Projekte und Showcase — Tools, Landing Pages und Open-Source von BERENT. |
| datenschutz.html | Datenschutzerklärung von BERENT | Beratung + Entwicklung. |
| impressum.html | Impressum von BERENT | Beratung + Entwicklung — Marcus Kunkel. |

## Aufgabe 2: Schema.org LD+JSON

In `index.html` im `<head>` einfügen:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "BERENT | Beratung + Entwicklung",
  "url": "https://www.berent.ai",
  "logo": "https://www.berent.ai/images/og-image.png",
  "founder": {
    "@type": "Person",
    "name": "Marcus Kunkel",
    "jobTitle": "KI-Strategieberater",
    "url": "https://www.berent.ai/profil"
  },
  "description": "KI-Strategieberatung und Transformation für den Mittelstand. TÜV-zertifizierter KI-Strategieberater und Hedy-Trainer.",
  "areaServed": {
    "@type": "Country",
    "name": "DE"
  },
  "knowsAbout": ["KI-Transformation", "Telefonassistenz", "VAaaS", "Automatisierung", "KI-Strategieberatung"],
  "sameAs": [
    "https://linkedin.com/in/berentai",
    "https://instagram.com/berent.ai"
  ]
}
</script>
```

## Aufgabe 3: Google Fonts lokal hosten

Die Fonts liegen bereits lokal vor (siehe assets/fonts/). Ersetze in index.html und allen anderen Seiten:

**Entfernen:**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=..." rel="stylesheet">
```

**Einfügen** (in output.css oder als inline `<style>` falls Tailwind das nicht abdeckt):
```css
@font-face {
  font-family: 'Bebas Neue';
  src: url('/assets/fonts/bebas-neue-regular.woff2') format('woff2');
  font-weight: 400;
  font-display: swap;
}
@font-face {
  font-family: 'Lora';
  src: url('/assets/fonts/lora-300.woff2') format('woff2');
  font-weight: 300;
  font-display: swap;
}
@font-face {
  font-family: 'Lora';
  src: url('/assets/fonts/lora-400.woff2') format('woff2');
  font-weight: 400;
  font-display: swap;
}
@font-face {
  font-family: 'Lora';
  src: url('/assets/fonts/lora-600.woff2') format('woff2');
  font-weight: 600;
  font-display: swap;
}
@font-face {
  font-family: 'Lora';
  src: url('/assets/fonts/lora-700.woff2') format('woff2');
  font-weight: 700;
  font-display: swap;
}
@font-face {
  font-family: 'JetBrains Mono';
  src: url('/assets/fonts/jetbrains-mono-400.woff2') format('woff2');
  font-weight: 400;
  font-display: swap;
}
```

Prüfe ob alle Font-Dateien unter `assets/fonts/` vorhanden sind. Falls lora-700.woff2 fehlt, lade sie von Google Fonts herunter.

## Aufgabe 4: Sitemap-URLs auf www

In `sitemap.xml` alle `<loc>` von `https://berent.ai/...` auf `https://www.berent.ai/...` ändern.

## Aufgabe 5: Sitemap-Index

Neue Datei `sitemap-index.xml` im Root:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://www.berent.ai/sitemap.xml</loc>
    <lastmod>2026-04-11</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://blog.berent.ai/sitemap.xml</loc>
    <lastmod>2026-04-11</lastmod>
  </sitemap>
</sitemapindex>
```

## Aufgabe 6: robots.txt aktualisieren

```
User-agent: *
Allow: /

Sitemap: https://www.berent.ai/sitemap-index.xml
```

## NICHT ändern

- Seitenstruktur, Navigation, Layout
- Testimonials, Inhalte
- CSS-Design
- Vercel-Konfiguration

## Abschluss

```bash
git add -A
git commit -m "[BER-61] done: SEO/GEO — Meta Descriptions, Schema.org, lokale Fonts, Sitemap-Index"
git push
```

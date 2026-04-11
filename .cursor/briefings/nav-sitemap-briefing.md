# Cursor-Briefing: Blog-Navigation + Sitemap für berent.ai

**Datum:** 11. April 2026
**Projekt:** berent.ai
**Repo:** `peerendees/berent.ai`
**Komplexität:** Einfach

## Ziel

Zwei Änderungen am Hauptrepo: (1) Blog-Link in die Navigation aller HTML-Seiten einbauen, (2) `sitemap.xml` + `robots.txt` für Google-Indexierung erstellen.

## Kontext

Die aktuelle Navigation (Desktop) sieht so aus:

```
+ BERENT | Beratung + Entwicklung    TELEFONASSISTENZ  ANWENDUNGEN  LEITFADEN  BUCH  ÜBER MICH  QUALIFIKATIONEN  KONTAKT  ⚙️
```

Die Schrift ist Bebas Neue, Uppercase. Es gibt ein Hamburger-Menü für Mobile/Tablet.

## Änderung 1: Blog-Link in der Navigation

### Positionierung

Blog wird **zwischen BUCH und ÜBER MICH** eingefügt. Neue Reihenfolge:

```
TELEFONASSISTENZ · ANWENDUNGEN · LEITFADEN · BUCH · BLOG · ÜBER MICH · QUALIFIKATIONEN · KONTAKT
```

### Desktop-Navigation

Suche in jeder HTML-Datei den Nav-Link zu "Buch" (oder `buch.html`). Füge **direkt danach** diesen Link ein:

```html
<a href="https://blog.berent.ai" target="_blank" rel="noopener">Blog</a>
```

Übernimm exakt dieselben CSS-Klassen wie die benachbarten Links (Buch, Über mich). Kein eigener Stil — der Blog-Link soll sich nahtlos einfügen.

**Wichtig:** `target="_blank" rel="noopener"` — der Blog öffnet in einem neuen Tab.

### Mobile-/Hamburger-Navigation

Im Mobile-Menü ebenfalls einen Eintrag ergänzen, an derselben Position (nach Buch, vor Über mich). Gleiche CSS-Klassen wie die anderen Mobile-Links.

### Spacing

Falls der zusätzliche Link die Desktop-Nav zu breit macht: den horizontalen Abstand zwischen den Links um eine Stufe reduzieren (z.B. von `gap-8` auf `gap-6`, oder von `space-x-8` auf `space-x-6` — je nachdem, welche Klasse aktuell verwendet wird). Nur anpassen, wenn es tatsächlich umbricht oder überlappt.

### Betroffene Dateien

Alle `.html`-Dateien im Repo, die die Navigation enthalten. Suche nach dem String `buch` oder `BUCH` in der Nav, um alle betroffenen Dateien zu identifizieren.

## Änderung 2: sitemap.xml

Erstelle eine `sitemap.xml` im Root des Repos.

### Schritt 1: Alle HTML-Seiten identifizieren

```bash
find . -maxdepth 1 -name "*.html" -type f | sort
```

Prüfe auch Unterordner (z.B. `/apps/`, `/guides/`) auf weitere HTML-Dateien.

### Schritt 2: sitemap.xml generieren

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://berent.ai/</loc>
    <lastmod>2026-04-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
  <!-- Für jede weitere HTML-Datei einen Eintrag -->
</urlset>
```

**Priority-Logik:**
- `index.html` (= `/`) → 1.0
- Hauptseiten (Telefonassistenz, Anwendungen, Buch, Profil, Termin) → 0.8
- Unterseiten (einzelne Apps, Leitfaden-Seiten) → 0.5
- Rechtliches (Impressum, Datenschutz) → 0.3

**lastmod:** Heutiges Datum (`2026-04-11`) für alle Seiten.

## Änderung 3: robots.txt

Erstelle eine `robots.txt` im Root (oder ergänze eine bestehende):

```
User-agent: *
Allow: /

Sitemap: https://berent.ai/sitemap.xml
```

## Akzeptanzkriterien

1. Alle HTML-Seiten mit Navigation enthalten den Blog-Link
2. Blog-Link steht zwischen BUCH und ÜBER MICH
3. Blog-Link öffnet in neuem Tab (`target="_blank" rel="noopener"`)
4. Blog-Link ist in Desktop- UND Mobile-Navigation vorhanden
5. Blog-Link hat dieselben CSS-Klassen wie die Nachbar-Links
6. Nav bricht auf Desktop (1280px) nicht um
7. `sitemap.xml` enthält alle HTML-Seiten mit korrekten Prioritäten
8. `robots.txt` verweist auf die Sitemap
9. Keine bestehende Funktionalität ist beeinträchtigt

## Dateien

- Alle `*.html` mit Navigation → Blog-Link ergänzen
- `/sitemap.xml` → neu erstellen
- `/robots.txt` → neu erstellen oder ergänzen

## Abschluss

Wenn alle Änderungen umgesetzt sind:
```bash
git add -A
git commit -m "feat: Blog-Link in Navigation + sitemap.xml + robots.txt"
git push
```

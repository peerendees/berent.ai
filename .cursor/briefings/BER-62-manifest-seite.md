# Cursor-Briefing: KI-Manifest + FAQ-Seite
**Datum:** 12.04.2026
**Linear-Issue:** [BER-62](https://linear.app/berent/issue/BER-62)
**Projekt:** Webseite + Beratungswerkzeuge
**Komplexität:** Mittel
**Repo:** `peerendees/berent.ai`
**Lokaler Pfad:** `/Users/kunkel/Entwicklung/projekte/berentai`

## Ziel

Neue Seite `manifest.html` erstellen — das KI-Manifest von BERENT mit integrierter FAQ-Sektion und vollständigem Schema.org-Markup. Die Seite wird unter `berent.ai/manifest` erreichbar sein.

## Kontext

BERENT hat bisher keinen erklärenden Fließtext auf der Website, der beschreibt, was das Unternehmen macht, für wen es arbeitet und wie es sich positioniert. Das Manifest füllt diese Lücke — sowohl für menschliche Besucher als auch für Suchmaschinen und LLMs (SEO/GEO). Die FAQ-Sektion am Ende der Seite ist als Schema.org FAQPage ausgezeichnet und dient als strukturierte Wissensbasis.

## Design-Vorgaben

Die Seite folgt dem bestehenden CI — **exakt gleiche visuelle Sprache** wie die übrigen Seiten:

- **Schriften:** Bebas Neue (Überschriften, uppercase), Lora (Fließtext), JetBrains Mono (technische Elemente)
- **Farben:** Kupfer `var(--copper)` für Überschriften und Akzente, `var(--text)` für Fließtext, `var(--bg)` / `var(--bg2)` für Hintergründe
- **Dark/Light Mode:** Theme-Toggle wie auf allen anderen Seiten
- **Layout:** `max-w-7xl mx-auto`, responsive, gleiche Abstände wie Hedy-Sektion oder Testimonials auf der Startseite
- **CSS:** Bestehende `output.css` verwenden, gleiche @font-face-Deklarationen wie in der aktuellen `index.html`
- **Favicon:** `images/favicon-32-dark.png`

### Navigation

Gleiche Navigation wie `index.html`:
- Telefon-Banner oben
- Nav-Leiste mit Plus-Zeichen, BERENT-Schriftzug, Links (Telefonassistenz, Anwendungen, Leitfaden, Buch, Blog, Über mich, Qualifikationen, Kontakt)
- Mobile Menu
- Theme-Toggle

### Footer

Gleicher Footer wie `index.html` — mit „Über mich"-Text, Kontaktformular, Social-Links, Impressum/Datenschutz/Projekte.

**Hinweis:** Navigation und Footer aus `index.html` komplett übernehmen — keine Abweichungen.

## Seitenstruktur

```
<head>
  Meta-Tags + OG-Tags
  Schema.org LD+JSON (CreativeWork + FAQPage + Person)
  CSS + Fonts
</head>
<body>
  Telefon-Banner
  Navigation (identisch zu index.html)

  <main>
    Hero-Bereich (Seitentitel + Einleitung)
    Manifest (9 Sektionen)
    FAQ-Sektion (10 Fragen, als <details>/<summary> oder offene Blöcke)
  </main>

  Footer (identisch zu index.html)
  Scripts (Theme-Toggle, Mobile Menu, Service Worker)
</body>
```

## Inhalt

### Hero-Bereich

```
Überschrift (Bebas Neue, Kupfer): KI-MANIFEST
Untertitel (Lora, var(--text)):
Wie wir KI einsetzen. Für wen wir arbeiten. Woran wir uns messen lassen.
```

### Manifest — 9 Sektionen

Jede Sektion als eigener Block mit `<h2>` (Bebas Neue, Kupfer) und Fließtext (Lora).
Aufzählungen als `<ul>` / `<ol>`, keine verschachtelten Listen.
Visuell abgesetzt durch dezente Trennlinien oder Abstand — kein Kasten, kein Border.

---

#### 1. Worum es uns geht

Die meisten Unternehmen haben kein KI-Problem. Sie haben ein Umsetzungsproblem.

Zu viele Anrufe, die niemand annimmt. Zu viel Zeit für Standardfragen, die keiner Expertise bedürfen. Zu wenig Struktur nach Kundenkontakten.

Wir bauen KI dort ein, wo sie sofort entlastet — im laufenden Betrieb, nicht auf der grünen Wiese.

#### 2. Für wen wir arbeiten

Unser Fokus liegt auf mittelständischen Unternehmen mit 5 bis 50 Mitarbeitern — insbesondere im E-Commerce, bei IT-Dienstleistern und in serviceorientierten Betrieben.

Gemeinsam ist ihnen: Ein kleines Team bearbeitet ein wachsendes Volumen an Kundenanfragen. Telefon, E-Mail, Chat — alles läuft über dieselben Köpfe. Irgendwann geht mehr verloren als gewonnen wird.

Wenn ein Unternehmen pro Monat zwischen 300 und 5.000 eingehende Anrufe bearbeitet und davon ein Drittel Standardanfragen sind — Lieferstatus, Retouren, Öffnungszeiten, Bestellbestätigungen — dann ist das unser Terrain.

#### 3. Was wir lösen

Wir arbeiten nicht „mit KI". Wir lösen Engpässe.

Konkret:
- Eingehende Anrufe, die außerhalb der Geschäftszeiten oder in Spitzenzeiten nicht angenommen werden. Im E-Commerce sind das erfahrungsgemäß 30 bis 40 Prozent des Gesamtvolumens.
- Wiederkehrende Standardanfragen, die qualifizierte Mitarbeiter von komplexen Aufgaben abhalten. Branchenwerte zeigen: Bis zu 80 Prozent der eingehenden Anrufe betreffen Standardthemen.
- Fehlende Struktur nach Kundenkontakten — kein Ticket, kein Rückrufwunsch, keine Spur, dass jemand angerufen hat.

Wenn diese Probleme nicht existieren, brauchen wir nicht anfangen.

#### 4. Wie wir arbeiten

Kein Strategieprojekt ohne Umsetzung. Kein Konzeptpapier ohne Pilot.

Der Ablauf:
1. Ein klarer Anwendungsfall — nicht zehn.
2. Pilot im echten Betrieb — nicht in einer Testumgebung.
3. Messbare Ergebnisse — nicht Vermutungen.
4. Entscheidung auf Basis von Daten: ausbauen oder stoppen.

Erste Ergebnisse entstehen innerhalb von 4 Stunden, nicht Monaten. Der KI-Telefonassistent ist am selben Tag einsatzbereit — mit einer trainierten Wissensdatenbank, angebunden an das bestehende System.

Ohne Pilot keine Diskussion.

#### 5. Was KI bei uns übernimmt — und was nicht

**Der KI-Assistent übernimmt:**
- Erstkontakt am Telefon — rund um die Uhr, auch außerhalb der Geschäftszeiten
- Beantwortung wiederkehrender Fragen in natürlicher Sprache
- Strukturierte Erfassung von Anliegen und Weiterleitung an das Team
- Echtzeit-Zugriff auf Shopsysteme für Lieferstatus, Bestelldaten, Retouren

**Das Team übernimmt:**
- Komplexe Fälle, die Urteilsvermögen erfordern
- Entscheidungen mit Kulanzspielraum
- Echte Kundenbeziehungen, die Empathie brauchen

KI ersetzt keine Mitarbeiter. KI entlastet Mitarbeiter von dem, was sie ohnehin nicht gerne tun.

#### 6. Woran wir uns messen lassen

Nicht an Präsentationen. Nicht an Konzepten.

Sondern an:
- Weniger verpassten Anrufen — messbar im Dashboard
- Kürzeren Bearbeitungszeiten für Standardanfragen
- Spürbarer Entlastung im Tagesgeschäft des Teams
- Erreichbarkeit außerhalb der Geschäftszeiten — ohne zusätzliches Personal

Wenn das nicht eintritt, war es die falsche Lösung. Dann stoppen wir.

#### 7. Unsere Technik

Wir entwickeln keine Systeme auf der grünen Wiese. Wir docken an:
- Bestehende Telefonanlagen (SIP-Integration)
- Warenwirtschafts- und Shopsysteme (REST-API)
- Bestehende Prozesse und Workflows

Ohne Systemwechsel. Ohne monatelange Migrationsprojekte. Der Assistent arbeitet mit dem, was da ist.

Die Plattform basiert auf VAaaS — Virtual Assistant as a Service. Nutzung statt Vorhaltung: Kein eigenes KI-Team aufbauen, keine Infrastruktur betreiben, keine Fixkosten für Kapazität, die nicht gebraucht wird.

#### 8. Was wir nicht tun

Wir bauen keine isolierten KI-Spielereien ohne Anschluss an den Betrieb. Keine komplizierten Plattformen, die ein eigenes IT-Team zur Wartung brauchen. Keine Projekte ohne klaren wirtschaftlichen Effekt.

Und wir verkaufen keine Visionen ohne Umsetzung.

#### 9. Zielbild

Ein Unternehmen, das erreichbar ist. Ohne Überlastung im Team.
Ein System, das Routine übernimmt, ohne Kontrolle abzugeben.
KI, die im Hintergrund arbeitet — und im Ergebnis sichtbar wird.

---

### FAQ-Sektion

Überschrift (Bebas Neue, Kupfer): HÄUFIGE FRAGEN

Jede Frage als eigener Block. Zwei mögliche Darstellungen — Cursor entscheidet, was besser zum CI passt:

**Option A:** Offene Blöcke (Frage als `<h3>`, Antwort als `<p>`)
**Option B:** `<details>` / `<summary>` (klappbar)

Wichtig: Unabhängig von der visuellen Darstellung muss das Schema.org FAQPage-Markup im `<head>` stehen (siehe unten).

---

**Frage 1: Was ist VAaaS?**

VAaaS steht für Virtual Assistant as a Service — ein KI-basierter Telefonassistent, der eingehende Anrufe für Unternehmen entgegennimmt. Der Assistent beantwortet Standardanfragen wie Lieferstatus, Retouren oder Öffnungszeiten in natürlicher Sprache, greift in Echtzeit auf Shopsysteme zu und leitet komplexe Anliegen strukturiert an das Team weiter. Kein Anrufbeantworter, sondern ein vollwertiger Gesprächspartner — rund um die Uhr, auch außerhalb der Geschäftszeiten.

**Frage 2: Für welche Unternehmen eignet sich VAaaS?**

VAaaS richtet sich an mittelständische Unternehmen mit 5 bis 50 Mitarbeitern, die ein wachsendes Volumen an Kundenanfragen bewältigen müssen — insbesondere E-Commerce-Händler, IT-Dienstleister und serviceorientierte Betriebe. Wenn pro Monat zwischen 300 und 5.000 Anrufe eingehen und ein erheblicher Teil davon Standardanfragen sind, ist VAaaS die richtige Lösung.

**Frage 3: Wie schnell ist VAaaS einsatzbereit?**

Der KI-Telefonassistent ist innerhalb von 4 Stunden live einsatzbereit. Die Einrichtung umfasst eine Bedarfsanalyse, die Konfiguration der Wissensdatenbank und die Anbindung an das bestehende System. Ein Systemwechsel ist nicht nötig.

**Frage 4: Was kostet VAaaS?**

VAaaS funktioniert nach dem Prinzip Nutzung statt Vorhaltung — keine Fixkosten für Personal, das auf Anrufe wartet. Die konkreten Konditionen hängen vom Anrufvolumen und der gewünschten Integration ab. Das Erstgespräch ist kostenfrei.

**Frage 5: Kann der KI-Assistent auf mein Shopsystem zugreifen?**

Ja. Der Assistent wird über REST-API an bestehende Warenwirtschafts- und Shopsysteme angebunden und kann in Echtzeit Bestelldaten, Lieferstatus und Kundeninformationen abrufen. Die Integration erfolgt ohne Systemwechsel.

**Frage 6: Was passiert bei komplexen Anfragen?**

Anliegen, die Urteilsvermögen, Entscheidungskompetenz oder Empathie erfordern — Reklamationen mit Kulanzentscheidung, emotionale Eskalationen, Sonderfälle — werden vom Assistenten strukturiert erfasst und zur Nachbearbeitung an das Team weitergeleitet. Der Mitarbeiter beginnt nicht von vorne, sondern hat alle relevanten Informationen aus dem Gespräch.

**Frage 7: Wer steckt hinter BERENT?**

BERENT | Beratung + Entwicklung wird geführt von Marcus Kunkel — TÜV-zertifizierter KI-Strategieberater und einer der weltweit 25 ersten zertifizierten Hedy-Trainer. Er begleitet mittelständische Unternehmen bei der Einführung von Automatisierung und KI mit systemischem Blick, klarer Bedarfsanalyse und praxisnahen Trainings.

**Frage 8: Was ist Hedy?**

Hedy ist ein KI-gestützter Meeting-Assistent, der Gespräche in Echtzeit analysiert und kontextbezogene Empfehlungen gibt — direkt während des Meetings. Hedy läuft auf dem eigenen Gerät, versteht 19 Sprachen und ist DSGVO-konform mit EU-Datenresidenz. Kein Bot, der dem Call beitritt. Keine Aufzeichnung auf fremden Servern.

**Frage 9: Wie kann ich ein Erstgespräch buchen?**

Über die Seite berent.ai/termin.html oder per E-Mail an office@berent.ai. Das Erstgespräch ist kostenfrei.

**Frage 10: Welche weiteren Tools bietet BERENT an?**

Neben VAaaS bietet BERENT eine Reihe kostenloser Werkzeuge an: einen ROI-Rechner für KI-Telefonassistenz (roi.berent.ai), die Textschmiede für KI-gestützte Textgenerierung (textschmiede-5tc.berent.ai), einen Webseiten-Relaunch-Guide (relaunch-guide.berent.ai) und einen Blog mit Praxiswissen zu KI im Mittelstand (blog.berent.ai).

---

## Schema.org LD+JSON

Im `<head>` der Seite drei separate `<script type="application/ld+json">`-Blöcke einfügen:

### Block 1: CreativeWork (Manifest)

```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "name": "KI-Manifest — BERENT | Beratung + Entwicklung",
  "author": {
    "@type": "Person",
    "name": "Marcus Kunkel",
    "jobTitle": "KI-Strategieberater",
    "url": "https://www.berent.ai/profil"
  },
  "publisher": {
    "@type": "Organization",
    "name": "BERENT | Beratung + Entwicklung",
    "url": "https://www.berent.ai"
  },
  "description": "Wie BERENT KI einsetzt: Telefonassistenz, Automatisierung und Pilotprojekte für E-Commerce und Mittelstand.",
  "inLanguage": "de",
  "url": "https://www.berent.ai/manifest",
  "datePublished": "2026-04-12",
  "keywords": ["KI-Manifest", "KI-Telefonassistent", "VAaaS", "E-Commerce Automatisierung", "Mittelstand KI"]
}
```

### Block 2: FAQPage

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Was ist VAaaS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "VAaaS steht für Virtual Assistant as a Service — ein KI-basierter Telefonassistent, der eingehende Anrufe für Unternehmen entgegennimmt. Der Assistent beantwortet Standardanfragen wie Lieferstatus, Retouren oder Öffnungszeiten in natürlicher Sprache und leitet komplexe Anliegen strukturiert an das Team weiter."
      }
    },
    {
      "@type": "Question",
      "name": "Für welche Unternehmen eignet sich VAaaS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "VAaaS richtet sich an mittelständische Unternehmen mit 5 bis 50 Mitarbeitern, die ein wachsendes Volumen an Kundenanfragen bewältigen müssen — insbesondere E-Commerce-Händler, IT-Dienstleister und serviceorientierte Betriebe."
      }
    },
    {
      "@type": "Question",
      "name": "Wie schnell ist VAaaS einsatzbereit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Der KI-Telefonassistent ist innerhalb von 4 Stunden live einsatzbereit. Die Einrichtung umfasst Bedarfsanalyse, Konfiguration der Wissensdatenbank und Anbindung an das bestehende System."
      }
    },
    {
      "@type": "Question",
      "name": "Was kostet VAaaS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "VAaaS funktioniert nach dem Prinzip Nutzung statt Vorhaltung — keine Fixkosten für Personal, das auf Anrufe wartet. Das Erstgespräch ist kostenfrei."
      }
    },
    {
      "@type": "Question",
      "name": "Kann der KI-Assistent auf mein Shopsystem zugreifen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Der Assistent wird über REST-API an bestehende Warenwirtschafts- und Shopsysteme angebunden und kann in Echtzeit Bestelldaten, Lieferstatus und Kundeninformationen abrufen."
      }
    },
    {
      "@type": "Question",
      "name": "Was passiert bei komplexen Anfragen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Komplexe Anliegen werden vom Assistenten strukturiert erfasst und zur Nachbearbeitung an das Team weitergeleitet. Der Mitarbeiter hat alle relevanten Informationen aus dem Gespräch."
      }
    },
    {
      "@type": "Question",
      "name": "Wer steckt hinter BERENT?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "BERENT wird geführt von Marcus Kunkel — TÜV-zertifizierter KI-Strategieberater und einer der weltweit 25 ersten zertifizierten Hedy-Trainer."
      }
    },
    {
      "@type": "Question",
      "name": "Was ist Hedy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hedy ist ein KI-gestützter Meeting-Assistent, der Gespräche in Echtzeit analysiert und kontextbezogene Empfehlungen gibt — DSGVO-konform mit EU-Datenresidenz."
      }
    },
    {
      "@type": "Question",
      "name": "Wie kann ich ein Erstgespräch buchen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Über berent.ai/termin.html oder per E-Mail an office@berent.ai. Das Erstgespräch ist kostenfrei."
      }
    },
    {
      "@type": "Question",
      "name": "Welche weiteren Tools bietet BERENT an?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Neben VAaaS bietet BERENT einen ROI-Rechner (roi.berent.ai), die Textschmiede (textschmiede-5tc.berent.ai), einen Webseiten-Relaunch-Guide (relaunch-guide.berent.ai) und einen Blog (blog.berent.ai)."
      }
    }
  ]
}
```

### Block 3: Person mit Credentials

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Marcus Kunkel",
  "jobTitle": "KI-Strategieberater",
  "url": "https://www.berent.ai/profil",
  "worksFor": {
    "@type": "Organization",
    "name": "BERENT | Beratung + Entwicklung",
    "url": "https://www.berent.ai"
  },
  "hasCredential": [
    {
      "@type": "EducationalOccupationalCredential",
      "name": "TÜV-zertifizierter Manager für angewandte KI-Transformation",
      "credentialCategory": "Professional Certification"
    },
    {
      "@type": "EducationalOccupationalCredential",
      "name": "Certified Hedy Trainer",
      "credentialCategory": "Professional Certification",
      "recognizedBy": {
        "@type": "Organization",
        "name": "Koerting Institute"
      }
    }
  ],
  "knowsAbout": ["KI-Transformation", "Telefonassistenz", "VAaaS", "Automatisierung", "KI-Strategieberatung", "Hedy AI", "E-Commerce"],
  "sameAs": [
    "https://linkedin.com/in/berentai",
    "https://instagram.com/berent.ai"
  ]
}
```

## Meta-Tags

```html
<title>KI-Manifest — BERENT | Beratung + Entwicklung</title>
<meta name="description" content="Wie BERENT KI einsetzt: Kein Hype, kein Konzeptpapier. Telefonassistenz, Automatisierung und Pilotprojekte für E-Commerce und Mittelstand — messbar, umsetzbar, ab 4 Stunden live.">
<link rel="canonical" href="https://www.berent.ai/manifest">
<meta property="og:title" content="KI-Manifest — BERENT | Beratung + Entwicklung">
<meta property="og:description" content="Wie BERENT KI einsetzt: Telefonassistenz, Automatisierung und Pilotprojekte für E-Commerce und Mittelstand.">
<meta property="og:url" content="https://www.berent.ai/manifest">
<meta property="og:type" content="article">
<meta property="og:image" content="https://www.berent.ai/images/og-image.png">
```

## Sitemap aktualisieren

In `sitemap.xml` einen neuen Eintrag hinzufügen:

```xml
<url>
  <loc>https://www.berent.ai/manifest</loc>
  <lastmod>2026-04-12</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
```

## NICHT ändern

- `index.html` — wird in Session 2 (separates Briefing) bearbeitet
- `output.css` — bleibt unverändert
- Andere HTML-Seiten — nicht anfassen
- Assets — bleiben

## Akzeptanzkriterien

1. `manifest.html` existiert im Repo-Root
2. Seite ist unter `berent.ai/manifest` erreichbar (Vercel Clean URLs)
3. Navigation und Footer sind identisch zur Startseite
4. Dark/Light Mode funktioniert
5. Mobile-responsive (Navigation, Layout, Schriftgrößen)
6. Schema.org-Markup ist valide (prüfbar unter https://validator.schema.org)
7. Alle 9 Manifest-Punkte und 10 FAQ-Fragen sind vorhanden
8. Meta-Tags und OG-Tags sind korrekt
9. Sitemap ist aktualisiert

## Abschluss

```bash
git add -A
git commit -m "[BER-62] done: Manifest-Seite mit FAQ und Schema.org"
git push
```

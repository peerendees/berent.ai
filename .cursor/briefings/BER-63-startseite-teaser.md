# Cursor-Briefing: Startseite Teaser-Sektion + Schema.org
**Datum:** 12.04.2026
**Linear-Issue:** [BER-63](https://linear.app/berent/issue/BER-63)
**Projekt:** Webseite + Beratungswerkzeuge
**Komplexität:** Einfach–Mittel
**Repo:** `peerendees/berent.ai`
**Lokaler Pfad:** `/Users/kunkel/Entwicklung/projekte/berentai`

## Ziel

Zwei Ergänzungen an der bestehenden `index.html`:
1. **Teaser-Sektion** zwischen Hero und Testimonials — drei kompakte Blöcke, die BERENT positionieren
2. **Schema.org-Erweiterung** im `<head>` — Service, WebSite und Person-Schema zusätzlich zum bestehenden ProfessionalService

## Kontext

Die Manifest-Seite (`berent.ai/manifest`, BER-62) steht bereits. Die Startseite braucht jetzt eine kurze Einführungs-Sektion, die erklärt wer BERENT ist und was angeboten wird — und einen Link zum Manifest. Zusätzlich fehlen im `<head>` noch Schema.org-Objekte für den Service (VAaaS), die Website und Marcus' Credentials.

## Änderung 1: Teaser-Sektion einfügen

### Platzierung

Die Sektion kommt **direkt nach dem schließenden `</div>` des Hero** (`hero-ber44`) und **vor** der Testimonials-Sektion (`section-ber-testimonials`).

In der aktuellen `index.html` ist das hier:

```html
    </div>  <!-- Ende hero-ber44 -->

    <!-- HIER EINFÜGEN: Teaser-Sektion -->

    <!-- LinkedIn-Testimonials -->
    <section class="section-ber-testimonials py-16 md:py-20">
```

### HTML der Teaser-Sektion

```html
<!-- Leistungs-Teaser -->
<section class="py-16 md:py-20" style="background:var(--bg);">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-10 md:grid-cols-3 md:gap-8">

            <!-- Block 1: Erreichbarkeit -->
            <div class="space-y-4">
                <h2 style="font-family:'Bebas Neue',sans-serif; color:var(--copper); font-size:clamp(1.25rem,2.5vw,1.75rem); letter-spacing:0.04em;">
                    ERREICHBARKEIT IST KEIN LUXUS
                </h2>
                <p style="font-family:'Lora',serif; color:var(--text); font-weight:300; line-height:1.8; font-size:0.95rem;">
                    Im E-Commerce gehen 30 bis 40 Prozent der Anrufe außerhalb der Geschäftszeiten ein. Ohne Antwort, ohne Ticket, ohne Spur. VAaaS übernimmt diese Anrufe — als KI-Telefonassistent, der Standardanfragen in natürlicher Sprache beantwortet und komplexe Fälle strukturiert an das Team weitergibt.
                </p>
                <p style="font-family:'Lora',serif; font-weight:300; font-size:0.95rem;">
                    <a href="https://vaaas.berent.ai" target="_blank" rel="noopener" style="color:var(--copper);">Mehr erfahren →</a>
                </p>
            </div>

            <!-- Block 2: Zielgruppe -->
            <div class="space-y-4">
                <h2 style="font-family:'Bebas Neue',sans-serif; color:var(--copper); font-size:clamp(1.25rem,2.5vw,1.75rem); letter-spacing:0.04em;">
                    MITTELSTAND. NICHT KONZERN.
                </h2>
                <p style="font-family:'Lora',serif; color:var(--text); font-weight:300; line-height:1.8; font-size:0.95rem;">
                    BERENT arbeitet mit Unternehmen zwischen 5 und 50 Mitarbeitern — E-Commerce-Händler, IT-Dienstleister, serviceorientierte Betriebe. Das Team ist zu klein für eine eigene Telefon-Schicht, aber zu groß, um jeden Anruf selbst zu beantworten.
                </p>
                <p style="font-family:'Lora',serif; font-weight:300; font-size:0.95rem;">
                    <a href="/termin" style="color:var(--copper);">Kostenloses Erstgespräch →</a>
                </p>
            </div>

            <!-- Block 3: Manifest -->
            <div class="space-y-4">
                <h2 style="font-family:'Bebas Neue',sans-serif; color:var(--copper); font-size:clamp(1.25rem,2.5vw,1.75rem); letter-spacing:0.04em;">
                    KI-MANIFEST
                </h2>
                <p style="font-family:'Lora',serif; color:var(--text); font-weight:300; line-height:1.8; font-size:0.95rem;">
                    Kein Hype. Keine leeren Versprechen. In 9 Punkten beschreiben wir, wie wir KI einsetzen, was wir nicht tun und woran wir uns messen lassen. Plus 10 häufige Fragen — beantwortet.
                </p>
                <p style="font-family:'Lora',serif; font-weight:300; font-size:0.95rem;">
                    <a href="/manifest" style="color:var(--copper);">Manifest lesen →</a>
                </p>
            </div>

        </div>
    </div>
</section>
```

### Design-Hinweise

- Gleiche visuelle Sprache wie Hedy-Sektion und Testimonials
- Bebas Neue für Überschriften, Lora für Fließtext
- Kupfer-Links ohne Unterstrich (wie bestehende Links)
- Auf Mobile stacken die drei Blöcke vertikal (`grid-cols-1`)
- Kein Border, kein Kasten — nur Abstand und Typografie

## Änderung 2: Schema.org im `<head>` ergänzen

Die bestehende `index.html` hat bereits ein `ProfessionalService`-Schema. **Dieses nicht verändern.** Die folgenden drei Blöcke **zusätzlich** einfügen, direkt nach dem bestehenden `</script>` des ProfessionalService-Schemas:

### Block 1: Service (VAaaS)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "VAaaS — Virtual Assistant as a Service",
  "provider": {
    "@type": "Organization",
    "name": "BERENT | Beratung + Entwicklung",
    "url": "https://www.berent.ai"
  },
  "description": "KI-basierte Telefonassistenz für E-Commerce und Mittelstand. Standardanfragen automatisieren, Erreichbarkeit sicherstellen, Team entlasten — innerhalb von 4 Stunden einsatzbereit.",
  "serviceType": "KI-Telefonassistenz",
  "areaServed": {
    "@type": "Country",
    "name": "DE"
  },
  "url": "https://vaaas.berent.ai",
  "offers": {
    "@type": "Offer",
    "description": "Kostenfreies Erstgespräch",
    "price": "0",
    "priceCurrency": "EUR"
  }
}
</script>
```

### Block 2: WebSite

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "BERENT | Beratung + Entwicklung",
  "url": "https://www.berent.ai",
  "description": "KI-Strategieberatung und Transformation für den Mittelstand. Telefonassistenz, Automatisierung, Trainings.",
  "publisher": {
    "@type": "Organization",
    "name": "BERENT | Beratung + Entwicklung"
  },
  "inLanguage": "de"
}
</script>
```

### Block 3: Person mit Credentials

```html
<script type="application/ld+json">
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
</script>
```

## NICHT ändern

- Hero-Sektion — nicht anfassen
- Testimonials — nicht anfassen
- Hedy-Sektion — nicht anfassen
- Footer — nicht anfassen
- `output.css` — nicht anfassen
- Bestehende Schema.org (ProfessionalService) — nicht verändern, nur ergänzen
- Andere HTML-Seiten — nicht anfassen

## Akzeptanzkriterien

1. Teaser-Sektion ist sichtbar zwischen Hero und Testimonials
2. Drei Blöcke: Erreichbarkeit, Mittelstand, KI-Manifest
3. Links funktionieren (vaaas.berent.ai, /termin, /manifest)
4. Mobile-responsive (Blöcke stacken auf Phones)
5. Dark/Light Mode funktioniert für die neuen Elemente
6. Schema.org: Service, WebSite, Person — valide im `<head>`
7. Bestehendes ProfessionalService-Schema unverändert

## Abschluss

```bash
git add -A
git commit -m "[BER-63] done: Teaser-Sektion + Schema.org auf Startseite"
git push
```

# Cursor-Briefing: Landingpage aufräumen + Testimonials + Hedy-Sektion
**Datum:** 04. April 2026
**Linear-Issue:** [BER-45](https://linear.app/berent/issue/BER-45/landingpage-aufraumen-sektionen-entfernen-linkedin-testimonials-hedy)
**Projekt:** Webseite + Beratungswerkzeuge
**Komplexität:** Mittel
**Voraussetzung:** BER-44 (Hero-Umbau) sollte abgeschlossen oder zumindest committet sein, damit kein Merge-Konflikt entsteht.

## Ziel

Die Landingpage auf den Baustellenmodus reduzieren: Alle bestehenden Content-Sektionen zwischen Hero und Footer entfernen. Stattdessen drei Elemente: LinkedIn-Testimonials, Hedy-Sektion, Kontaktformular.

**Seitenstruktur danach:**
```
Navigation (fixed)
Hero-Sektion (BER-44)
LinkedIn-Testimonials (NEU)
Hedy-Sektion (NEU)
Kontaktformular (bestehend, angepasst)
Footer
```

## Schritt 1: Sektionen entfernen

Folgende Blöcke aus `index.html` komplett löschen (den HTML-Code entfernen, nicht nur ausblenden):

1. **Leistungen-Sektion** — `<section id="leistungen">` bis zum schließenden `</section>` (inkl. aller 4 Feature-Karten und dem Nutzen-Block)
2. **„Was ich Dir noch sagen möchte"-Block** — Teil der Leistungen-Sektion (6 Karten Herausforderungen + 6 Karten Zukunftssicher)
3. **„Meine Kunden schätzen an mir"-Block** — `<div class="relative bg-[#80331A]/90 ...">` (dunkler Hintergrund mit 6 Karten)

**Beibehalten:**
- Navigation (komplett)
- Hero-Sektion (komplett, wurde in BER-44 umgebaut)
- Footer (komplett, inkl. Kontaktformular)

## Schritt 2: LinkedIn-Testimonials Sektion

Neue Sektion direkt nach der Hero-Sektion einfügen.

### Design
- Hintergrund: `#090806` (CI-Hintergrund) oder leicht abgesetzt `#110E0A` (Card)
- Überschrift: „Was andere sagen" — Bebas Neue, Kupfer `#B5742A`, UPPERCASE
- 2-3 Testimonial-Karten nebeneinander (Desktop), untereinander (Mobile)

### Kartenstruktur pro Testimonial
```html
<div style="background:#110E0A; border:1px solid #2A2118; border-radius:8px; padding:24px;">
    <!-- Anführungszeichen-Icon -->
    <svg><!-- Anführungszeichen in Kupfer #B5742A --></svg>
    
    <!-- Zitat-Text -->
    <p style="font-family:'Lora',serif; color:#C4BCB1; font-weight:300; font-size:16px; line-height:1.7;">
        „Hier steht das Testimonial-Zitat von LinkedIn..."
    </p>
    
    <!-- Person -->
    <div style="margin-top:16px; display:flex; align-items:center; gap:12px;">
        <!-- Platzhalter-Avatar (Kreis mit Initialen) -->
        <div style="width:48px; height:48px; border-radius:50%; background:#2A2118; display:flex; align-items:center; justify-content:center;">
            <span style="color:#B5742A; font-family:'Bebas Neue',sans-serif; font-size:18px;">MK</span>
        </div>
        <div>
            <p style="color:#C4BCB1; font-family:'Lora',serif; font-weight:600; font-size:14px;">Vorname Nachname</p>
            <p style="color:#7A6A58; font-family:'Lora',serif; font-weight:300; font-size:13px;">Position, Firma</p>
        </div>
    </div>
</div>
```

### Testimonial-Inhalte (echte LinkedIn-Empfehlungen)

**Testimonial 1:**
- Name: Lutz Beutgen
- Initialen: LB
- Position: Interim Manager · Effizienzsteigerung in Produktion und Supply Chain durch KI-Lösungen
- Zitat: „Marcus Kunkel verbindet technologische Expertise mit einem tiefen Verständnis für systemische Prozesse – besonders im Mittelstand. Seine Fähigkeit, Künstliche Intelligenz nicht nur technisch umzusetzen, sondern auch menschlich dem Mitarbeiter zu vermitteln, macht ihn zu einem außergewöhnlich wirksamen Begleiter in Transformationsprozessen. Besonders hervorzuheben ist seine methodische Herangehensweise: erst analysieren, dann umsetzen – mit Werkzeugen, die wirklich passen, und mit Trainings, die ankommen."

**Testimonial 2:**
- Name: Christine van Tübbergen
- Initialen: CT
- Position: Speakerin · KI-Trainerin · Unternehmerin
- Zitat: „Marcus erklärt selbst komplexe Themen rund um KI und Automatisierung so verständlich, dass man sich abgeholt und sicher fühlt – ganz ohne Buzzwords oder Druck. Er denkt ganzheitlich, stellt kluge Fragen und bringt Technik und Menschen wirklich zusammen. Substanz statt Hype, Struktur statt Überforderung, und Lösungen, die langfristig wirken."

**Testimonial 3:**
- Name: Holger Dominik Steinbichler
- Initialen: HS
- Position: Berater · Handlungsspielräume für die Zukunft
- Zitat: „Marcus Kunkel überzeugt durch seine Fähigkeit, Digitalisierung und KI nicht nur technisch, sondern vor allem auch menschlich greifbar zu machen. Mit einem klaren Blick für den Mittelstand schafft er es, Teams mitzunehmen, sinnvolle Automatisierung umzusetzen und Prozesse so zu gestalten, dass sie wirklich wirken."

### Responsives Verhalten
- **Desktop (≥1024px):** 3 Karten nebeneinander (Grid 3 Spalten)
- **Tablet (768–1023px):** 2 Karten + 1 Karte darunter
- **Mobile (<768px):** Alle Karten untereinander (1 Spalte)

## Schritt 3: Hedy-Sektion

Neue Sektion nach den Testimonials, vor dem Footer.

### Inhalt

**Überschrift:** „DEIN KI-MEETING-COACH" — Bebas Neue, Kupfer, UPPERCASE

**Beschreibungstext (Lora, #C4BCB1):**

> Hedy ist ein KI-gestützter Meeting-Assistent, der Gespräche in Echtzeit analysiert und dir kontextbezogene Empfehlungen gibt — direkt während des Meetings. Kein Bot, der deinem Call beitritt. Keine Aufzeichnung auf fremden Servern. Hedy läuft auf deinem Gerät, versteht 19 Sprachen und ist DSGVO-konform mit EU-Datenresidenz.

**Badge/Highlight-Box:**
```
CERTIFIED HEDY TRAINER
Einer der weltweit 25 ersten zertifizierten Hedy-Trainer.
Erste Trainingsgruppe am Koerting Institut in Zusammenarbeit mit Hedy AI.
```
- Styling: Card-Hintergrund `#110E0A`, Kupfer-Border links (4px solid), Text in `#C4BCB1`
- „CERTIFIED HEDY TRAINER" in Bebas Neue, Kupfer

**Features (3 Punkte, nebeneinander auf Desktop):**

1. **Echtzeit-Coaching** — Bekomme im Gespräch Vorschläge für Fragen, Argumente und Gesprächsstrategien.
2. **Datenschutz first** — Spracherkennung on-device, EU-Datenhaltung, kein Bot in deinem Call. SOC 2 Type II und HIPAA in Zertifizierung.
3. **Integration** — MCP-Anbindung an Claude, n8n-Workflows, API für eigene Anwendungen.

Jedes Feature als kleine Card mit Icon (SVG, Kupfer) + Titel (Lora 600, #C4BCB1) + Text (Lora 300, #7A6A58).

**CTA-Button:**
```
Hedy kennenlernen → hedy.ai
```
- Button: Kupfer-Hintergrund `#B5742A`, Text `#090806`, abgerundet
- Link: `https://www.hedy.ai`

### Design
- Hintergrund: `#090806` (Standard) oder dezent abgesetzt mit einem subtilen Kupfer-Gradient am oberen Rand
- Layout: Zweispaltig auf Desktop (Text links, Badge/Features rechts), einspaltig auf Mobile

## Schritt 4: Footer/Kontaktformular anpassen

Das Kontaktformular im Footer bleibt bestehen, aber visuell anpassen:

- Hintergrund: von `background-image: url('images/hintergrund-footer.jpg')` auf `#090806` (CI-konform) — oder behalten, wenn es gut aussieht
- Formular-Felder: `bg-gray-800` → `#110E0A`, Border `#2A2118`
- Labels/Text: `#C4BCB1`
- Submit-Button: Kupfer `#B5742A` statt weiß
- „Über mich"-Text und „Soziale Medien"-Block können bleiben, Text-Farbe auf `#C4BCB1` umstellen
- Impressum/Datenschutz-Links beibehalten

## CI-Referenz

Siehe `.cursor/rules/berent-ci.md` im Repo.

Kurzfassung:
```
Hintergrund: #090806 | Card: #110E0A | Border: #2A2118
Kupfer: #B5742A | Gold (nur +Symbol): #E8C98A
Text: #C4BCB1 | Muted: #7A6A58
Headlines: Bebas Neue (UPPERCASE) | Body: Lora (300/400/600) 
```

## Dateien
- `index.html` — Sektionen entfernen, neue einfügen, Footer anpassen
- `input.css` / `output.css` — bei Bedarf neue Tailwind-Klassen, dann `npx tailwindcss -i input.css -o output.css`
- Keine neuen Bilder nötig (Hedy-Logo optional, aber kein Muss)

## Akzeptanzkriterien
- [ ] Alte Sektionen (Leistungen, Nutzen, Herausforderungen, Kunden schätzen) komplett entfernt
- [ ] Testimonials-Sektion mit 3 Platzhalter-Karten sichtbar und responsive
- [ ] Hedy-Sektion mit Beschreibung, Badge und 3 Feature-Karten
- [ ] Kontaktformular weiterhin funktional
- [ ] Seite scrollt flüssig: Hero → Testimonials → Hedy → Kontakt/Footer
- [ ] Neues CI durchgängig in den neuen Sektionen (Farben, Fonts)
- [ ] Keine Console-Errors

## Abschluss
Wenn alle Änderungen umgesetzt sind:
```bash
git add -A
git commit -m "[BER-45] done: Landingpage aufgeräumt, Testimonials + Hedy-Sektion ergänzt"
git push
```
Dieser Commit triggert den automatischen Rückkanal (Linear → Done, Threema-Benachrichtigung, Notion-Marker).

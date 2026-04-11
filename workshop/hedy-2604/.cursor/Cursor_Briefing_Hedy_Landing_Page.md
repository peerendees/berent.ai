# Cursor-Briefing: Hedy Experience Sprint Landing Page

## Ziel
Die heruntergeladene Datei `hedy-2604-landing-page.html` in die korrekte Projektstruktur überführen, Hell-Dunkel-Toggle ergänzen und nach GitHub pushen.

---

## Schritt 1: Datei umbenennen und einordnen

Die heruntergeladene Datei liegt vermutlich in `~/Downloads/`.

```
mkdir -p app/hedy-2604/danke
mv ~/Downloads/hedy-2604-landing-page.html app/hedy-2604/index.html
```

## Schritt 2: Hell-Dunkel-Toggle

Integriere den Hell-Dunkel-Toggle aus den bestehenden BERENT-Seiten (z. B. webseiten-relaunch). Der Toggle muss:

- In der Navigation rechts neben dem CTA-Button "Platz sichern" sitzen
- Dieselbe Funktionalität und dasselbe Aussehen wie auf den anderen BERENT-Seiten haben
- Den Zustand in `localStorage` speichern
- Beim Laden den gespeicherten Zustand wiederherstellen

**Light-Mode Farbschema (analog zu den anderen BERENT-Seiten):**
- Hintergrund: `#F5EFE4` (Champagne)
- Card-Hintergrund: `#FFFFFF`
- Text: `#2A1A08` (Warmbraun)
- Sekundärtext: `#7A6A58`
- Border: `#E0D5C5`
- Kupfer und Gold bleiben unverändert

Referenz: Schau Dir den Toggle in `@webseiten-relaunch/index.html` an und übernimm die Implementierung.

## Schritt 3: Danke-Seite erstellen

Erstelle `app/hedy-2604/danke/index.html` mit folgendem Inhalt:

- Gleiches Design wie die Landing Page (inkl. Hell-Dunkel-Toggle)
- Überschrift: "Du bist dabei!"
- Text: "Danke für Deine Buchung. Du erhältst in Kürze eine Bestätigungsmail mit allen Details und Deiner Vorbereitungsanleitung. Ich freue mich auf den Workshop mit Dir."
- Details: Termin 28.–29. April 2026, 18:45 Uhr / Online via Zoom / Nächster Schritt: Schau in Dein Postfach
- Navigation und Footer identisch zur Landing Page
- Kein CTA-Button

## Schritt 4: DSGVO – Google Fonts entfernen

Die Landing Page lädt aktuell Schriften über Google Fonts CDN. Das ist nicht DSGVO-konform.

1. Lade die Schriften Bebas Neue, Lora (300, 400, 600) und JetBrains Mono (300, 400, 700) als WOFF2 herunter
2. Lege sie unter `assets/fonts/` ab
3. Ersetze den Google Fonts `<link>` durch lokale `@font-face`-Deklarationen
4. Dasselbe für die Danke-Seite

## Schritt 5: Prüfung vor Push

Vor dem Commit sicherstellen:

- [ ] `index.html` liegt in `app/hedy-2604/`
- [ ] `danke/index.html` liegt in `app/hedy-2604/danke/`
- [ ] Fonts liegen lokal in `assets/fonts/` – kein Google Fonts CDN
- [ ] Hell-Dunkel-Toggle funktioniert und speichert den Zustand
- [ ] Alle internen Links stimmen (CTA → `#buchen`, Nav → `https://berent.ai`)
- [ ] Footer: Impressum-Link + "Zurück zur Hauptseite" (ohne Pfeil)
- [ ] Stripe Payment Link ist noch `#` (Platzhalter) – das ist korrekt, wird später ersetzt
- [ ] Termin überall: 28.–29. April 2026 (Di–Mi), 18:45 Uhr
- [ ] Preise im Währungsformat: 149,00 € zzgl. MwSt.

## Schritt 6: Commit und Push

```
git add .
git commit -m "feat: Landing Page Hedy Experience Sprint 2604"
git push
```

Vercel deployed automatisch nach Push.

---

## Offene Punkte (NICHT in diesem Briefing)

- Stripe Payment Link einfügen (sobald Produkt angelegt)
- Affiliate-Link zu Hedy auf der Seite platzieren
- OG-Meta-Tags für LinkedIn-Vorschau ergänzen
- Favicon einbinden

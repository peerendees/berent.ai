# Cursor-Briefing: Landing Page Nachbesserungen

## Referenz
Design-Referenz ist der Webseiten-Relaunch-Leitfaden unter `@webseiten-relaunch/index.html`. Gleiche die Landing Page an dessen Typografie, Abstände und Designelemente an.

---

## 1. Navigation: Button entfernen

Entferne den CTA-Button "Platz sichern" rechts oben in der Navigation komplett. Die Navigation enthält nur noch den Brand-Link (Plus-Symbol + BERENT.AI) und den Hell-Dunkel-Toggle.

## 2. CTA-Button: Dezente Größe

Der Button "Jetzt Platz sichern" ist aktuell über die volle Breite – das ist viel zu groß. Änderungen:

- Button auf `display: inline-block` mit `padding: 1rem 2.5rem` (nicht volle Breite)
- Zentriert im Container, aber nicht 100% breit
- Gleiches Styling wie im Relaunch-Leitfaden (falls dort Buttons vorhanden)
- Gilt für beide CTA-Buttons (Hero + Block 9)

## 3. Typografie und Abstände angleichen

Vergleiche die Landing Page mit `@webseiten-relaunch/index.html` und passe an:

### Headlines (Bebas Neue)
- Aktuell zu groß und zu eng. Reduziere die `font-size` der Section-Headlines (h2) auf das Niveau des Relaunch-Leitfadens
- Mehr `line-height` (ca. 1.15–1.2) für bessere Lesbarkeit
- Mehr `margin-bottom` zwischen Headline und Fließtext (mind. 2rem)

### Fließtext (Lora)
- `font-weight: 300` beibehalten
- `line-height: 1.7` beibehalten
- Ausreichend Abstand zum nächsten Block

### Sektionsnummern
- Übernimm das Muster aus dem Relaunch-Leitfaden: kleine Sektionsnummer in JetBrains Mono oberhalb der Headline, z. B. `01 — PROBLEM`, `02 — LÖSUNG`, etc.
- Farbe: `var(--muted)` oder `var(--copper)` je nach Referenz
- `font-size: 0.7rem`, `letter-spacing: 0.12em`, `text-transform: uppercase`

### Generell
- Mehr Weißraum zwischen den Sektionen
- Ruhigerer Rhythmus – die Seite soll atmen, nicht erschlagen

## 4. Senkrechte Striche konsistent

Die senkrechten Kupfer-Striche (`border-left: 2px solid var(--copper)`) an den Fließtext-Blöcken beibehalten, aber prüfen:

- Stimmen Farbe und Stärke mit dem Relaunch-Leitfaden überein?
- Werden sie dort auch an Unter-Blöcken (Cards, Infoboxen) verwendet?
- Falls ja: auch an den Session-Cards und Trust-Items anwenden

## 5. Block 7 "Auf einen Blick" – Fünfter Punkt

Ergänze nach "Preis" einen fünften Detail-Punkt:

```html
<div class="detail-item" style="grid-column: 1 / -1;">
  <p class="detail-label">Voraussetzung</p>
  <p class="detail-value">Hedy Pro Account (Jahresabo oder Lifetime-Lizenz)</p>
  <p class="price-note">Den Link zum vergünstigten Jahresabo erhältst Du mit der Buchungsbestätigung.</p>
</div>
```

## 6. FAQ anpassen

### Bestehende Frage ersetzen

Die Frage "Brauche ich einen Hedy Pro Account?" durch folgende ersetzen:

**Frage:** "Welchen Hedy Account brauche ich?"

**Antwort:** "Für den Workshop ist ein Hedy Pro Account erforderlich (Jahresabo oder Lifetime-Lizenz). Mit der Buchungsbestätigung erhältst Du einen Link zum vergünstigten Jahresabo. Falls Du die Lifetime-Lizenz in Betracht ziehst, stehe ich Dir gern für einen kurzen persönlichen Austausch zur Verfügung."

## 7. Prüfung vor Commit

- [ ] Nav-Button rechts oben entfernt
- [ ] CTA-Buttons dezent, nicht volle Breite
- [ ] Headlines kleiner, mehr Abstand
- [ ] Sektionsnummern vorhanden (01–10)
- [ ] Senkrechte Striche konsistent mit Relaunch-Leitfaden
- [ ] Block 7: Voraussetzung Hedy Pro ergänzt
- [ ] FAQ: Account-Frage angepasst
- [ ] Keine Preise von Hedy Pro auf der Seite

## 8. Commit und Push

```
git add .
git commit -m "fix: Design-Angleichung an Relaunch-Leitfaden, FAQ-Update"
git push
```

# Cursor-Briefing: Hero-Sektion Umbau — Baustellenseite
**Datum:** 04. April 2026
**Linear-Issue:** [BER-44](https://linear.app/berent/issue/BER-44/hero-sektion-umbau-baustellenseite-mit-personenfoto-am-bildschirmrand)
**Projekt:** Webseite + Beratungswerkzeuge
**Komplexität:** Mittel

## Ziel

Die Hero-Sektion der `index.html` komplett umbauen zu einer temporären „Baustellenseite". Die Botschaft: Die Webseite wird gerade umgebaut — aber die Kompetenz steht. Gleichzeitig wird das **neue BERENT CI** (dunkler Hintergrund, Kupfer/Gold, Bebas Neue/Lora) eingeführt — mindestens für die Hero-Sektion.

## Kontext

Die aktuelle Hero-Sektion ist VAaaS-fokussiert mit altem CI (`#80331A`, `#D6B366`, system-ui Font). Die neue Seite positioniert Marcus Kunkel als Person und KI-Strategieberater, nicht ein einzelnes Produkt. Das neue CI ist definiert in `.cursor/rules/berent-ci.md` (falls vorhanden) oder im Abschnitt „CI-Referenz" unten.

## Inhalt der neuen Hero-Sektion

### 1. Headline (mehrzeilig, gestaffelt animiert wie bisher)
```
Ich baue meine Webseite UM...
und dein Unternehmen.
```
- Font: **Bebas Neue**, UPPERCASE, Farbe: Kupfer `#B5742A`
- Responsive Größen beibehalten (Mobile 40px → Tablet 80px → Desktop 100px)
- Animation: fade-in-up, gestaffelt (300ms Versatz pro Zeile, wie bisher)
- „UM..." steht am Ende der ersten Zeile mit Auslassungspunkten
- Zweite Zeile: „UND DEIN UNTERNEHMEN."

### 2. Untertitel
```
TÜV-zertifizierter KI-Strategieberater und Hedy-Trainer
```
- Font: **Lora**, 300 weight, Farbe: Text `#C4BCB1`
- Unter der Headline, ebenfalls fade-in-up

### 3. Personenfoto
- Datei: `images/marcus-freigestellt.png` (freigestelltes PNG mit transparentem Hintergrund). Arbeite aktuell noch mit einem Platzhalter.
- **Desktop (≥1024px):** Person am rechten Bildschirmrand, `position: absolute`, rechts bündig, unten bündig (über der Trust-Zeile), `right: 0`, ca. 50-60% der Viewport-Höhe
- **Tablet (768–1023px):** Etwas kleiner, weiterhin rechts
- **Mobile (<768px):** Unter dem Text, zentriert, maximal 70% Breite, ODER am unteren Rand kleiner
- Das Bild darf den Text **nicht** überlappen — z-index so setzen, dass Text immer lesbar bleibt
- Kein Schatten, kein Border — nur das freigestellte Foto

### 4. Hedy-Badge (NEU — vor der Trust-Zeile)
```
Einer der weltweit 25 ersten Hedy-Trainer
Erste Trainingsgruppe am Koerting Institut · Hedy AI
```
- Position: zwischen Hero-Inhalt und Trust-Zeile (Kundenlogos)
- Styling: kleiner Badge/Chip, Hintergrund `#110E0A` (Card), Border `#2A2118`, Text `#C4BCB1`
- Font: Lora, kleiner als Untertitel (ca. 14px)
- Zweite Zeile noch kleiner / muted (`#7A6A58`)
- Fade-in-up Animation, erscheint nach dem Untertitel

### 5. Trust-Zeile (Kundenlogos)
- **Bleibt unverändert** in Struktur und Funktionalität
- Hintergrund evtl. anpassen: von `bg-white` auf `#110E0A` oder halbtransparent, damit es zum neuen CI passt

## CI-Referenz (falls `.cursor/rules/berent-ci.md` nicht existiert)

```css
:root {
  --bg:      #090806;
  --card:    #110e0a;
  --border:  #2a2118;
  --copper:  #B5742A;
  --gold:    #E8C98A;
  --text:    #C4BCB1;
  --muted:   #7A6A58;
  --muted2:  #9a8870;
}
```

Fonts:
- Headlines: **Bebas Neue** (UPPERCASE, `letter-spacing: 0.04em`)
- Body: **Lora** (300/400/600, kein italic)
- Code/Labels: **JetBrains Mono**

Für lokale Entwicklung Google Fonts CDN okay:
```html
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Lora:wght@300;400;600&display=swap" rel="stylesheet">
```

**Wichtig:** Niemals `#000000` oder `#FFFFFF` verwenden. Gold `#E8C98A` nur für das `+` Symbol.

## Umsetzung

### Schritt 1: Fonts einbinden
- Google Fonts CDN Link für Bebas Neue + Lora im `<head>` hinzufügen (Entwicklung)
- Bestehende `font-condensed` Klasse durch Bebas Neue ersetzen

### Schritt 2: Hero-Sektion ersetzen
Die gesamte Hero-Sektion (von `<!-- Hero Section -->` bis zum Ende des Hero-`div`) ersetzen. Grundstruktur:

```html
<!-- Hero Section -->
<div class="relative pt-16 flex content-center items-center justify-center min-h-[100svh]" style="background-color: #090806;">
    <div class="container relative mx-auto z-10">
        <div class="w-full px-4 text-left max-w-2xl">
            <!-- Headline -->
            <h1 class="hero-animate" style="font-family:'Bebas Neue',sans-serif; color:#B5742A; text-transform:uppercase; letter-spacing:0.04em; line-height:1.1;">
                ICH BAUE MEINE WEBSEITE UM...
            </h1>
            <h1 class="hero-animate" style="font-family:'Bebas Neue',sans-serif; color:#B5742A; text-transform:uppercase; letter-spacing:0.04em; line-height:1.1;">
                UND DEIN UNTERNEHMEN.
            </h1>
            <!-- Untertitel -->
            <p class="hero-animate" style="font-family:'Lora',serif; color:#C4BCB1; font-weight:300;">
                TÜV-zertifizierter KI-Strategieberater und Hedy-Trainer
            </p>
        </div>
    </div>

    <!-- Personenfoto -->
    <img src="images/marcus-freigestellt.png" alt="Marcus Kunkel"
         class="absolute bottom-[80px] right-0 h-[60vh] object-contain pointer-events-none hidden lg:block"
         style="max-height: 70vh;">

    <!-- Hedy Badge -->
    <div class="hero-animate absolute bottom-[90px] left-4 sm:left-8 z-20"
         style="background:#110e0a; border:1px solid #2a2118; border-radius:8px; padding:12px 20px;">
        <p style="font-family:'Lora',serif; color:#C4BCB1; font-size:14px; margin:0;">
            Einer der weltweit 25 ersten Hedy-Trainer
        </p>
        <p style="font-family:'Lora',serif; color:#7A6A58; font-size:12px; margin:4px 0 0 0;">
            Erste Trainingsgruppe am Koerting Institut · Hedy AI
        </p>
    </div>

    <!-- Trust-Zeile (Kundenlogos) — UNVERÄNDERT, nur Farbanpassung -->
    <section class="absolute bottom-0 left-0 right-0 w-full py-4 shadow-md"
             style="background-color: #110e0a;">
        <!-- Bestehender Inhalt der Kundenlogo-Sektion beibehalten -->
    </section>
</div>
```

**Hinweis:** Das ist eine Richtungsvorgabe, kein Copy-Paste-Template. Cursor soll die responsive Breakpoints sauber implementieren und die bestehenden Tailwind-Klassen mit dem neuen CI verbinden. Inline-Styles nur wo nötig — bevorzugt CSS-Variablen über eine `<style>`-Sektion.

### Schritt 3: Responsive Anpassungen
- **Mobile (<768px):** Kein Personenfoto ODER Foto zentriert unter dem Text, kleiner
- **Tablet (768–1023px):** Foto rechts, kleiner skaliert
- **Desktop (≥1024px):** Foto am rechten Rand, volle Höhe
- Hedy-Badge: auf Mobile ggf. über der Trust-Zeile statt absolut positioniert

### Schritt 4: Rest der Seite
- Navigation, Features, Footer **vorerst nicht ändern** — nur die Hero-Sektion
- Die weiße Navigation oben kann vorerst bleiben (wird in einem späteren Issue auf dunkles CI umgestellt)

## Vorbedingung (manuell, vor Cursor-Start)

**Das Foto `images/marcus-freigestellt.png` muss existieren.** Freistellen z.B. mit:
- https://remove.bg (Web-Tool, kostenlos)
- `rembg` CLI: `rembg i input.jpg output.png`
- Photoshop / Canva

Ohne dieses Bild kann Cursor das Layout bauen, aber das visuelle Ergebnis stimmt nicht.

## Dateien
- `index.html` — Hero-Sektion ersetzen, Fonts einbinden
- `input.css` / `output.css` — ggf. neue Tailwind-Klassen, dann `npx tailwindcss -i input.css -o output.css` neu kompilieren
- `images/marcus-freigestellt.png` — neues Bild (manuell bereitstellen)

## Prüfung nach Umsetzung
- [ ] Seite lokal im Browser öffnen, alle drei Breakpoints prüfen
- [ ] Headline korrekt: „ICH BAUE MEINE WEBSEITE UM..." / „UND DEIN UNTERNEHMEN."
- [ ] Untertitel korrekt
- [ ] Personenfoto am rechten Rand (Desktop), kein Textüberlappen
- [ ] Hedy-Badge sichtbar
- [ ] Trust-Zeile (Kundenlogos) funktional
- [ ] Navigation weiterhin funktional (Mobile Hamburger-Menü, Desktop-Links)
- [ ] Keine Console-Errors

## Abschluss
Wenn alle Änderungen umgesetzt sind:
```bash
git add -A
git commit -m "[BER-44] done: Hero-Sektion Umbau zur Baustellenseite mit neuem CI"
git push
```
Dieser Commit triggert den automatischen Rückkanal (Linear → Done, Threema-Benachrichtigung, Notion-Marker).

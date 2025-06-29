# Entwicklungsanleitung

Diese Dokumentation beschreibt den Entwicklungs- und Deployment-Prozess für berent.ai.

## Lokales Setup

1. Repository klonen:
   ```bash
   git clone https://github.com/peerend/berent.git
   cd berent
   ```

2. Dependencies installieren:
   ```bash
   npm install
   ```

3. Entwicklungsserver starten:
   ```bash
   npm run dev
   ```

## Technologie-Stack

- HTML5
- Tailwind CSS für Styling
- JavaScript für Interaktivität
- GitHub Pages für Hosting
- GitHub Actions für CI/CD

## Build-Prozess

Der Build-Prozess wird automatisch durch GitHub Actions ausgeführt:

1. CSS wird mit Tailwind kompiliert
2. Assets werden optimiert
3. Deployment auf GitHub Pages

Für lokales Building:
```bash
npm run build
```

## Deployment

Das Deployment erfolgt automatisch bei Push auf den main Branch:

1. GitHub Action wird getriggert
2. Build-Prozess läuft
3. Deployment auf GitHub Pages
4. DNS-Updates über IONOS

## Code-Standards

- Semantisches HTML
- Mobile-First Design
- Accessibility-Best-Practices
- Progressive Enhancement

## Sicherheit

- Regelmäßige Dependency-Updates
- CodeQL Analyse
- Security Scans
- HTTPS-Only

## Kontakt

Bei Fragen oder Problemen:
- E-Mail: mail@berent.ai 
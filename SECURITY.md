# Sicherheitsrichtlinien

## 🔒 Geschützte Daten

Die folgenden Daten werden NIEMALS im Repository gespeichert:

- API-Schlüssel oder Tokens
- Passwörter oder Zugangsdaten
- Private Schlüssel oder Zertifikate
- Persönliche Daten von Kunden oder Mitarbeitern
- Interne Geschäftsdaten oder -dokumente

## 📝 Richtlinien für Entwickler

### Commits & Pull Requests
- Keine sensiblen Daten in Commit-Messages
- Code-Reviews vor Merge in `main` oder `staging`
- Automatische Sicherheitschecks müssen bestanden werden

### Umgang mit sensiblen Daten
- Umgebungsvariablen in `.env` Dateien speichern
- `.env` Dateien NIEMALS committen
- GitHub Secrets für CI/CD Pipeline nutzen
- Regelmäßige Sicherheitsaudits durchführen

## 🛡️ Sicherheitsmaßnahmen

### Automatisierte Checks
- Gitleaks für Secrets-Scanning
- npm audit für Dependency-Checks
- Wöchentliche Sicherheits-Scans

### Zugriffskontrolle
- Branch Protection Rules für `main` und `staging`
- Zwei-Faktor-Authentifizierung für alle Entwickler
- Regelmäßige Überprüfung der Zugriffsrechte

## 🚨 Sicherheitslücken melden

Bei Entdeckung von Sicherheitslücken:
1. NICHT öffentlich kommunizieren
2. Sofort per E-Mail melden: office [at] berent [.] ai
3. Detaillierte Beschreibung bereitstellen
4. Auf Bestätigung warten

## 📋 Checkliste vor Deployment

- [ ] Keine sensiblen Daten im Code
- [ ] Alle Secrets in GitHub Secrets
- [ ] Security Scans bestanden
- [ ] Code-Review durchgeführt
- [ ] Tests erfolgreich
- [ ] Dokumentation aktuell 
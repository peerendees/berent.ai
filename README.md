# berent.ai Website

## Deployment-Prozess

### 1. Entwicklung und Test
- Alle Änderungen werden zunächst auf dem `main` Branch entwickelt
- Push auf `main` deployed automatisch zu GitHub Pages (preview.berent.ai)
- Dort können Änderungen getestet werden

### 2. Production Release
Wenn die Änderungen getestet und freigegeben sind:

1. Gehe zu "Actions" im GitHub Repository
2. Wähle "Deploy to Production"
3. Klicke "Run workflow"
4. Wähle den Release-Typ:
   - `patch`: für Bugfixes (z.B. 1.0.0 -> 1.0.1)
   - `minor`: für neue Features (z.B. 1.0.0 -> 1.1.0)
   - `major`: für Breaking Changes (z.B. 1.0.0 -> 2.0.0)

Der Workflow wird automatisch:
- Eine neue Version generieren
- Ein GitHub Release erstellen
- Die Seite zu IONOS deployen

### Commit-Konventionen
Die Versionsnummer wird automatisch basierend auf deinen Commit-Messages erhöht:
- `feat: neue Funktion` -> Minor Version
- `fix: Bugfix` -> Patch Version
- `BREAKING CHANGE: große Änderung` -> Major Version

### GitHub Secrets Setup
Folgende Secrets müssen in den GitHub Repository Settings konfiguriert sein:
- FTP_SERVER: IONOS FTP Server
- FTP_USERNAME: IONOS FTP Benutzername
- FTP_PASSWORD: IONOS FTP Passwort
- FTP_SERVER_DIR: Zielverzeichnis auf dem Server 
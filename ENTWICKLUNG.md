# 🚀 Entwicklungs-Workflow für berent.ai

## 📋 Branch-Struktur

```
main               → 🌍 Produktion (berent.ai)
staging            → 🧪 Test-Umgebung (staging.berent.ai)
feature/datenschutz → 👀 Preview (preview-datenschutz.berent.ai)
```

## 🔄 Workflow für neue Features

### 1. Feature entwickeln
```bash
# Neuen Feature-Branch erstellen
git checkout main
git pull origin main
git checkout -b feature/mein-neues-feature

# Entwickeln...
# Dateien bearbeiten

# Committen
git add .
git commit -m "feat: Mein neues Feature"
git push -u origin feature/mein-neues-feature
```

### 2. Preview anschauen
- **Automatisch:** Pull Request erstellen
- **Preview URL:** `https://preview-mein-neues-feature.berent.ai`
- **GitHub kommentiert automatisch** die Preview-URL

### 3. Testen auf Staging
```bash
# Feature in Staging mergen
git checkout staging
git merge feature/mein-neues-feature
git push origin staging
```
- **Test-URL:** `https://staging.berent.ai`

### 4. Produktion deployen
```bash
# In Produktion mergen
git checkout main
git merge staging
git push origin main
```
- **Live-URL:** `https://berent.ai`

## 🛡️ Sicherheitsnetz

### Rollback bei Problemen
```bash
# Letzten funktionierenden Commit finden
git log --oneline

# Rollback zu bestimmtem Commit
git checkout main
git revert <commit-hash>
git push origin main
```

### Hotfixes
```bash
# Dringender Fix direkt auf main
git checkout main
git checkout -b hotfix/kritischer-bug
# Fix entwickeln...
git push -u origin hotfix/kritischer-bug
# Sofort mergen und deployen
```

## 🎯 Automatische Deployments

- **✅ Push auf `main`** → Automatisches Deployment auf `berent.ai`
- **✅ Push auf `staging`** → Automatisches Deployment auf `staging.berent.ai`  
- **✅ Pull Request** → Preview-URL wird automatisch erstellt
- **✅ Tailwind CSS** wird automatisch kompiliert
- **✅ Service Worker** wird automatisch aktualisiert

## 📁 Setup für neue Features

```bash
# Standard-Workflow starten
git checkout main
git pull origin main
git checkout -b feature/beschreibung

# Entwickeln, testen, deployen...
```

## 🔧 Domain-Setup erforderlich

Für vollständigen Workflow müssen folgende Subdomains eingerichtet werden:
- `staging.berent.ai` → GitHub Pages
- `preview-*.berent.ai` → GitHub Pages (Wildcard)

Das machen wir als nächstes! 🚀 
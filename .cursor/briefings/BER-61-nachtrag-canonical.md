## Nachtrag: Canonical URLs prüfen (ergänzend zu BER-61)

Cursor muss in ALLEN HTML-Seiten im berentai-Repo prüfen:
- `<link rel="canonical" href="...">` → muss `https://www.berent.ai/...` sein
- `<meta property="og:url" content="...">` → muss `https://www.berent.ai/...` sein
- Falls `mainEntityOfPage` in LD+JSON → ebenfalls `www.berent.ai`

Grund: Vercel redirected berent.ai → www.berent.ai (301). Die kanonische Variante ist also www.

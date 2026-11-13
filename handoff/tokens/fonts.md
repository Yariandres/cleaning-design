# Fonts

| Family | Role | Weights | Licence | Source |
|---|---|---|---|---|
| Bricolage Grotesque (variable) | display: h1-h3, big prices, logo wordmark | 500-800 | SIL OFL 1.1 | Fontsource `@fontsource-variable/bricolage-grotesque` 5.3.0 |
| Figtree (variable) | body, UI, labels, numbers | 400-700 | SIL OFL 1.1 | Fontsource `@fontsource-variable/figtree` 5.3.0 |

- Self-hosted through `@nuxt/fonts` (no Google requests at runtime). Load the **latin** and **latin-ext** subsets only; Polish needs latin-ext (ą ć ę ł ń ó ś ź ż).
- Prototype reference: `prototypes/stroller/fonts/` holds the four WOFF2 files with the `unicode-range` declarations in `prototypes/stroller/base.css`.
- Use `font-display: swap`. Bricolage's optical-size axis is not loaded.

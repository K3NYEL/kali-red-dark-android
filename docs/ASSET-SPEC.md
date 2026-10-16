# Asset specification

This document defines the files required before Kali Red Dark for Android can be described as a complete visual kit. A listed specification is not proof that an asset has been tested on the target device.

## 1. Wallpaper

**Design direction:** minimal, near-black background with an original vivid-red geometric creature emblem. The artwork must not copy an official logo or imply endorsement by Kali Linux or Offensive Security.

- Vector master: `assets/wallpapers/kali-red-dark-wallpaper-portrait.svg`.
- Phone export: PNG rendered at 1080 × 2400 by the [Build wallpaper PNG workflow](../.github/workflows/build-wallpaper.yml).
- Colors: background `#0B0B0D`; bright-red accent `#FF0000`; optional original-theme red `#EC0101`.
- Composition: centered emblem with relatively quiet top and bottom areas for Android UI.
- Quality checks still needed: inspect on the actual phone, check icon-label contrast at normal brightness, and test both home and lock screens.
- PNG workflow artifacts are temporary downloads retained for 30 days; the SVG source is permanent in the repository.

## 2. Icon pack

A folder of PNGs alone is not an installable Android icon pack. Before selecting a delivery format, verify the installed launcher supports it.

For a first asset collection:

- Create original artwork; do not redistribute third-party app logos without checking their licenses and trademark rules.
- Keep a consistent visual grid, stroke weight, corner treatment, and optical size.
- Provide transparent PNG or SVG source files where appropriate, and document any conversion used for delivery.
- Define a clear list of supported apps and use a neutral fallback for apps without a matching icon.
- Test icon labels, masks, dark wallpaper contrast, and any monochrome/themed-icon behavior on the target device.
- Document whether the result is a manual per-icon customization set or a genuine installable icon pack.

No installable icon pack is currently included in this repository.

## 3. Preview images

- Use actual committed project assets and clearly label mockups as mockups.
- Do not present an illustrative device mockup as a screenshot from the Cubot device.
- Include a home-screen preview and, if available, a separate icon-detail preview.
- Keep previews readable on mobile and compress them reasonably for GitHub.

## 4. Required metadata

For each asset, document:

- Path and filename
- Format and pixel dimensions
- Creator/source
- License or usage terms
- Whether it has been tested on the target device
- Known limitations

## 5. Current status

| Asset | Status |
|---|---|
| Original vector wallpaper | Included; not yet device-tested |
| Phone-ready PNG | Generated as a temporary GitHub Actions artifact |
| Custom icon pack | Not included |
| Preview mockups | Not included |
| Color token JSON | Available at `theme/colors.json` |

See the [roadmap](ROADMAP.md) for planned milestones.

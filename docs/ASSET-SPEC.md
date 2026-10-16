# Asset specification

This document defines the files required before Kali Red Dark for Android can be described as a complete visual kit. A listed specification is not proof that the asset already exists.

## 1. Wallpaper

**Design direction:** minimal, near-black background with an original vivid-red dragon-inspired emblem. The artwork must not copy an official logo or imply endorsement by Kali Linux or Offensive Security.

- Primary export: portrait PNG or high-quality WebP.
- Composition: phone wallpaper with the emblem centered; keep the top and bottom relatively quiet so the status bar, app labels, and dock remain legible.
- Colors: background `#0B0B0D`; bright-red accent `#FF0000`; optional original-theme red `#EC0101`.
- Resolution: provide a high-resolution master and a phone-ready export; record the actual pixel dimensions in the asset README.
- Quality checks: inspect at normal phone brightness, confirm icon labels remain readable, check for banding/compression artifacts, and test both home and lock screens.
- File naming: `kali-red-dark-wallpaper-portrait.png` (or a matching `.webp` extension).

Do not claim that an asset is included until the image file is committed to `assets/wallpapers/`.

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
- Do not present a generated or illustrative device mockup as a screenshot from the Cubot device.
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
| Wallpaper | Not yet included |
| Custom icon pack | Not yet included |
| Preview mockups | Not yet included |
| Color token JSON | Available at `theme/colors.json` |

See the [roadmap](ROADMAP.md) for planned milestones.

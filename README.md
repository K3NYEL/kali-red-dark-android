# Kali Red Dark for Android

A no-root Android personalization kit inspired by the **Kali Red Dark** palette from the [original VS Code theme](https://github.com/K3NYEL/kali-red-dark). This repository adapts the palette for Android launchers and customization apps; it is a separate project and does not modify the original VS Code theme.

> **Target device:** Cubot KINGKONG ACE 2 running Android 14  
> **Current status:** Documentation, manual setup guide, automated validation, and original vector wallpaper source. The icon pack, previews, and installable theme package are not available yet.

## Color palette

| Role | Color | Hex |
|---|---|---|
| Original theme primary | Red | `#EC0101` |
| Brighter mobile accent option | Pure red | `#FF0000` |
| Main background | Near-black | `#0B0B0D` |
| Secondary background | Deep black | `#09090B` |
| Surface | Charcoal | `#1A1A1F` |
| Main text | Soft white | `#E8E8E8` |
| Muted text | Gray | `#777777` |
| Strings / positive accent | Green | `#7EE787` |
| Variables / links | Blue | `#79C0FF` |
| Functions | Orange | `#FF9F43` |
| Classes / types | Yellow | `#FFD166` |
| Built-in support | Cyan | `#67E8F9` |
| Constants | Purple | `#C084FC` |

The original red remains `#EC0101`. Use `#FF0000` only if a brighter red is preferred and the launcher accepts custom hexadecimal colors. The launcher accent may not recolor icons, widgets, or Android system surfaces.

## Documentation

- [Installation guide](docs/INSTALL.md)
- [Lawnchair setup guide](docs/LAWNCHAIR-SETUP.md)
- [Asset specifications and status](docs/ASSET-SPEC.md)
- [Roadmap](docs/ROADMAP.md)
- [Color token reference](theme/README.md)
- [Contribution guide](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)

## Wallpaper

The original vector wallpaper source is available at [`assets/wallpapers/kali-red-dark-wallpaper-portrait.svg`](assets/wallpapers/kali-red-dark-wallpaper-portrait.svg). GitHub Actions can render a 1080 × 2400 PNG and publish it as a temporary downloadable artifact. Follow [the wallpaper instructions](assets/wallpapers/README.md) to retrieve it.

## Automated validation

GitHub Actions runs the project validator on pushes to `main`, pull requests, and manual workflow dispatch. The validator checks that `theme/colors.json` is valid JSON, required metadata is present, every color uses six-digit hexadecimal RGB, and the project remains marked as an Android no-root personalization kit.

Run the same check locally with Python 3:

```bash
python scripts/validate_theme.py
```

## What is included today

- Machine-readable color tokens in `theme/colors.json`
- Original vector wallpaper source plus a workflow to render a phone-ready PNG
- Automated validation script and GitHub Actions workflows
- Android 14 installation notes and manual Lawnchair configuration instructions

## What is not included yet

- A custom icon pack
- Preview/mockup images
- An installable APK, launcher theme package, or system-wide theme

Do not treat this repository as a ROM, firmware image, or Kali NetHunter installer. It only documents safe, reversible personalization settings. Android's Quick Settings, notifications, Settings app, and status bar may keep the colors supplied by the device manufacturer.

## Device compatibility

The documentation targets Lawnchair on a Cubot KINGKONG ACE 2 running Android 14, but exact menus and supported options depend on the installed Lawnchair version and device firmware. The wallpaper has not yet been tested on the target device.

## License

This repository is distributed under the MIT License. See [LICENSE](LICENSE).

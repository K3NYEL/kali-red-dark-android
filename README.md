# Kali Red Dark for Android

A no-root Android personalization kit inspired by the **Kali Red Dark** palette from the [original VS Code theme](https://github.com/K3NYEL/kali-red-dark). This repository adapts the palette for Android launchers and customization apps; it is a separate project and does not modify the original VS Code theme.

> **Target device:** Cubot KINGKONG ACE 2 running Android 14  
> **Current status:** Documentation and manual setup guide. A complete wallpaper, icon pack, preview images, and installable theme package are not available yet.

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

## What is included today

- Machine-readable color tokens in `theme/colors.json`
- Android 14 installation notes
- Manual Lawnchair configuration instructions
- Documented requirements for future wallpaper, icons, and preview assets

## What is not included yet

- A finished Kali Red Dark wallpaper
- A complete icon pack
- Preview/mockup images
- An installable APK, launcher theme package, or system-wide theme

Do not treat this repository as a ROM, firmware image, or Kali NetHunter installer. It only documents safe, reversible personalization settings. Android's Quick Settings, notifications, Settings app, and status bar may keep the colors supplied by the device manufacturer.

## Device compatibility

The documentation targets Lawnchair on a Cubot KINGKONG ACE 2 running Android 14, but exact menus and supported options depend on the installed Lawnchair version and device firmware. Steps that have not been verified on the exact device are identified as recommendations rather than guaranteed behavior.

## License

This repository is distributed under the MIT License. See [LICENSE](LICENSE).

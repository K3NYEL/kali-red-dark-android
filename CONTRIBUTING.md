# Contributing

Thanks for helping improve Kali Red Dark for Android.

## Project scope

This repository is a no-root Android personalization kit focused on colors, wallpaper, launcher setup, icon options, and documentation. It is not a ROM, firmware package, or system-wide theme installer.

## Before opening a change

1. Check the [roadmap](docs/ROADMAP.md) to avoid duplicating work.
2. Keep the original theme palette intact unless a deliberate palette change is proposed.
3. Clearly distinguish verified device behavior from general recommendations.
4. Do not claim an asset, APK, or launcher integration exists until it is committed and tested.

## Asset contributions

- Prefer original artwork or assets with clear redistribution rights.
- Include source and license information for third-party resources.
- Follow [asset specifications](docs/ASSET-SPEC.md).
- Do not copy official logos or imply endorsement by Kali Linux or Offensive Security.
- Keep source files where practical and include a usable export.
- Never label a mockup as a real device screenshot.

## Documentation changes

- Use concise Markdown headings and working relative links.
- State the launcher and Android version when a step depends on them.
- Mention when menu names may vary by version or manufacturer.
- Avoid promising that Lawnchair can recolor Android system panels or every app icon.

## Suggested workflow

1. Create a feature branch.
2. Make one focused change.
3. Check Markdown links and JSON syntax.
4. Verify that status claims match the actual repository files.
5. Open a pull request with a summary, testing notes, and screenshots for visual changes when available.

## Testing checklist

- [ ] JSON files parse successfully.
- [ ] Markdown links point to existing files.
- [ ] New assets include source/license metadata.
- [ ] Device compatibility claims are appropriately qualified.
- [ ] No generated binaries or unrelated files are included accidentally.

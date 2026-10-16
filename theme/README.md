# Color tokens

The machine-readable palette is stored in [`colors.json`](colors.json). It records the original Kali Red Dark-inspired palette and an optional brighter red for mobile use.

## Red values

| Token | Hex | Intended use |
|---|---|---|
| `primary` | `#EC0101` | Original theme primary red |
| `mobileAccentBright` | `#FF0000` | Optional stronger red when a launcher accepts custom hex colors |

Keep these values separate so the original palette remains traceable. A launcher accepting a color value does not mean it applies that color to every UI element.

## Usage notes

- `background` and `backgroundSecondary` are dark surfaces.
- `surface` is a raised charcoal surface.
- `text` and `textMuted` are foreground text colors.
- Remaining tokens preserve syntax-inspired accent colors from the source theme.

This JSON file is a reference for designers and future tooling. Android and Lawnchair do not automatically read it as a theme package. Values must be applied through supported settings or integrated into a future, compatible deliverable.

## Validation

The file should remain valid JSON, use six-digit hexadecimal RGB strings, and retain the target metadata unless the supported device scope changes.

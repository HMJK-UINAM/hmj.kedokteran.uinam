# Background Configuration Guide for Danus Department

The hero background can now be fully customized through the `danus.json` file! Here are the available options:

## Background Configuration Options

In `data/danus.json`, under `hero.background`, you can configure:

### 1. Image Background
```json
"background": {
  "type": "image",
  "useImage": true,
  "imagePath": "img/backgrounds/your-image.jpg",
  "imageOverlay": 0.3,
  "backgroundSize": "cover",
  "backgroundPosition": "center",
  "backgroundAttachment": "fixed"
}
```

### 2. Gradient Background
```json
"background": {
  "type": "gradient",
  "useImage": false,
  "gradient": ["#638949", "#EFFFE1"]
}
```

### 3. Solid Color Background
```json
"background": {
  "type": "color",
  "useImage": false,
  "backgroundColor": "#638949"
}
```

## Available Properties

- **type**: "image", "gradient", or "color"
- **useImage**: true/false to use image background
- **imagePath**: Path to your image file
- **imageOverlay**: 0-1 (opacity for dark overlay on image)
- **gradient**: Array of two colors for gradient
- **backgroundColor**: Solid color for background
- **backgroundSize**: "cover", "contain", "auto", or specific size
- **backgroundPosition**: "center", "top", "bottom", "left", "right"
- **backgroundAttachment**: "fixed" or "scroll"
- **enablePattern**: true/false to enable animated pattern overlay

## Examples

### Dark Overlay on Image
```json
"background": {
  "useImage": true,
  "imagePath": "img/backgrounds/danus-hero.jpg",
  "imageOverlay": 0.5,
  "backgroundColor": "#000000"
}
```

### No Overlay (Clean Image)
```json
"background": {
  "useImage": true,
  "imagePath": "img/backgrounds/danus-hero.jpg",
  "imageOverlay": 0
}
```

### Gradient Only
```json
"background": {
  "useImage": false,
  "gradient": ["#2A6403", "#EFFFE1"]
}
```

### Solid Color
```json
"background": {
  "useImage": false,
  "backgroundColor": "#2A6403"
}
```

## Animated Pattern

You can also control the animated pattern overlay:
```json
"animatedPattern": {
  "show": true,
  "animationSpeed": "20s",
  "opacity": 0.5
}
```

Set `"show": false` to disable the pattern completely.

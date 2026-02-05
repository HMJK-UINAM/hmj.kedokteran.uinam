# 🚀 Quick Reference: Mengubah Hero & Tagline Background

## Fitur Terbaru
Sekarang Anda bisa mengatur **hero background**, **tagline background**, dan **animated pattern** tanpa coding!

## 3 Cara Setting Background

### 1. Gradasi Warna (Default)
```json
"background": {
  "useImage": false,
  "gradient": ["#638949", "#EFFFE1"]
}
```

### 2. Gambar Saja
```json
"background": {
  "useImage": true,
  "imagePath": "img/backgrounds/danus-hero.jpg",
  "imageOverlay": 0.5
}
```
- `imageOverlay` = seberapa gelap (0.2-0.8)

### 3. Sinkronkan Tagline dengan Hero
```json
"taglineSection": {
  "useHeroBackground": true
}
```
✅ Tagline otomatis pakai background yang sama dengan hero!

## Atur Animasi Pattern
```json
"animatedPattern": {
  "show": true,           ← true/false untuk tampilkan
  "animationSpeed": "20s", ← Kecepatan (misal: "15s", "25s")
  "opacity": 0.5          ← Transparansi (0-1)
}
```

## File untuk Diupload
1. Simpan gambar di folder: `img/backgrounds/`
2. Ubah path di JSON: `"imagePath": "img/backgrounds/nama-file.jpg"`
3. Save → Done!

## Contoh Praktis

**Hero dengan gambar gelap:**
```json
{
  "hero": {
    "background": {
      "useImage": true,
      "imagePath": "img/backgrounds/office.jpg",
      "imageOverlay": 0.6
    },
    "animatedPattern": {
      "show": true,
      "animationSpeed": "25s",
      "opacity": 0.3
    }
  },
  "taglineSection": {
    "useHeroBackground": true,
    "animatedPattern": {
      "show": false
    }
  }
}
```

Hasilnya:
- 🎨 Hero: Gambar office + pattern animasi
- 🎨 Tagline: Sama background + tanpa pattern

Selesai! 🎉

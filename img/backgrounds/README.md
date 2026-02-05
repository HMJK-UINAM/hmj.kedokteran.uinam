# Background Images untuk Hero Sections

Folder ini berisi gambar-gambar background untuk section hero di halaman departemen.

## Cara Menggunakan

### 1. Tambahkan Gambar
Letakkan file gambar di folder ini dengan format:
- `danus-hero.jpg` → Dana dan Usaha
- `hublu-hero.jpg` → Hubungan Luar
- `jarkom-hero.jpg` → Jaringan & Komunikasi
- dll.

### 2. Edit JSON Departemen
Buka file `data/[nama-departemen].json` dan ubah field hero:

**Untuk menggunakan gambar background:**
```json
"hero": {
  "title": "Nama Departemen",
  "subtitle": "HMJ Kedokteran UIN Alauddin Makassar",
  "tagline": "Tagline departemen",
  "background": {
    "useImage": true,
    "imagePath": "img/backgrounds/nama-file.jpg",
    "imageOverlay": 0.5,
    "gradient": ["#638949", "#EFFFE1"]
  }
}
```

**Untuk menggunakan gradasi (default):**
```json
"hero": {
  "background": {
    "useImage": false,
    "imagePath": "img/backgrounds/nama-file.jpg",
    "imageOverlay": 0.5,
    "gradient": ["#638949", "#EFFFE1"]
  }
}
```

## Parameter

| Field | Tipe | Deskripsi |
|-------|------|-----------|
| `useImage` | boolean | Gunakan gambar? `true` atau `false` |
| `imagePath` | string | Path ke file gambar |
| `imageOverlay` | number | Opacity overlay (0-1). 0.5 = 50% gelap |
| `gradient` | array | Warna gradasi `["color1", "color2"]` |

## Contoh Overlay Values
- `0.2` → Terang, gambar terlihat jelas
- `0.4` → Sedang
- `0.6` → Gelap, teks lebih terbaca
- `0.8` → Sangat gelap

## Tips
- Gunakan gambar landscape (16:9 aspect ratio) untuk hasil terbaik
- File JPG/PNG ukuran 1-3MB untuk loading optimal
- Jika `useImage: false`, gambar tidak diload meski ada di JSON

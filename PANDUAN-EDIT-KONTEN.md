# 📋 Panduan Pengubahan Konten Departemen Tanpa Coding

Halaman departemen sekarang **sepenuhnya data-driven**. Ubah konten, warna, dan background hero cukup dengan mengedit file JSON!

## 🎯 File-File Penting

```
📁 data/
  └── danus.json          ← Edit file ini untuk mengubah Dana & Usaha
  
📁 img/backgrounds/
  ├── README.md           ← Panduan background images
  └── [gambar-gambar hero]
```

## 🔧 Cara Mengubah Konten

### 1️⃣ Judul & Subtitle Hero
Edit `data/danus.json`:
```json
"hero": {
  "title": "Dana dan Usaha",           ← Ubah judul di sini
  "subtitle": "HMJ Kedokteran UIN...", ← Ubah subtitle di sini
  "tagline": "Vaskularisasi Dana..."   ← Ubah tagline di sini
}
```

### 2️⃣ Profil Departemen
```json
"profil": "Departemen Dana dan Usaha berperan dalam... [ubah teks di sini]"
```

### 3️⃣ Ketua Departemen
```json
"ketua": {
  "nama": "Nama Ketua",
  "foto": "img/danus/ketua.jpg",
  "deskripsi": "Deskripsi peran ketua"
}
```

### 4️⃣ Anggota Departemen
```json
"anggota": [
  { "nama": "Nama Anggota 1", "foto": "img/danus/anggota1.jpg" },
  { "nama": "Nama Anggota 2", "foto": "img/danus/anggota2.jpg" }
]
```

### 5️⃣ Program Kerja
```json
"programKerja": [
  {
    "nama": "Nama Program",
    "deskripsi": "Deskripsi program kerja"
  }
]
```

## 🎨 Mengubah Background Hero

### Opsi 1: Gradasi (Default)
```json
"hero": {
  "background": {
    "useImage": false,
    "gradient": ["#638949", "#EFFFE1"]
  }
}
```

### Opsi 2: Gambar + Overlay
1. **Upload gambar** ke `img/backgrounds/`
2. **Edit JSON**:
```json
"hero": {
  "background": {
    "useImage": true,
    "imagePath": "img/backgrounds/danus-hero.jpg",
    "imageOverlay": 0.5,
    "gradient": ["#638949", "#EFFFE1"]
  }
}
```

**Nilai `imageOverlay`:**
- `0.2` = Terang (gambar dominan)
- `0.5` = Sedang
- `0.8` = Gelap (teks dominan)

### Animasi Background Pattern
Atur kecepatan dan tampilan animated pattern di hero:
```json
"hero": {
  "animatedPattern": {
    "show": true,
    "animationSpeed": "20s",
    "opacity": 0.5
  }
}
```

## 🎨 Mengubah Tagline Section

Tagline section bisa mengikuti background hero atau punya background sendiri:

### Default: Mengikuti Hero
```json
"taglineSection": {
  "text": "Vaskularisasi Dana, Vitalitas Himpunan",
  "useHeroBackground": true,
  "animatedPattern": {
    "show": true,
    "animationSpeed": "30s",
    "opacity": 0.1
  }
}
```

### Variasi: Custom Background
```json
"taglineSection": {
  "text": "Tagline custom",
  "useHeroBackground": false,
  "background": {
    "useImage": true,
    "imagePath": "img/backgrounds/tagline-bg.jpg",
    "imageOverlay": 0.4,
    "gradient": ["#2A6403", "#DEF0CF"]
  },
  "animatedPattern": {
    "show": false
  }
}
```

### Animasi Pattern Tagline
- `show`: `true/false` - Tampilkan pattern bergerak?
- `animationSpeed`: Kecepatan animasi (misal: `"20s"`, `"30s"`)
- `opacity`: Transparansi pattern (0-1)


## 🎨 Mengubah Warna

Edit field `colors` di JSON:
```json
"colors": {
  "primary": "#2A6403",           ← Warna hijau utama
  "accent": "#224B06",            ← Warna hijau gelap
  "text": "#12210A",              ← Warna teks hitam hijau
  "muted": "#465247",             ← Warna teks secondary
  "background": "#F8F7E0",        ← Background cream
  "heroGradientStart": "#638949", ← Gradasi awal hero
  "heroGradientEnd": "#EFFFE1",   ← Gradasi akhir hero
  "footerTitle": "#DEF0CF"        ← Warna judul footer
}
```

## 📝 Template JSON Lengkap

```json
{
  "hero": {
    "title": "Dana dan Usaha",
    "subtitle": "HMJ Kedokteran UIN Alauddin Makassar",
    "tagline": "Vaskularisasi Dana, Vitalitas Himpunan",
    "background": {
      "useImage": false,
      "imagePath": "img/backgrounds/danus-hero.jpg",
      "imageOverlay": 0.5,
      "gradient": ["#638949", "#EFFFE1"]
    },
    "animatedPattern": {
      "show": true,
      "animationSpeed": "20s",
      "opacity": 0.5
    }
  },

  "taglineSection": {
    "text": "Vaskularisasi Dana, Vitalitas Himpunan",
    "useHeroBackground": true,
    "animatedPattern": {
      "show": true,
      "animationSpeed": "30s",
      "opacity": 0.1
    }
  },

  "profil": "Teks profil departemen...",

  "ketua": {
    "nama": "Nama Ketua",
    "foto": "img/danus/ketua.jpg",
    "deskripsi": "Deskripsi ketua..."
  },

  "anggota": [
    { "nama": "Nama 1", "foto": "img/danus/anggota1.jpg" },
    { "nama": "Nama 2", "foto": "img/danus/anggota2.jpg" }
  ],

  "programKerja": [
    { "nama": "Program 1", "deskripsi": "Deskripsi..." }
  ],

  "jobdesk": [
    { "nama": "Jobdesk 1", "deskripsi": "Deskripsi..." }
  ],

  "colors": {
    "primary": "#2A6403",
    "accent": "#224B06",
    "text": "#12210A",
    "muted": "#465247",
    "background": "#F8F7E0",
    "heroGradientStart": "#638949",
    "heroGradientEnd": "#EFFFE1",
    "footerTitle": "#DEF0CF"
  }
}
```

## ✅ Langkah-Langkah Cepat

1. **Buka** `data/danus.json` di text editor
2. **Edit** field yang diinginkan
3. **Simpan** file
4. **Refresh** browser untuk melihat perubahan

Selesai! 🎉

## ⚠️ Tips Penting

- **Jangan hapus kurung atau koma** - JSON syntax harus benar
- **Gunakan path relatif** untuk gambar (dari root)
- **Escape backslash** jika di Windows path: `\\` → `/`
- **Test di browser** setelah perubahan

## 🆘 Troubleshooting

**Perubahan tidak muncul?**
- Hard refresh browser: `Ctrl+Shift+Delete`
- Cek syntax JSON di [jsonlint.com](https://jsonlint.com)

**Gambar tidak tampil?**
- Cek path di `imagePath` sudah benar
- Pastikan file gambar ada di folder `img/backgrounds/`

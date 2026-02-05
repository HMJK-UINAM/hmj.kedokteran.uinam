# Panduan Edit Konten Departemen Danus

## 📝 Cara Mengedit Konten di `data/danus.json`

### 🖼️ **1. Mengubah Background Hero**

```json
"hero": {
  "background": {
    "imagePath": "img/backgrounds/nama-file-gambar.jpg",
    "imageOverlay": 0.3,
    "backgroundColor": "#000000"
  }
}
```

**Opsi Background:**
- `imagePath`: Path ke file gambar (relative dari root folder)
- `imageOverlay`: 0-1 (0 = transparan, 1 = gelap total)
- `backgroundColor`: Warna overlay (gunakan hex code)

---

### 👥 **2. Mengedit Data Anggota**

```json
"anggota": [
  { 
    "nama": "Nama Anggota 1", 
    "foto": "img/danus/anggota1.jpg" 
  },
  { 
    "nama": "Nama Anggota 2", 
    "foto": "img/danus/anggota2.jpg" 
  },
  { 
    "nama": "Nama Anggota 3", 
    "foto": "img/danus/anggota3.jpg" 
  }
]
```

**Cara Menambah/Hapus Anggota:**
- **Tambah**: Tambahkan objek baru di dalam array `anggota`
- **Hapus**: Hapus baris objek anggota yang tidak diperlukan
- **Edit**: Ubah `nama` dan/atau `foto` sesuai kebutuhan

---

### 💼 **3. Mengedit Program Kerja**

```json
"programKerja": [
  {
    "nama": "Nama Program 1",
    "deskripsi": "Deskripsi lengkap program kerja ini..."
  },
  {
    "nama": "Nama Program 2", 
    "deskripsi": "Deskripsi lengkap program kerja ini..."
  }
]
```

**Cara Mengatur Program Kerja:**
- **Tambah**: Tambahkan objek baru di dalam array `programKerja`
- **Hapus**: Hapus baris objek program yang tidak diperlukan
- **Edit**: Ubah `nama` dan `deskripsi` sesuai kebutuhan

---

### 📋 **4. Mengedit Jobdesk**

```json
"jobdesk": [
  {
    "nama": "Nama Jobdesk 1",
    "deskripsi": "Deskripsi tugas dan tanggung jawab..."
  },
  {
    "nama": "Nama Jobdesk 2",
    "deskripsi": "Deskripsi tugas dan tanggung jawab..."
  }
]
```

**Cara Mengatur Jobdesk:**
- **Tambah**: Tambahkan objek baru di dalam array `jobdesk`
- **Hapus**: Hapus baris objek jobdesk yang tidak diperlukan
- **Edit**: Ubah `nama` dan `deskripsi` sesuai kebutuhan

---

### 👤 **5. Mengedit Data Ketua**

```json
"ketua": {
  "nama": "Nama Ketua Departemen",
  "foto": "img/danus/ketua.jpg",
  "deskripsi": "Deskripsi singkat tentang ketua departemen..."
}
```

---

### 📝 **6. Mengedit Profil Departemen**

```json
"profil": "Deskripsi lengkap tentang departemen Dana dan Usaha..."
```

---

### 🎨 **7. Mengedit Warna Tema**

```json
"colors": {
  "primary": "#2A6403",
  "accent": "#224B06",
  "text": "#224b06",
  "muted": "#465247",
  "background": "#F8F7E0"
}
```

---

## 📁 **Struktur File yang Direkomendasikan**

```
img/
├── backgrounds/
│   └── danus-hero.jpg
└── danus/
    ├── ketua.jpg
    ├── anggota1.jpg
    ├── anggota2.jpg
    └── anggota3.jpg
```

---

## ⚠️ **Penting!**

1. **Backup**: Selalu backup file `danus.json` sebelum mengedit
2. **Format JSON**: Pastikan format JSON tetap valid (gunakan comma, bracket, dll)
3. **Path Gambar**: Pastikan path gambar benar dan file ada
4. **Test**: Buka halaman untuk melihat perubahan setelah edit

---

## 🔧 **Tips Edit Cepat**

### Menambah Anggota Baru:
```json
// Salin baris ini dan edit:
{ "nama": "Nama Baru", "foto": "img/danus/nama-baru.jpg" }
```

### Menambah Program Kerja Baru:
```json
// Salin baris ini dan edit:
{
  "nama": "Nama Program Baru",
  "deskripsi": "Deskripsi program baru..."
}
```

### Validasi JSON:
Gunakan online JSON validator seperti: https://jsonlint.com/

---

## 📞 **Bantuan**

Jika mengalami masalah:
1. Periksa format JSON (comma, bracket, curly brace)
2. Pastikan path gambar benar
3. Refresh browser (Ctrl+F5)
4. Check browser console untuk error

**Happy Editing! 🎉**

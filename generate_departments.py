import re

departments = {
    "hublu.html": {
        "title": "Departemen Hubungan Luar",
        "name": "Hubungan Luar",
        "description": "Membangun jaringan dengan organisasi eksternal",
        "profil": [
            "Departemen Hubungan Luar (HubLu) adalah departemen yang bertanggung jawab dalam membangun dan memelihara hubungan baik dengan organisasi eksternal, institusi pendidikan, organisasi mitra, dan stakeholder lainnya.",
            "Melalui komunikasi yang strategis dan program-program kerjasama yang berkelanjutan, HubLu memperkuat posisi HMJ Kedokteran UINAM di tingkat universitas, regional, maupun nasional, serta membuka peluang kolaborasi yang saling menguntungkan."
        ],
        "ketua_name": "Azizah Nur Pratiwi",
        "ketua_desc": "Memimpin Departemen Hubungan Luar dengan visi membangun jaringan strategis, memperkuat komunikasi eksternal, dan menciptakan peluang kolaborasi berkelanjutan.",
        "anggota": [
            ("Hanif Wijaya", "Anggota"),
            ("Siti Nurhaliza", "Anggota"),
            ("Budi Santoso", "Anggota"),
            ("Dwi Putri Rahayu", "Anggota"),
            ("Ahmad Fauzi", "Anggota")
        ]
    },
    "danus.html": {
        "title": "Departemen Dana dan Usaha",
        "name": "Dana dan Usaha",
        "description": "Mengelola keuangan dan mengembangkan usaha",
        "profil": [
            "Departemen Dana dan Usaha (DANUS) adalah departemen yang bertugas mengelola keuangan organisasi, mencari sumber pendanaan, serta mengembangkan usaha-usaha yang menguntungkan untuk mendukung operasional HMJ Kedokteran UINAM.",
            "DANUS menjalankan peran strategis dalam perencanaan anggaran, akuntabilitas keuangan, serta inovasi usaha sosial yang memberikan nilai tambah bagi anggota dan organisasi secara keseluruhan."
        ],
        "ketua_name": "Raka Darmawan",
        "ketua_desc": "Memimpin Departemen Dana dan Usaha dengan fokus pada manajemen keuangan profesional, transparansi penuh, dan pengembangan usaha yang berkelanjutan.",
        "anggota": [
            ("Nur Azizah Farah", "Anggota"),
            ("Yusuf Hermawan", "Anggota"),
            ("Intan Cahya Putri", "Anggota"),
            ("Eka Pratama", "Anggota"),
            ("Siti Hajar", "Anggota"),
            ("Muhammad Hasan", "Anggota")
        ]
    },
    "jarkom.html": {
        "title": "Departemen Jaringan dan Komunikasi",
        "name": "Jaringan dan Komunikasi",
        "description": "Menjalin komunikasi internal dan media sosial",
        "profil": [
            "Departemen Jaringan dan Komunikasi (JARKOM) adalah departemen yang bertanggung jawab dalam mengelola komunikasi internal organisasi, media sosial, publikasi, dan strategi komunikasi HMJ Kedokteran UINAM.",
            "JARKOM memastikan informasi mengalir dengan efektif, memperkuat brand organisasi, serta membangun engagement yang kuat dengan komunitas melalui berbagai platform komunikasi modern dan efektif."
        ],
        "ketua_name": "Putri Amelia Sanjaya",
        "ketua_desc": "Memimpin Departemen Jaringan dan Komunikasi dengan komitmen mengembangkan strategi komunikasi inovatif, mengelola media sosial profesional, dan memperkuat identitas HMJ.",
        "anggota": [
            ("Rizky Mahendra", "Anggota"),
            ("Ayu Salsabila", "Anggota"),
            ("Jaka Wira Sentosa", "Anggota"),
            ("Siti Nur Annisa", "Anggota"),
            ("Farhan Alfareza", "Anggota")
        ]
    },
    "pmb.html": {
        "title": "Departemen Pengembangan Minat dan Bakat",
        "name": "Pengembangan Minat dan Bakat",
        "description": "Mengembangkan potensi dan bakat anggota",
        "profil": [
            "Departemen Pengembangan Minat dan Bakat (PMB) adalah departemen yang berdedikasi untuk menggali, mengembangkan, dan mengasah potensi serta bakat setiap anggota HMJ Kedokteran UINAM melalui program-program pelatihan dan kompetisi.",
            "Melalui berbagai kegiatan workshop, seminar, kompetisi akademik, dan lomba non-akademik, PMB menciptakan ekosistem pembelajaran yang mendorong setiap anggota untuk terus berkembang dan mencapai prestasi tertinggi mereka."
        ],
        "ketua_name": "Salehudin Rasyid",
        "ketua_desc": "Memimpin Departemen PMB dengan visi menciptakan platform pengembangan diri yang komprehensif, memfasilitasi bakat setiap anggota, dan membangun budaya keunggulan.",
        "anggota": [
            ("Nurul Aisyah", "Anggota"),
            ("Doni Pratama", "Anggota"),
            ("Zea Nurbaity", "Anggota"),
            ("Ahmad Rizki", "Anggota"),
            ("Mira Puspita", "Anggota"),
            ("Bagas Suryanto", "Anggota")
        ]
    },
    "pengmas.html": {
        "title": "Departemen Pengabdian Masyarakat",
        "name": "Pengabdian Masyarakat",
        "description": "Program kegiatan untuk masyarakat luas",
        "profil": [
            "Departemen Pengabdian Masyarakat (PENGMAS) adalah departemen yang fokus pada pelaksanaan program-program sosial, kesehatan, dan pemberdayaan masyarakat yang relevan dengan bidang kedokteran dan kemanusiaan.",
            "PENGMAS menjalankan misi mengamalkan ilmu pengetahuan kedokteran untuk memberikan manfaat nyata bagi masyarakat, membangun empati sosial, dan berkontribusi aktif dalam pembangunan masyarakat yang lebih sejahtera dan sehat."
        ],
        "ketua_name": "Alif Nurrahman Hakim",
        "ketua_desc": "Memimpin Departemen PENGMAS dengan dedikasi tinggi untuk menciptakan dampak sosial positif, memberdayakan masyarakat, dan mewujudkan tanggung jawab sosial organisasi.",
        "anggota": [
            ("Salma Zahra Aulia", "Anggota"),
            ("Farah Amir", "Anggota"),
            ("Ridho Salman", "Anggota"),
            ("Nadia Kusuma", "Anggota"),
            ("Irfan Habibi", "Anggota")
        ]
    },
    "kastrad.html": {
        "title": "Departemen Kajian Strategi dan Advokasi",
        "name": "Kajian Strategi dan Advokasi",
        "description": "Riset dan advokasi strategis organisasi",
        "profil": [
            "Departemen Kajian Strategi dan Advokasi (KASTRAD) adalah departemen yang melakukan riset, analisis strategis, dan advokasi terhadap isu-isu yang berkaitan dengan pendidikan kedokteran, kesehatan, dan hak-hak mahasiswa.",
            "KASTRAD berperan dalam pengembangan kebijakan internal organisasi, advokasi kepada pihak eksternal, serta menciptakan ekosistem pembelajaran kritis yang mendorong pemikiran strategis dan inovasi dalam setiap inisiatif organisasi."
        ],
        "ketua_name": "Ratna Wijayanto",
        "ketua_desc": "Memimpin Departemen KASTRAD dengan komitmen mengembangkan pemikiran strategis, melakukan riset mendalam, dan memperkuat kapasitas advokasi organisasi.",
        "anggota": [
            ("Ismail Maulana", "Anggota"),
            ("Sinta Dewi Putri", "Anggota"),
            ("Ardi Wijaya", "Anggota"),
            ("Fahira Salmah", "Anggota"),
            ("Bambang Sutrisno", "Anggota")
        ]
    },
    "p2.html": {
        "title": "Departemen Pendidikan dan Penelitian",
        "name": "Pendidikan dan Penelitian",
        "description": "Pengembangan akademik dan penelitian",
        "profil": [
            "Departemen Pendidikan dan Penelitian (P2) adalah departemen yang berkomitmen meningkatkan kualitas akademik, mendorong budaya penelitian, dan mengembangkan literasi ilmiah di kalangan mahasiswa kedokteran UINAM.",
            "P2 menjalankan berbagai program pembelajaran kolaboratif, workshop metodologi penelitian, dan fasilitasi penelitian yang mendukung pengembangan akademik setiap anggota serta kontribusi nyata terhadap kemajuan ilmu pengetahuan kedokteran."
        ],
        "ketua_name": "Al'zena Nurul Zahra",
        "ketua_desc": "Memimpin Departemen P2 dengan visi membangkitkan semangat pembelajaran berkelanjutan, mengembangkan budaya riset yang kuat, dan mendorong inovasi akademik.",
        "anggota": [
            ("Zahira Puspita Sari", "Anggota"),
            ("Mufti Radhitya", "Anggota"),
            ("Fitriana Cahya", "Anggota"),
            ("Rendra Wijaya", "Anggota"),
            ("Nita Suhartini", "Anggota"),
            ("Wahyu Santoso", "Anggota")
        ]
    },
    "psdm.html": {
        "title": "Departemen Pengembangan Sumber Daya Manusia",
        "name": "Pengembangan Sumber Daya Manusia",
        "description": "Program pelatihan dan pengembangan SDM",
        "profil": [
            "Departemen Pengembangan Sumber Daya Manusia (PSDM) adalah departemen yang fokus pada pengembangan karakter, kepemimpinan, life skills, dan kualitas SDM setiap anggota HMJ Kedokteran UINAM.",
            "PSDM menyelenggarakan program pengembangan diri, leadership training, mentoring, dan soft skills development yang dirancang untuk menciptakan generasi pemimpin yang visioner, integritas tinggi, dan siap menghadapi tantangan global."
        ],
        "ketua_name": "Siti Khadijah Zahra",
        "ketua_desc": "Memimpin Departemen PSDM dengan fokus mengembangkan karakter unggul, membangun pemimpin masa depan, dan menciptakan budaya pembelajaran personal yang berkelanjutan.",
        "anggota": [
            ("Ariana Putri", "Anggota"),
            ("Hari Supriyanto", "Anggota"),
            ("Fitri Handayani", "Anggota"),
            ("Rizal Kurniawan", "Anggota"),
            ("Maya Sariawan", "Anggota"),
            ("Budi Harjanto", "Anggota")
        ]
    },
    "pikis.html": {
        "title": "Departemen Pengembangan Ilmu dan Karakter Islam",
        "name": "Pengembangan Ilmu dan Karakter Islam",
        "description": "Pendidikan Islam dan pengembangan karakter",
        "profil": [
            "Departemen Pengembangan Ilmu dan Karakter Islam (PIKIS) adalah departemen yang bertugas mengembangkan pemahaman Islam yang mendalam, karakter islami yang kuat, dan integrasi nilai-nilai Islam dalam setiap aspek kehidupan mahasiswa kedokteran.",
            "PIKIS menyelenggarakan kajian Islam, mentoring spiritual, program dakwah, dan berbagai kegiatan yang meningkatkan kepribadian Islami, moralitas tinggi, serta membangun generasi medis yang tidak hanya ahli dalam ilmu kedokteran tetapi juga kuat dalam iman dan akhlak."
        ],
        "ketua_name": "Muhammad Zainul Arifin",
        "ketua_desc": "Memimpin Departemen PIKIS dengan dedikasi mengembangkan pemahaman Islam yang komprehensif, memperkuat karakter islami, dan menciptakan komunitas yang taat dan bermoral.",
        "anggota": [
            ("Nur Safiyyah", "Anggota"),
            ("Amira Fauziah", "Anggota"),
            ("Kharis Ismail", "Anggota"),
            ("Aisha Mawaddah", "Anggota"),
            ("Hasan Alfurqan", "Anggota"),
            ("Laila Husnayain", "Anggota")
        ]
    }
}

template = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Departemen {title} | HMJ Kedokteran UIN Alauddin Makassar</title>

  <!-- Bootstrap -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

  <!-- Bootstrap Icons -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css">

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap" rel="stylesheet">

  <!-- Custom Style -->
  <style>
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}

    html {{
      scroll-behavior: smooth;
    }}

    body {{
      font-family: 'Montserrat', sans-serif;
      color: #333;
      line-height: 1.6;
      background: #fafafa;
    }}

    /* ===== NAVBAR MODERN STYLING ===== */
    .navbar-custom {{
      background-color: #ffffff;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
      padding: 1rem 0;
      position: sticky;
      top: 0;
      z-index: 1000;
      transition: all 0.3s ease;
    }}

    .navbar-custom.scrolled {{
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
      padding: 0.6rem 0;
    }}

    .navbar-custom .navbar-brand {{
      font-weight: 700;
      font-size: 1.3rem;
      color: #8B7355 !important;
      margin-right: 3rem;
      display: flex;
      align-items: center;
      gap: 10px;
      letter-spacing: 0.8px;
      transition: all 0.3s ease;
    }}

    .navbar-custom .navbar-brand i {{
      font-size: 1.6rem;
    }}

    .navbar-custom .nav-link {{
      color: #5f6368 !important;
      font-weight: 500;
      font-size: 0.95rem;
      padding: 0.6rem 1.1rem !important;
      margin: 0 3px;
      border-radius: 6px;
      transition: all 0.3s ease;
      position: relative;
    }}

    .navbar-custom .nav-link::after {{
      content: '';
      position: absolute;
      bottom: 0;
      left: 50%;
      width: 0;
      height: 2px;
      background: #8B7355;
      transition: all 0.3s ease;
      transform: translateX(-50%);
    }}

    .navbar-custom .nav-link:hover::after {{
      width: 80%;
    }}

    .navbar-custom .dropdown-menu {{
      background-color: #ffffff;
      border: none;
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
      border-radius: 8px;
      margin-top: 10px;
      min-width: 260px;
      padding: 0.8rem 0;
      animation: slideDown 0.3s ease;
    }}

    @keyframes slideDown {{
      from {{
        opacity: 0;
        transform: translateY(-10px);
      }}
      to {{
        opacity: 1;
        transform: translateY(0);
      }}
    }}

    .navbar-custom .dropdown-item {{
      color: #5f6368;
      font-weight: 500;
      font-size: 0.9rem;
      padding: 0.8rem 1.5rem;
      transition: all 0.2s ease;
      border-left: 3px solid transparent;
    }}

    .navbar-custom .dropdown-item:hover {{
      background-color: #F5F3F0;
      color: #8B7355;
      border-left-color: #8B7355;
      padding-left: 1.8rem;
    }}

    .navbar-social-icons {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-left: 2rem;
      padding-left: 2rem;
      border-left: 1px solid #e8e8e8;
    }}

    .navbar-social-icons a {{
      width: 38px;
      height: 38px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      background-color: #F5F3F0;
      color: #8B7355;
      text-decoration: none;
      transition: all 0.3s ease;
      font-size: 1.1rem;
    }}

    .navbar-social-icons a:hover {{
      background-color: #8B7355;
      color: #ffffff;
      transform: translateY(-4px);
      box-shadow: 0 4px 12px rgba(139, 115, 85, 0.25);
    }}

    .navbar-toggler {{
      border: none;
      color: #8B7355;
    }}

    @media (max-width: 991px) {{
      .navbar-custom .nav-link {{
        padding: 0.7rem 0.8rem !important;
      }}

      .navbar-collapse {{
        background-color: #ffffff;
        border-top: 1px solid #e8e8e8;
        margin-top: 0.8rem;
        padding: 0.8rem 0;
      }}

      .navbar-social-icons {{
        margin-left: 0;
        margin-top: 1rem;
        padding-left: 0;
        border-left: none;
        border-top: 1px solid #e8e8e8;
      }}
    }}

    /* ===== HERO SECTION ===== */
    .department-hero {{
      min-height: 80vh;
      background: linear-gradient(135deg, #8B7355 0%, #6B8E8E 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      text-align: center;
      position: relative;
      overflow: hidden;
    }}

    .department-hero::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
      opacity: 0.5;
      animation: movePattern 20s linear infinite;
    }}

    @keyframes movePattern {{
      0% {{ transform: translate(0, 0); }}
      100% {{ transform: translate(60px, 60px); }}
    }}

    .department-hero-content {{
      position: relative;
      z-index: 2;
      animation: fadeInUp 0.8s ease-out;
      max-width: 900px;
      padding: 0 30px;
    }}

    .department-hero h1 {{
      font-size: clamp(2.5rem, 7vw, 4rem);
      font-weight: 800;
      letter-spacing: 2px;
      margin-bottom: 15px;
      line-height: 1.2;
    }}

    .department-hero p {{
      font-size: clamp(1rem, 2.5vw, 1.3rem);
      font-weight: 400;
      letter-spacing: 1px;
      opacity: 0.95;
    }}

    @keyframes fadeInUp {{
      from {{
        opacity: 0;
        transform: translateY(40px);
      }}
      to {{
        opacity: 1;
        transform: translateY(0);
      }}
    }}

    /* ===== DEPARTMENT SECTION ===== */
    .department-section {{
      padding: 80px 0;
      background: #ffffff;
    }}

    .department-section:nth-child(even) {{
      background: #fafafa;
    }}

    .section-title {{
      font-size: 2.8rem;
      font-weight: 800;
      text-align: center;
      margin-bottom: 15px;
      color: #333;
      letter-spacing: 0.5px;
    }}

    .section-divider {{
      width: 60px;
      height: 3px;
      background: #8B7355;
      margin: 0 auto 50px;
      border-radius: 2px;
    }}

    .profil-content {{
      font-size: 1rem;
      color: #5f6368;
      line-height: 1.9;
      max-width: 1000px;
      margin: 0 auto;
    }}

    .profil-content p {{
      margin-bottom: 20px;
    }}

    /* ===== KETUA CARD ===== */
    .ketua-card {{
      max-width: 350px;
      margin: 0 auto;
      background: white;
      border-radius: 12px;
      padding: 50px 40px;
      text-align: center;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
      transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
      border-top: 5px solid #8B7355;
      position: relative;
      overflow: hidden;
    }}

    .ketua-card::before {{
      content: '';
      position: absolute;
      top: 0;
      right: 0;
      width: 100px;
      height: 100px;
      background: linear-gradient(135deg, #8B7355 0%, transparent 70%);
      opacity: 0.1;
      border-radius: 50%;
    }}

    .ketua-card:hover {{
      transform: translateY(-8px);
      box-shadow: 0 12px 35px rgba(0, 0, 0, 0.1);
    }}

    .ketua-photo {{
      width: 200px;
      height: 200px;
      margin: 0 auto 25px;
      border-radius: 50%;
      object-fit: cover;
      border: 5px solid #8B7355;
      box-shadow: 0 8px 25px rgba(139, 115, 85, 0.2);
      transition: all 0.3s ease;
      flex-shrink: 0;
      position: relative;
      z-index: 2;
    }}

    .ketua-card:hover .ketua-photo {{
      transform: scale(1.08);
      box-shadow: 0 12px 35px rgba(139, 115, 85, 0.3);
    }}

    .ketua-name {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #333;
      margin-bottom: 10px;
      position: relative;
      z-index: 2;
    }}

    .ketua-position {{
      font-size: 0.9rem;
      color: #8B7355;
      font-weight: 600;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 20px;
      position: relative;
      z-index: 2;
    }}

    .ketua-description {{
      color: #5f6368;
      font-size: 0.95rem;
      line-height: 1.8;
      position: relative;
      z-index: 2;
    }}

    /* ===== ANGGOTA GRID ===== */
    .anggota-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 35px;
      margin-top: 50px;
      max-width: 1200px;
      margin-left: auto;
      margin-right: auto;
    }}

    .anggota-card {{
      background: white;
      border-radius: 12px;
      padding: 35px 25px;
      text-align: center;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
      transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
      border-top: 4px solid #8B7355;
      position: relative;
      overflow: hidden;
    }}

    .anggota-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(135deg, rgba(139, 115, 85, 0.05) 0%, transparent 100%);
      opacity: 0;
      transition: all 0.3s ease;
    }}

    .anggota-card:hover {{
      transform: translateY(-10px);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
    }}

    .anggota-card:hover::before {{
      opacity: 1;
    }}

    .anggota-photo {{
      width: 140px;
      height: 140px;
      margin: 0 auto 20px;
      border-radius: 50%;
      object-fit: cover;
      border: 4px solid #8B7355;
      box-shadow: 0 6px 18px rgba(139, 115, 85, 0.15);
      transition: all 0.3s ease;
      flex-shrink: 0;
      position: relative;
      z-index: 2;
    }}

    .anggota-card:hover .anggota-photo {{
      transform: scale(1.12);
      box-shadow: 0 10px 28px rgba(139, 115, 85, 0.25);
    }}

    .anggota-name {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #333;
      margin-bottom: 8px;
      position: relative;
      z-index: 2;
    }}

    .anggota-position {{
      font-size: 0.8rem;
      color: #8B7355;
      font-weight: 600;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      position: relative;
      z-index: 2;
    }}

    /* ===== FOOTER ===== */
    .footer {{
      background: #333;
      color: #fff;
      padding: 60px 0 20px;
    }}

    .footer-content {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 40px;
      margin-bottom: 40px;
    }}

    .footer-section h5 {{
      font-size: 1.1rem;
      margin-bottom: 20px;
      font-weight: 700;
      color: #8B7355;
      letter-spacing: 0.5px;
    }}

    .footer-section p {{
      font-size: 0.9rem;
      color: #ccc;
      line-height: 1.8;
    }}

    .footer-section ul {{
      list-style: none;
      padding: 0;
    }}

    .footer-section ul li {{
      margin-bottom: 12px;
    }}

    .footer-section ul li a {{
      color: #ccc;
      text-decoration: none;
      font-size: 0.9rem;
      transition: all 0.3s ease;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .footer-section ul li a:hover {{
      color: #8B7355;
      transform: translateX(4px);
    }}

    .footer-divider {{
      border-top: 1px solid #555;
      padding-top: 30px;
      margin-top: 30px;
      text-align: center;
    }}

    .footer-divider p {{
      font-size: 0.85rem;
      color: #999;
      margin: 0;
    }}

    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {{
      .department-section {{
        padding: 60px 0;
      }}

      .section-title {{
        font-size: 2rem;
      }}

      .anggota-grid {{
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 25px;
      }}
    }}

    @media (max-width: 576px) {{
      .department-hero {{
        min-height: 60vh;
      }}

      .department-hero h1 {{
        font-size: 2rem;
      }}

      .profil-content {{
        font-size: 0.95rem;
      }}

      .ketua-card {{
        padding: 35px 25px;
      }}

      .anggota-grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>

<body>
  <!-- ========== NAVBAR ========== -->
  <nav class="navbar navbar-expand-lg navbar-custom">
    <div class="container-fluid px-3 px-md-4">
      <a class="navbar-brand" href="index.html">
        <i class="bi bi-hospital-fill"></i>
        <span>HMJ KEDOKTERAN</span>
      </a>

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <i class="bi bi-list"></i>
      </button>

      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <a class="nav-link" href="index.html">
              <i class="bi bi-house-door-fill"></i>
              <span>Beranda</span>
            </a>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="departemenDropdown" role="button" data-bs-toggle="dropdown">
              <i class="bi bi-diagram-3-fill"></i>
              <span>Departemen</span>
            </a>
            <ul class="dropdown-menu" aria-labelledby="departemenDropdown">
              <li><a class="dropdown-item" href="admin.html"><i class="bi bi-file-earmark-text"></i> Administrasi</a></li>
              <li><a class="dropdown-item" href="hublu.html"><i class="bi bi-globe"></i> Hubungan Luar</a></li>
              <li><a class="dropdown-item" href="danus.html"><i class="bi bi-cash-coin"></i> Dana dan Usaha</a></li>
              <li><a class="dropdown-item" href="jarkom.html"><i class="bi bi-share-fill"></i> Jaringan & Komunikasi</a></li>
              <li><a class="dropdown-item" href="pmb.html"><i class="bi bi-star-fill"></i> Pengembangan Minat & Bakat</a></li>
              <li><a class="dropdown-item" href="pengmas.html"><i class="bi bi-heart-fill"></i> Pengabdian Masyarakat</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="kastrad.html"><i class="bi bi-lightbulb"></i> Kajian Strategi & Advokasi</a></li>
              <li><a class="dropdown-item" href="p2.html"><i class="bi bi-book-fill"></i> Pendidikan & Penelitian</a></li>
              <li><a class="dropdown-item" href="psdm.html"><i class="bi bi-people-fill"></i> Pengembangan SDM</a></li>
              <li><a class="dropdown-item" href="pikis.html"><i class="bi bi-brightness-high-fill"></i> Pengembangan Ilmu & Karakter Islam</a></li>
            </ul>
          </li>

          <li class="nav-item">
            <div class="navbar-social-icons">
              <a href="https://www.instagram.com/hmjkuinam" target="_blank" title="Instagram HMJ Kedokteran">
                <i class="bi bi-instagram"></i>
              </a>
              <a href="https://www.tiktok.com/@hmjkuinam?_r=1&_t=ZS-93GMKX5Mlqq" target="_blank" title="TikTok HMJ Kedokteran">
                <i class="bi bi-tiktok"></i>
              </a>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- ========== HERO SECTION ========== -->
  <section class="department-hero">
    <div class="department-hero-content">
      <h1>Departemen {name}</h1>
      <p>HMJ Kedokteran UIN Alauddin Makassar</p>
    </div>
  </section>

  <!-- ========== PROFIL DEPARTEMEN ========== -->
  <section class="department-section">
    <div class="container">
      <h2 class="section-title">Profil Departemen</h2>
      <div class="section-divider"></div>
      <div class="profil-content">
        <p>{profil1}</p>
        <p>{profil2}</p>
      </div>
    </div>
  </section>

  <!-- ========== KETUA DEPARTEMEN ========== -->
  <section class="department-section">
    <div class="container">
      <h2 class="section-title">Ketua Departemen</h2>
      <div class="section-divider"></div>
      <div class="ketua-card">
        <img src="" alt="{ketua_name}" class="ketua-photo">
        <div class="ketua-name">{ketua_name}</div>
        <div class="ketua-position">KETUA DEPARTEMEN</div>
        <p class="ketua-description">{ketua_desc}</p>
      </div>
    </div>
  </section>

  <!-- ========== ANGGOTA DEPARTEMEN ========== -->
  <section class="department-section">
    <div class="container">
      <h2 class="section-title">Anggota Departemen</h2>
      <div class="section-divider"></div>
      <div class="anggota-grid">
        {anggota_html}
      </div>
    </div>
  </section>

  <!-- ========== FOOTER ========== -->
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-section">
          <h5><i class="bi bi-hospital-fill"></i> Tentang Kami</h5>
          <p>Himpunan Mahasiswa Jurusan Kedokteran UINAM adalah organisasi yang berdedikasi untuk mengembangkan mahasiswa kedokteran menjadi profesional yang kompeten dan berakhlak mulia.</p>
        </div>

        <div class="footer-section">
          <h5><i class="bi bi-link-45deg"></i> Link Cepat</h5>
          <ul>
            <li><a href="index.html"><i class="bi bi-house"></i> Beranda</a></li>
            <li><a href="index.html#departemen"><i class="bi bi-building"></i> Departemen</a></li>
            <li><a href="index.html#visi"><i class="bi bi-eye"></i> Visi & Misi</a></li>
            <li><a href="index.html#pengurus"><i class="bi bi-people"></i> Kepengurusan</a></li>
          </ul>
        </div>

        <div class="footer-section">
          <h5><i class="bi bi-envelope"></i> Hubungi Kami</h5>
          <ul>
            <li><a href="mailto:hmjk.uinam@gmail.com"><i class="bi bi-envelope"></i> hmjk.uinam@gmail.com</a></li>
            <li><a href="https://instagram.com/hmjkuinam" target="_blank"><i class="bi bi-instagram"></i> @hmjkuinam</a></li>
            <li><a href="https://www.tiktok.com/@hmjkuinam?_r=1&_t=ZS-93GMKX5Mlqq" target="_blank"><i class="bi bi-tiktok"></i> @hmjkuinam</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-divider">
        <p>&copy; 2026 HMJ Kedokteran UIN Alauddin Makassar. Dikembangkan dengan <span style="color: #8B7355;">❤</span> untuk Pendidikan Kedokteran Berkualitas.</p>
      </div>
    </div>
  </footer>

</body>

<!-- Bootstrap JS Bundle -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

<!-- Custom JavaScript -->
<script>
  // Navbar scroll effect
  window.addEventListener('scroll', function() {{
    const navbar = document.querySelector('.navbar-custom');
    if (window.scrollY > 50) {{
      navbar.classList.add('scrolled');
    }} else {{
      navbar.classList.remove('scrolled');
    }}
  }});

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
    anchor.addEventListener('click', function (e) {{
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {{
        target.scrollIntoView({{ behavior: 'smooth' }});
      }}
    }});
  }});

  // Add animation on scroll
  const observerOptions = {{
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
  }};

  const observer = new IntersectionObserver(function(entries) {{
    entries.forEach(entry => {{
      if (entry.isIntersecting) {{
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }}
    }});
  }}, observerOptions);

  document.querySelectorAll('.anggota-card, .ketua-card').forEach(el => {{
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'all 0.6s ease';
    observer.observe(el);
  }});
</script>

</html>
"""

for filename, data in departments.items():
    anggota_html = '\n        '.join([
        f'<div class="anggota-card">\n          <img src="" alt="{name}" class="anggota-photo">\n          <div class="anggota-name">{name}</div>\n          <div class="anggota-position">{pos}</div>\n        </div>'
        for name, pos in data["anggota"]
    ])
    
    content = template.format(
        title=data["title"],
        name=data["name"],
        profil1=data["profil"][0],
        profil2=data["profil"][1],
        ketua_name=data["ketua_name"],
        ketua_desc=data["ketua_desc"],
        anggota_html=anggota_html
    )
    
    filepath = f"d:\\HJMK-UINAM\\{filename}"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Created: {filename}")

print("\n✓ Semua 9 departemen telah di-modernisasi!")

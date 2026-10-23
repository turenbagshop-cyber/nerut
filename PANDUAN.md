# Pasang situs tools di Blogger + GitHub Pages

## 1. GitHub (tempat file tools)
1. Buat repo publik, mis. `turenlabs-tools`.
2. Unggah ISI folder ini (index.html, layout-editor/, rx3-editor/, db-editor/, .nojekyll). Folder `blogger/` tidak wajib diunggah.
3. Settings > Pages > Source: "Deploy from a branch" > branch `main`, folder `/ (root)` > Save.
4. Tunggu 1-2 menit. Tes: `https://USERNAME.github.io/turenlabs-tools/layout-editor/`

## 2. Blogger (tampilan situs)
1. Buat laman (Laman > Laman baru), pindah ke "Tampilan HTML", tempel isi file di `blogger/`:
   - Beranda  -> halaman-beranda.html
   - Layout Editor -> halaman-layout-editor.html (permalink kustom: layout-editor)
   - RX3 Editor -> halaman-rx3-editor.html (permalink: rx3-editor)
   - DB Editor -> halaman-db-editor.html (permalink: db-editor)
2. Di file iframe, ganti USERNAME dan NAMAREPO.
3. Tata letak > Tambah gadget "Laman" untuk menu navigasi.
4. Pengaturan > Preferensi laman beranda: jadikan laman Beranda sebagai laman utama (opsional).

## Catatan
- Di dalam iframe, "Buka folder" tidak tersedia (batasan browser); pakai ZIP, atau tombol "Buka layar penuh".
- Edit editor: ubah web-src di proyek asli, jalankan tools/build-web.py, lalu `python3 build/make_site.py <folder-proyek> <folder-keluaran>`.

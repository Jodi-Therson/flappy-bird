# Flappy Bird - Edisi Pygame
> Sebuah remake dari game klasik Flappy Bird, dikembangkan menggunakan Pygame. Dengan desain nuansa alam Indonesia khususnya pulau Bali. Ditambah efek animasi dan ledakan saat burung tabrakan dengan pipa atau tanah.

## Instalasi
Jalankan command ini di terminal (Khusus Windows):
```
git clone https://github.com/Jodi-Therson/flappy-bird.git
cd flappy-bird
pip install -r requirements.txt
python main.py
```

## Struktur Proyek
```
flappy-bird/
├── dist/                  # Folder aplikasi
│   ├── Flappy Bird.exe     # Versi 1.1
│   └── main.exe            # Versi 1.0
│
├── img/                    # Folder aset gambar
│   ├── bg.png
│   ├── bird_asli1.png
│   ├── bird_asli2.png
│   ├── bird_asli3.png
│   ├── bird_blue1.png
│   ├── bird_blue2.png
│   ├── bird_blue3.png
│   ├── bird_red1.png
│   ├── bird_red2.png
│   ├── bird_red3.png
│   ├── bird1.png
│   ├── bird2.png
│   ├── bird3.png
│   ├── ground.png
│   ├── pipe.png
│   └── restart.png
│
├── sound/                  # Folder aset suara
│   ├── crash.mp3
│   ├── sfx_point.mp3
│   ├── sfx_pop.mp3
│   └── sfx_wing.mp3
│
├── main.py                 # File utama game
├── highscore.txt           # (Otomatis dibuat di APPDATA)
├── achievements.json       # (Otomatis dibuat di APPDATA)
├── requirements.txt        # Library yang diperlukan
├── CHANGELOG.md            # Berisi perubahan proyek
└── README.md
```

## Build ke .exe (opsional)
Jika ingin membungkus game ini menjadi .exe, jalankan command ini di terminal (Khusus Windows):
```
pyinstaller --name "Flappy Bird" --onefile --windowed --add-data "img;img" --add-data "sound;sound" main.py
```

## Changelog
Untuk riwayat lengkap perubahan dan pembaruan proyek, silakan lihat file [CHANGELOG.md](CHANGELOG.md).

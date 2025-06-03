# Flappy Bird - Edisi Pygame
> Sebuah remake dari game klasik Flappy Bird, dikembangkan menggunakan Pygame. Dengan desain nuansa alam Indonesia khususnya pulau Bali. Ditambah efek animasi dan ledakan saat burung tabrakan dengan pipa atau tanah.

## Instalasi
Jalankan command ini di terminal (Khusus Windows):
```
git clone https://github.com/Jodi-Therson/flappy-bird.git
cd flappy-bird
pip install requirements.txt
python main.py
```

## Struktur Proyek
```
flappy-bird/
├── dist/                  # Folder aplikasi
│   ├── main.exe
│
├── img/                    # Folder aset gambar
│   ├── bird1.png
│   ├── bird2.png
│   ├── bird3.png
│   ├── bg.png
│   ├── ground.png
│   ├── pipe.png
│   └── restart.png
│
├── sound/                  # Folder aset suara
│   ├── sfx_wing.mp3
│   ├── sfx_point.mp3
│   └── crash.mp3
│
├── main.py                 # File utama game
├── highscore.txt           # (Otomatis dibuat di APPDATA)
├── requirements.txt        # Library yang diperlukan
└── README.md
```

## Build ke .exe (opsional)
Jika ingin membungkus game ini menjadi .exe, jalankan command ini di terminal (Khusus Windows):
```
pyinstaller --onefile --windowed --add-data "img;img" --add-data "sound;sound" main.py
```

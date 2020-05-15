# Cara menggunakan

- Buka Command Prompt atau Windows Powershell
- Masuk ke directory yang digunakan untuk menyimpan project ini

1. ketik `git clone https://github.com/informatikaA2017/Pengolahan-Citra.git`
2. ketik `cd Pengolahan-Citra` lalu enter
3. ketik `git checkout -b <namabranch>` ex. `git checkout -b tugas/zakky`

Next step

4. ketik `pip install virtualenv` lalu enter
5. ketik `virtualenv <namaenv>` ex. `virtualenv venv`
6. ketik `cd <namaenv>` enter, lalu `Scripts\activate`
7. ketik `pip install opencv-python` lalu enter
8. ketik `pip install opencv-contrib-python` lalu enter

> Pastikan untuk no. 6 output di cmd `(venv) PS D:\Kuliah\Semester 6\Pengolahan Citra\Pengolahan-Citra\venv` ada nama env kalian di awalnya. ex. `venv`

9. Kembali ke directory sebelumnya, atau ketik `cd ..`
10. Ketik `python`
11. Ketik `import cv2` lalu enter
12. Ketik `cv2.__version__` lalu enter. Jika muncul versinya berarti sukses
13. Ketik `exit()` untuk keluar dari python


Untuk menjalankan code yang sudah dibuat
```
Ketik `python <namafile>.py`
```

Untuk contoh code bisa dilihat [disini](https://github.com/informatikaA2017/Pengolahan-Citra/blob/master/example.py)

## Cara Push ke Repository

1. Ketik `git add .`
2. Ketik `git commit -m "commit message"`
3. Ketik `git push origin <namabranch>`
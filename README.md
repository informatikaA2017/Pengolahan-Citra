# Pengolahan Citra

Ini adalah Repository informatika 2017, untuk memenuhi tugas Pengolahan Citra

## Installation OpenCV

1. Download [python](https://www.python.org/downloads/)
2. Open your Command Prompt or Terminal

```
1. pip install numpy
2. pip install matplotlib
3. pip install opencv-python
4. pip install opencv-contrib-python
5. pip install opencv-python-headless
6. pip install opencv-contrib-python-headless
```

> *Note :* for testing `import cv2` hit enter , run `print cv2.__version__`

## Belajar-Git

Git adalah version control system yang digunakan para developer untuk mengembangkan software secara bersama-bersama. Fungsi utama git yaitu mengatur versi dari source code program anda dengan mengasih tanda baris dan code mana yang ditambah atau diganti.

### Prerequisites

1. Download [Git](https://git-scm.com/)
2. Buat Akun di [Github](https://github.com) atau [Gitlab](https://gitlab.com)

### Git Basic Commands

| Command | Description |
| --- | --- |
| `git config --global user.email sam@example.com` | Inisialisasi User untuk Git |
| `git init` | Untuk membuat repository pada file lokal |
| `git remote add origin <server>` | Untuk menghubungkan repository lokal ke server |
| `git add <filename>` or `git add *` | Menambahkan satu file atau banyak file pada Repository |
| `git commit -m "Commit message"` | Untuk menyimpan perubahan yang dilakukan, tetapi tidak ada perubahan pada remote repository |
| `git push origin <branch>` | Untuk mengirimkan perubahan file setelah di commit ke remote repository |
| `git clone /path/to/repository` | Membuat Salinan repository lokal |
| `git status` | Melihat list yang sudah dirubah dan memerlukan commit |
| `git checkout -b <branchname>` | Membuat branch baru di repository |
| `git checkout <branchname>` | Pindah ke branch lain yang ada di repository |
| `git pull` | Menarik code dari repository ke local |
| `git merge <branchname>` | Menggabungkan branch ke branch aktif |

Dokumentasi lainnya bisa di cek [disini](https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html)

### Usage

1. `git config --global user.email sam@example.com`
2. `git clone https://github.com/informatika2017/Pengolahan-Citra.git` in the terminal or command prompt
3. `git checkout -b <namebranch>` for create new branch ex. your name
4. `git add <filename> or git add .` for add any file from local to remote repository
5. `git status` for check changes file in local repository
6. `git commit -m "commit message"` for send changes file to remote repository but repository not changes before push
7. `git push origin <branchname>` for send changes file after commit to repository

> *Note :* Dont touch master branch , create new branch instead

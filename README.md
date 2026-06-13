# Game Inventory API (Manajemen Item & Equipment Game)

Proyek backend API berbasis **Django** & **Django REST Framework (DRF)** dengan database **SQLite** untuk memenuhi kebutuhan tugas **Ujian Akhir Semester (UAS) Praktikum Kualitas Perangkat Lunak**.

API ini dirancang untuk mengelola data penyimpanan item/equipment game (CRUD) dengan respon JSON standar dan kode status HTTP yang tepat.

---

## Fitur & Spesifikasi API

### 1. Struktur Data Item (Model)
Setiap item dalam inventory memiliki atribut/field sebagai berikut:
* `id` (Integer, Auto Increment)
* `item_name` (CharField) -> Contoh: `"Excalibur"`, `"Health Potion"`
* `item_type` (CharField) -> Contoh: `"Weapon"`, `"Consumable"`, `"Armor"`
* `rarity` (CharField) -> Contoh: `"Common"`, `"Epic"`, `"Legendary"`
* `stat_value` (Integer) -> Nilai stat poin (misal: damage, defense, atau healing amount)
* `is_equipped` (Boolean) -> Status kelengkapan item pada karakter (Default: `false`)
* `created_at` (DateTimeField) -> Waktu penambahan item (Otomatis)
* `updated_at` (DateTimeField) -> Waktu pembaruan item terakhir (Otomatis)

### 2. Endpoints API
| Method | Endpoint | Fungsi | Status Code Sukses |
|---|---|---|---|
| **POST** | `/items/` | Menambahkan item baru ke inventory | `201 Created` |
| **GET** | `/items/` | Mengambil seluruh daftar item di inventory | `200 OK` |
| **GET** | `/items/<id>/` | Mengambil detail spesifik satu item | `200 OK` |
| **PUT** | `/items/<id>/` | Memperbarui data item secara penuh berdasarkan ID | `200 OK` |
| **PATCH** | `/items/<id>/` | Memperbarui sebagian data item (misal: equip status) | `200 OK` |
| **DELETE** | `/items/<id>/` | Menghapus item dari inventory | `204 No Content` |

---

## Panduan Instalasi & Cara Menjalankan Project

### 1. Klon / Buka Direktori Project
Buka terminal/command prompt lalu masuk ke direktori project:
```bash
git clone https://github.com/Nazlul31/uas-prakkpl-game-inventory.git
cd uas-prakkpl-game-inventory
```

### 2. Buat & Aktifkan Virtual Environment (venv)
* **Membuat venv:**
  ```bash
  python -m venv venv
  ```
* **Mengaktifkan venv:**
  * **Windows (PowerShell):**
    ```powershell
    .\venv\Scripts\Activate.ps1
    ```
  * **Windows (CMD / Command Prompt):**
    ```cmd
    .\venv\Scripts\activate.bat
    ```

### 3. Install Dependensi
```bash
pip install django djangorestframework
```

### 4. Jalankan Migrasi Database
Siapkan skema database SQLite bawaan:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Jalankan Server Development
```bash
python manage.py runserver
```
Server akan aktif di: **`http://127.0.0.1:8000/`**

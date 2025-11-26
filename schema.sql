-- Buat database dan tabel
CREATE DATABASE IF NOT EXISTS uts_pbo;
USE uts_pbo;

CREATE TABLE IF NOT EXISTS rapot_mahasiswa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nim VARCHAR(20) NOT NULL,
    nama VARCHAR(100) NOT NULL,
    prodi VARCHAR(100) NOT NULL,        
    matkul VARCHAR(100) NOT NULL,
    nilai_angka INT NOT NULL,
    nilai_huruf CHAR(1) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Contoh data awal
INSERT INTO rapot_mahasiswa (nim, nama, prodi, matkul, nilai_angka, nilai_huruf) VALUES
('240105001', 'Muhammad ABil', 'Informatika', 'Bahasa Indonesia', 88, 'A'),
('240105002', 'Nanda Anggraini', 'Informatika', 'Bahasa Indonesia', 74, 'B');
('240106001', 'Azizi Fahmi Yusuf', 'Farmasi', 'Aswaja', 84, 'B');
('240106002', 'Nazwa Amelia', 'Farmasi', 'Aswaja', 90, 'B');
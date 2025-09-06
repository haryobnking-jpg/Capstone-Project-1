CREATE DATABASE SMA2;

USE SMA2;

CREATE TABLE nilai_siswa(
 id_siswa INT AUTO_INCREMENT PRIMARY KEY,
 Nama VARCHAR(20) NOT NULL,
 Kelas VARCHAR(10) NOT NULL,
 Mata_Pelajaran VARCHAR(20) NOT NULL,
 Nilai INT NOT NULL,
 Umur INT NOT NULL,
 Gender VARCHAR(20) NOt NULL
 );
 
INSERT INTO nilai_siswa (Nama, Kelas, Mata_Pelajaran, Nilai, Umur,Gender)
VALUES
('Alwy', 'X-E', 'Biologi', 78, 18,'Male'),
('Ahmed', 'X-D', 'Matematika', 65, 17,'Male'),
('Bayu', 'X-F', 'Sejarah', 90, 16,'Male'),
('Ray', 'X-D', 'Ekonomi', 82, 17,'Male'),
('Panji', 'X-D', 'Matematika', 55, 17,'Male'),
('Bian', 'X-D', 'Ekonomi', 88, 18,'Male'),
('Dzaki', 'X-E', 'Matematika', 60, 18,'Male'),
('Raja', 'X-F', 'Biologi', 72, 17,'Male'),
('Varel', 'X-F', 'Ekonomi', 81, 15,'Male'),
('Ayu', 'X-E', 'Sejarah', 95, 16,'Female'),
('Dessi', 'X-D', 'Sejarah', 70, 16,'Female'),
('Sakura', 'X-E', 'Biologi', 50, 17,'Female'),
('Putri', 'X-F', 'Matematika', 89, 17,'Female'),
('Echa', 'X-F', 'Sejarah', 77, 17,'Female'),
('Nayla', 'X-E', 'Biologi', 66, 15,'Female');
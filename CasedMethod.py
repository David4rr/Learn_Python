import numpy as np
from scipy.stats import pearsonr, ttest_ind

# 1. Pengumpulan Data
np.random.seed(42)
aktivitas_kelas_A = np.random.randint(10, 41, size=30)
hasil_kelas_A = np.random.randint(0, 101, size=30)

aktivitas_kelas_B = np.random.randint(10, 41, size=30)
hasil_kelas_B = np.random.randint(0, 101, size=30)

# 2. Uji Normalitas dan Homogenitas (tidak disertakan dalam contoh kode)

# 3. Analisis Aktivitas Belajar dan Hasil Belajar
correlation_A, _ = pearsonr(aktivitas_kelas_A, hasil_kelas_A)
correlation_B, _ = pearsonr(aktivitas_kelas_B, hasil_kelas_B)

# 4. Analisis Pengaruh Pembelajaran Berbasis Cased Method
t_stat, p_value = ttest_ind(hasil_kelas_A, hasil_kelas_B)

# 5. Interpretasi Hasil
print(f"Korelasi Aktivitas dan Hasil Belajar Kelas A: {correlation_A}")
print(f"Korelasi Aktivitas dan Hasil Belajar Kelas B: {correlation_B}")
print(f"Pengaruh Pembelajaran Berbasis Cased Method: p-value = {p_value}")

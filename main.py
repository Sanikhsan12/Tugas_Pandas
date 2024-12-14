# library
import pandas as pd

# ? SOAL 1
# * membuat dataframe 
# ! Dataframe
dataframe = pd.read_csv('ikhsan\Tugas9\data_sampah.csv')
df_filter = dataframe.dropna(subset=['jumlah_produksi_sampah'])
df_filter = df_filter[['nama_kabupaten_kota', 'jumlah_produksi_sampah', 'tahun']]
def buat_dataframe():
    print('\nSOAL 1')
    print(df_filter)

# ? SOAL 2
# * hitung total sampah pada tahun tertentu
def total_sampah_tahun_tertentu(tahun):
    print(f'\nSOAL 2')
    sampah = []
    for index , value in dataframe.iterrows():
        if value['tahun'] == tahun:
            sampah.append(value['jumlah_produksi_sampah'])  
    produksi = round(sum(sampah),2)
    print(f'Total sampah pada tahun {tahun} adalah {produksi} ton/hari')

# ? SOAL 3
# * hitung total sampah per tahun
def total_sampah_per_tahun():
    print('\nSOAL 3')
    sampah = {}
    for index, value in dataframe.iterrows():
        tahun = value['tahun']
        sampah_tahun = round(value['jumlah_produksi_sampah']*365,1) # ! mengubah jumlah sampah per hari menjadi jumlah sampah per tahun

        if tahun not in sampah:
            sampah[tahun] = 0
        sampah[tahun] += sampah_tahun

    for tahun, produksi in sampah.items():
        print(f'Tahun: {tahun} , Jumlah Sampah: {round(produksi,1)} ton/tahun')

# ? SOAL 4
# * jumlahkan data per kota/kabupaten dan pertahun
def total_sampah_per_kota():
    print(f'\nSOAL 4')
    kota_data = {}

    # ! perulangan dataframe
    for key , value in df_filter.iterrows():
        kota = value['nama_kabupaten_kota']
        tahun = value['tahun']
        sampah = round(value['jumlah_produksi_sampah']*365,1)

        if tahun not in kota_data:
            kota_data[tahun] = {}
        if kota not in kota_data[tahun]:
            kota_data[tahun][kota] = 0
        kota_data[tahun][kota] += sampah

    list_data = [] 
    for tahun, data in kota_data.items():
        for kota , sampah in data.items():
            list_data.append([tahun, kota, sampah])

    # ! konversi ke csv
    df = pd.DataFrame(list_data, columns=['tahun_produksi', 'nama_kabupaten_kota', 'sampah_tahunan']) 
    df.to_csv('ikhsan\Tugas9\output.csv', index=False)

    # ! konversi ke excel
    df.to_excel('ikhsan\Tugas9\output.xlsx', index=False)

# ? main
def main():
    buat_dataframe()
    total_sampah_tahun_tertentu(2018)
    total_sampah_per_tahun()
    total_sampah_per_kota()

# ! run program
if __name__ == '__main__':
    main()
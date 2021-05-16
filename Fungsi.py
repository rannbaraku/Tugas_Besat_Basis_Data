#Modularitas yang digunakan
from os import stat_result
import mysql.connector 
from datetime import datetime
from datetime import date
from threading import Thread

#koneksi database
db = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd="",
	database="Newperpus"
)
cursor = db.cursor()


class Perpustakaan :

	#Magic methode konstroktor
	#Penerapan Overloading
	def __init__(self,id_perpustakaan,nama_perpustakaan= " ") :
		if nama_perpustakaan == None : 
			sql = """SELECT nama_perpustakaan * FROM perpustakaan WHERE id_perpustakaan = "%s" """ % (self.id_perpustakaan)
			cursor.execute(sql)
			result = cursor.fetchall()
			self.nama_perpustakaan = result
		else : self.nama_perpustakaan = nama_perpustakaan
		self.id_perpustakaan = id_perpustakaan

	#Penerapan Overriding
	#Penerapan DuckTyping
	def Identitas (self) :
		print (" \n====== Mengakses Perpustakaan terpilih ======")
		print ("     nama perpustakaan : ", self.nama_perpustakaan)
		print ("     id   perpustakaan : ", self.id_perpustakaan)
		print (" =============================================")

	def Tampil_item_perpus(self) :
		sql = """SELECT * FROM item WHERE id_perpustakaan = "%s" """ % (self.id_perpustakaan)
		cursor.execute(sql)
		result = cursor.fetchall()
		for basdat in result:
			#abstrkasi
			item_perpus=Item(basdat)
			item_perpus.Identitas()

	def Tambah_item_perpus(self) :
		data=[" "," "," "," "," "," "," "," "]
		data[0]=str(input("Masukkan ID Item  : "))
		data[1]=self.id_perpustakaan    
		data[2]=str(input("Masukan kategori Item : "))
		data[3]=str(input("Masukan judul : "))
		data[4]=str(input("Masukan penulis : "))
		data[5]=str(input("Masukan penerbit : "))
		data[6]=str(input("tahun produksi : "))
		data[7]=int(input("Salinan ke : "))
		#abstraksi
		item_tambah=Item(data)
		item_tambah.tambahItem()

	def Hapus_item_perpus(self):
		id_item=str(input("Masukkan Id Item yang akan diHapus : "))
		sql = """SELECT * FROM item WHERE id_perpustakaan= "%s" and id_item = "%s" """ % (self.id_perpustakaan,id_item)
		cursor.execute(sql)
		result = cursor.fetchall()
		count = 0
		for item_cari in result:
			#abstrakasi
			item_hapus=Item(item_cari)
			item_hapus.hapusItem()
			count += 1

		if (count == 0):
			print ("Data Tidak ada")
	
	def Ubah_item_perpus(self):
		id_item=str(input("Masukkan Id Item yang akan diubah : "))
		sql = """SELECT * FROM item WHERE id_perpustakaan= "%s" and id_item = "%s" """ % (self.id_perpustakaan,id_item)
		cursor.execute(sql)
		result = cursor.fetchall()
		count = 0
		for item_cari in result:
			#abstraksi
			item_ubah=Item(item_cari)
			item_ubah.ubahItem()
			count += 1

		if (count == 0):
			print ("Data Tidak ada")

#Penerapan Inhitence		
class Item (Perpustakaan) :

	#Magic Method Konstruktor
	def __init__(self,data_item)	:
		#Akses Inhiritence
		super().__init__(data_item[1])
		self.id_item=data_item[0]
		self.id_perpustakaan=data_item[1]
		self.kategori=data_item[2]
		self.judul=data_item[3]
		self.penulis=data_item[4]
		self.penerbit=data_item[5]
		self.tahun_produksi=data_item[6]
		self.salinan=data_item[7]

	#Penerapan overridding
	#Penerapan Ducktyping
	def Identitas(self) :
		print("Id Buku         : ",self.id_item)
		print("Id Perpustakaan : ",self.id_perpustakaan)
		print("Kategori        : ",self.kategori)
		print("Judul           : ",self.judul)
		print("Penulis         : ",self.penulis)
		print("Penerbit        : ",self.penerbit)
		print("Tahun Produksi  : ",self.tahun_produksi)
		print("Salinan         : ",self.salinan,"\n")

	def tambahItem(self) :
		sql = "INSERT INTO item (id_item, id_perpustakaan, kategori, judul, penulis, penerbit, tahun_produksi, salinan) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
		val = (self.id_item,self.id_perpustakaan,self.kategori,self.judul,self.penulis,self.penerbit,self.tahun_produksi,self.salinan)
		cursor.execute(sql,val)
		db.commit()
		print("Berhasil Disimpan")

	def hapusItem(self) :
		sql = """DELETE FROM item WHERE id_perpustakaan = "%s" and id_item = "%s" """ % (self.id_perpustakaan,self.id_item)
		cursor.execute(sql)
		db.commit()
		print("Data Berhasil dihapus")
	
	def ubahItem(self) :
		print("Perubahan Data Buku")
		print("1. Id Buku")
		print("2. Id Perpustakaan")
		print("3. Kategori")
		print("4. Judul")
		print("5. Penulis")
		print("6. Penerbit")
		print("7. Tahun Produksi")
		print("8. Salinan")
		pilihan=int(input("Masukkan Pilihan : "))
		if(pilihan==1) :
			id_baru=str(input("Masukkan Id baru Buku : "))
			sql = """UPDATE item SET id_item="%s" WHERE id_item ="%s" """ % (id_baru, self.id_item)
			cursor.execute(sql)
			db.commit()
			print("Data Berhasil Diubah")
		elif(pilihan==2) :
			id_baru=str(input("Masukkan Id baru Perpustakaan : "))
			sql = """UPDATE item SET id_perpustakaan="%s" WHERE id_item ="%s" """ % (id_baru, self.id_item)
			cursor.execute(sql)
			db.commit()
			print("Data Berhasil Diubah")
		elif(pilihan==3) :
			kategori_baru=str(input("Masukkan Kategori baru Buku : "))
			sql = """UPDATE item SET kategori="%s" WHERE id_item ="%s" """ % (kategori_baru, self.id_item)
			cursor.execute(sql)
			db.commit()
			print("Data Berhasil Diubah")
		elif(pilihan==4) :
			judul_baru=str(input("Masukkan Judul baru Buku : "))
			sql = """UPDATE item SET judul="%s" WHERE id_item ="%s" """ % (judul_baru, self.id_item)
			cursor.execute(sql)
			db.commit()
			print("Data Berhasil Diubah")
		elif(pilihan==5) :
			penulis_baru=str(input("Masukkan Penulis baru Buku : "))
			sql = """UPDATE item SET penulis="%s" WHERE id_item ="%s" """ % (penulis_baru, self.id_item)
			cursor.execute(sql)
			db.commit()
			print("Data Berhasil Diubah")
		elif(pilihan==6) :
			penerbit_baru=str(input("Masukkan Penerbit baru Buku : "))
			sql = """UPDATE item SET penerbit="%s" WHERE id_item ="%s" """ % (penerbit_baru, self.id_item)
			cursor.execute(sql)
			db.commit()
			print("Data Berhasil Diubah")
		elif(pilihan==7) :
			tahun_baru=int(input("Masukkan Tahun Produksi baru Buku : "))
			sql = """UPDATE item SET tahun_produksi="%s" WHERE id_item ="%s" """ % (tahun_baru, self.id_item)
			cursor.execute(sql)
			db.commit()
			print("Data Berhasil Diubah")
		elif(pilihan==8) :
			salinan_baru=int(input("Masukkan Id baru Buku : "))
			sql = """UPDATE item SET salinan="%s" WHERE id_item ="%s" """ % (salinan_baru, self.id_item)
			cursor.execute(sql)
			db.commit()
			print("Data Berhasil Diubah")	

class Pelanggan :

	#Magic Methode Konstruktor
	#Penerapan Enkapsulasi
	def __init__(self,data_pelanggan):
		self.id_pelanggan=data_pelanggan[0]
		self.type=data_pelanggan[1]
		self.nama=data_pelanggan[2]
		self.alamat=data_pelanggan[3]
		self.no_hp=data_pelanggan[4]
		self.email=data_pelanggan[5]
		#Penerapan Enkapsulasi
		self.__pengenal = 0

	#Penerapan Ducktyping
	def Identitas(self) :
		print("Id Pelanggan : ",self.id_pelanggan)
		print("Type         : ",self.type)
		print("Nama         : ",self.nama)
		print("Alamat       : ",self.alamat)
		print("No. Hp       : ",self.no_hp)
		print("E-mail       : ",self.email,"\n")

	def tambahPelanggan(self) :
		sql = "INSERT INTO pelanggan (id_pelanggan, type, nama, alamat, no_hp, email) VALUES (%s,%s,%s,%s,%s,%s)"
		val = (self.id_pelanggan,self.type,self.nama,self.alamat,self.no_hp,self.email)
		cursor.execute(sql,val)
		db.commit()
		print("Berhasil Disimpan")

	def hapusPelanggan(self) :
		sql = """DELETE FROM pelanggan WHERE id_pelanggan = "%s" """ % (self.id_pelanggan)
		cursor.execute(sql)
		db.commit()
		print("Data Berhasil dihapus")
	
	#Penerapan Enkapsulasi
	def ujiPelangan (self,idP):
		print("id pelanggan : ", idP)
		sql = """SELECT nama,type FROM pelanggan WHERE id_pelanggan = "%s" """ % (idP)
		cursor.execute(sql)
		result = cursor.fetchall()
		#Penerapan enkapsulasi
		self.__pengenal = result[0]
	
	#Penerapan metode Getter
	def getnama(self) :
		return self.__pengenal[0]
	
	#Penerapan metode Getter
	def gettype(self) :
		return self.__pengenal[1]	

	def dendaPelanggan(self, tipe, waktu) :
		if tipe == "Gold" or tipe == "gold":
			if waktu >90 :
				denda = 1000*(waktu-90)
				print("Waktu peminjaman melebihi ketentuan selama : ", waktu-90," hari")
				return denda
			else : 
				print("Pengembalian dilakukan tepat waktu")
				return 0

		else :
			if waktu >21 :
				denda = 1000*(waktu-21)
				print("Waktu peminjaman melebihi ketentuan selama : ", waktu-21," hari")
				return denda
			else : 
				print("Pengembalian dilakukan tepat waktu")
				return 0

	def UbahPelanggan(self) :
		print("Perubahan Data Pelanggan")
		print("1. Id Pelanggan")
		print("2. Type")
		print("3. Nama")
		print("4. Alamat")
		print("5. No. Hp")
		print("6. E-mail")
		pilihan=int(input("Masukkan Pilihan : "))
		if(pilihan==1) :
			id_baru=str(input("Masukkan Id baru Pelanggan : "))
			sql = """UPDATE pelanggan SET id_pelanggan="%s" WHERE id_pelanggan ="%s" """ % (id_baru, self.id_pelanggan)
			cursor.execute(sql)
			db.commit()
			print("Data Berhasil Diubah")
		elif(pilihan==2) :
			type_baru=str(input("Masukkan Type baru Pelanggan : "))
			sql = """UPDATE pelanggan SET type="%s" WHERE id_pelanggan ="%s" """ % (type_baru, self.id_pelanggan)
			cursor.execute(sql)
			db.commit()
			print("Data Berhasil Diubah")
		elif(pilihan==3) :
			nama_baru=str(input("Masukkan Nama baru Pelanggan : "))
			sql = """UPDATE pelanggan SET nama="%s" WHERE id_pelanggan ="%s" """ % (nama_baru, self.id_pelanggan)
			cursor.execute(sql)
			db.commit()
		elif(pilihan==4) :
			alamat_baru=str(input("Masukkan Alamat baru Pelanggan : "))
			sql = """UPDATE pelanggan SET alamat="%s" WHERE id_pelanggan ="%s" """ % (alamat_baru, self.id_pelanggan)
			cursor.execute(sql)
			db.commit()
			print("Data Berhasil Diubah")
		elif(pilihan==5) :
			no_hp_baru=str(input("Masukkan No. Hp baru Pelanggan : "))
			sql = """UPDATE pelanggan SET no_hp="%s" WHERE id_pelanggan ="%s" """ % (no_hp_baru, self.id_pelanggan)
			cursor.execute(sql)
			db.commit()
			print("Data Berhasil Diubah")
		elif(pilihan==6) :
			email_baru=str(input("Masukkan E-mail baru Pelanggan : "))
			sql = """UPDATE pelanggan SET email="%s" WHERE id_pelanggan ="%s" """ % (email_baru, self.id_pelanggan)
			cursor.execute(sql)
			db.commit()
			print("Data Berhasil Diubah")

#Penerapan Inhiritance
class Peminjaman(Pelanggan):
	
	#penerapan magic methode konstruktor
	def __init__(self,data) :
		#Penerapan Inhiritance
		super().__init__(data)
		self.id_pelanggan=data[0]
		self.tanggal_peminjaman=data[1]
		self.id_item=data[2]
		self.tanggal_pengembalian=data[3]
		self.biaya=data[4]
		self.status=data[5]
		self.lamawaktu = 1

	#Penerapan Magic methode __str__
	def __str__(self) : return(""" 
ID Pelanggan         : {}
Tanggal Peminjaman   : {}
ID Item              : {}
anggal Pengembalian  : {}
Biaya                : {}
Status               : {} """).format(self.id_pelanggan,self.tanggal_peminjaman,self.id_item, self.tanggal_pengembalian,self.biaya, self.status)

	def tambahPeminjam(self) :
		sql = "INSERT INTO peminjaman (id_pelanggan, tanggal_peminjaman, id_item, tanggal_pengembalian, biaya, Status) VALUES (%s,%s,%s,%s,%s,%s)"
		val = (self.id_pelanggan,self.tanggal_peminjaman,self.id_item,self.tanggal_pengembalian,self.biaya,self.status)
		cursor.execute(sql,val)
		db.commit()
		print("Berhasil Disimpan")
		
	def hapusPeminjam(self):
		sql = """DELETE FROM peminjaman WHERE id_pelanggan = "%s" """ % (self.id_pelanggan)
		cursor.execute(sql)
		db.commit()
		print("Data Berhasil dihapus")

	def lamapinjam (self):
		sql = """SELECT DATEDIFF("%s", "%s") """ % (self.tanggal_pengembalian,self.tanggal_peminjaman)
		cursor.execute(sql)
		result = cursor.fetchall()
		oper = (" ".join(map(str, result[0])))		
		self.lamawaktu = int(oper)

	def mengembalikanPeminjam(self):
		print("\n======Melakukan pengembalian Item====== \n")
		self.tanggal_pengembalian = str(input("Mengembalikan pada tanggal : "))

		#Penerapn Konkurensi (Threading)
		t1 = Thread(target = self.lamapinjam())
		t2 = Thread(target = super().ujiPelangan(self.id_pelanggan))
	
		t1.start()
		t2.start()
		t1.join()
		t2.join()

		#Penerapan fungsi getter
		nama = super().getnama()
		tipe = super().gettype()
		print("Peminjam atas nama   : ",nama)
		print("dengan tipe          : ", tipe) 
		sql = """UPDATE `peminjaman` SET `tanggal_pengembalian` = "%s" WHERE `peminjaman`.`id_item` = "%s" AND Status = "Dipinjam" """ % (self.tanggal_pengembalian,self.id_item)
		cursor.execute(sql)
		db.commit()

		print ("dengan masa peminjaman : ", self.lamawaktu," hari")
		self.status = str("Dikembalikan")
		
		#inhiritence 
		#abstraksi
		self.biaya	= super().dendaPelanggan(tipe,self.lamawaktu)

		sql = """UPDATE `peminjaman` SET `biaya` = "%s" WHERE `peminjaman`.`id_item` = "%s"   AND Status = "Dipinjam" """ % (self.biaya,self.id_item)
		cursor.execute(sql)
		db.commit()

		sql = """UPDATE `peminjaman` SET `Status` = "%s" WHERE `peminjaman`.`id_item` = "%s"  AND Status = "Dipinjam" """ % (self.status,self.id_item)
		cursor.execute(sql)
		db.commit()

		print("\nPengembalian sukses dengan denda : Rp.", self.biaya)
		print("mengikuti ketentuan perpustakaan Rp.1000/hari keterlambatan")

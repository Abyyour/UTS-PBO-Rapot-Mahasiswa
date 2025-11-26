from app.model import RapotModel
from app.view import RapotView
from tkinter import messagebox

class RapotController:
    def __init__(self):
        self.model = RapotModel()
        self.view = RapotView(self)
        self.load_initial()
        self.view.mainloop()

    # ===================== LOAD AWAL =====================
    def load_initial(self):
        rows = self.model.fetch_all()
        self.view.refresh_table(rows)

        # AMBIL ANGKATAN DARI 2 DIGIT DEPAN NIM
        angkatan = sorted({r["nim"][:2] for r in rows})
        prodi = sorted({r["prodi"] for r in rows})
        matkul = sorted({r["matkul"] for r in rows})

        self.view.update_filter_options(angkatan, prodi, matkul)


    # ===================== FILTER =====================
    def apply_filters(self):
        rows = self.model.fetch_all()

        f_id = self.view.filter_id.get()
        f_prodi = self.view.filter_prodi.get()
        f_matkul = self.view.filter_matkul.get()

        # FILTER ANGKATAN → 2 DIGIT DEPAN NIM
        if f_id != "Semua":
            rows = [r for r in rows if r["nim"][:2] == f_id]

        # FILTER PRODI
        if f_prodi != "Semua":
            rows = [r for r in rows if r["prodi"] == f_prodi]

        # FILTER MATKUL
        if f_matkul != "Semua":
            rows = [r for r in rows if r["matkul"] == f_matkul]

        self.view.refresh_table(rows)


    # ===================== CRUD =====================
    def create_record(self, nim, nama, prodi, matkul, nilai):
        ok, msg = self.model.create(nim, nama, prodi, matkul, nilai)
        if ok:
            messagebox.showinfo("Sukses", "Data berhasil ditambahkan!")
            self.reload()
        else:
            messagebox.showerror("Gagal", msg)

    def update_record(self, id_, nim, nama, prodi, matkul, nilai):
        ok, msg = self.model.update(id_, nim, nama, prodi, matkul, nilai)
        if ok:
            messagebox.showinfo("Sukses", "Data berhasil diperbarui!")
            self.reload()
        else:
            messagebox.showerror("Gagal", msg)

    def delete_record(self, id_):
        ok, msg = self.model.delete(id_)
        if ok:
            messagebox.showinfo("Sukses", "Data berhasil dihapus!")
            self.reload()
        else:
            messagebox.showerror("Gagal", msg)

    # ===================== UTIL =====================
    def reload(self):
        self.load_initial()

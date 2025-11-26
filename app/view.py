import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox

class RapotView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Aplikasi Rapot Mahasiswa - Abil")
        self.geometry("1000x550")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # ========== FRAME INPUT KIRI ==========
        frame_left = ctk.CTkFrame(self, width=220)
        frame_left.pack(side="left", fill="y", padx=12, pady=12)

        ctk.CTkLabel(frame_left, text="Input Data", font=("Sans", 16)).pack(pady=(0,8))

        self.entry_nim = ctk.CTkEntry(frame_left, placeholder_text="NIM")
        self.entry_nim.pack(pady=6, fill="x")

        self.entry_nama = ctk.CTkEntry(frame_left, placeholder_text="Nama Lengkap")
        self.entry_nama.pack(pady=6, fill="x")

        self.entry_prodi = ctk.CTkComboBox(
            frame_left,
            values=["Informatika", "Akutansi", "Farmasi"],
            state="readonly"
        )
        self.entry_prodi.set("Informatika")
        self.entry_prodi.pack(pady=6, fill="x")

        self.entry_matkul = ctk.CTkComboBox(
            frame_left,
            values=["Bahasa Indonesia", "Desain & Pemrograman Visual", "Aswaja"],
            state="readonly"
        )
        self.entry_matkul.set("Bahasa Indonesia")
        self.entry_matkul.pack(pady=6, fill="x")

        self.entry_nilai = ctk.CTkEntry(frame_left, placeholder_text="Nilai Angka (0-100)")
        self.entry_nilai.pack(pady=6, fill="x")

        ctk.CTkButton(frame_left, text="Tambah Data", command=self._on_add).pack(pady=6, fill="x")
        ctk.CTkButton(frame_left, text="Update Data", command=self._on_update).pack(pady=6, fill="x")
        ctk.CTkButton(frame_left, text="Hapus Data", command=self._on_delete).pack(pady=6, fill="x")
        ctk.CTkButton(frame_left, text="Bersihkan", command=self.clear_inputs).pack(pady=6, fill="x")

        # ========== FRAME KANAN (FILTER + TABEL) ==========
        frame_right = ctk.CTkFrame(self)
        frame_right.pack(side="right", fill="both", expand=True, padx=12, pady=12)

        # ========== FRAME FILTER ==========
        filter_frame = ctk.CTkFrame(frame_right)
        filter_frame.pack(fill="x", pady=(0,10))

        # FILTER ANGKATAN
        ctk.CTkLabel(filter_frame, text="Filter Angkatan:").grid(row=0, column=0, padx=5)
        self.filter_id = ctk.CTkComboBox(
            filter_frame, values=["Semua"], state="readonly",
            command=self._on_filter_change
        )
        self.filter_id.set("Semua")
        self.filter_id.grid(row=0, column=1, padx=5)

        # FILTER PRODI
        ctk.CTkLabel(filter_frame, text="Filter Prodi:").grid(row=0, column=2, padx=5)
        self.filter_prodi = ctk.CTkComboBox(
            filter_frame, values=["Semua"], state="readonly",
            command=self._on_filter_prodi_change
        )
        self.filter_prodi.set("Semua")
        self.filter_prodi.grid(row=0, column=3, padx=5)

        # FILTER MATA KULIAH
        ctk.CTkLabel(filter_frame, text="Filter Matkul:").grid(row=0, column=4, padx=5)
        self.filter_matkul = ctk.CTkComboBox(
            filter_frame, values=["Semua"], state="readonly",
            command=self._on_filter_matkul_change
        )
        self.filter_matkul.set("Semua")
        self.filter_matkul.grid(row=0, column=5, padx=5)

        # ========== TABEL ==========

        cols = ("id", "nim", "nama", "prodi", "matkul", "nilai_angka", "nilai_huruf")
        self.tree = ttk.Treeview(frame_right, columns=cols, show="headings", height=18)

        for c in cols:
            self.tree.heading(c, text=c.upper())
            if c in ("nama", "prodi", "matkul"):
                self.tree.column(c, width=150, anchor="w")
            else:
                self.tree.column(c, width=80, anchor="center")

        self.tree.pack(fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_right, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.tree.bind("<<TreeviewSelect>>", self._on_select)

    # ===================== EVENT HANDLERS =====================

    def _on_add(self):
        nim = self.entry_nim.get().strip()
        nama = self.entry_nama.get().strip()
        prodi = self.entry_prodi.get().strip()
        matkul = self.entry_matkul.get().strip()

        try:
            nilai = int(self.entry_nilai.get().strip())
        except:
            messagebox.showerror("Error", "Nilai harus angka!")
            return

        self.controller.create_record(nim, nama, prodi, matkul, nilai)

    def _on_update(self):
        selected = self._selected_id()
        if selected is None:
            messagebox.showwarning("Pilih baris", "Pilih baris yang mau diperbarui.")
            return

        nim = self.entry_nim.get().strip()
        nama = self.entry_nama.get().strip()
        prodi = self.entry_prodi.get().strip()
        matkul = self.entry_matkul.get().strip()

        try:
            nilai = int(self.entry_nilai.get().strip())
        except:
            messagebox.showerror("Error", "Nilai harus angka!")
            return

        self.controller.update_record(selected, nim, nama, prodi, matkul, nilai)

    def _on_delete(self):
        selected = self._selected_id()
        if selected is None:
            messagebox.showwarning("Pilih baris", "Tidak ada data yang dipilih.")
            return

        if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data ini?"):
            self.controller.delete_record(selected)

    def _on_select(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        values = self.tree.item(sel[0], "values")

        self.entry_nim.delete(0, tk.END); self.entry_nim.insert(0, values[1])
        self.entry_nama.delete(0, tk.END); self.entry_nama.insert(0, values[2])
        self.entry_prodi.set(values[3])
        self.entry_matkul.set(values[4])
        self.entry_nilai.delete(0, tk.END); self.entry_nilai.insert(0, values[5])

    # ===================== FILTER EVENT =====================

    def _on_filter_change(self, choice):
        self.controller.apply_filters()

    def _on_filter_prodi_change(self, choice):
        self.controller.apply_filters()

    def _on_filter_matkul_change(self, choice):
        self.controller.apply_filters()

    # ===================== UTIL =====================

    def clear_inputs(self):
        self.entry_nim.delete(0, "end")
        self.entry_nama.delete(0, "end")
        self.entry_prodi.set("")
        self.entry_matkul.set("")
        self.entry_nilai.delete(0, "end")

    def _selected_id(self):
        sel = self.tree.selection()
        if not sel:
            return None
        return int(self.tree.item(sel[0], "values")[0])

    def refresh_table(self, rows):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for r in rows:
            self.tree.insert("", "end", values=(
                r['id'], r['nim'], r['nama'], r['prodi'],
                r['matkul'], r['nilai_angka'], r['nilai_huruf']
            ))

    def update_filter_options(self, angkatan_list, prodi_list, matkul_list):
        self.filter_id.configure(values=["Semua"] + angkatan_list)
        self.filter_prodi.configure(values=["Semua"] + prodi_list)
        self.filter_matkul.configure(values=["Semua"] + matkul_list)

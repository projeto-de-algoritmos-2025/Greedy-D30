import tkinter as tk
from tkinter import filedialog, messagebox
import os


class App():
    def __init__(self, root):
        self.root = root
        self.root.title("Interface Huffman - Compactador")
        self.root.resizable(False, False)

        frame = tk.Frame(self.root, padx=12, pady=12)
        frame.pack()

        btn_compress = tk.Button(frame, text="Compactar", width=12, command=self.compress)
        btn_decompress = tk.Button(frame, text="Descompactar", width=12, state='disabled', command=self.decompress)
        btn_exit = tk.Button(frame, text="Sair", width=12, command=self.root.destroy)

        btn_compress.grid(row=0, column=0, padx=5, pady=5)
        btn_decompress.grid(row=0, column=1, padx=5, pady=5)
        btn_exit.grid(row=0, column=2, padx=5, pady=5)


    def compress(self):
        filepath = filedialog.askopenfilename(
            title="Selecione um arquivo de texto (plain text)",
            filetypes=[("All files", "*.*")]
        )
        if not filepath:
            return

        try:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(filepath, 'r', encoding='latin-1') as f:
                    content = f.read()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível ler o arquivo:\n{e}")
            return

        base, _ = os.path.splitext(filepath)
        outpath = base + "_converted.txt"

        if os.path.exists(outpath):
            resp = messagebox.askyesno("Sobrescrever?", f"O arquivo {os.path.basename(outpath)} já existe. Sobrescrever?")
            if not resp:
                outpath = filedialog.asksaveasfilename(
                    defaultextension=".txt",
                    initialfile=os.path.basename(base + "_converted.txt"),
                    title="Salvar como",
                    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
                )
                if not outpath:
                    return

        try:
            with open(outpath, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar o arquivo:\n{e}")
            return

        messagebox.showinfo("Pronto", f"Conteúdo salvo em:\n{outpath}")


    def decompress(self):
        pass
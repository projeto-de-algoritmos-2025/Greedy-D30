from src.huffman import char_count
import tkinter as tk
import os


class App():
    def __init__(self, root):
        self.root = root
        self.root.title("Compactador de Textos - Huffman")
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

        # Select file
        filepath = self.open_file()
        if not filepath:
            return

        # Read file
        try:
            content = self.read_file(filepath)
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Não foi possível ler o arquivo:\n{e}")
            return

        # Take output file path
        outpath = self.outpath(filepath, "compressed/")
        if not outpath:
            return
        #print(f"{outpath}") # Debug

        # Count unique chars
        chars = char_count(content)

        # Save file
        if not self.save_file(outpath, content):
            return

        tk.messagebox.showinfo("Compressão Finalizada", f"Conteúdo salvo em:\n{outpath}")


    def decompress(self):
        pass


    def open_file(self):
        return tk.filedialog.askopenfilename(
            title="Selecione um arquivo de texto (plain text)",
            filetypes=[("All files", "*.*")]
        )
    

    def read_file(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            with open(filepath, 'r', encoding='latin-1') as f:
                return f.read()
    

    def save_file(self, outpath, content):
        try:
            with open(outpath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Não foi possível salvar o arquivo:\n{e}")
            return


    def outpath(self, filepath, outfolder):
        os.makedirs(outfolder, exist_ok=True)
        filename = os.path.basename(filepath)

        base, ext = os.path.splitext(filename)
        outpath = outfolder + base + "_cmprssd.txt"

        if not os.path.exists(outpath):
            return outpath
        else:
            resp = tk.messagebox.askyesno("Sobrescrever?", f"O arquivo {os.path.basename(outpath)} já existe. Sobrescrever?")
            if not resp:
                outpath = tk.filedialog.asksaveasfilename(
                    defaultextension=".txt",
                    initialfile=os.path.basename(base + "_cmprssd.txt"),
                    initialdir=outfolder,
                    title="Salvar como",
                    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
                )
                if not outpath:
                    return
            return outpath
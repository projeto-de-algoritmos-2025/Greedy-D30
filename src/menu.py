from src.huffman import char_count, prefix_tree, prefix_codes
from tkinter import filedialog, messagebox
import tkinter as tk
import json
import os


class App():
    def __init__(self, root):
        self.root = root
        self.root.title("Compactador de Textos - Huffman")
        self.root.resizable(False, False)
        self.header_bool = tk.BooleanVar()

        frame = tk.Frame(self.root, padx=32, pady=8)
        frame.pack()

        title = tk.Label(frame, text="Compressor de\nHuffman", font='sylfaen')
        btn_compress = tk.Button(frame, text="Compactar", width=12, command=self.compress)
        btn_decompress = tk.Button(frame, text="Descompactar", width=12, state='disabled', command=self.decompress)
        btn_exit = tk.Button(frame, text="Sair", width=12, command=self.root.destroy)
        checkbox = tk.Checkbutton(frame, text="Printar Header", variable=self.header_bool)

        title.grid(row=0, column=1, padx=0, pady=(0, 16))
        btn_compress.grid(row=1, column=1, padx=5, pady=5)
        btn_decompress.grid(row=2, column=1, padx=5, pady=5)
        btn_exit.grid(row=3, column=1, padx=5, pady=5)
        checkbox.grid(row=4, column=1, padx=5, pady=(16, 0))


    def compress(self):

        # Select file
        filepath = self.open_file()
        if not filepath:
            return

        # Read file
        try:
            content = self.read_file(filepath)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível ler o arquivo:\n{e}")
            return

        # Take output file path
        outpath = self.outpath(filepath, "compressed/")
        if not outpath:
            return
        #print(f"{outpath}") # Debug

        # Prefix codes
        chars = char_count(content)
        n, tree = prefix_tree(chars)
        prefix = prefix_codes(tree)

        # Header
        _, ext = os.path.splitext(filepath)
        header = {
            'header_length': 0,
            'string_length': n,
            'extension': ext,
            'prefix_codes': prefix
        }

        # Serializar o Header
        header_bytes = json.dumps(header).encode('utf-8') # Serializa cada caracter do dicionário como um byte
        header["header_length"] = len(header_bytes)-1 # Salva a quantidade de bytes do header
        bytes_number = len(str(header["header_length"])) # Quantidade de bytes da quantidade de bytes do header
        if(len(str((bytes_number + header["header_length"]))) > bytes_number): # Se haverá aumento de 1 byte
            header["header_length"] += bytes_number + 1
        else:
            header["header_length"] += bytes_number
        size_bytes = json.dumps(header["header_length"]).encode('utf-8') # Serializa o tamanho do header
        header_bytes = b'{"header_length": ' + size_bytes + header_bytes[19:] # Dicionário serializado, com seu próprio tamanho
        
        # Visualizar o Header
        if(self.header_bool.get()):
            print('-'*100)
            for key, value in header.items():
                print(f'{key}: {value};')
            print('-'*100)

        # Save file
        if not self.save_file(outpath, header_bytes, content):
            return

        messagebox.showinfo("Compressão Finalizada", f"Conteúdo salvo em:\n{outpath}")


    def decompress(self):
        pass


    def open_file(self):
        return filedialog.askopenfilename(
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
    

    def save_file(self, outpath, header, content):
        try:
            with open(outpath, 'wb') as f:
                f.write(header)
            return True
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar o arquivo:\n{e}")
            return


    def outpath(self, filepath, outfolder):
        os.makedirs(outfolder, exist_ok=True)
        filename = os.path.basename(filepath)

        base, ext = os.path.splitext(filename)
        outpath = outfolder + base + "_cmprssd.huff"

        if not os.path.exists(outpath):
            return outpath
        else:
            resp = messagebox.askyesno("Sobrescrever?", f"O arquivo {os.path.basename(outpath)} já existe. Sobrescrever?")
            if not resp:
                outpath = filedialog.asksaveasfilename(
                    defaultextension=".txt",
                    initialfile=os.path.basename(base + "_cmprssd.txt"),
                    initialdir=outfolder,
                    title="Salvar como",
                    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
                )
                if not outpath:
                    return
            return outpath
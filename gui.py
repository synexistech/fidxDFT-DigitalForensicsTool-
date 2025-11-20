import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import threading

# Import modules
from dft.modules.hashcalc import calculate_hashes
from dft.modules.exif_extractor import extract_exif
from dft.modules.pcap_analyzer import analyze_pcap, export_pcap_csv
from dft.modules.browser_history import parse_browser_history, export_history_csv
from dft.modules.file_carver import carve_files
from dft.modules.timeline import generate_timeline
from dft.utils.logger import logger

# Color Palette (Cyber Red)
COLORS = {
    "bg_dark": "#121212",       # Very dark background
    "bg_panel": "#1e1e1e",      # Panel background
    "fg_text": "#e0e0e0",       # Light grey text
    "accent": "#d32f2f",        # Red accent
    "accent_hover": "#b71c1c",  # Darker red for hover
    "success": "#388e3c",       # Green for success
    "warning": "#fbc02d",       # Yellow for warning
    "border": "#333333"         # Border color
}

class DFTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FidxDFT-Toolkit v1 (Digital ForensicsTool)")
        self.root.geometry("1000x700")
        self.root.configure(bg=COLORS["bg_dark"])
        
        # Configure Styles
        self.setup_styles()
        
        # Main Container
        main_frame = tk.Frame(root, bg=COLORS["bg_dark"])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Header
        header_frame = tk.Frame(main_frame, bg=COLORS["bg_dark"])
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        title_label = tk.Label(
            header_frame, 
            text="FidxDFT-Toolkit v1 (Digital ForensicsTool)", 
            font=("Segoe UI", 18, "bold"), 
            bg=COLORS["bg_dark"], 
            fg=COLORS["accent"]
        )
        title_label.pack(side=tk.LEFT)
        
        version_label = tk.Label(
            header_frame, 
            text="v1.0 | EDUCATIONAL USE ONLY", 
            font=("Segoe UI", 10), 
            bg=COLORS["bg_dark"], 
            fg="#757575"
        )
        version_label.pack(side=tk.RIGHT, anchor="s", pady=5)

        # Tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(expand=True, fill='both')
        
        # Initialize tabs
        self.init_hash_tab()
        self.init_exif_tab()
        self.init_pcap_tab()
        self.init_browser_tab()
        self.init_carver_tab()
        self.init_timeline_tab()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("System Ready")
        self.status_bar = tk.Label(
            root, 
            textvariable=self.status_var, 
            bg=COLORS["accent"], 
            fg="white", 
            font=("Segoe UI", 9, "bold"),
            anchor=tk.W,
            padx=10,
            pady=2
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Notebook (Tabs)
        style.configure("TNotebook", background=COLORS["bg_dark"], borderwidth=0)
        style.configure("TNotebook.Tab", 
            background=COLORS["bg_panel"], 
            foreground=COLORS["fg_text"], 
            padding=[15, 5], 
            font=("Segoe UI", 10)
        )
        style.map("TNotebook.Tab", 
            background=[("selected", COLORS["accent"])],
            foreground=[("selected", "white")]
        )
        
        # Frames
        style.configure("TFrame", background=COLORS["bg_panel"])
        style.configure("TLabelframe", background=COLORS["bg_panel"], foreground=COLORS["accent"], bordercolor=COLORS["border"])
        style.configure("TLabelframe.Label", background=COLORS["bg_panel"], foreground=COLORS["accent"], font=("Segoe UI", 11, "bold"))
        
        # Buttons
        style.configure("TButton", 
            background=COLORS["bg_panel"], 
            foreground=COLORS["fg_text"], 
            borderwidth=1, 
            font=("Segoe UI", 10),
            focuscolor=COLORS["accent"]
        )
        style.map("TButton", 
            background=[("active", COLORS["accent"]), ("disabled", COLORS["bg_dark"])], 
            foreground=[("active", "white")]
        )
        
        # Accent Button Style
        style.configure("Accent.TButton", 
            background=COLORS["accent"], 
            foreground="white", 
            font=("Segoe UI", 10, "bold")
        )
        style.map("Accent.TButton", 
            background=[("active", COLORS["accent_hover"])]
        )

    def create_scrolled_text(self, parent):
        st = scrolledtext.ScrolledText(
            parent, 
            height=15, 
            bg="#252526", 
            fg="#d4d4d4", 
            insertbackground="white",
            font=("Consolas", 10),
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        st.pack(padx=10, pady=10, fill='both', expand=True)
        return st

    def log(self, message):
        self.status_var.set(f"STATUS: {message}")
        logger.info(message)

    def init_hash_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="HASH")
        
        frame = ttk.LabelFrame(tab, text=" FILE INTEGRITY CHECK ")
        frame.pack(padx=15, pady=15, fill='x')
        
        desc = tk.Label(frame, text="Calculate MD5, SHA1, and SHA256 hashes.", bg=COLORS["bg_panel"], fg=COLORS["fg_text"])
        desc.pack(anchor="w", padx=10, pady=(5,0))

        btn = ttk.Button(frame, text="SELECT FILE", style="Accent.TButton", command=self.run_hash)
        btn.pack(anchor="w", padx=10, pady=10)
        
        self.hash_output = self.create_scrolled_text(tab)

    def run_hash(self):
        filepath = filedialog.askopenfilename()
        if not filepath:
            return
        
        self.log(f"Calculating hashes for {os.path.basename(filepath)}...")
        self.hash_output.delete(1.0, tk.END)
        
        def task():
            hashes = calculate_hashes(filepath)
            if hashes:
                out = f"FILE: {filepath}\n"
                out += "-" * 60 + "\n"
                for algo, val in hashes.items():
                    out += f"{algo.upper():<10}: {val}\n"
                self.update_text(self.hash_output, out)
                self.log("Hash calculation complete.")
            else:
                self.update_text(self.hash_output, "Error calculating hashes.")
                self.log("Error calculating hashes.")

        threading.Thread(target=task).start()

    def init_exif_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="EXIF")
        
        frame = ttk.LabelFrame(tab, text=" METADATA EXTRACTION ")
        frame.pack(padx=15, pady=15, fill='x')
        
        btn = ttk.Button(frame, text="LOAD IMAGE", style="Accent.TButton", command=self.run_exif)
        btn.pack(anchor="w", padx=10, pady=10)
        
        self.exif_output = self.create_scrolled_text(tab)

    def run_exif(self):
        filepath = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.jpeg *.png *.tiff")])
        if not filepath:
            return
            
        self.log(f"Extracting EXIF for {os.path.basename(filepath)}...")
        self.exif_output.delete(1.0, tk.END)
        
        def task():
            data = extract_exif(filepath)
            if data is not None:
                if not data:
                    out = "No EXIF data found."
                else:
                    out = f"FILE: {filepath}\n"
                    out += "-" * 60 + "\n"
                    for k, v in data.items():
                        out += f"{k:<25}: {v}\n"
                self.update_text(self.exif_output, out)
                self.log("EXIF extraction complete.")
            else:
                self.update_text(self.exif_output, "Error extracting EXIF.")
                self.log("Error extracting EXIF.")
                
        threading.Thread(target=task).start()

    def init_pcap_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="PCAP")
        
        frame = ttk.LabelFrame(tab, text=" NETWORK ANALYSIS ")
        frame.pack(padx=15, pady=15, fill='x')
        
        btn_frame = tk.Frame(frame, bg=COLORS["bg_panel"])
        btn_frame.pack(anchor="w", padx=10, pady=10)

        btn = ttk.Button(btn_frame, text="LOAD PCAP", style="Accent.TButton", command=self.run_pcap)
        btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.btn_pcap_export = ttk.Button(btn_frame, text="EXPORT CSV", state=tk.DISABLED, command=self.export_pcap)
        self.btn_pcap_export.pack(side=tk.LEFT)
        
        self.pcap_output = self.create_scrolled_text(tab)
        self.current_pcap_stats = None

    def run_pcap(self):
        filepath = filedialog.askopenfilename(filetypes=[("PCAP Files", "*.pcap *.pcapng *.cap")])
        if not filepath:
            return
            
        self.log(f"Analyzing {os.path.basename(filepath)}...")
        self.pcap_output.delete(1.0, tk.END)
        self.btn_pcap_export.config(state=tk.DISABLED)
        
        def task():
            stats = analyze_pcap(filepath)
            if stats:
                self.current_pcap_stats = stats
                out = f"FILE: {filepath}\n"
                out += f"PACKET COUNT: {stats['packet_count']}\n"
                out += "-" * 60 + "\n\n"
                
                out += "[TOP SOURCE IPs]\n"
                for ip, count in stats['src_ips'].most_common(5):
                    out += f"{ip:<20} : {count}\n"
                out += "\n"

                out += "[TOP DESTINATION IPs]\n"
                for ip, count in stats['dst_ips'].most_common(5):
                    out += f"{ip:<20} : {count}\n"
                out += "\n"

                out += "[TOP PORTS]\n"
                for port, count in stats['top_ports'].most_common(5):
                    out += f"{port:<20} : {count}\n"
                out += "\n"

                out += "[PROTOCOLS]\n"
                for proto, count in stats['protocols'].items():
                    out += f"{proto:<20} : {count}\n"
                
                self.update_text(self.pcap_output, out)
                self.root.after(0, lambda: self.btn_pcap_export.config(state=tk.NORMAL))
                self.log("PCAP analysis complete.")
            else:
                self.update_text(self.pcap_output, "Error analyzing PCAP.")
                self.log("Error analyzing PCAP.")
                
        threading.Thread(target=task).start()

    def export_pcap(self):
        if not self.current_pcap_stats:
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        if path:
            if export_pcap_csv(self.current_pcap_stats, path):
                messagebox.showinfo("Success", "PCAP data exported successfully.")
            else:
                messagebox.showerror("Error", "Failed to export data.")

    def init_browser_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="BROWSER")
        
        frame = ttk.LabelFrame(tab, text=" HISTORY PARSER ")
        frame.pack(padx=15, pady=15, fill='x')
        
        btn_frame = tk.Frame(frame, bg=COLORS["bg_panel"])
        btn_frame.pack(anchor="w", padx=10, pady=10)

        btn = ttk.Button(btn_frame, text="LOAD HISTORY DB", style="Accent.TButton", command=self.run_browser)
        btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.btn_browser_export = ttk.Button(btn_frame, text="EXPORT CSV", state=tk.DISABLED, command=self.export_browser)
        self.btn_browser_export.pack(side=tk.LEFT)
        
        self.browser_output = self.create_scrolled_text(tab)
        self.current_history = None

    def run_browser(self):
        filepath = filedialog.askopenfilename()
        if not filepath:
            return
            
        self.log(f"Parsing {os.path.basename(filepath)}...")
        self.browser_output.delete(1.0, tk.END)
        self.btn_browser_export.config(state=tk.DISABLED)
        
        def task():
            history = parse_browser_history(filepath)
            if history is not None:
                self.current_history = history
                out = f"FILE: {filepath}\n"
                out += f"TOTAL ENTRIES: {len(history)}\n"
                out += "-" * 60 + "\n"
                for i, entry in enumerate(history[:20]): 
                    out += f"[{entry['last_visit_time']}] {entry['url'][:60]}...\n"
                if len(history) > 20:
                    out += f"\n... and {len(history)-20} more entries. Export to CSV to view all."
                
                self.update_text(self.browser_output, out)
                self.root.after(0, lambda: self.btn_browser_export.config(state=tk.NORMAL))
                self.log("History parsing complete.")
            else:
                self.update_text(self.browser_output, "Error parsing history.")
                self.log("Error parsing history.")
                
        threading.Thread(target=task).start()

    def export_browser(self):
        if not self.current_history:
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        if path:
            if export_history_csv(self.current_history, path):
                messagebox.showinfo("Success", "History exported successfully.")
            else:
                messagebox.showerror("Error", "Failed to export data.")

    def init_carver_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="CARVER")
        
        frame = ttk.LabelFrame(tab, text=" DATA RECOVERY ")
        frame.pack(padx=15, pady=15, fill='x')
        
        btn = ttk.Button(frame, text="SELECT BINARY & RECOVER", style="Accent.TButton", command=self.run_carver)
        btn.pack(anchor="w", padx=10, pady=10)
        
        self.carver_output = self.create_scrolled_text(tab)

    def run_carver(self):
        filepath = filedialog.askopenfilename()
        if not filepath:
            return
        
        out_dir = filedialog.askdirectory(title="Select Output Directory")
        if not out_dir:
            return
            
        self.log(f"Carving files from {os.path.basename(filepath)}...")
        self.carver_output.delete(1.0, tk.END)
        
        def task():
            counts = carve_files(filepath, out_dir)
            if counts:
                out = f"SOURCE: {filepath}\n"
                out += f"DESTINATION: {out_dir}\n"
                out += "-" * 60 + "\n"
                out += f"RECOVERED JPGs: {counts['jpg']}\n"
                out += f"RECOVERED PNGs: {counts['png']}\n"
                self.update_text(self.carver_output, out)
                self.log("File carving complete.")
            else:
                self.update_text(self.carver_output, "Error carving files.")
                self.log("Error carving files.")
                
        threading.Thread(target=task).start()

    def init_timeline_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="TIMELINE")
        
        frame = ttk.LabelFrame(tab, text=" REPORT GENERATION ")
        frame.pack(padx=15, pady=15, fill='x')
        
        btn = ttk.Button(frame, text="GENERATE REPORT (PDF)", style="Accent.TButton", command=self.run_timeline)
        btn.pack(anchor="w", padx=10, pady=10)
        
        self.timeline_output = self.create_scrolled_text(tab)

    def run_timeline(self):
        if not self.current_history:
            messagebox.showwarning("Warning", "Please load Browser History first to generate a timeline.")
            return
            
        json_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON", "*.json")], title="Save Timeline JSON")
        if not json_path:
            return
        pdf_path = json_path.replace(".json", ".pdf")
        
        self.log("Generating timeline...")
        
        def task():
            events = []
            for h in self.current_history:
                events.append({
                    'timestamp': h['last_visit_time'],
                    'source': 'Chrome History',
                    'description': f"Visited {h['title']} ({h['url']})"
                })
            
            if generate_timeline(events, json_path, pdf_path):
                self.update_text(self.timeline_output, f"REPORT GENERATED SUCCESSFULLY!\n\nJSON: {json_path}\nPDF: {pdf_path}")
                self.log("Timeline generation complete.")
            else:
                self.update_text(self.timeline_output, "Error generating timeline.")
                self.log("Error generating timeline.")
                
        threading.Thread(target=task).start()

    def update_text(self, widget, text):
        widget.delete(1.0, tk.END)
        widget.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = DFTApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import time

# ==================== 安装向导 ====================
class InstallWizard:
    """360不安全卫士 安装向导（恶搞版）"""

    def __init__(self, root):
        self.root = root
        self.root.title("360不安全卫士 安装向导")
        self.root.geometry("600x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#1E293B")

        self.install_path = tk.StringVar(value="C:\\Program Files\\360不安全卫士")
        self.current_step = 0
        self.container = tk.Frame(self.root, bg="#1E293B")
        self.container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.pages = []
        self.create_page_welcome()
        self.create_page_license()
        self.create_page_path()
        self.create_page_install()
        self.create_page_finish()
        self.show_page(0)

    def show_page(self, index):
        for i, page in enumerate(self.pages):
            if i == index:
                page.pack(fill=tk.BOTH, expand=True)
            else:
                page.pack_forget()
        self.current_step = index

    def create_page_welcome(self):
        page = tk.Frame(self.container, bg="#1E293B")
        self.pages.append(page)
        tk.Label(page, text="🛡️ 欢迎安装 360 不安全卫士", font=("微软雅黑", 18, "bold"), fg="#38BDF8", bg="#1E293B").pack(pady=(30, 10))
        tk.Label(page, text="您的电脑即将获得「最不安全」的保护！\n我们保证：安装后您的电脑会变得更加危险。", font=("微软雅黑", 11), fg="#CBD5E1", bg="#1E293B", justify=tk.CENTER).pack(pady=10)
        tk.Label(page, text="🔧 ⚠️ 🐛 ☠️ 💀", font=("Segoe UI Emoji", 30), bg="#1E293B").pack(pady=20)
        tk.Button(page, text="下一步 →", command=lambda: self.show_page(1), font=("微软雅黑", 10, "bold"), bg="#38BDF8", fg="white", relief=tk.FLAT, padx=20, pady=6, cursor="hand2").pack(pady=20)

    def create_page_license(self):
        page = tk.Frame(self.container, bg="#1E293B")
        self.pages.append(page)
        tk.Label(page, text="📜 最终用户许可协议", font=("微软雅黑", 16, "bold"), fg="#38BDF8", bg="#1E293B").pack(pady=(20, 10))
        license_text = tk.Text(page, height=8, font=("Consolas", 9), bg="#0F172A", fg="#CBD5E1", relief=tk.FLAT, wrap=tk.WORD, state=tk.DISABLED)
        license_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        agreement = """
【360不安全卫士 最终用户许可协议】

1. 您同意放弃所有智商，并承认本软件是您电脑上最大的病毒。
2. 您允许本软件在您桌面上创建 999 个快捷方式（全部指向同一张猫图）。
3. 您承诺每次开机时都会高喊三声“360 最棒！”（否则电脑蓝屏）。
4. 本软件可能会占用您 100% 的 CPU，但您不得抱怨，因为这是“保护”的一部分。
5. 您理解并同意：本软件的唯一作用是浪费您的时间。

点击“我同意”即表示您已认真阅读并接受以上条款。
（不同意就没办法继续安装哦～）
"""
        license_text.config(state=tk.NORMAL)
        license_text.insert(tk.END, agreement)
        license_text.config(state=tk.DISABLED)

        btn_frame = tk.Frame(page, bg="#1E293B")
        btn_frame.pack(pady=15)
        tk.Button(btn_frame, text="❌ 我不同意", command=lambda: messagebox.showinfo("哼！", "不同意也得同意！"), font=("微软雅黑", 10), bg="#FB7185", fg="white", relief=tk.FLAT, padx=15, pady=5, cursor="hand2").pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="✅ 我同意（其实没得选）", command=lambda: self.show_page(2), font=("微软雅黑", 10, "bold"), bg="#34D399", fg="white", relief=tk.FLAT, padx=15, pady=5, cursor="hand2").pack(side=tk.LEFT, padx=10)

    def create_page_path(self):
        page = tk.Frame(self.container, bg="#1E293B")
        self.pages.append(page)
        tk.Label(page, text="📁 选择安装位置", font=("微软雅黑", 16, "bold"), fg="#38BDF8", bg="#1E293B").pack(pady=(30, 20))
        path_frame = tk.Frame(page, bg="#1E293B")
        path_frame.pack(pady=10, padx=20, fill=tk.X)
        tk.Entry(path_frame, textvariable=self.install_path, font=("微软雅黑", 10), bg="#0F172A", fg="white", relief=tk.FLAT, width=40).pack(side=tk.LEFT, padx=(0, 10))
        tk.Button(path_frame, text="浏览...", command=self.browse_path, font=("微软雅黑", 9), bg="#94A3B8", fg="white", relief=tk.FLAT, padx=10, pady=4, cursor="hand2").pack(side=tk.LEFT)
        tk.Label(page, text="💡 提示：您选哪个路径，我们都不会真的创建文件夹，\n因为这只是个恶搞软件！", font=("微软雅黑", 9), fg="#94A3B8", bg="#1E293B", justify=tk.CENTER).pack(pady=20)
        tk.Button(page, text="下一步 →", command=lambda: self.show_page(3), font=("微软雅黑", 10, "bold"), bg="#38BDF8", fg="white", relief=tk.FLAT, padx=20, pady=6, cursor="hand2").pack(pady=10)

    def browse_path(self):
        path = filedialog.askdirectory(title="选择安装目录（实际无效）")
        if path:
            self.install_path.set(path)

    def create_page_install(self):
        page = tk.Frame(self.container, bg="#1E293B")
        self.pages.append(page)
        tk.Label(page, text="⏳ 正在安装...", font=("微软雅黑", 16, "bold"), fg="#38BDF8", bg="#1E293B").pack(pady=(30, 10))
        self.install_log = tk.Text(page, height=6, font=("Consolas", 9), bg="#0F172A", fg="#CBD5E1", relief=tk.FLAT, wrap=tk.WORD, state=tk.DISABLED)
        self.install_log.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        self.install_progress = ttk.Progressbar(page, length=400, mode='determinate')
        self.install_progress.pack(pady=10)
        tk.Button(page, text="🚀 开始安装（很危险）", command=self.start_install, font=("微软雅黑", 10, "bold"), bg="#FB7185", fg="white", relief=tk.FLAT, padx=20, pady=8, cursor="hand2").pack(pady=15)
        self.is_installing = False

    def start_install(self):
        if self.is_installing:
            return
        self.is_installing = True
        for child in self.pages[3].winfo_children():
            if isinstance(child, tk.Button) and "开始安装" in child["text"]:
                child.config(state=tk.DISABLED)
        self.install_log.config(state=tk.NORMAL)
        self.install_log.delete(1.0, tk.END)
        self.install_log.config(state=tk.DISABLED)
        self.install_step = 0
        self.install_messages = [
            "🔧 正在复制病毒文件到系统目录...",
            "🦠 正在注入恶意代码到注册表（假的）...",
            "💀 正在创建桌面快捷方式（共 999 个）...",
            "🔥 正在将 CPU 占用率提升至 100%（模拟）...",
            "✅ 安装完成！您的电脑已成功被「保护」！"
        ]
        self.install_progress['value'] = 0
        self._do_install_step()

    def _do_install_step(self):
        if self.install_step >= len(self.install_messages):
            self.show_page(4)
            self.is_installing = False
            return
        self.install_log.config(state=tk.NORMAL)
        self.install_log.insert(tk.END, self.install_messages[self.install_step] + "\n")
        self.install_log.see(tk.END)
        self.install_log.config(state=tk.DISABLED)
        self.install_progress['value'] = (self.install_step + 1) * 20
        self.install_step += 1
        delay = random.randint(500, 1500)
        self.root.after(delay, self._do_install_step)

    def create_page_finish(self):
        page = tk.Frame(self.container, bg="#1E293B")
        self.pages.append(page)
        tk.Label(page, text="🎉 安装完成！", font=("微软雅黑", 20, "bold"), fg="#34D399", bg="#1E293B").pack(pady=(40, 20))
        tk.Label(page, text="360 不安全卫士 已成功安装在您的电脑上。\n（虽然我们什么都没装，但您已经上当了！）", font=("微软雅黑", 11), fg="#CBD5E1", bg="#1E293B", justify=tk.CENTER).pack(pady=10)
        tk.Button(page, text="🚀 启动 360 不安全卫士", command=self.launch_main_app, font=("微软雅黑", 12, "bold"), bg="#38BDF8", fg="white", relief=tk.FLAT, padx=30, pady=10, cursor="hand2").pack(pady=30)

    def launch_main_app(self):
        self.root.destroy()
        main_root = tk.Tk()
        app = Unsafe360(main_root)
        main_root.mainloop()


# ==================== 主程序（暗黑版） ====================
class Unsafe360:
    """360不安全卫士 - 暗黑科技风恶搞版"""

    def __init__(self, root):
        self.root = root
        self.root.title("360不安全卫士 Pro Max")
        self.root.geometry("680x520")
        self.root.resizable(False, False)

        self.colors = {
            "bg_dark": "#0B1120", "bg_card": "#1E293B", "bg_input": "#0F172A",
            "primary": "#38BDF8", "danger": "#FB7185", "success": "#34D399",
            "text_light": "#F8FAFC", "text_muted": "#94A3B8", "btn_hover": "#7DD3FC"
        }
        self.root.configure(bg=self.colors["bg_dark"])

        self.btn_style = {
            "font": ("微软雅黑", 10, "bold"), "fg": "white", "bg": self.colors["primary"],
            "activebackground": self.colors["btn_hover"], "activeforeground": "white",
            "relief": tk.FLAT, "padx": 12, "pady": 6, "cursor": "hand2"
        }
        self.danger_btn_style = self.btn_style.copy()
        self.danger_btn_style["bg"] = self.colors["danger"]
        self.danger_btn_style["activebackground"] = "#FDA4AF"

        self.create_widgets()
        self.status.set("🚨 系统处于极度危险状态！")
        self.log("🛸 欢迎降临 360 不安全卫士...")
        self.log("💀 检测到 9999+ 个变异病毒，请做好心理准备！")

    def create_widgets(self):
        top_frame = tk.Frame(self.root, bg=self.colors["bg_card"], height=80)
        top_frame.pack(fill=tk.X, pady=(0, 15), padx=15)
        title_label = tk.Label(top_frame, text="🛡️ 360 不安全卫士", font=("微软雅黑", 24, "bold"), fg=self.colors["primary"], bg=self.colors["bg_card"])
        title_label.pack(side=tk.LEFT, padx=20, pady=15)
        self.status = tk.StringVar()
        status_label = tk.Label(top_frame, textvariable=self.status, font=("微软雅黑", 11, "bold"), fg=self.colors["danger"], bg=self.colors["bg_card"])
        status_label.pack(side=tk.RIGHT, padx=20, pady=15)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TProgressbar", background=self.colors["primary"], troughcolor=self.colors["bg_input"],
                        bordercolor=self.colors["bg_card"], lightcolor=self.colors["primary"],
                        darkcolor=self.colors["primary"], thickness=18)
        self.progress = ttk.Progressbar(self.root, style="TProgressbar", length=550, mode='determinate')
        self.progress.pack(pady=10)

        btn_card = tk.Frame(self.root, bg=self.colors["bg_card"], relief=tk.FLAT)
        btn_card.pack(pady=15, padx=15, fill=tk.X)
        buttons = [("🔍 全面体检", self.full_check), ("🧬 病毒查杀", self.virus_scan),
                   ("⚡ 一键加速", self.speed_up), ("🗑️ 垃圾清理", self.clean_garbage),
                   ("💀 退出程序", self.exit_app)]
        for text, cmd in buttons:
            style_use = self.danger_btn_style if text == "💀 退出程序" else self.btn_style
            btn = tk.Button(btn_card, text=text, command=cmd, **style_use)
            btn.pack(side=tk.LEFT, padx=8, pady=10, expand=True, fill=tk.X)

        log_frame = tk.LabelFrame(self.root, text="📋 实时运行日志", font=("微软雅黑", 10, "bold"),
                                  fg=self.colors["text_light"], bg=self.colors["bg_card"],
                                  relief=tk.FLAT, labelanchor="n")
        log_frame.pack(pady=(10, 15), padx=15, fill=tk.BOTH, expand=True)
        text_container = tk.Frame(log_frame, bg=self.colors["bg_card"])
        text_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.log_text = tk.Text(text_container, height=12, font=("Consolas", 10), bg=self.colors["bg_input"],
                                fg=self.colors["text_light"], insertbackground="white",
                                relief=tk.FLAT, wrap=tk.WORD, state=tk.DISABLED)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(text_container, command=self.log_text.yview, bg=self.colors["bg_card"])
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=scrollbar.set)

    def log(self, msg):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, msg + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        self.root.update()

    def _simulate_progress(self, steps=10, delay=0.1):
        for i in range(1, 101, steps):
            time.sleep(delay)
            self.progress['value'] = i
            self.root.update()
        self.progress['value'] = 100

    def full_check(self):
        self.status.set("🔎 正在挖地三尺扫描...")
        self.progress['value'] = 0
        self.log("🚀 开始全面体检...")
        problems = ["🐛 发现木马：您的鼠标指针里有虫子！", "🧠 发现漏洞：您的智商余额不足，请充值！",
                    "📁 发现风险：桌面上有 1 个隐藏文件夹，名字叫 '千万别点'",
                    "🌐 主页被劫持：浏览器默认打开的是 4399 小游戏！",
                    "💾 发现垃圾：内存条里住着一只蟑螂。"]
        for i in range(1, 101, 15):
            time.sleep(0.08)
            self.progress['value'] = i
            self.root.update()
            if i % 30 == 0:
                self.log("⚠️ " + random.choice(problems))
        self.progress['value'] = 100
        self.log("✅ 体检完成！结论：您的大脑需要格式化！")
        self.status.set("😈 体检结束，危险值爆表！")

    def virus_scan(self):
        self.status.set("🧬 正在培养病毒...")
        self.progress['value'] = 0
        self.log("🧫 开始病毒查杀（其实是养蛊）...")
        viruses = ["Trojan.智商税", "Worm.熬夜猝死", "Ransom.减肥失败", "Adware.脱发"]
        for i in range(1, 101, 20):
            time.sleep(0.1)
            self.progress['value'] = i
            self.root.update()
            if i % 40 == 0:
                self.log(f"🦠 发现新型病毒：{random.choice(viruses)}，已隔离（骗你的）")
        self.progress['value'] = 100
        self.log("🧪 查杀完毕！本软件就是最大的病毒，告辞！")
        self.status.set("☣️ 病毒已占领高地！")

    def speed_up(self):
        self.status.set("⚡ 正在超频（模拟）...")
        self.progress['value'] = 0
        self.log("🏎️ 开始加速...")
        self._simulate_progress(steps=25, delay=0.05)
        mem = random.randint(200, 999)
        self.log(f"💨 加速完成！释放了 {mem} MB 假内存。")
        self.status.set("🐢 加速完毕，速度降为 0！")

    def clean_garbage(self):
        self.status.set("🗑️ 正在倒垃圾...")
        self.progress['value'] = 0
        self.log("🧹 开始清理垃圾...")
        self._simulate_progress(steps=20, delay=0.06)
        garbage = random.randint(5, 20)
        self.log(f"♻️ 清理完成！清理了 {garbage} GB 垃圾（其实是删除了回收站的快捷方式）")
        self.status.set("🗑️ 垃圾已倒进您的脑子里！")

    def exit_app(self):
        if messagebox.askyesno("☠️ 终极警告", "确定退出吗？退出后电脑将自动爆炸（假的）！"):
            self.root.destroy()
        else:
            self.log("😎 聪明！继续留在危险之中吧！")


# ==================== 程序入口 ====================
if __name__ == "__main__":
    install_root = tk.Tk()
    wizard = InstallWizard(install_root)
    install_root.mainloop()

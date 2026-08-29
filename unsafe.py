import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

class Unsafe360:
    """360不安全卫士 - 暗黑科技风恶搞版"""

    def __init__(self, root):
        self.root = root
        self.root.title("360不安全卫士 Pro Max")
        self.root.geometry("680x520")
        self.root.resizable(False, False)

        # ------------------- 1. 设置全局配色（方便你换主题） -------------------
        self.colors = {
            "bg_dark": "#0B1120",       # 最深色（窗口背景）
            "bg_card": "#1E293B",       # 卡片深灰蓝（放组件的底框）
            "bg_input": "#0F172A",      # 日志框背景
            "primary": "#38BDF8",       # 亮蓝色（主色调）
            "danger": "#FB7185",        # 粉红色（警告、危险）
            "success": "#34D399",       # 翠绿色（成功）
            "text_light": "#F8FAFC",    # 白色偏灰（主要文字）
            "text_muted": "#94A3B8",    # 灰色（次要文字）
            "btn_hover": "#7DD3FC"      # 按钮悬停颜色
        }

        # 设置主窗口背景色
        self.root.configure(bg=self.colors["bg_dark"])

        # ------------------- 2. 美化成现代扁平风格按钮样式 -------------------
        # 这里我们自定义按钮风格，后面创建按钮直接用这个模板
        self.btn_style = {
            "font": ("微软雅黑", 10, "bold"),
            "fg": "white",
            "bg": self.colors["primary"],
            "activebackground": self.colors["btn_hover"],
            "activeforeground": "white",
            "relief": tk.FLAT,           # 扁平无边框（现代 UI 常用）
            "padx": 12,
            "pady": 6,
            "cursor": "hand2"            # 鼠标移上去变成小手
        }

        # 危险按钮（退出）单独用红色
        self.danger_btn_style = self.btn_style.copy()
        self.danger_btn_style["bg"] = self.colors["danger"]
        self.danger_btn_style["activebackground"] = "#FDA4AF"

        # ------------------- 3. 开始画界面 -------------------
        self.create_widgets()

        # ------------------- 4. 初始状态吓唬人 -------------------
        self.status.set("🚨 系统处于极度危险状态！")
        self.log("🛸 欢迎降临 360 不安全卫士...")
        self.log("💀 检测到 9999+ 个变异病毒，请做好心理准备！")

    # ================== 界面绘制函数 ==================
    def create_widgets(self):
        """所有 UI 组件都画在这里"""
        
        # -------- 3.1 顶部标题横幅（深色渐变感） --------
        top_frame = tk.Frame(self.root, bg=self.colors["bg_card"], height=80)
        top_frame.pack(fill=tk.X, pady=(0, 15), padx=15)  # fill=tk.X 横向拉满

        # 标题（左对齐）
        title_label = tk.Label(
            top_frame,
            text="🛡️ 360 不安全卫士",
            font=("微软雅黑", 24, "bold"),
            fg=self.colors["primary"],
            bg=self.colors["bg_card"]
        )
        title_label.pack(side=tk.LEFT, padx=20, pady=15)

        # 状态标签（右对齐，显示动态警告）
        self.status = tk.StringVar()
        status_label = tk.Label(
            top_frame,
            textvariable=self.status,
            font=("微软雅黑", 11, "bold"),
            fg=self.colors["danger"],
            bg=self.colors["bg_card"]
        )
        status_label.pack(side=tk.RIGHT, padx=20, pady=15)

        # -------- 3.2 进度条（加了圆角效果） --------
        # 使用 ttk 进度条，并切换主题为 'clam'（更好看）
        style = ttk.Style()
        style.theme_use('clam')  # 'clam' 主题允许我们改颜色
        style.configure(
            "TProgressbar",
            background=self.colors["primary"],   # 进度条颜色
            troughcolor=self.colors["bg_input"], # 背景槽颜色
            bordercolor=self.colors["bg_card"],
            lightcolor=self.colors["primary"],
            darkcolor=self.colors["primary"],
            thickness=18                         # 进度条高度
        )
        
        self.progress = ttk.Progressbar(
            self.root,
            style="TProgressbar",
            length=550,
            mode='determinate'
        )
        self.progress.pack(pady=10)

        # -------- 3.3 核心按钮区（用 Frame 包裹并加卡片背景） --------
        btn_card = tk.Frame(self.root, bg=self.colors["bg_card"], relief=tk.FLAT)
        btn_card.pack(pady=15, padx=15, fill=tk.X)

        # 定义按钮文本和对应的执行函数
        buttons = [
            ("🔍 全面体检", self.full_check),
            ("🧬 病毒查杀", self.virus_scan),
            ("⚡ 一键加速", self.speed_up),
            ("🗑️ 垃圾清理", self.clean_garbage),
            ("💀 退出程序", self.exit_app)  # 这个单独用红色
        ]

        # 循环创建按钮，并放在卡片里
        for text, cmd in buttons:
            # 判断是否是退出按钮，切换不同颜色
            if text == "💀 退出程序":
                btn = tk.Button(btn_card, text=text, command=cmd, **self.danger_btn_style)
            else:
                btn = tk.Button(btn_card, text=text, command=cmd, **self.btn_style)
            
            # 让按钮横向排列，并均匀分布（expand=True 让它平均占位）
            btn.pack(side=tk.LEFT, padx=8, pady=10, expand=True, fill=tk.X)

        # -------- 3.4 日志区域（用 LabelFrame 加上标题边框） --------
        log_frame = tk.LabelFrame(
            self.root,
            text="📋 实时运行日志",
            font=("微软雅黑", 10, "bold"),
            fg=self.colors["text_light"],
            bg=self.colors["bg_card"],
            relief=tk.FLAT,
            labelanchor="n"  # 标签放在左上角
        )
        log_frame.pack(pady=(10, 15), padx=15, fill=tk.BOTH, expand=True)

        # 日志文本框（带滚动条，这里用 Text + 滚动条组合）
        text_container = tk.Frame(log_frame, bg=self.colors["bg_card"])
        text_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.log_text = tk.Text(
            text_container,
            height=12,
            font=("Consolas", 10),
            bg=self.colors["bg_input"],
            fg=self.colors["text_light"],
            insertbackground="white",  # 光标颜色
            relief=tk.FLAT,
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 加一个纵向滚动条（更专业）
        scrollbar = tk.Scrollbar(text_container, command=self.log_text.yview, bg=self.colors["bg_card"])
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=scrollbar.set)

    # ================== 辅助工具函数 ==================
    def log(self, msg):
        """向日志区追加文字（并自动解锁/加锁）"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, msg + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        self.root.update()

    def _simulate_progress(self, steps=10, delay=0.1):
        """模拟进度条前进（内部使用）"""
        for i in range(1, 101, steps):
            time.sleep(delay)
            self.progress['value'] = i
            self.root.update()
        self.progress['value'] = 100

    # ================== 四大恶搞功能（逻辑和之前一样，加了些表情） ==================
    def full_check(self):
        self.status.set("🔎 正在挖地三尺扫描...")
        self.progress['value'] = 0
        self.log("🚀 开始全面体检...")
        
        problems = [
            "🐛 发现木马：您的鼠标指针里有虫子！",
            "🧠 发现漏洞：您的智商余额不足，请充值！",
            "📁 发现风险：桌面上有 1 个隐藏文件夹，名字叫 '千万别点'",
            "🌐 主页被劫持：浏览器默认打开的是 4399 小游戏！",
            "💾 发现垃圾：内存条里住着一只蟑螂。"
        ]
        
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
        """退出搞怪弹窗"""
        if messagebox.askyesno("☠️ 终极警告", "确定退出吗？退出后电脑将自动爆炸（假的）！"):
            self.root.destroy()
        else:
            self.log("😎 聪明！继续留在危险之中吧！")


# ================== 启动程序 ==================
if __name__ == "__main__":
    root = tk.Tk()
    app = Unsafe360(root)
    root.mainloop()

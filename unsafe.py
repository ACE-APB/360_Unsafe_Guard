import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import threading

class Unsafe360:
    """360不安全卫士 - 恶搞安全软件"""

    def __init__(self, root):
        self.root = root
        self.root.title("360不安全卫士")
        self.root.geometry("620x450")
        self.root.resizable(False, False)

        # 界面组件
        self.create_widgets()

        # 初始化状态
        self.status.set("⚠️ 您的电脑处于极度危险状态！")
        self.log("欢迎使用360不安全卫士！")
        self.log("您的电脑已感染了 999+ 个病毒，请立即处理！")

    def create_widgets(self):
        # 标题
        tk.Label(
            self.root,
            text="360不安全卫士",
            font=("微软雅黑", 22, "bold"),
            fg="#1E90FF"      # 道奇蓝，模仿安全软件风格
        ).pack(pady=10)

        # 状态标签
        self.status = tk.StringVar()
        tk.Label(
            self.root,
            textvariable=self.status,
            font=("微软雅黑", 12),
            fg="red"
        ).pack()

        # 进度条
        self.progress = ttk.Progressbar(
            self.root,
            length=450,
            mode='determinate'
        )
        self.progress.pack(pady=15)

        # 按钮区域
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        buttons = [
            ("🔍 全面体检", self.full_check),
            ("🛡️ 病毒查杀", self.virus_scan),
            ("⚡ 电脑加速", self.speed_up),
            ("🗑️ 垃圾清理", self.clean_garbage),
            ("🚪 退出", self.exit_app)
        ]

        for text, cmd in buttons:
            btn = tk.Button(
                btn_frame,
                text=text,
                command=cmd,
                width=12,
                height=1,
                font=("微软雅黑", 10)
            )
            btn.pack(side=tk.LEFT, padx=4)

        # 日志文本框（只读）
        self.log_text = tk.Text(
            self.root,
            height=10,
            width=70,
            font=("Consolas", 9),
            state=tk.DISABLED,
            wrap=tk.WORD
        )
        self.log_text.pack(pady=10)

    def log(self, msg):
        """向日志区域添加一行消息"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, msg + "\n")
        self.log_text.see(tk.END)          # 自动滚动到底部
        self.log_text.config(state=tk.DISABLED)
        self.root.update()

    def _simulate_progress(self, steps=10, delay=0.12):
        """模拟进度条递增（装饰器或内部调用）"""
        for i in range(1, 101, steps):
            time.sleep(delay)
            self.progress['value'] = i
            self.root.update()
        self.progress['value'] = 100

    # ---------- 各功能按钮回调 ----------

    def full_check(self):
        self.status.set("🔎 正在全面体检...")
        self.progress['value'] = 0
        self.log("开始全面体检...")

        problems = [
            "发现木马：您竟然还在用 Windows 7！",
            "发现漏洞：您的密码是 '123456'，已被黑客窃取！",
            "发现风险：桌面上有 3 个未读快捷方式，可能包含病毒！",
            "发现广告：浏览器主页被恶意篡改为百度（好吧，这不算恶意）",
            "发现垃圾：回收站里有 1 个被删除的文件，其实它很重要！",
            "发现异常：CPU 使用率高达 2%，建议立即关机！"
        ]

        # 循环进度并随机输出搞笑问题
        for i in range(1, 101, 12):
            time.sleep(0.1)
            self.progress['value'] = i
            self.root.update()
            if i % 25 == 0:
                self.log(random.choice(problems))

        self.progress['value'] = 100
        self.log("✅ 体检完成！发现重大问题：您的智商低于平均水平！")
        self.log("💡 建议立即卸载本软件，以免被继续欺骗！")
        self.status.set("⚠️ 体检结束，您的电脑依然很危险！")

    def virus_scan(self):
        self.status.set("🛡️ 正在查杀病毒...")
        self.progress['value'] = 0
        self.log("开始病毒查杀...")

        viruses = [
            "Trojan.Win32.智商清零",
            "Worm.浏览器被劫持",
            "Backdoor.摄像头开启",
            "Ransom.锁屏勒索",
            "Adware.弹窗广告"
        ]

        for i in range(1, 101, 15):
            time.sleep(0.1)
            self.progress['value'] = i
            self.root.update()
            if i % 30 == 0:
                self.log(f"🦠 发现病毒：{random.choice(viruses)}，已成功隔离（其实没有）")

        self.progress['value'] = 100
        self.log("✅ 病毒查杀完成！共发现 0 个病毒，因为本软件本身就是最大的病毒！")
        self.status.set("🦠 查杀完毕，您的电脑已‘中毒’更深！")

    def speed_up(self):
        self.status.set("⚡ 正在加速...")
        self.progress['value'] = 0
        self.log("正在加速电脑...")

        self._simulate_progress(steps=20, delay=0.08)

        mem = random.randint(100, 500)
        self.log(f"✅ 加速完成！释放了 {mem} MB 内存（其实是假的，您被骗了）")
        self.status.set("⚡ 加速完毕，速度提升 0%！")

    def clean_garbage(self):
        self.status.set("🗑️ 正在清理垃圾...")
        self.progress['value'] = 0
        self.log("正在清理垃圾...")

        self._simulate_progress(steps=20, delay=0.08)

        garbage = random.randint(1, 10)
        self.log(f"✅ 清理完成！清理了 {garbage} GB 垃圾")
        self.status.set("🗑️ 清理完毕，垃圾更多了！")

    def exit_app(self):
        """退出时弹出搞笑确认框"""
        if messagebox.askyesno(
            "⚠️ 危险操作",
            "您确定要退出吗？您的电脑将失去保护，面临巨大风险！"
        ):
            self.root.destroy()
        else:
            self.log("😊 您做出了明智的选择！继续保护您的电脑")


# ---------- 启动 ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = Unsafe360(root)
    root.mainloop()
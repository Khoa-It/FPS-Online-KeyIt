from tkinter import Tk, Label, Entry, Button, Canvas, font, messagebox
from PIL import ImageTk, Image
import webbrowser

from ursina import Func


class LoginForm:
    def __init__(self, callback):
        self.callback = callback

        self.win = Tk()  # khoi tao bien "win" la cua so Tk()
        self.win.title('Blaze Battlegrounds')

        # Lấy kích thước của màn hình
        screen_width = self.win.winfo_screenwidth()
        screen_height = self.win.winfo_screenheight()

        # Kích thước của cửa sổ
        win_width = 880 + 250
        win_height = 520 + 100

        # Tính toán vị trí để cửa sổ xuất hiện ở giữa màn hình
        x_position = (screen_width - win_width) // 2
        y_position = (screen_height - win_height) // 2

        self.win.geometry(f'{win_width}x{win_height}+{x_position}+{y_position}')

        self.win.overrideredirect(True)

        self.win['bg'] = '#233657'

        # Chèn ảnh
        # Load hình ảnh từ đường dẫn
        image_path = "asset/static/login_gui/background_33pt.png"
        original_image = Image.open(image_path)

        # Điều chỉnh kích thước ảnh
        new_size = (768, 417)
        resized_image = original_image.resize(new_size)

        # Tạo một đối tượng PhotoImage từ hình ảnh
        photo = ImageTk.PhotoImage(resized_image)

        # Tạo một nhãn (label) để hiển thị hình ảnh và điều chỉnh vị trí
        label = Canvas(self.win, width=win_width, height=win_height, bg='#233657', highlightthickness=0)
        label.create_image(0, 0, anchor='nw', image=photo)
        label.image = photo  # Giữ một tham chiếu đến hình ảnh để tránh bị hủy
        label.place(x=50, y=50)  # Điều chỉnh vị trí của nhãn

        # Khởi tạo biến chữ Fanpage
        fanpageTxt = Label(self.win, text='Fanpage', font=('Times New Roman', 14), bg='#233657', fg='white')
        fanpageTxt.place(x=(win_width - fanpageTxt.winfo_reqwidth()) // 2, y=20)

        # Gán sự kiện click cho chữ Fanpage
        fanpageTxt.bind("<Button-1>", lambda event: self.open_fanpage())

        # Gán sự kiện di chuột vào và ra khỏi widget
        fanpageTxt.bind("<Enter>", self.change_cursor(self))
        fanpageTxt.bind("<Leave>", self.revert_cursor(self))

        # Khởi tạo biến chữ Home
        homeTxt = Label(self.win, text='Home', font=('Times New Roman', 14), bg='#233657', fg='white')
        homeTxt.place(x=(win_width - fanpageTxt.winfo_reqwidth()) // 2 - 200, y=20)

        # Gán sự kiện click cho chữ Home
        homeTxt.bind("<Button-1>", lambda event: self.open_home())

        # Gán sự kiện di chuột vào và ra khỏi widget
        homeTxt.bind("<Enter>", self.change_cursor(self))
        homeTxt.bind("<Leave>", self.revert_cursor(self))

        # Khởi tạo biến chữ Twitter
        twitterTxt = Label(self.win, text='Twitter', font=('Times New Roman', 14), bg='#233657', fg='white')
        twitterTxt.place(x=(win_width - fanpageTxt.winfo_reqwidth()) // 2 + 200, y=20)

        # Gán sự kiện click cho chữ Tw
        twitterTxt.bind("<Button-1>", lambda event: self.open_twitter())

        # Gán sự kiện di chuột vào và ra khỏi widget
        twitterTxt.bind("<Enter>", self.change_cursor(self))
        twitterTxt.bind("<Leave>", self.revert_cursor(self))

        # Khởi tạo biến chữ Blaze Battlegrounds - Win or loss based on your skills
        sloganTxt = Label(self.win, text='Blaze Battlegrounds - Win or loss based on your skills',
                          font=('Times New Roman', 14),
                          bg='#233657', fg='white')
        sloganTxt.place(x=(win_width - sloganTxt.winfo_reqwidth()) // 2, y=470)

        # Tạo textbox
        self.nameTb = Entry(self.win, width=20, font=('Times New Roman', 16))
        self.nameTb.place(x=170, y=240)

        # Vẽ văn bản "Enter your name" trên Canvas
        custom_font = font.Font(family='Times New Roman', size=18)
        text_x = 230
        text_y = 140
        label.create_text(text_x, text_y, text='Enter your name', font=custom_font, fill='white')

        # Tạo textbox cho IP room (không bắt buộc)
        self.ipTb = Entry(self.win, width=20, font=('Times New Roman', 16))
        self.ipTb.place(x=170, y=330)

        # Vẽ văn bản "Enter IP room" trên Canvas
        text_x = 270
        text_y = 250
        label.create_text(text_x, text_y, text='Nhập IP phòng (nếu có)', font=custom_font, fill='white')

        # Khởi tạo nút Start
        startBtn = Button(self.win, text='Start', fg='#233657', width=15, command=self.submit_username)
        startBtn.place(x=225, y=380)

        # Chèn ảnh
        # Load hình ảnh từ đường dẫn
        image_path = "asset/static/login_gui/logo.jpg"
        original_image = Image.open(image_path)

        # Điều chỉnh kích thước ảnh
        new_size = (250, 250)
        resized_image = original_image.resize(new_size)

        # Tạo một đối tượng PhotoImage từ hình ảnh
        photo = ImageTk.PhotoImage(resized_image)

        # Tạo một nhãn (label) để hiển thị hình ảnh và điều chỉnh vị trí
        label = Label(self.win, image=photo)
        label.image = photo  # Giữ một tham chiếu đến hình ảnh để tránh bị hủy
        label.place(x=550, y=135)  # Điều chỉnh vị trí của nhãn

        # hinh 18+
        image_path = "asset/static/login_gui/18+.png"
        original_image = Image.open(image_path)
        new_size = (40, 40)
        resized_image = original_image.resize(new_size)
        photo = ImageTk.PhotoImage(resized_image)
        label = Canvas(self.win, width=50, height=50, bg='#233657', highlightthickness=0)
        label.create_image(0, 0, anchor='nw', image=photo)
        label.image = photo
        label.place(x=50, y=50)

        # logo fb
        image_path = "asset/static/login_gui/fb.png"
        original_image = Image.open(image_path)
        new_size = (30, 30)
        resized_image = original_image.resize(new_size)
        photo = ImageTk.PhotoImage(resized_image)
        label = Canvas(self.win, width=30, height=30, bg='#233657', highlightthickness=0)
        label.create_image(0, 0, anchor='nw', image=photo)
        label.image = photo
        label.place(x=(win_width - fanpageTxt.winfo_reqwidth()) // 2 - 35, y=18)

        # logo twitter
        image_path = "asset/static/login_gui/twitter.png"
        original_image = Image.open(image_path)
        new_size = (30, 30)
        resized_image = original_image.resize(new_size)
        photo = ImageTk.PhotoImage(resized_image)
        label = Canvas(self.win, width=30, height=30, bg='#233657', highlightthickness=0)
        label.create_image(0, 0, anchor='nw', image=photo)
        label.image = photo
        label.place(x=(win_width - fanpageTxt.winfo_reqwidth()) // 2 + 200 - 35, y=18)

        # logo Home
        image_path = "asset/static/login_gui/home.png"
        original_image = Image.open(image_path)
        new_size = (30, 30)
        resized_image = original_image.resize(new_size)
        photo = ImageTk.PhotoImage(resized_image)
        label = Canvas(self.win, width=30, height=30, bg='#233657', highlightthickness=0)
        label.create_image(0, 0, anchor='nw', image=photo)
        label.image = photo
        label.place(x=(win_width - fanpageTxt.winfo_reqwidth()) // 2 - 200 - 35, y=15)

        # Hiển thị cửa sổ
        self.win.mainloop()

    def change_cursor(self, event):
        # Thay đổi hình ảnh con trỏ chuột thành hình bàn tay
        self.win.config(cursor="hand2")

    def revert_cursor(self, event):
        # Khôi phục hình ảnh con trỏ chuột ban đầu
        self.win.config(cursor="")

    def open_home(self):
        webbrowser.open_new("https://fb.com/thegirls.fanpage")

    def open_fanpage(self):
        webbrowser.open_new("https://google.com")

    def open_twitter(self):
        webbrowser.open_new("https://youtube.com")

    def submit_username(self):
        username = self.nameTb.get()
        ip_room = self.ipTb.get()  # Lấy giá trị từ trường nhập IP room

        # Kiểm tra nếu người dùng đã nhập tên người dùng
        if username.strip():
            # Gọi hàm callback và truyền tên người dùng và IP room (có thể là chuỗi rỗng)
            self.callback[0]((username, ip_room))
            self.win.destroy()  # Đóng cửa sổ sau khi nhấn nút "Submit"
        else:
            # Hiển thị cảnh báo nếu tên người dùng không được nhập
            messagebox.showwarning("Warning", "Vui lòng nhập tên người chơi.")
    def setter_usname(self, username):
        self.callback[0](username)


def create_client(data):
    username, ip_room = data
    print(f"Creating client for user: {username}, IP room: {ip_room}")


def open_login_window(callback):
    LoginForm(callback)


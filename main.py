import tkinter as tk
from tkinter import ttk


def create_form():
    window = tk.Tk()
    window.title("Thông tin nhân viên")

    # Define labels and entry fields
    labels = ["Mã", "Tên", "Đơn vị", "Chức danh", "Ngày sinh", "Giới tính", "Số CMND", "Ngày cấp", "Nơi cấp"]
    entries = {}
    for i, label in enumerate(labels):
        tk.Label(window, text=label).grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entries[label] = tk.Entry(window)
        entries[label].grid(row=i, column=1, padx=10, pady=5)

    # Gender radio buttons
    gender_var = tk.StringVar(value="Nam")
    tk.Label(window, text="Giới tính").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
    tk.Radiobutton(window, text="Nam", variable=gender_var, value="Nam").grid(row=4, column=1, sticky=tk.W)
    tk.Radiobutton(window, text="Nữ", variable=gender_var, value="Nữ").grid(row=4, column=1, sticky=tk.E)

    # Checkboxes
    is_customer = tk.BooleanVar()
    is_supplier = tk.BooleanVar()
    tk.Checkbutton(window, text="Là khách hàng", variable=is_customer).grid(row=9, column=0, padx=10, pady=5,
                                                                            sticky=tk.W)
    tk.Checkbutton(window, text="Là nhà cung cấp", variable=is_supplier).grid(row=10, column=0, padx=10, pady=5,
                                                                              sticky=tk.W)

    # Submit button
    tk.Button(window, text="Submit", command=window.quit).grid(row=11, column=0, columnspan=2, pady=10)

    window.mainloop()


create_form()

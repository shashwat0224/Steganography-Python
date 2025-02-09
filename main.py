from tkinter import messagebox, filedialog
import customtkinter as ctk
from PIL import Image
import cv2
import numpy as np
import random

class Steganography:
    def __init__(self):
        pass

    def home(self,frame):
            if frame.winfo_exists(): 
                frame.pack_forget()
                frame.destroy()
                self.main(root)

    def update_window_size(self):
        """Update root window size based on current frame content"""
        root.update_idletasks()  # Ensures widgets are fully rendered
        width = root.winfo_reqwidth()
        height = root.winfo_reqheight()
        root.geometry(f"{width}x{height}")

    def main(self,root):
        root.title("Steganography")
        root.geometry("800x600")
        root.configure(bg="#f0f0f0" )
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        ctk.set_appearance_mode("light")

        menu_frame = ctk.CTkFrame(root, fg_color="white")
        menu_frame.pack(anchor="center", padx=15, pady=15)
        menu_frame.pack_propagate(True)

        img_in_img_button = ctk.CTkButton(menu_frame, text="Image in Image", font=("Arial", 16), command=lambda: self.img_menu(menu_frame))
        img_in_img_button.pack(anchor="center", pady=2)

        txt_in_img_button = ctk.CTkButton(menu_frame, text="Text in Image", font=("Arial", 16), command=lambda: self.txt_menu(menu_frame))
        txt_in_img_button.pack(anchor="center", pady=2)

        self.update_window_size()

        root.mainloop()

    def img_menu(self,frame):
        frame.destroy()
        img_menu_frame = ctk.CTkFrame(root, fg_color="white")
        img_menu_frame.pack(padx=15, pady=15,fill="both", expand=True)
        img_menu_frame.pack_propagate(True)
        encode_button = ctk.CTkButton(img_menu_frame, text="Encode", font=("Arial", 16), command=lambda: self.encode_frame1_img(img_menu_frame))
        encode_button.pack()
        decode_button = ctk.CTkButton(img_menu_frame, text="Decode", font=("Arial", 16), command=lambda: self.decode_frame1_img(img_menu_frame))
        decode_button.pack()
        main_menu_button = ctk.CTkButton(img_menu_frame, text="Main Menu", font=("Arial", 16), command=lambda: self.home(img_menu_frame))
        main_menu_button.pack()
        self.update_window_size()

    def txt_menu(self,frame):
        frame.destroy()
        txt_menu_frame = ctk.CTkFrame(root, fg_color="white")
        txt_menu_frame.pack(padx=15, pady=15,fill="both", expand=True)
        txt_menu_frame.pack_propagate(True)
        encode_button = ctk.CTkButton(txt_menu_frame, text="Encode", font=("Arial", 16), command=lambda: self.encode_frame1_txt(txt_menu_frame))
        encode_button.pack()
        decode_button = ctk.CTkButton(txt_menu_frame, text="Decode", font=("Arial", 16), command=lambda: self.decode_frame1_txt(txt_menu_frame))
        decode_button.pack()
        main_menu_button = ctk.CTkButton(txt_menu_frame, text="Main Menu", font=("Arial", 16), command=lambda: self.home(txt_menu_frame))
        main_menu_button.pack()
        self.update_window_size()
        
    def encode_frame1_img(self,frame):
        frame.destroy()
        enc_frame1 = ctk.CTkFrame(root, fg_color="white")
        enc_frame1.pack(padx=15, pady=15,fill="both", expand=True)
        enc_frame1.pack_propagate(True)
        enc_label1 = ctk.CTkLabel(enc_frame1, text="Select an image to hide another image", font=("Arial", 16))
        enc_label1.pack()
        select_button = ctk.CTkButton(enc_frame1, text="Select Image-1", font=("Arial", 16), command=lambda: self.encode_frame2_img(enc_frame1))
        select_button.pack()
        main_menu_button = ctk.CTkButton(enc_frame1, text="Main Menu", font=("Arial", 16), command=lambda: self.home(enc_frame1))
        main_menu_button.pack()
        note_label = ctk.CTkLabel(enc_frame1, font=("Arial", 12), fg_color="white", text_color="red",
                        text="Note: It is recommended to use images of same dimensions...\n      Otherwise --> Image-1 should be same or larger than Image-2 in dimensions")
        note_label.pack()
        self.update_window_size()

    def encode_frame2_img(self,frame):
        enc_frame2 = ctk.CTkFrame(root, fg_color="white")
        myfile1 = filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile1:
            messagebox.showerror("Error", "No file selected")
        else:
            enc_frame2.pack(padx=15, pady=15,fill="both", expand=True)
            enc_frame2.pack_propagate(True)
            frame.destroy()
            myimage = cv2.imread(myfile1)
            my_image = cv2.resize(myimage, (300, 300))
            image_rgb = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
            image1 = ctk.CTkImage(light_image=Image.fromarray(image_rgb),dark_image=Image.fromarray(image_rgb),size=(300,300))
            image_label = ctk.CTkButton(enc_frame2, image=image1, state="disabled", fg_color="white", text="")
            image_label.image = image1
            image_label.pack()
            label1 = ctk.CTkLabel(enc_frame2, text="Selected Image ( In Which Image To Be Hidden!! )", font=("Arial", 16))
            label1.pack()
            select_button = ctk.CTkButton(enc_frame2, text="Select Image-2", font=("Arial", 16), command=lambda: self.encode_frame3_img( enc_frame2, image1, myfile1))
            select_button.pack()
            main_menu_button = ctk.CTkButton(enc_frame2, text="Main Menu", font=("Arial", 16), command=lambda: self.home(enc_frame2))
            main_menu_button.pack()
            self.update_window_size()

    def encode_frame3_img(self,frame,image1,myfile1):
            enc_frame3 = ctk.CTkScrollableFrame(root, width= 350, height= 350, fg_color="white", orientation="vertical")
            myfile2 = filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
            if not myfile2:
                messagebox.showerror("Error", "No file selected")
            else:
                enc_frame3.pack(padx=15, pady=15,fill="both", expand=True)
                enc_frame3.pack_propagate(True)
                frame.destroy()
                myimage = cv2.imread(myfile2)
                my_image = cv2.resize(myimage, (300, 300))
                image_rgb = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
                image2 = ctk.CTkImage(light_image=Image.fromarray(image_rgb),dark_image=Image.fromarray(image_rgb),size=(300,300))
                image1_label = ctk.CTkButton(enc_frame3, image=image1, text=" ", fg_color="white", state='disabled')
                image1_label.image = image1
                image1_label.pack()
                label1 = ctk.CTkLabel(enc_frame3, text="main Image ( In Which Image To Be Hidden )", font=("Arial", 16))
                label1.pack()
                image2_label = ctk.CTkButton(enc_frame3, image=image2, text=" ", fg_color="white", state="disabled")
                image2_label.image = image2
                image2_label.pack()
                label2 = ctk.CTkLabel(enc_frame3, text="Secret Image ( Image To Be Hidden )", font=("Arial", 16))
                label2.pack()
                encode_button = ctk.CTkButton(enc_frame3, text="Encode", font=("Arial", 16), command=lambda: self.encode_img(myfile1, myfile2, enc_frame3))
                encode_button.pack()
                main_menu_button = ctk.CTkButton(enc_frame3, text="Main Menu", font=("Arial", 16), command=lambda: self.home(enc_frame3))
                main_menu_button.pack()
                self.update_window_size()

    def decode_frame1_img(self,frame):
        frame.destroy()
        dec_frame1 = ctk.CTkFrame(root, fg_color="white")
        dec_frame1.pack(padx=15, pady=15,fill="both", expand=True)
        dec_frame1.pack_propagate(True)
        dec_label1 = ctk.CTkLabel(dec_frame1, text="Select the image with hidden image", font=("Arial", 16))
        dec_label1.pack()
        select_button = ctk.CTkButton(dec_frame1, text="Select", font=("Arial", 16), command=lambda: self.decode_frame2_img(dec_frame1))
        select_button.pack()
        main_menu_button = ctk.CTkButton(dec_frame1, text="Main Menu", font=("Arial", 16), command=lambda: self.home(dec_frame1))
        main_menu_button.pack()
        note_label = ctk.CTkLabel(dec_frame1, font=("Arial", 12), text_color="red", fg_color="white",
                        text="Note: Secret/Hidden Image will be the part which has \n      proper image in the Extracted Hidden Image.\n\n      It majorly depends on the dimensdions of the images used.")
        note_label.pack()
        self.update_window_size()

    def decode_frame2_img(self,frame):
        dec_frame2 = ctk.CTkScrollableFrame(root, width= 350, height= 450, fg_color="white", orientation="vertical")
        dec_frame2.pack(padx=15, pady=15, fill="both", expand=True)
        dec_frame2.pack_propagate(True)
        myfile = filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error", "No file selected")
        else:
            frame.destroy()
            dec_frame2.pack(padx=15, pady=15,fill="both", expand=True)
            dec_frame2.pack_propagate(True)
            myimage = cv2.imread(myfile)
            my_image = cv2.resize(myimage, (300, 300))
            image_rgb = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
            image = ctk.CTkImage(light_image=Image.fromarray(image_rgb),dark_image=Image.fromarray(image_rgb),size=(300,300))
            image_label = ctk.CTkButton(master= dec_frame2, image=image, state="disabled", fg_color="white", text = "")
            image_label.pack()
            label1 = ctk.CTkLabel(master= dec_frame2, text="Selected Image", font=("Arial", 16))
            label1.pack()
            decode_button = ctk.CTkButton(master= dec_frame2, text="Decode", state="normal", font=("Arial", 16), command=lambda: self.decode_img(myfile, decode_button, label1, dec_frame2))
            decode_button.pack()
            main_menu_button = ctk.CTkButton(master= dec_frame2, text="Main Menu", font=("Arial", 16), command=lambda: self.home(dec_frame2))
            main_menu_button.pack()
            self.update_window_size()	

    def encode_frame1_txt(self,frame):
        frame.destroy()
        enc_frame1 = ctk.CTkFrame(root, fg_color="white")
        enc_frame1.pack(padx=15, pady=15,fill="both", expand=True)
        enc_frame1.pack_propagate(True)
        enc_label1 = ctk.CTkLabel(enc_frame1, text="Select an image to hide text", font=("Arial", 16))
        enc_label1.pack()
        select_button = ctk.CTkButton(enc_frame1, text="Select", font=("Arial", 16), command=lambda: self.encode_frame2_txt(enc_frame1))
        select_button.pack()
        main_menu_button = ctk.CTkButton(enc_frame1, text="Main Menu", font=("Arial", 16), command=lambda: self.home(enc_frame1))
        main_menu_button.pack()
        self.update_window_size()
        
    def encode_frame2_txt(self,frame):
        enc_frame2 = ctk.CTkFrame(root, fg_color="white")
        myfile = filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error", "No file selected")
        else:
            enc_frame2.pack(padx=15, pady=15,fill="both", expand=True)
            enc_frame2.pack_propagate(True)
            frame.destroy()
            myimage = cv2.imread(myfile)
            my_image = cv2.resize(myimage, (300, 300))
            image_rgb = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
            image = ctk.CTkImage(light_image=Image.fromarray(image_rgb),dark_image=Image.fromarray(image_rgb),size=(300,300))
            label1 = ctk.CTkLabel(enc_frame2, text="Selected Image", font=("Arial", 16))
            label1.pack()
            image_label = ctk.CTkButton(enc_frame2, image=image, text=" ", fg_color="white", state="disabled")
            image_label.image = image
            image_label.pack()
            text_label = ctk.CTkLabel(enc_frame2, text="Enter text to hide", font=("Arial", 16))
            text_label.pack()
            text_area = ctk.CTkTextbox(enc_frame2, font=("Arial", 16), width=50, height=5)
            text_area.pack()
            data = text_area.get("1.0", "END")
            encode_button = ctk.CTkButton(enc_frame2, text="Encode", font=("Arial", 16), command=lambda: self.encode_txt(myfile, data, text_area, enc_frame2))
            encode_button.pack()
            main_menu_button = ctk.CTkButton(enc_frame2, text="Main Menu", font=("Arial", 16), command=lambda: self.home(enc_frame2))
            main_menu_button.pack()
            self.update_window_size()

    def decode_frame1_txt(self,frame):
        frame.destroy()
        dec_frame1 = ctk.CTkFrame(root, fg_color="white")
        dec_frame1.pack(padx=15, pady=15,fill="both", expand=True)
        dec_frame1.pack_propagate(True)
        dec_label1 = ctk.CTkLabel(dec_frame1, text="Select the image with hidden text", font=("Arial", 16))
        dec_label1.pack()
        select_button = ctk.CTkButton(dec_frame1, text="Select", font=("Arial", 16), command=lambda: self.decode_frame2_txt(dec_frame1))
        select_button.pack()
        main_menu_button = ctk.CTkButton(dec_frame1, text="Main Menu", font=("Arial", 16), command=lambda: self.home(dec_frame1))
        main_menu_button.pack()
        self.update_window_size()

    def decode_frame2_txt(self,frame):
        dec_frame2 = ctk.CTkFrame(root, fg_color="white")
        myfile = filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error", "No file selected")
        else:
            dec_frame2.pack(padx=15, pady=15,fill="both", expand=True)
            dec_frame2.pack_propagate(True)
            frame.destroy()
            myimage = cv2.imread(myfile)
            my_image = cv2.resize(myimage, (300, 300))
            image_rgb = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
            image = ctk.CTkImage(light_image=Image.fromarray(image_rgb),dark_image=Image.fromarray(image_rgb),size=(300,300))
            label1 = ctk.CTkLabel(dec_frame2, text="Selected Image", font=("Arial", 16))
            label1.pack()
            image_label = ctk.CTkButton(dec_frame2, image=image, text=" ", fg_color="white", state="disabled")
            image_label.image = image
            image_label.pack()
            text_label = ctk.CTkLabel(dec_frame2, text="Text Hidden In Image", font=("Arial", 16))
            text_label.pack()
            text_area = ctk.CTkTextbox(dec_frame2, font=("Arial", 16), width=50, height=5)
            text_area.configure(state="DISABLED")
            text_area.pack()
            decode_button = ctk.CTkButton(dec_frame2, text="Decode", font=("Arial", 16), command=lambda: self.decode_txt(myfile, text_area))
            decode_button.pack()
            main_menu_button = ctk.CTkButton(dec_frame2, text="Main Menu", font=("Arial", 16), command=lambda: self.home(dec_frame2))
            main_menu_button.pack()
            self.update_window_size()

    def encode_txt(self,image,data,text_area,frame):
        text_area.delete("1.0", "END")
        img = cv2.imread(image)
        width, height, _ = img.shape
        img_arr = np.array(list(img.getdata()))

        if img.mode == "p":
            messagebox.showerror("Error", "Image mode is not supported")
            self.decode_frame1_txt(frame)

        channels = 4 if img.mode == 'RGBA' else 3
        pixels = img_arr.shape // channels
        stop_indicator = "$$$"
        stop_indicator_length = len(stop_indicator)
        data += stop_indicator
        byte_message = ''.join([format(ord(i), "08b") for i in data])
        bits = len(byte_message)

        if bits > pixels :
            messagebox.showerror("Error", "Insufficient pixels, need larger image")
            self.decode_frame1_txt(frame)
        else:
            index = 0
            for i in range(pixels):
                for j in range(3):
                    if index < bits:
                        img_arr[i][j] = int(bin(img_arr[i][j])[2:9] + byte_message[index], 2)
                        index += 1  

        img_arr = img_arr.reshape(width, height, channels)                  
        save_path = filedialog.asksaveasfilename(filetypes = ([('png', '*.png')]),defaultextension=".png")
        if save_path:
            # cv2.imwrite(save_path, img_arr)
            img = Image.fromarray(img_arr)
            img.save(save_path)
            messagebox.showinfo("Success", "Text hidden successfully")
            self.home(frame)
    
    def decode_txt(self,image,text_area):
        img = cv2.imread(image)
        img_arr = np.array(list(img.getdata()))
        if img.mode == "p":
            messagebox.showerror("Error", "Image mode is not supported")
            exit()

        channels = 4 if img.mode == 'RGBA' else 3
        pixels = img_arr.shape // channels
        bits = [bin(img_arr[i][j])[-1] for i in range(pixels) for j in range(3)]
        bits = ''.join(bits)
        bytes = [bits[i:i+8] for i in range(0, len(bits), 8)]
        secret_data = [chr(int(byte, 2)) for byte in bytes]
        stop_indicator = "$$"

        if stop_indicator in secret_data:
            text_area.configure(state="NORMAL")
            text_area.delete("1.0", "END")
            text_area.insert("END", secret_data[:secret_data.index(stop_indicator)])
            messagebox.showinfo("Success", "Text extracted successfully")
        else:
            messagebox.showerror("Error", "Couldn't find secret message")

        text_area.configure(state="DISABLED")
    
    def encode_img(self,image1,image2,frame):
        img1 = cv2.imread(image1) 
        img2 = cv2.imread(image2) 
        
        for i in range(img2.shape[0]): 
            for j in range(img2.shape[1]): 
                for l in range(3): 
                    
                    # v1 and v2 are 8-bit pixel values 
                    # of img1 and img2 respectively 
                    v1 = format(img1[i][j][l], '08b') 
                    v2 = format(img2[i][j][l], '08b') 
                    
                    # Taking 4 MSBs of each image 
                    v3 = v1[:4] + v2[:4] 
                    
                    img1[i][j][l]= int(v3, 2) 
                    
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if save_path:
            cv2.imwrite(save_path, img1)
            self.home(frame)

    def decode_img(self,image,decode_button,label1,frame):
        decode_button.configure(state="disabled")
        img = cv2.imread(image) 
        width = img.shape[0] 
        height = img.shape[1] 
        
        image1 = np.zeros((width, height, 3), np.uint8) 
        image2 = np.zeros((width, height, 3), np.uint8) 
        
        for i in range(width): 
            for j in range(height): 
                for l in range(3): 
                    v1 = format(img[i][j][l], '08b') 
                    v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4
                    v3 = v1[4:] + chr(random.randint(0, 1)+48) * 4
                    
                    # Appending data to img1 and img2 
                    image1[i][j][l]= int(v2, 2) 
                    image2[i][j][l]= int(v3, 2) 
        
        best_score = -1
        best_image = None
        best_size = None

        for scale in range(10, 200, 10):  # Test resizing between 10% and 200% of the main image size
            new_width = int(image2.shape[1] * scale / 100)
            new_height = int(image2.shape[0] * scale / 100)

            resized_hidden_image = cv2.resize(image2, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

            # Perform edge detection using Canny
            edges = cv2.Canny(resized_hidden_image, 100, 200)
            edge_score = np.sum(edges)  # Sum of all edge intensities

            # Select the size with the highest edge score
            if edge_score > best_score:
                best_score = edge_score
                best_image = resized_hidden_image
                best_size = (new_width, new_height)
        
	    # These are two images produced from 
	    # the encrypted image save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        save_path1 = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if save_path1:
            cv2.imwrite(save_path1, image1) 
        save_path2 = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if save_path2:
            cv2.imwrite(save_path2, best_image)
        best_image_rgb = cv2.cvtColor(best_image, cv2.COLOR_BGR2RGB)
        best_image_ = ctk.CTkImage(light_image=Image.fromarray(best_image_rgb),dark_image=Image.fromarray(best_image_rgb),size=(300,300))
        hidden_image_label = ctk.CTkButton(master=frame, text="", state="disabled", fg_color="white", image=best_image_)
        hidden_image_label.pack(after=label1)
        label2 = ctk.CTkLabel(master= frame, text="Hidden Image", font=("Arial", 16))
        label2.pack(after=hidden_image_label)
        messagebox.showinfo("Success", "Images extracted and saved successfully")

root = ctk.CTk(fg_color="white")
app = Steganography()
app.main(root)

root.mainloop()

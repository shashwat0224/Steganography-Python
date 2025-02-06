import tkinter
from tkinter import messagebox, filedialog
from customtkinter import *
from PIL import Image
import cv2
import numpy as np
import random

class Steganography:
    def __init__(self):
        pass

    def home(self,frame):
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

        # root.resizable(False, False)
        root.configure(bg="#f0f0f0" )

        # Create a frame
        
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        menu_frame = CTkFrame(root)
        menu_frame.pack(anchor="center", padx=15, pady=15)
        menu_frame.pack_propagate(True)

        img_in_img_button = CTkButton(menu_frame, text="Image in Image", font=("Arial", 16), command=lambda: self.img_menu(menu_frame))
        img_in_img_button.pack(anchor="center", pady=2)

        txt_in_img_button = CTkButton(menu_frame, text="Text in Image", font=("Arial", 16), command=lambda: self.txt_menu(menu_frame))
        txt_in_img_button.pack(anchor="center", pady=2)

        self.update_window_size()

        root.mainloop()

    def img_menu(self,frame):
        frame.destroy()
        img_menu_frame = CTkFrame(root)
        img_menu_frame.pack(padx=15, pady=15)
        img_menu_frame.pack_propagate(True)
        encode_button = CTkButton(img_menu_frame, text="Encode", font=("Arial", 16), command=lambda: self.encode_frame1_img(img_menu_frame))
        encode_button.pack()
        decode_button = CTkButton(img_menu_frame, text="Decode", font=("Arial", 16), command=lambda: self.decode_frame1_img(img_menu_frame))
        decode_button.pack()
        main_menu_button = CTkButton(img_menu_frame, text="Main Menu", font=("Arial", 16), command=lambda: self.home(img_menu_frame))
        main_menu_button.pack()
        self.update_window_size()

    def txt_menu(self,frame):
        frame.destroy()
        txt_menu_frame = CTkFrame(root)
        txt_menu_frame.pack(padx=15, pady=15)
        txt_menu_frame.pack_propagate(True)
        encode_button = CTkButton(txt_menu_frame, text="Encode", font=("Arial", 16), command=lambda: self.encode_frame1_txt(txt_menu_frame))
        encode_button.pack()
        decode_button = CTkButton(txt_menu_frame, text="Decode", font=("Arial", 16), command=lambda: self.decode_frame1_txt(txt_menu_frame))
        decode_button.pack()
        main_menu_button = CTkButton(txt_menu_frame, text="Main Menu", font=("Arial", 16), command=lambda: self.home(txt_menu_frame))
        main_menu_button.pack()
        self.update_window_size()
        
    def encode_frame1_img(self,frame):
        frame.destroy()
        enc_frame1 = CTkFrame(root)
        enc_frame1.pack(padx=15, pady=15)
        enc_frame1.pack_propagate(True)
        enc_label1 = CTkLabel(enc_frame1, text="Select an image to hide another image", font=("Arial", 16))
        enc_label1.pack()
        select_button = CTkButton(enc_frame1, text="Select Image-1", font=("Arial", 16), command=lambda: self.encode_frame2_img(enc_frame1))
        select_button.pack()
        main_menu_button = CTkButton(enc_frame1, text="Main Menu", font=("Arial", 16), command=lambda: self.home(enc_frame1))
        main_menu_button.pack()
        note_label = CTkLabel(enc_frame1, font=("Arial", 12), fg_color="red",
                        text="Note: It is recommended to use images of same dimensions...\n      Otherwise --> Image-1 should be same or larger than Image-2 in dimensions")
        note_label.pack()
        self.update_window_size()

    def encode_frame2_img(self,frame):
        enc_frame2 = CTkFrame(root)
        myfile1 = filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile1:
            messagebox.showerror("Error", "No file selected")
        else:
            myimage = cv2.imread(myfile1)
            my_image = cv2.resize(myimage, (300, 300))
            image_rgb = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
            image1 = CTkImage(light_image=Image.fromarray(image_rgb),dark_image=Image.fromarray(image_rgb))
            image_label = CTkLabel(enc_frame2, image=image1)
            image_label.image = image1
            image_label.pack()
            label1 = CTkLabel(enc_frame2, text="Selected Image ( In Which Image To Be Hidden!! )", font=("Arial", 16))
            label1.pack()
            select_button = CTkButton(enc_frame2, text="Select Image-2", font=("Arial", 16), command=lambda: self.encode_frame3_img( enc_frame2, image1, myfile1))
            select_button.pack()
            main_menu_button = CTkButton(enc_frame2, text="Main Menu", font=("Arial", 16), command=lambda: self.home(enc_frame2))
            main_menu_button.pack()
            enc_frame2.pack(padx=15, pady=15)
            enc_frame2.pack_propagate(True)
            frame.destroy()
            self.update_window_size()

    def encode_frame3_img(self,frame,image1,myfile1):
            enc_frame3 = CTkFrame(root)
            myfile2 = filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
            if not myfile2:
                messagebox.showerror("Error", "No file selected")
            else:
                myimage = cv2.imread(myfile2)
                my_image = cv2.resize(myimage, (300, 300))
                image_rgb = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
                image2 = CTkImage(light_image=Image.fromarray(image_rgb),dark_image=Image.fromarray(image_rgb))
                image1_label = CTkLabel(enc_frame3, image=image1)
                image1_label.image = image1
                image1_label.pack()
                label1 = CTkLabel(enc_frame3, text="main Image ( In Which Image To Be Hidden )", font=("Arial", 16))
                label1.pack()
                image2_label = CTkLabel(enc_frame3, image=image2)
                image2_label.image = image2
                image2_label.pack()
                label2 = CTkLabel(enc_frame3, text="Secret Image ( Image To Be Hidden )", font=("Arial", 16))
                label2.pack()
                encode_button = CTkButton(enc_frame3, text="Encode", font=("Arial", 16), command=lambda: self.encode_img(myfile1, myfile2, enc_frame3))
                encode_button.pack()
                main_menu_button = CTkButton(enc_frame3, text="Main Menu", font=("Arial", 16), command=lambda: self.home(enc_frame3))
                main_menu_button.pack()
                enc_frame3.pack(padx=15, pady=15)
                frame.destroy()
                self.update_window_size()

    def decode_frame1_img(self,frame):
        frame.destroy()
        dec_frame1 = CTkFrame(root)
        dec_frame1.pack(padx=15, pady=15)
        dec_frame1.pack_propagate(True)
        dec_label1 = CTkLabel(dec_frame1, text="Select the image with hidden image", font=("Arial", 16))
        dec_label1.pack()
        select_button = CTkButton(dec_frame1, text="Select", font=("Arial", 16), command=lambda: self.decode_frame2_img(dec_frame1))
        select_button.pack()
        main_menu_button = CTkButton(dec_frame1, text="Main Menu", font=("Arial", 16), command=lambda: self.home(dec_frame1))
        main_menu_button.pack()
        note_label = CTkLabel(dec_frame1, font=("Arial", 12), fg_color="red",
                        text="Note: Secret/Hidden Image will be the part which has \n      proper image in the Extracted Hidden Image.\n\n      It majorly depends on the dimensdions of the images used.")
        note_label.pack()
        self.update_window_size()

    def decode_frame2_img(self,frame):
        dec_frame2 = CTkFrame(root)
        dec_frame2.place(relx=0.5, rely=0.5, anchor= tkinter.CENTER)
        dec_frame2.pack_propagate(True)
        myfile = filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error", "No file selected")
        else:
            myimage = cv2.imread(myfile)
            my_image = cv2.resize(myimage, (300, 300))
            image_rgb = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
            image = CTkImage(light_image=Image.fromarray(image_rgb),dark_image=Image.fromarray(image_rgb))
            image_label = CTkLabel(master= dec_frame2, image=image)
            image_label.image = image
            image_label.pack()
            label1 = CTkLabel(master= dec_frame2, text="Selected Image", font=("Arial", 16))
            label1.pack()
            hidden_image = None
            hidden_image_label = CTkLabel(master= dec_frame2, image=hidden_image)
            hidden_image_label.pack()
            label2 = CTkLabel(master=dec_frame2, text="Hidden Image", font=("Arial", 16))
            label2.pack()
            label2.grid_forget()
            decode_button = CTkButton(master= dec_frame2, text="Decode", state="normal", font=("Arial", 16), command=lambda: self.decode_img(myfile, image_label, hidden_image_label, decode_button, label2))
            decode_button.pack()
            main_menu_button = CTkButton(master= dec_frame2, text="Main Menu", font=("Arial", 16), command=lambda: self.home(dec_frame2))
            main_menu_button.pack()
            frame.destroy()
            self.update_window_size()	

    def encode_frame1_txt(self,frame):
        frame.destroy()
        enc_frame1 = CTkFrame(root)
        enc_frame1.pack(padx=15, pady=15)
        enc_frame1.pack_propagate(True)
        enc_label1 = CTkLabel(enc_frame1, text="Select an image to hide text", font=("Arial", 16))
        enc_label1.pack()
        select_button = CTkButton(enc_frame1, text="Select", font=("Arial", 16), command=lambda: self.encode_frame2_txt(enc_frame1))
        select_button.pack()
        main_menu_button = CTkButton(enc_frame1, text="Main Menu", font=("Arial", 16), command=lambda: self.home(enc_frame1))
        main_menu_button.pack()
        self.update_window_size()
        
    def encode_frame2_txt(self,frame):
        enc_frame2 = CTkFrame(root)
        myfile = filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error", "No file selected")
        else:
            myimage = cv2.imread(myfile)
            my_image = cv2.resize(myimage, (300, 300))
            image_rgb = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
            image = CTkImage(light_image=Image.fromarray(image_rgb),dark_image=Image.fromarray(image_rgb))
            label1 = CTkLabel(enc_frame2, text="Selected Image", font=("Arial", 16))
            label1.pack()
            image_label = CTkLabel(enc_frame2, image=image)
            image_label.image = image
            image_label.pack()
            text_label = CTkLabel(enc_frame2, text="Enter text to hide", font=("Arial", 16))
            text_label.pack()
            text_area = CTkTextbox(enc_frame2, font=("Arial", 16), width=50, height=5)
            text_area.pack()
            data = text_area.get("1.0", END)
            encode_button = CTkButton(enc_frame2, text="Encode", font=("Arial", 16), command=lambda: self.encode_txt(myfile, data, text_area))
            encode_button.pack()
            main_menu_button = CTkButton(enc_frame2, text="Main Menu", font=("Arial", 16), command=lambda: self.home(enc_frame2))
            main_menu_button.pack()
            enc_frame2.pack(padx=15, pady=15)
            enc_frame2.pack_propagate(True)
            frame.destroy()
            self.update_window_size()

    def decode_frame1_txt(self,frame):
        frame.destroy()
        dec_frame1 = CTkFrame(root)
        dec_frame1.pack(padx=15, pady=15)
        dec_frame1.pack_propagate(True)
        dec_label1 = CTkLabel(dec_frame1, text="Select the image with hidden text", font=("Arial", 16))
        dec_label1.pack()
        select_button = CTkButton(dec_frame1, text="Select", font=("Arial", 16), command=lambda: self.decode_frame2_txt(dec_frame1))
        select_button.pack()
        main_menu_button = CTkButton(dec_frame1, text="Main Menu", font=("Arial", 16), command=lambda: self.home(dec_frame1))
        main_menu_button.pack()
        self.update_window_size()

    def decode_frame2_txt(self,frame):
        dec_frame2 = CTkFrame(root)
        myfile = filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error", "No file selected")
        else:
            myimage = cv2.imread(myfile)
            my_image = cv2.resize(myimage, (300, 300))
            image_rgb = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
            image = CTkImage(light_image=Image.fromarray(image_rgb),dark_image=Image.fromarray(image_rgb))
            label1 = CTkLabel(dec_frame2, text="Selected Image", font=("Arial", 16))
            label1.pack()
            image_label = CTkLabel(dec_frame2, image=image)
            image_label.image = image
            image_label.pack()
            text_label = CTkLabel(dec_frame2, text="Text Hidden In Image", font=("Arial", 16))
            text_label.pack()
            hidden_text = "Chulbul Pandey"
            # hidden_text = self.decode(myfile)
            text_area = CTkTextbox(dec_frame2, font=("Arial", 16), width=50, height=5)
            text_area.pack()
            text_area.insert(END, hidden_text)
            text_area.configure(state=DISABLED)
            decode_button = CTkButton(dec_frame2, text="Decode", font=("Arial", 16), command=lambda: self.decode_txt(myfile, text_area))
            decode_button.pack()
            main_menu_button = CTkButton(dec_frame2, text="Main Menu", font=("Arial", 16), command=lambda: self.home(dec_frame2))
            main_menu_button.pack()
            dec_frame2.pack(padx=15, pady=15)
            dec_frame2.pack_propagate(True)
            frame.destroy()
            self.update_window_size()

    def decode_txt(self,image,text_area):
        hidden_text = "kundalhalli"
        text_area.configure(state=NORMAL)
        text_area.delete("1.0", END)
        text_area.insert(END, hidden_text)
        return hidden_text

    def encode_txt(self,image,data,text_area):
        text_area.delete("1.0", END)
        messagebox.showinfo("Success", "Text hidden successfully")

        # newimg.save(filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('png', '*.png')]),defaultextension=".png"))
    
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

    def decode_img(self,image,image_label,hidden_image_label,decode_button,label2):
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
        image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
        best_image_rgb = cv2.cvtColor(best_image, cv2.COLOR_BGR2RGB)
        image1_pil = CTkImage(light_image=Image.fromarray(image1_rgb),dark_image=Image.fromarray(image1_rgb),size=(300,300))
        best_image_pil = CTkImage(light_image=Image.fromarray(best_image_rgb),dark_image=Image.fromarray(best_image_rgb),size=(300,300)) 
        image_label.configure(image=image1_pil)
        hidden_image_label.configure(image=best_image_pil)
        image_label.image = image1_pil
        image_label.pack()
        hidden_image_label.image = best_image_pil
        hidden_image_label.pack()
        label2.pack()
        decode_button.configure(state="disabled")
        self.update_window_size()
        messagebox.showinfo("Success", "Images extracted and saved successfully")

root = CTk()
app = Steganography()
app.main(root)

root.mainloop()

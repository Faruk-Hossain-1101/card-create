import tkinter
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter import filedialog
from tkinter import ttk
import pyqrcode
import png


def clear_input_data():
    customer_name_entry.delete(0, tkinter.END)
    product_name_entry.delete(0, tkinter.END)
    weight_entry.delete(0, tkinter.END)
    
def select_file():
    global product_image
    try:
        path = filedialog.askopenfilename(title="Choose Product Image", filetypes=[('image files','*.jpg'), ('image files','*.png')])
        j_img= Image.open(path)
        j_img=j_img.resize((150, 100), Image.ANTIALIAS) 
        j_img=ImageTk.PhotoImage(j_img)
        label= tkinter.Label(image_select_frame, image= j_img)
        label.image= j_img
        label.grid(row=1, column=0)
        product_image = path
    except:
        product_image = ""

def genarate_image():
    customer_name = customer_name_entry.get()
    product_name = product_name_entry.get()
    weight = weight_entry.get()
    karat = karat_entry.get()
    gold = gold_entry.get()
    copper = copper_entry.get()
    silver = silver_entry.get()
    other = other_entry.get()
    
    if not customer_name:
        tkinter.messagebox.showwarning(title="Error", message="Customer name is required.")
    elif not product_name:
        tkinter.messagebox.showwarning(title="Error", message="Product name is required.")
    elif not weight:
        tkinter.messagebox.showwarning(title="Error", message="Weight is required.")
    elif not karat:
        tkinter.messagebox.showwarning(title="Error", message="Karat is required.")
    elif not gold:
        tkinter.messagebox.showwarning(title="Error", message="Gold percentage is required.")
    elif not copper:
        tkinter.messagebox.showwarning(title="Error", message="Copper percentage is required.")
    elif not silver:
        tkinter.messagebox.showwarning(title="Error", message="Silver percentage is required.")
    elif not other:
        tkinter.messagebox.showwarning(title="Error", message="Other percentage is required.")
    else:
        img = Image.open('nre_n.jpg')
        fnt = ImageFont.truetype('roboto/RobotoCondensed-Regular.ttf', 25)
        d = ImageDraw.Draw(img)

        # Name
        d.text((30, 150), "Customer Name  :", font=fnt, fill=(0, 0, 0))
        d.text((250, 150), customer_name, font=fnt, fill=(0, 0, 0))

        # Phone
        d.text((30, 200), "Phone  :", font=fnt, fill=(0, 0, 0))
        d.text((150, 200), "9775797992", font=fnt, fill=(0, 0, 0))

        # Item
        d.text((30, 250), "Product  :", font=fnt, fill=(0, 0, 0))
        d.text((170, 250), product_name, font=fnt, fill=(0, 0, 0))


        # Weight
        d.text((30, 300), "Weight  :", font=fnt, fill=(0, 0, 0))
        d.text((150, 300), weight+' Grm', font=fnt, fill=(0, 0, 0))

        # Carate
        d.text((30, 350), "Karat  :", font=fnt, fill=(0, 0, 0))
        d.text((150, 350), karat, font=fnt, fill=(0, 0, 0))

        d.line((30, 400, 670, 400), fill=(251, 223, 126), width=5)
        d.line((700, 122, 700, 568), fill=(251, 223, 126), width=2)


        # Metal Detail Report
        d.text((240, 420), "Metal Detail Report", font=fnt, fill=(0, 0, 0))

        m_font = ImageFont.truetype('roboto/Roboto-Black.ttf', 20)

        # Gold
        d.text((70, 475), "Gold :", font=m_font, fill=(150, 75, 0))
        d.text((150, 475), gold+'%', font=m_font, fill=(150, 75, 0))

        # Copper
        d.text((400, 475), "Copper :", font=m_font, fill=(150, 75, 0))
        d.text((500, 475), copper+'%', font=m_font, fill=(150, 75, 0))

        # Silver
        d.text((70, 525), "Silver :", font=m_font, fill=(150, 75, 0))
        d.text((150, 525), silver+'%', font=m_font, fill=(150, 75, 0))

        # Other
        d.text((400, 525), "Other :", font=m_font, fill=(150, 75, 0))
        d.text((500, 525), other+'%', font=m_font, fill=(150, 75, 0))
        
        # Address
        a_font = ImageFont.truetype('roboto/Roboto-LightItalic.ttf', 18)
        d.text((340, 578), "Ronogram Bridge, Kandi, Murshidabad, 742136", font=a_font, fill=(0, 0, 0))


        # QR Code implementation
        url = pyqrcode.create("NRE Jewellery Ranagram Bridge,"+customer_name+", Product: "+product_name+", Weight: "+weight+"Grm")
        url.png('myqr.png', scale = 6)
        
        qr = Image.open('myqr.png')
        qr = qr.resize((200, 200)) 
        Image.Image.paste(img, qr, (775, 125))

        # Jewellery Image Insert
        try:
            jewllery = Image.open(product_image)
            jewllery = jewllery.resize((300, 240)) 
            Image.Image.paste(img, jewllery, (725, 325))
        except:
            print("Product image is blank!");


#         img.show()
        
        hsl = filedialog.asksaveasfile(mode='w', defaultextension=".jpg", initialfile=customer_name)
        if hsl is None:
            return
        
        img.save(hsl)
        tkinter.messagebox.showinfo("Success", "Image created successfully!")
        clear_input_data()
            
        
        
m = tkinter.Tk()
m.title('NRE')
frame = tkinter.Frame(m)
frame.pack()

# Customer inforamation
customer_info_frame =tkinter.LabelFrame(frame, text="Product & Customer")
customer_info_frame.grid(row= 0, column=0, padx=20, pady=10)

# First Row
customer_name_label = tkinter.Label(customer_info_frame, text="Customer Name")
customer_name_label.grid(row=0, column=0)
product_name_label = tkinter.Label(customer_info_frame, text="Product Name")
product_name_label.grid(row=0, column=1)

# Second Row
customer_name_entry = tkinter.Entry(customer_info_frame, width=30)
customer_name_entry.grid(row=1, column=0, ipady=4)
product_name_entry = tkinter.Entry(customer_info_frame, width=30)
product_name_entry.grid(row=1, column=1, ipady=4)


# Third Row
weight_label = tkinter.Label(customer_info_frame, text="Weight (gram)")
weight_label.grid(row=2, column=0)
karat_label = tkinter.Label(customer_info_frame, text="Karat")
karat_label.grid(row=2, column=1)

# Second Row
weight_entry = tkinter.Entry(customer_info_frame, width=30)
weight_entry.grid(row=3, column=0, ipady=4)
karat_entry = tkinter.Entry(customer_info_frame, width=30)
karat_entry.grid(row=3, column=1, ipady=4)
karat_entry.insert(1, '22')

for widget in customer_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
    
    
# Metal inforamation
metal_info_frame =tkinter.LabelFrame(frame, text="Metal inforamation")
metal_info_frame.grid(row= 1, column=0, padx=20, pady=10)

# Second grid First Row
gold_label = tkinter.Label(metal_info_frame, text="Gold")
gold_label.grid(row=0, column=0)
copper_label = tkinter.Label(metal_info_frame, text="Copper")
copper_label.grid(row=0, column=1)
    
# Second grid second row
gold_entry = tkinter.Entry(metal_info_frame, width=20)
gold_entry.grid(row=1, column=0, ipady=4)
gold_entry.insert(1, '91.60')

copper_entry =tkinter.Entry(metal_info_frame, width=20)
copper_entry.grid(row=1, column=1, ipady=4)
copper_entry.insert(1, '3.10')

# Second grid Third Row
silver_label = tkinter.Label(metal_info_frame, text="Silver")
silver_label.grid(row=2, column=0)
other_label = tkinter.Label(metal_info_frame, text="Other")
other_label.grid(row=2, column=1)
    
# Second grid Fourth row
silver_entry = tkinter.Entry(metal_info_frame, width=20)
silver_entry.grid(row=3, column=0, ipady=4)
silver_entry.insert(1, '5.30')

other_entry =tkinter.Entry(metal_info_frame, width=20)
other_entry.grid(row=3, column=1, ipady=4)
other_entry.insert(1, '0.0')


for widget in metal_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Image selection
image_select_frame =tkinter.LabelFrame(frame, text="Product Image")
image_select_frame.grid(row= 2, column=0, padx=20, pady=10)
    
# Second grid First Row
image_entry= ttk.Button(image_select_frame, text="Choose Product Image", command= select_file)
image_entry.grid(row=0, column=0, padx=20, pady=10)

# Button
button = tkinter.Button(frame, text="Generate", command= genarate_image, bg="green", fg="white")
button.grid(row=3, column=0, padx=20, pady=10)



m.mainloop()
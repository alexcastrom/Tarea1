import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time
import pyperclip



c=0
d=0

class Application(ttk.Frame):
    
	def __init__(self, main_window):
		super().__init__(main_window)
		main_window.title("Tarea 1")
		main_window.configure(width=500, height=300)
		main_window.columnconfigure(1, weight=1)
		main_window.rowconfigure(1, weight=1)
		
		self.label3 = ttk.Label(self, text="|")
		self.label3.grid(row=0, column=1)		
		self.label3 = ttk.Label(self, text="|")
		self.label3.grid(row=1, column=1)		
		self.label3 = ttk.Label(self, text="|")
		self.label3.grid(row=2, column=1)		
		self.label3 = ttk.Label(self, text="|")
		self.label3.grid(row=3, column=1)		
		self.label3 = ttk.Label(self, text="|")
		self.label3.grid(row=4, column=1)
		
		self.label = ttk.Label(self, text="SuperSol")####################SUPERSOL
		self.label.grid(row=0, column=0)
		
		self.one = ttk.Button(self, text = "Login")
		#self.one["command"] = self.say_hi
		self.one["command"] = self.login
		self.one.grid(row=1, column=0)
		
		self.two = tk.Button(self, text="Registrar")
		self.two["command"] = self.reg
		self.two.grid(row=2, column=0)
		
		self.tr3 = tk.Button(self, text="Cambio Contraseña")
		self.tr3["command"] = self.chpass
		self.tr3.grid(row=3, column=0)
		
		self.tr4 = tk.Button(self, text="Olvide pass")
		self.tr4["command"] = self.forpass
		self.tr4.grid(row=4, column=0)
		
		self.label2 = ttk.Label(self, text="Comenta")##############COMENTA
		self.label2.grid(row=0, column=2)
		
		self.tr5 = tk.Button(self, text="Login")
		self.tr5["command"] = self.loginc
		self.tr5.grid(row=1, column=2)
		
		self.tr6 = tk.Button(self, text="Registrar")
		self.tr6["command"] = self.regc
		self.tr6.grid(row=2, column=2)
		
		self.tr7 = tk.Button(self, text="Cambio Contraseña")
		self.tr7["command"] = self.chpassc
		self.tr7.grid(row=3, column=2)
		
		self.tr8 = tk.Button(self, text="Olvide pass")
		self.tr8["command"] = self.forpassc
		self.tr8.grid(row=4, column=2)
		self.grid(sticky="nsew")
		
		#self.x = tk.Button(self, text="Salir", fg="red",command=self.master.destroy)
		#self.x.pack(side="bottom")


		
	def login(self): ######################################SOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL
		
		driver.get("https://www.google.com/")
		driver.get("http://www.supersol.es/")

		elem = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/a/em').click() #abrir login

		time.sleep(1)

		elem = driver.find_element_by_name("email") #nombre
		elem.send_keys("tareaybasura@gmail.com")

		elem = driver.find_element_by_name("pass") #pass
		elem.send_keys("aaaaaa")
		pyautogui.hotkey("return")
		global c
		c=1
		
	def reg(self): ###################registrar
	
		drivers = webdriver.Firefox()
		drivers.get("http://www.supersol.es/")

		elem = drivers.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/a').click() #abrir reg

		time.sleep(3) #esperar a que cargue

		action = ActionChains(drivers)
		elem = drivers.find_element_by_name("aceptoCondiciones") #check condition
		action.click(elem)
		action.perform()#PORFINAAAAAAAAAAAAAAAAAAAA

		elem = drivers.find_element_by_name("nombre") #nombre
		elem.send_keys("lala")

		elem = drivers.find_element_by_name("apellidos") #apellido
		elem.send_keys("lele lolo")

		elem = drivers.find_element_by_name("codigoPostal") #codpostal
		elem.send_keys("1234")
		# es necesario para moverse al nacimientoya que no permite pegar un elemento, es necesario escribirlo
		pyautogui.hotkey('Tab')
		pyautogui.write('13051998')
		# por alguna razon desde el correo en adelante son elementos inalcanzables por keybord, por ende es necesario navegar de manera "manual"
		pyautogui.hotkey('Tab') 
		pyperclip.copy("ll@fuluj.com")
		pyautogui.hotkey("ctrl", "v")
		pyautogui.hotkey('Tab') #contraseña
		pyperclip.copy("asdasd")
		pyautogui.hotkey("ctrl", "v")
		pyautogui.hotkey('Tab') #confirmar contraseña
		pyperclip.copy("asdasd")
		pyautogui.hotkey("ctrl", "v")
		pyautogui.hotkey("return")
		
		
		time.sleep(4)
		drivers.quit()
		
	def chpass(self): ##########################CAMBIAR CONTRASEÑA
		if c==1:
			time.sleep(2)
			driver.get("http://www.supersol.es/area-personal/mis-datos/")

			elem = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/form/fieldset/div[1]/a').click() #editar

			elem = driver.find_element_by_name("pass") #pass
			elem.send_keys("aaaaaa")

			elem = driver.find_element_by_name("nuevoPass") #nuevapass
			elem.send_keys("aaaaaa")

			elem = driver.find_element_by_name("nuevoPassConfirmar") #passconfirm
			elem.send_keys("aaaaaa")

			pyautogui.hotkey("return")
			
		
	def forpass(self):
		drivers = webdriver.Firefox()
		drivers.get("http://www.supersol.es/")

		elem = drivers.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/a/em').click() #abrir login

		time.sleep(1)

		elem = drivers.find_element_by_class_name("btnRestablecerPass").click() #nombre
		time.sleep(1)

		elem = drivers.find_elements_by_name("email") #ya que existen dos elementos con el mismo nombre, es necesario encontrar su lista
		elem[1].send_keys("ivont_e609n@fuluj.com") #para este segmento es necesario la

		pyautogui.hotkey('Tab')

		pyautogui.hotkey("return")
		
		time.sleep(4)
		drivers.quit()
		
#######################################################################################################COMENTA
	def loginc(self): ###########LOGIN
	
		driver.get("http://www.comenta.cl/mi-cuenta/")
		elem = driver.find_element_by_id("username")
		elem.send_keys("tareaybasura@gmail.com")
		elem = driver.find_element_by_id("password")
		elem.send_keys("Asd123.-.,")
		elem = driver.find_element_by_name("login").click()
		global d
		d=1
		
	def regc(self): ###################registrar
		drivers = webdriver.Firefox()
		drivers.get("http://www.comenta.cl/mi-cuenta/")
		elem = drivers.find_element_by_id("reg_email")
		elem.send_keys("tareaybasura@gmail.com")
		elem = drivers.find_element_by_id("reg_password").click()
		elem = drivers.find_element_by_id("reg_password")
		elem.send_keys("Asd123.-.,")
		pyautogui.hotkey('enter')
		elem = drivers.find_element_by_name("register").click()
		time.sleep(10)
		drivers.quit()
		
		
	def chpassc(self): ##########################CAMBIAR CONTRASEÑA
		if d==1:
			driver.get("http://www.comenta.cl/mi-cuenta/edit-account/")
			elem = driver.find_element_by_id("account_first_name")
			elem.send_keys("asdasd")
			elem = driver.find_element_by_id("account_last_name")
			elem.send_keys("dsadsa")
			elem = driver.find_element_by_id("password_current")
			elem.send_keys("Asd123.-.,")
			elem = driver.find_element_by_id("password_1").click()
			elem = driver.find_element_by_id("password_1")
			elem.send_keys("Asd123.-.,")
			elem = driver.find_element_by_id("password_2").click()
			elem = driver.find_element_by_id("password_2")
			elem.send_keys("Asd123.-.,")
			pyautogui.hotkey('enter')
			
		
	def forpassc(self):
		drivers = webdriver.Firefox()
		drivers.get("http://www.comenta.cl/mi-cuenta/lost-password/")
		time.sleep(10)
		elem = drivers.find_element_by_id("user_login")
		elem.send_keys("tareaybasura@gmail.com")
		elem = drivers.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/main/article/div/div/form/p[3]/input[2]").click()
		time.sleep(4)
		drivers.quit()

		



driver = webdriver.Firefox()


main_window = tk.Tk()
app = Application(main_window)
app.mainloop()



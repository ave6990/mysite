from pyscript import display
from datetime import datetime

def display_date():
  now = datetime.now()
  display(now.strftime("%Y-%m-%d"))

from js import document
from pyodide.ffi import create_proxy

def button_click(event):
  tr = event.target.parentNode

  if event.ctrlKey:
    tr.classList.toggle("selected")

def setup():
  click_proxy = create_proxy(button_click)
  cells = document.getElementsByTagName("td")

  for el in cells:
    el.addEventListener("click", click_proxy)


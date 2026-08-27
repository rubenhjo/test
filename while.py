a = ""
while True:
  if a == "Stopp":
    print("Koding er gøy!!!")
    break
  else:
      a = input ("Hva heter du?")
      for i in range (0,9):
          print(f"{a} Elsker koding!!")

def ortalama_hesapla(kullanicinin_girdigi_sayilar):
   total = sum(kullanicinin_girdigi_sayilar)
   girilen_sayilarin_adeti = len(kullanicinin_girdigi_sayilar)
   sayilarin_ortalamasi = total / girilen_sayilarin_adeti
   print(f"Girdiğiniz sayilarin ortalamasi: {sayilarin_ortalamasi}")
   
ortalama_hesapla([1,3,5,10,20,50,100]) #you can enter the numbers here

#This code will help you calculate the average of the numbers you enter.

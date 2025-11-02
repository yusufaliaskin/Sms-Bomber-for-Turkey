import tkinter as tk

def kontrol_et():
    tc_no_str = entry_tc.get()

    if not (len(tc_no_str) == 11 and tc_no_str.isdigit()):
        label_sonuc.config(text="Tüm T.C hanelerini dogru giriniz!!", fg="red")
        label_detay.config(text="")
        return

    tc_no_rakamlari = [int(hane) for hane in tc_no_str]

    ilk_on_hane_toplami = sum(tc_no_rakamlari[0:10])
    hesaplanan_kalan = ilk_on_hane_toplami % 10
    onbirinci_hane = tc_no_rakamlari[10]

    detay_mesaji = (
        f"İlk 10 Hane Toplamı: {ilk_on_hane_toplami}\n"
        f"Hesaplanan 11. Hane (Kalan): {hesaplanan_kalan}\n"
        f"Girdiğiniz Son Hane: {onbirinci_hane}"
    )
    
    label_detay.config(text=detay_mesaji)

    if hesaplanan_kalan == onbirinci_hane:
        label_sonuc.config(text="Doğru. Rakamlar eşleşiyor.", fg="green")
    else:
        label_sonuc.config(text="Yanlış. Rakamlar eşleşmiyor.", fg="red")


pencere = tk.Tk()
pencere.title("TCKN 11. Hane Kural Kontrolü")
pencere.geometry("350x250")
pencere.resizable(False, False)

label_talimat = tk.Label(pencere, text="T.C. Kimlik Numarasını giriniz:", font=("Arial", 12))
label_talimat.pack(pady=10)

entry_tc = tk.Entry(pencere, width=20, font=("Arial", 14), justify="center")
entry_tc.pack(pady=5)

buton_kontrol = tk.Button(pencere, text="Kontrol Et", command=kontrol_et, font=("Arial", 10, "bold"))
buton_kontrol.pack(pady=10)

label_sonuc = tk.Label(pencere, text="", font=("Arial", 12, "bold"))
label_sonuc.pack(pady=5)

label_detay = tk.Label(pencere, text="", justify="left")
label_detay.pack(pady=5)

pencere.mainloop()

from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading
import sys
import subprocess

# Gerekli kütüphaneleri kontrol et ve eksik olanları yükle - Optimize edilmiş
def check_and_install_libraries():
    required_libraries = ['colorama', 'pyfiglet', 'rich', 'psutil', 'requests']
    missing_libraries = []
    
    for lib in required_libraries:
        try:
            __import__(lib)
        except ImportError:
            missing_libraries.append(lib)
    
    if missing_libraries:
        print(f"{Fore.YELLOW}Eksik kütüphaneler tespit edildi. Yükleniyor...{Style.RESET_ALL}")
        for lib in missing_libraries:
            print(f"Yükleniyor: {lib}")
            # Daha hızlı yükleme için quiet modunu kullan
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib, "-q"])
        print(f"{Fore.GREEN}Tüm kütüphaneler başarıyla yüklendi!{Style.RESET_ALL}")
        # Gereksiz gecikmeyi azalt
        sleep(0.5)

# Kütüphaneleri kontrol et ve yükle
check_and_install_libraries()

# Şimdi gerekli tüm kütüphaneleri içe aktarabiliriz
import pyfiglet
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.layout import Layout
from rich.live import Live
from rich.align import Align
from rich.style import Style
from rich.prompt import Prompt
from rich import box
import psutil
import socket
from datetime import datetime
import requests

# Konsol ve zengin çıktı için gerekli nesneleri oluştur
console = Console()

# Renk teması - Daha uyumlu ve profesyonel renkler
theme = {
    "primary": "#3498db",       # Mavi tonu
    "secondary": "#2980b9",    # Koyu mavi
    "accent": "#9b59b6",       # Mor
    "warning": "#f39c12",      # Turuncu
    "error": "#e74c3c",        # Kırmızı
    "success": "#2ecc71",      # Yeşil
    "info": "#1abc9c",         # Turkuaz
    "background": "#2c3e50",   # Koyu lacivert
    "text": "#ecf0f1",         # Açık gri
    "muted": "#95a5a6",        # Gri
    "highlight": "#f1c40f"     # Sarı
}

# İnternet bağlantısını kontrol et
def check_internet_connection():
    try:
        requests.get("https://google.com", timeout=3)
        return True
    except:
        return False

# Açılış animasyonu göster - Optimize edilmiş
def show_startup_animation():
    # Ekranı temizle
    system("cls||clear")
    
    # Animasyonlu başlık - optimize edilmiş
    for i in range(3):  # Döngü sayısını azalt
        system("cls||clear")
        if i % 2 == 0:
            console.print(f"\n\n[bold {theme['primary']}]Yükleniyor...[/]\n", justify="center")
        else:
            console.print(f"\n\n[bold {theme['secondary']}]Yükleniyor...[/]\n", justify="center")
        sleep(0.1)  # Gecikmeyi azalt
    
    # ASCII logo oluştur (geliştirilmiş font seçimi)
    fonts = ["slant", "banner3-D", "standard", "big"]
    logo = pyfiglet.figlet_format("SMS PANEL", font=fonts[0])
    
    # Optimize edilmiş logo animasyonu - daha az renk ve daha kısa gecikmeler
    colors = [theme["primary"], theme["accent"], theme["highlight"]]  # Renk sayısını azalt
    for color in colors:
        system("cls||clear")
        # Logo etrafına dekoratif panel ekle
        logo_panel = Panel(
            f"[{color}]{logo}[/]", 
            border_style=color,
            box=box.DOUBLE,
            padding=(1, 3)
        )
        console.print(logo_panel, justify="center")
        sleep(0.15)  # Gecikmeyi azalt
    
    # Son logo gösterimi - geliştirilmiş stil
    system("cls||clear")
    final_logo_panel = Panel(
        f"[{theme['primary']}]{logo}[/]",
        border_style=theme["primary"],
        box=box.DOUBLE_EDGE,
        padding=(1, 3),
        title=f"[bold {theme['highlight']}]✨ Hoş Geldiniz ✨[/]",
        subtitle=f"[{theme['muted']}]v1.0[/]"
    )
    console.print(final_logo_panel, justify="center")
    
    # Geliştirilmiş alt başlık
    console.print(f"[bold {theme['secondary']}]✦ Modern SMS Gönderim Paneli ✦[/]", justify="center")
    console.print("\n")
    
    # Optimize edilmiş yükleme animasyonu
    with Progress(
        SpinnerColumn(style=theme["accent"]),
        TextColumn(f"[bold {theme['info']}]🚀 Sistem Başlatılıyor..."),
        BarColumn(complete_style=theme["success"], finished_style=theme["success"]),
        TextColumn(f"[bold {theme['primary']}]{{task.percentage:.0f}}%"),
        TimeElapsedColumn(),
        expand=True
    ) as progress:
        task = progress.add_task("[green]Yükleniyor...", total=100)
        
        # Geliştirilmiş yükleme adımları
        steps = [
            "✓ Servisler kontrol ediliyor",
            "✓ Bağlantı testi yapılıyor",
            "✓ Arayüz hazırlanıyor",
            "✓ Sistem hazırlanıyor"
        ]
        
        # Adımları ve ağırlıklarını tanımla - Daha verimli yükleme
        weights = [20, 30, 25, 25]  # Toplam 100
        current_step = 0
        
        for i, step in enumerate(steps):
            progress.update(task, description=f"[bold {theme['info']}]{step}")
            for j in range(weights[i]):
                sleep(0.01)  # Gecikmeyi azalt
                progress.update(task, advance=1)
            current_step += weights[i]
    
    # Geliştirilmiş başarılı mesajı
    success_panel = Panel(
        "[bold]Tüm servisler aktif ve çalışıyor![/]",
        title=f"[bold {theme['success']}]✅ Sistem Başarıyla Başlatıldı[/]",
        border_style=theme["success"],
        box=box.ROUNDED
    )
    console.print(success_panel, justify="center")
    sleep(0.5)  # Gecikmeyi azalt

# Servis listesini oluştur
servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

# Dashboard bilgilerini göster
def show_dashboard():
    # Sistem bilgilerini al
    is_online = check_internet_connection()
    connection_status = "✔ Online" if is_online else "❌ Offline"
    connection_color = theme["success"] if is_online else theme["error"]
    service_count = len(servisler_sms)
    try:
        ip_address = socket.gethostbyname(socket.gethostname())
    except:
        ip_address = "Bilinmiyor"
    system_time = datetime.now().strftime("%H:%M:%S")
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent

    
    # Modern başlık
    header = Panel(
        Align.center(
            Text("Sistem Bilgileri", style=f"bold {theme['primary']}"),
            vertical="middle"
        ),
        border_style="purple",
        box=box.ROUNDED,
        padding=(1, 2),
        width=60
    )
    
    # Modern sistem bilgileri tablosu
    system_table = Table(
        show_header=False,
        box=box.SIMPLE_HEAD,
        expand=False,
        width=58,
        border_style="purple",
        highlight=True
    )
    
    system_table.add_column("Bilgi", style=f"bold {theme['text']}", width=14, justify="left")
    system_table.add_column("Değer", style=theme["text"], width=44, justify="left")
    
    # Bağlantı durumu için stil
    connection_style = Style(color="red", bold=True)
    connection_text = Text("Offline", style=connection_style)
    
    # Gelişmiş ilerleme çubukları
    cpu_bar = "[" + "█" * int(cpu_usage / 10) + "░" * (10 - int(cpu_usage / 10)) + "]"
    ram_bar = "[" + "█" * int(ram_usage / 10) + "░" * (10 - int(ram_usage / 10)) + "]"
    
    # Gelişmiş tablo satırları
    system_table.add_row("[bold cyan]Bağlantı[/]", connection_text)
    system_table.add_row("[bold cyan]Servisler[/]", f"[bold cyan]{service_count}[/] aktif servis")
    system_table.add_row("[bold cyan]IP Adresi[/]", f"[bold cyan]{ip_address}[/]")
    system_table.add_row("[bold cyan]Saat[/]", f"[bold green]{system_time}[/]")
    system_table.add_row("[bold cyan]CPU[/]", f"{cpu_bar} [bold red]%{cpu_usage}[/]")
    system_table.add_row("[bold cyan]RAM[/]", f"{ram_bar} [bold magenta]%{ram_usage}[/]")
    
    # Sistem bilgileri paneli - Daha kompakt panel
    system_panel = Panel(
        system_table,
        title="[bold]Sistem Bilgileri[/]",
        border_style=theme["accent"],
        box=box.ROUNDED,
        padding=(0, 1),  # Padding'i azalt
        width=60,  # Genişliği sınırla
        title_align="left"
    )
    
    # Panelleri yazdır - Sola hizalanmış görünüm
    console.print(Align.left(header))
    console.print(Align.left(system_panel))

# Ana menüyü göster - Daha kompakt ve estetik tasarım
def show_main_menu():
    # Menü başlığı - Daha kompakt başlık
    menu_title = Panel(
        Align.left(
            Text("📱 ANA MENÜ", style=f"bold {theme['primary']}"),
            vertical="middle"
        ),
        border_style=theme["primary"],
        box=box.ROUNDED,
        padding=(0, 1),  # Padding'i azalt
        width=60  # Genişliği sınırla
    )
    
    # Modern menü seçenekleri tablosu
    menu_table = Table(
        show_header=False,
        box=box.SIMPLE_HEAD,
        expand=False,
        width=60,
        border_style="purple",
        highlight=True
    )
    
    menu_table.add_column("Seçenek", style="bold cyan", width=6, justify="center")
    menu_table.add_column("Açıklama", style="white", width=54, justify="left")
    
    # Modern menü seçenekleri
    menu_options = [
        ("[1]", "[bold cyan]Normal SMS Gönder[/] - Tek tek SMS gönderimi"),
        ("[2]", "[bold magenta]Turbo SMS Gönder[/] - Hızlı çoklu SMS gönderimi"),
        ("[3]", "[bold green]Servisleri Göster[/] - Aktif servisleri listele"),
        ("[0]", "[bold red]Çıkış[/] - Programdan çık")
    ]
    for option, description in menu_options:
        menu_table.add_row(option, description)
    
    # Modern menü paneli
    menu_panel = Panel(
        menu_table,
        title="[bold cyan]MENÜ SEÇENEKLERİ[/]",
        border_style="purple",
        box=box.ROUNDED,
        padding=(1, 2),
        width=60,
        title_align="center"
    )
    
    # Menüyü göster - Sola hizalanmış görünüm
    console.print(Align.left(menu_title))
    console.print(Align.left(menu_panel))
    
    # Animasyonlu seçim promptu - Daha kısa bekleme süresi
    with console.status("[bold green]Seçim bekleniyor...", spinner="dots"):
        sleep(0.2)  # Daha kısa animasyon için bekleme
    
    # Kullanıcı girişi al - Daha kompakt prompt
    return Prompt.ask("[bold yellow]👉[/]", console=console)

            
# Servisleri göster - Daha kompakt ve estetik tasarım
def show_services():
    system("cls||clear")
    show_dashboard()  # Dashboard'u göster
    
    # Modern başlık paneli
    service_title = Panel(
        Align.center(
            Text("SERVİSLER", style="bold cyan"),
            vertical="middle"
        ),
        border_style="purple",
        box=box.ROUNDED,
        padding=(1, 2),
        width=60
    )
    
    # Servisleri kategorilere ayırma
    populer_servisler = ["Getir", "Yemeksepeti", "Trendyol", "Hepsiburada"]
    yemek_servisler = ["KahveDunyasi", "Wmf", "Bim", "Yemeksepeti"]
    alisveris_servisler = ["Trendyol", "Hepsiburada", "Englishhome", "Bim"]
    diger_servisler = [s for s in servisler_sms if s not in populer_servisler and s not in yemek_servisler and s not in alisveris_servisler]
    
    # Ana tablo
    service_table = Table(
        title="",
        box=box.ROUNDED,
        border_style="purple",
        padding=(1, 1),
        highlight=True,
        width=80
    )
    
    service_table.add_column("Kategori", style="bold cyan", width=20)
    service_table.add_column("Servisler", style="bold white")
    
    # Servisleri kontrol etme animasyonu
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold green]Servisler kontrol ediliyor..."),
        transient=True
    ) as progress:
        task = progress.add_task("Kontrol ediliyor...", total=len(servisler_sms))
        
        # Kategorilere göre servisleri işleme
        for i, service in enumerate(servisler_sms):
            sleep(0.01)  # Daha kısa bekleme süresi ile hızlandırılmış animasyon
            progress.update(task, advance=1)
    
    # Popüler servisler
    populer_text = ""
    for service in populer_servisler:
        if service in servisler_sms:
            populer_text += f"[bold green]✓[/] [bold white]{service}[/]   "
    
    # Yemek servisleri
    yemek_text = ""
    for service in yemek_servisler:
        if service in servisler_sms:
            yemek_text += f"[bold green]✓[/] [bold white]{service}[/]   "
    
    # Alışveriş servisleri
    alisveris_text = ""
    for service in alisveris_servisler:
        if service in servisler_sms:
            alisveris_text += f"[bold green]✓[/] [bold white]{service}[/]   "
    
    # Diğer servisler
    diger_text = ""
    for service in diger_servisler:
        if service in servisler_sms:
            diger_text += f"[bold green]✓[/] [bold white]{service}[/]   "
    
    # Tabloyu doldurma
    service_table.add_row("[bold cyan]Popüler Servisler[/]", populer_text)
    service_table.add_row("[bold cyan]Yemek Servisleri[/]", yemek_text)
    service_table.add_row("[bold cyan]Alışveriş Servisleri[/]", alisveris_text)
    service_table.add_row("[bold cyan]Diğer Servisler[/]", diger_text)
    
    # Toplam servis sayısı - Daha düzenli özet paneli
    summary = Panel(
        f"[bold cyan]Toplam: [bold white]{len(servisler_sms)}[/] Aktif Servis[/]",
        border_style="cyan",
        box=box.ROUNDED,
        padding=(1, 2),
        width=80
    )
    
    # Animasyonlu geçiş efekti - Daha kısa bekleme süresi
    with console.status("[bold green]Servis listesi yükleniyor...", spinner="dots"):
        sleep(0.2)  # Daha kısa animasyon için bekleme
    
    # Panelleri yazdır - Ortalanmış görünüm
    console.print(Align.center(service_title))
    console.print(Align.center(service_table))
    console.print(Align.center(summary))
    
    # Geri dönüş butonu - Daha kompakt buton
    back_panel = Panel(
        "[bold yellow]👉 Menüye dönmek için Enter tuşuna basın[/]",
        border_style=theme["warning"],
        box=box.ROUNDED,
        padding=(0, 1),  # Padding'i azalt
        width=40  # Genişliği sınırla
    )
    console.print(Align.center(back_panel))
    input()

# Çıkış animasyonu - Daha kompakt ve estetik tasarım
def show_exit_animation():
    # Ekranı temizle
    system("cls||clear")
    show_dashboard()  # Son kez dashboard'u göster
    
    # Çıkış başlığı - Daha kompakt başlık
    exit_title = Panel(
        Align.center(
            Text("🔻 SİSTEM KAPATILIYOR", style=f"bold {theme['error']}"),
            vertical="middle"
        ),
        border_style=theme["error"],
        box=box.ROUNDED,
        padding=(0, 1),  # Padding'i azalt
        width=60  # Genişliği sınırla
    )
    console.print(Align.center(exit_title))  # Ortalanmış görünüm
    
    # Animasyonlu veda mesajı - Daha kompakt animasyon
    messages = [
        "Servisler durduruluyor...",
        "Bağlantılar kapatılıyor...",
        "Veriler kaydediliyor...",
        "Sistem kapatılıyor..."
    ]
    
    # İlerleme çubuğu - Daha kompakt ve hızlı animasyon
    with Progress(
        SpinnerColumn(style=theme["error"]),
        TextColumn(f"[bold {theme['error']}]{{task.description}}"),
        BarColumn(complete_style=theme["error"], finished_style=theme["error"]),
        TextColumn(f"[bold {theme['primary']}]{{task.percentage:.0f}}%"),
        expand=False,  # Genişlemeyi engelle
        width=60      # Sabit genişlik
    ) as progress:
        task = progress.add_task(messages[0], total=100)
        
        step_size = 100 // len(messages)
        current_step = 0
        
        for message in messages:
            progress.update(task, description=message)
            for i in range(step_size):
                sleep(0.005)  # Gecikmeyi daha da azalt
                progress.update(task, advance=1)
            current_step += step_size
        
        # Kalan kısmı tamamla - Daha hızlı
        remaining = 100 - current_step
        for i in range(remaining):
            sleep(0.002)  # Gecikmeyi daha da azalt
            progress.update(task, advance=1)
    
    # ASCII veda mesajı - Daha kompakt görünüm
    goodbye = pyfiglet.figlet_format("Güle Güle!", font="small")  # Daha küçük font
    
    # Veda animasyonu - Daha az tekrar ve daha kısa bekleme
    for i in range(2):  # Tekrar sayısını daha da azalt
        system("cls||clear")
        color = theme["primary"] if i % 2 == 0 else theme["secondary"]
        # Ortalanmış ve sınırlı genişlikte görünüm
        console.print(Align.center(Panel(f"[{color}]{goodbye}[/]", width=60, padding=(0, 1), border=False)))
        sleep(0.05)  # Gecikmeyi daha da azalt
    
    # Son mesaj - Daha kısa bekleme ve kompakt görünüm
    console.print(Align.center(Panel(f"[bold {theme['success']}]✔ İyi günler dileriz![/]", width=60, padding=(0, 1), border=False)))
    sleep(0.3)  # Gecikmeyi azalt

# Ana program döngüsü
def main():
    # Açılış animasyonu göster
    system("cls||clear")
    show_startup_animation()
    
    while True:
        system("cls||clear")
        show_dashboard()  # Dashboard'u göster
        menu_choice = show_main_menu()  # Ana menüyü göster
        
        try:
            if menu_choice == "":
                continue
            menu_choice = int(menu_choice)
        except ValueError:
            system("cls||clear")
            console.print("[bold red]Hatalı giriş yaptın. Tekrar deneyiniz.[/]")
            sleep(2)
            continue
        # Normal SMS gönderme fonksiyonu - Performans optimizasyonu yapılmış
        if menu_choice == 1:
            system("cls||clear")
            show_dashboard()  # Dashboard'u göster
            
            # Başlık paneli - Önbelleğe alınmış stil
            header_style = Style(color=theme['primary'])
            header = Panel(
                Align.center(
                    Text("📱 NORMAL SMS GÖNDERME", style=f"bold {theme['primary']}"),
                    vertical="middle"
                ),
                border_style=theme["primary"],
                box=box.ROUNDED
            )
            console.print(header)
            
            # Telefon numarası al - Daha verimli panel oluşturma
            tel_panel = Panel.fit(f"[bold {theme['warning']}]Telefon numarasını başında '+90' olmadan yazınız\n(Birden çoksa 'enter' tuşuna basınız)[/]", border_style=theme["secondary"])
            console.print(tel_panel)
            
            # Animasyonlu giriş promptu - Daha kısa bekleme
            with console.status(f"[bold {theme['info']}]Telefon numarası bekleniyor...", spinner="dots"):
                sleep(0.2)  # Daha kısa animasyon için bekleme
            
            tel_no = console.input(f"[bold {theme['success']}]Telefon: [/]")
            tel_liste = []
            
            if tel_no == "":
                system("cls||clear")
                show_dashboard()  # Dashboard'u göster
                console.print(header)
                
                file_panel = Panel.fit(f"[bold {theme['warning']}]Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız[/]", border_style=theme["secondary"])
                console.print(file_panel)
                
                # Animasyonlu dosya seçim promptu
                with console.status(f"[bold {theme['info']}]Dosya dizini bekleniyor...", spinner="dots"):
                    sleep(0.3)  # Kısa bir animasyon için bekleme
                
                dizin = console.input(f"[bold {theme['success']}]Dosya Dizini: [/]")
                try:
                    # Dosya yükleme animasyonu
                    with Progress(
                        SpinnerColumn(style=theme["accent"]),
                        TextColumn(f"[bold {theme['info']}]Dosya yükleniyor..."),
                        BarColumn(complete_style=theme["success"]),
                        expand=True
                    ) as progress:
                        task = progress.add_task("Yükleniyor", total=100)
                        
                        with open(dizin, "r", encoding="utf-8") as f:
                            content = f.read().strip().split("\n")
                            total = len(content)
                            loaded = 0
                            
                            for i in content:
                                if len(i) == 10:
                                    tel_liste.append(i)
                                loaded += 1
                                progress.update(task, completed=int(loaded/total*100))
                                sleep(0.01)  # Yükleme animasyonu için kısa bekleme
                    
                    sonsuz = ""
                    console.print(f"[bold {theme['success']}]✅ {len(tel_liste)} adet numara başarıyla yüklendi![/]")
                    sleep(1)
                except FileNotFoundError:
                    system("cls||clear")
                    error_panel = Panel(
                        f"Dosya bulunamadı: {dizin}\nLütfen doğru dosya yolunu girdiğinizden emin olun.",
                        title=f"[{theme['error']}]Hata[/]",
                        border_style=theme["error"],
                        box=box.ROUNDED
                    )
                    console.print(error_panel)
                    sleep(2)
                    continue
            else:
                try:
                    int(tel_no)
                    if len(tel_no) != 10:
                        raise ValueError
                    tel_liste.append(tel_no)
                    sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
                except ValueError:
                    system("cls||clear")
                    error_panel = Panel(
                        "Hatalı telefon numarası.\nLütfen 10 haneli geçerli bir numara girin.",
                        title=f"[{theme['error']}]Hata[/]",
                        border_style=theme["error"],
                        box=box.ROUNDED
                    )
                    console.print(error_panel)
                    sleep(2)
                    continue
            
            # Mail adresi al
            system("cls||clear")
            show_dashboard()  # Dashboard'u göster
            console.print(header)
            
            mail_panel = Panel.fit(f"[bold {theme['warning']}]Mail adresi (Bilmiyorsanız 'enter' tuşuna basın)[/]", border_style=theme["secondary"])
            console.print(mail_panel)
            
            # Animasyonlu mail promptu
            with console.status(f"[bold {theme['info']}]Mail adresi bekleniyor...", spinner="dots"):
                sleep(0.3)  # Kısa bir animasyon için bekleme
            
            mail = console.input(f"[bold {theme['success']}]Mail: [/]")
            
            if ("@" not in mail or ".com" not in mail) and mail != "":
                system("cls||clear")
                error_panel = Panel(
                    "Hatalı mail adresi.\nLütfen geçerli bir mail adresi girin.",
                    title=f"[{theme['error']}]Hata[/]",
                    border_style=theme["error"],
                    box=box.ROUNDED
                )
                console.print(error_panel)
                sleep(2)
                continue
            
            # SMS sayısı al
            system("cls||clear")
            show_dashboard()  # Dashboard'u göster
            console.print(header)
            
            count_panel = Panel.fit(f"[bold {theme['warning']}]Kaç adet SMS göndermek istiyorsun {sonsuz}[/]", border_style=theme["secondary"])
            console.print(count_panel)
            
            # Animasyonlu SMS sayısı promptu
            with console.status(f"[bold {theme['info']}]SMS sayısı bekleniyor...", spinner="dots"):
                sleep(0.3)  # Kısa bir animasyon için bekleme
            
            try:
                kere_input = console.input(f"[bold {theme['success']}]SMS Sayısı: [/]")
                kere = int(kere_input) if kere_input else None
            except ValueError:
                system("cls||clear")
                error_panel = Panel(
                    "Hatalı giriş yaptınız.\nLütfen geçerli bir sayı girin.",
                    title=f"[{theme['error']}]Hata[/]",
                    border_style=theme["error"],
                    box=box.ROUNDED
                )
                console.print(error_panel)
                sleep(2)
                continue
            
            # Gönderim aralığı al
            system("cls||clear")
            show_dashboard()  # Dashboard'u göster
            console.print(header)
            
            interval_panel = Panel.fit(f"[bold {theme['warning']}]Kaç saniye aralıkla göndermek istiyorsun[/]", border_style=theme["secondary"])
            console.print(interval_panel)
            
            # Animasyonlu aralık promptu
            with console.status(f"[bold {theme['info']}]Saniye aralığı bekleniyor...", spinner="dots"):
                sleep(0.3)  # Kısa bir animasyon için bekleme
            
            try:
                aralik = int(console.input(f"[bold {theme['success']}]Saniye: [/]"))
            except ValueError:
                system("cls||clear")
                error_panel = Panel(
                    "Hatalı giriş yaptınız.\nLütfen geçerli bir sayı girin.",
                    title=f"[{theme['error']}]Hata[/]",
                    border_style=theme["error"],
                    box=box.ROUNDED
                )
                console.print(error_panel)
                sleep(2)
                continue
            
            # Onay paneli
            system("cls||clear")
            show_dashboard()  # Dashboard'u göster
            console.print(header)
            
            confirm_panel = Panel(
                f"""
                [bold]Gönderim Özeti:[/]
                • Toplam Numara: [bold]{len(tel_liste)}[/]
                • SMS Sayısı: [bold]{kere if kere else 'Sonsuz'}[/]
                • Gönderim Aralığı: [bold]{aralik} saniye[/]
                """,
                title=f"[{theme['warning']}]Onay[/]",
                border_style=theme["warning"],
                box=box.ROUNDED
            )
            console.print(confirm_panel)
            
            # Onay alma
            confirm = Prompt.ask(
                f"[bold {theme['warning']}]Gönderimi başlatmak istiyor musunuz?[/]", 
                choices=["e", "h"], 
                default="e"
            )
            
            if confirm.lower() == "h":
                console.print(f"\n[{theme['info']}]İşlem iptal edildi.[/]")
                sleep(1)
                continue
            
            # SMS gönderme işlemi
            system("cls||clear")
            show_dashboard()  # Dashboard'u göster
            
            # Gönderim başlık paneli
            sending_panel = Panel(
                Align.center(
                    Text("🚀 SMS GÖNDERİLİYOR", style=f"bold {theme['primary']}"),
                    vertical="middle"
                ),
                border_style=theme["primary"],
                box=box.ROUNDED
            )
            console.print(sending_panel)
            
            if kere is None: 
                sms = SendSms(tel_no, mail)
                gonderilen = 0
                
                try:
                    with Progress(
                        SpinnerColumn(style=theme["accent"]),
                        TextColumn(f"[bold {theme['primary']}]Gönderiliyor..."),
                        TextColumn(f"[bold {theme['info']}]Gönderilen: {{task.completed}}"),
                        TimeElapsedColumn(),
                        expand=True
                    ) as progress:
                        task = progress.add_task("Gönderiliyor", total=None)
                        
                        while True:
                            for attribute in dir(SendSms):
                                attribute_value = getattr(SendSms, attribute)
                                if callable(attribute_value) and not attribute.startswith('__'):
                                    try:
                                        method = getattr(sms, attribute)
                                        method()
                                        gonderilen += 1
                                        progress.update(task, completed=gonderilen, description=f"[bold {theme['info']}]Servis: {attribute}()")
                                        sleep(aralik)
                                    except Exception as e:
                                        console.print(f"[bold {theme['error']}]Hata: {attribute} servisinde sorun oluştu - {str(e)}[/]")
                                        sleep(0.5)
                except KeyboardInterrupt:
                    pass
            
            for i in tel_liste:
                sms = SendSms(i, mail)
                if isinstance(kere, int):
                    gonderilen = 0
                    
                    with Progress(
                        SpinnerColumn(style=theme["accent"]),
                        TextColumn(f"[bold {theme['primary']}]Numara: {i}"),
                        BarColumn(complete_style=theme["success"], finished_style=theme["success"]),
                        TextColumn(f"[bold {theme['info']}]{{task.completed}}/{{task.total}}"),
                        TextColumn(f"[bold {theme['secondary']}]{{task.percentage:.0f}}%"),
                        TimeElapsedColumn(),
                        TimeRemainingColumn(),
                        expand=True
                    ) as progress:
                        task = progress.add_task("Gönderiliyor", total=kere)
                        
                        while sms.adet < kere:
                            for attribute in dir(SendSms):
                                attribute_value = getattr(SendSms, attribute)
                                if callable(attribute_value) and not attribute.startswith('__'):
                                    if sms.adet == kere:
                                        break
                                    try:
                                        method = getattr(sms, attribute)
                                        method()
                                        gonderilen += 1
                                        progress.update(task, completed=gonderilen, description=f"[bold cyan]Servis: {attribute}")
                                        sleep(aralik)
                                    except Exception as e:
                                        console.print(f"[bold red]Hata: {attribute} servisinde sorun oluştu - {str(e)}[/]")
                                        sleep(0.5)
            
            # Sonuç paneli
            result_panel = Panel(
                f"""
                [bold]Gönderim Tamamlandı![/]
                
                • Toplam Numara: [bold]{len(tel_liste)}[/]
                • Gönderilen SMS: [bold]{gonderilen}[/]
                """,
                title=f"[{theme['success']}]Başarılı[/]",
                border_style=theme["success"],
                box=box.ROUNDED
            )
            console.print(result_panel)
            
            # Geri dönüş butonu
            back_panel = Panel(
                "Ana menüye dönmek için ENTER tuşuna basın",
                border_style=theme["secondary"],
                box=box.ROUNDED
            )
            console.print(back_panel)
            input()
        
        # Turbo SMS gönderme fonksiyonu - Standart tasarım
        elif menu_choice == 2:
            system("cls||clear")
            show_dashboard()  # Dashboard'u göster
            
            # Başlık paneli - Sola hizalanmış standart tasarım
            header = Panel(
                Align.left(
                    Text("🚀 TURBO SMS GÖNDERME", style=f"bold {theme['primary']}"),
                    vertical="middle"
                ),
                border_style=theme["primary"],
                box=box.ROUNDED
            )
            console.print(header)
            
            # Dosya seçim paneli - Sola hizalanmış standart tasarım
            file_panel = Panel(
                """
                [bold]Lütfen SMS gönderilecek numaraların bulunduğu dosyayı seçin.[/]
                Dosya her satırda bir numara içermelidir.
                """,
                title=f"[{theme['secondary']}]Dosya Seçimi[/]",
                border_style=theme["secondary"],
                box=box.ROUNDED,
                title_align="left"
            )
            console.print(file_panel)
            
            # Dosya yolu girişi - Daha hızlı prompt
            file_path = Prompt.ask(
                f"[{theme['secondary']}]Dosya yolunu girin[/]", 
                default="liste.txt"
            )
            
            try:
                # Dosya yükleme animasyonu - Optimize edilmiş
                with Progress(
                    SpinnerColumn(style=theme["info"]),
                    TextColumn(f"[{theme['info']}]Dosya yükleniyor..."),
                    expand=True
                ) as progress:
                    task = progress.add_task("Yükleniyor", total=1)
                    with open(file_path, "r") as file:
                        numbers = file.read().splitlines()
                    sleep(0.3)  # Daha kısa bekleme süresi
                    progress.update(task, completed=1)
                
                # Başarılı yükleme mesajı - Daha kısa bekleme
                console.print(f"\n[{theme['success']}]✓ {len(numbers)} numara başarıyla yüklendi.[/]")
                sleep(0.3)  # Daha kısa bekleme süresi
                
                # Parametre girişi paneli - Sola hizalanmış standart tasarım
                params_panel = Panel(
                    "Gönderim parametrelerini ayarlayın:",
                    title=f"[{theme['secondary']}]Gönderim Ayarları[/]",
                    border_style=theme["secondary"],
                    box=box.ROUNDED,
                    title_align="left"
                )
                console.print(params_panel)
                
                # Mail sayısı girişi - Daha hızlı prompt
                mail_count = int(Prompt.ask(
                    f"[{theme['secondary']}]Mail sayısını girin[/]", 
                    default="1"
                ))
                
                # SMS sayısı girişi - Daha hızlı prompt
                sms_count = int(Prompt.ask(
                    f"[{theme['secondary']}]SMS sayısını girin[/]", 
                    default="1"
                ))
                
                # Thread sayısı girişi - Sola hizalanmış standart tasarım
                thread_panel = Panel(
                    """
                    [bold]Thread Sayısı:[/]
                    Daha yüksek değerler daha hızlı gönderim sağlar ancak sistem performansını etkileyebilir.
                    Önerilen değer: 10-50 arası
                    Maksimum değer: 200
                    """,
                    title=f"[{theme['secondary']}]Performans Ayarı[/]",
                    border_style=theme["secondary"],
                    box=box.ROUNDED,
                    title_align="left"
                )
                console.print(thread_panel)
                
                thread_count = min(200, max(1, int(Prompt.ask(
                    f"[{theme['secondary']}]Thread sayısını girin (1-200)[/]", 
                    default="20"
                ))))
                
                # Onay paneli - Sola hizalanmış standart tasarım
                confirm_panel = Panel(
                    f"""
                    [bold]Gönderim Özeti:[/]
                    • Toplam Numara: [bold]{len(numbers)}[/]
                    • Mail Sayısı: [bold]{mail_count}[/]
                    • SMS Sayısı: [bold]{sms_count}[/]
                    • Thread Sayısı: [bold]{thread_count}[/]
                    • Toplam Gönderim: [bold]{len(numbers) * (mail_count + sms_count)}[/]
                    """,
                    title=f"[{theme['secondary']}]Onay[/]",
                    border_style=theme["secondary"],
                    box=box.ROUNDED,
                    title_align="left"
                )
                console.print(confirm_panel)
                
                # Onay alma - Daha hızlı prompt
                confirm = Prompt.ask(
                    f"[bold {theme['warning']}]Gönderimi başlatmak istiyor musunuz?[/]", 
                    choices=["e", "h"], 
                    default="e"
                )
                
                if confirm.lower() == "h":
                    console.print(f"\n[{theme['info']}]İşlem iptal edildi.[/]")
                    sleep(0.5)  # Daha kısa bekleme süresi
                    continue
                
                # Gönderim başlık paneli - Sola hizalanmış standart tasarım
                sending_panel = Panel(
                    Align.left(
                        Text("🚀 TURBO SMS GÖNDERİLİYOR", style=f"bold {theme['primary']}"),
                        vertical="middle"
                    ),
                    border_style=theme["primary"],
                    box=box.ROUNDED
                )
                console.print(sending_panel)
                
                # Thread'leri başlat - Optimize edilmiş değişkenler
                threads = []
                sent_count = 0
                active_threads = 0
                lock = threading.Lock()
                running = True  # Gönderim durumunu kontrol etmek için bayrak
                
                def send_sms(number, service_name):
                    nonlocal sent_count, active_threads
                    # Gerçek SMS gönderimi
                    try:
                        sms = SendSms(number, "")
                        method = getattr(sms, service_name, None)
                        if method and callable(method):
                            method()
                    except Exception as e:
                        pass  # Hataları sessizce geç
                    
                    # Gönderim sayacını güncelle
                    with lock:
                        sent_count += 1
                        active_threads -= 1
                
                # Canlı ilerleme göstergesi - Daha verimli güncelleme
                with Live(refresh_per_second=5) as live:  # Daha hızlı yenileme
                    # İlerleme çubuğu - Optimize edilmiş
                    progress = Progress(
                        SpinnerColumn(style=theme["accent"]),
                        TextColumn(f"[bold {theme['accent']}]Turbo Gönderiliyor..."),
                        BarColumn(complete_style=theme["success"], finished_style=theme["success"]),
                        TextColumn(f"[bold {theme['info']}]{{task.completed}}/{{task.total}}"),
                        TextColumn(f"[bold {theme['secondary']}]{{task.percentage:.0f}}%"),
                        TimeElapsedColumn(),
                        TimeRemainingColumn(),
                        expand=True
                    )
                    
                    # Aktif thread sayacı - Optimize edilmiş
                    thread_progress = Progress(
                        TextColumn(f"[bold {theme['warning']}]Aktif Thread:"),
                        BarColumn(complete_style=theme["warning"]),
                        TextColumn(f"[bold {theme['warning']}]{{task.completed}}/{{task.total}}"),
                        expand=True
                    )
                    
                    # Servis dağılımı - Optimize edilmiş
                    services_progress = Progress(
                        TextColumn(f"[bold {theme['info']}]Servis Kullanımı:"),
                        BarColumn(complete_style=theme["info"]),
                        TextColumn(f"[bold {theme['info']}]{{task.description}}"),
                        expand=True
                    )
                    
                    # Layout oluştur - Tek seferde oluşturma
                    layout = Layout()
                    layout.split(
                        Layout(name="main"),
                        Layout(name="stats")
                    )
                    layout["stats"].split_row(
                        Layout(name="threads"),
                        Layout(name="services")
                    )
                    
                    # Progress barları ekle - Tek seferde ekleme
                    layout["main"].update(progress)
                    layout["threads"].update(thread_progress)
                    layout["services"].update(services_progress)
                    
                    # Görevleri ekle - Optimize edilmiş
                    task = progress.add_task("[green]Gönderiliyor...", total=len(numbers) * sms_count)
                    thread_task = thread_progress.add_task("Aktif", total=thread_count)
                    
                    # Servis görevleri - Daha verimli oluşturma
                    service_tasks = {}
                    services = [attr for attr in dir(SendSms) if callable(getattr(SendSms, attr)) and not attr.startswith('__')]
                    for service in services:
                        service_tasks[service] = services_progress.add_task(service, total=100, completed=0)
                    
                    # Thread'leri başlat - Optimize edilmiş
                    total_services = len(service_tasks)
                    service_counts = {service: 0 for service in service_tasks}
                    current_number_index = 0
                    
                    # Durdurma fonksiyonu
                    def stop_sending():
                        nonlocal running
                        running = False
                        console.print(f"\n[{theme['warning']}]Gönderim durduruluyor...[/]")
                    
                    # Klavye kesintisi dinleyicisi
                    keyboard_listener = threading.Thread(target=lambda: input("Durdurmak için ENTER tuşuna basın") or stop_sending())
                    keyboard_listener.daemon = True
                    keyboard_listener.start()
                    
                    try:
                        # Sürekli gönderim döngüsü
                        while running:
                            # Mevcut numara
                            number = numbers[current_number_index]
                            
                            # Tüm servisleri kullanarak SMS gönder
                            for service in services:
                                if not running:
                                    break
                                    
                                # Thread sayısı kontrolü
                                while active_threads >= thread_count and running:
                                    sleep(0.005)  # Kısa bekleme
                                    thread_progress.update(thread_task, completed=active_threads)
                                    live.update(layout)
                                
                                if not running:
                                    break
                                    
                                with lock:
                                    active_threads += 1
                                
                                # Servis sayacını güncelle
                                service_counts[service] += 1
                                total_sent = sum(service_counts.values())
                                
                                # Servis istatistiklerini güncelle
                                if total_sent % 10 == 0:  # Her 10 işlemde bir güncelle
                                    for s, count in service_counts.items():
                                        percentage = (count / total_sent) * 100 if total_sent > 0 else 0
                                        services_progress.update(service_tasks[s], completed=percentage, description=f"{s}: {count}")
                                
                                # Thread'i başlat
                                t = threading.Thread(target=send_sms, args=(number, service))
                                threads.append(t)
                                t.start()
                                
                                # İlerleme çubuğunu güncelle
                                progress.update(task, completed=sent_count)
                                
                                # Saniyede bir SMS gönderimi için bekleme
                                sleep(1.0 / thread_count)  # Thread sayısına göre ayarlanmış bekleme
                            
                            # Sonraki numaraya geç
                            current_number_index = (current_number_index + 1) % len(numbers)
                            
                    except KeyboardInterrupt:
                        stop_sending()
                        
                    # Tüm aktif thread'lerin tamamlanmasını bekle
                    while active_threads > 0:
                        sleep(0.1)
                        thread_progress.update(thread_task, completed=active_threads)
                        progress.update(task, completed=sent_count)
                        live.update(layout)
                    
                    # Kalan thread'lerin tamamlanmasını bekle - Daha verimli bekleme
                    while active_threads > 0:
                        sleep(0.05)  # Daha kısa bekleme süresi
                        thread_progress.update(thread_task, completed=active_threads)
                        progress.update(task, completed=sent_count)
                        live.update(layout)
                    
                    # Son güncelleme - Tek seferde güncelleme
                    progress.update(task, completed=len(numbers) * sms_count * total_services)
                    thread_progress.update(thread_task, completed=0)
                    live.update(layout)
                
                # Sonuç paneli - Tek seferde render
                result_panel = Panel(
                    f"""
                    [bold]Gönderim Tamamlandı![/]
                    
                    • Toplam Numara: [bold]{len(numbers)}[/]
                    • Gönderilen Mail: [bold]{mail_count * len(numbers)}[/]
                    • Gönderilen SMS: [bold]{sms_count * len(numbers)}[/]
                    • Kullanılan Thread: [bold]{thread_count}[/]
                    • Toplam Gönderim: [bold]{sent_count}[/]
                    """,
                    title=f"[{theme['success']}]Başarılı[/]",
                    border_style=theme["success"],
                    box=box.ROUNDED
                )
                console.print(result_panel)
                
                # Geri dönüş butonu - Tek seferde render
                back_panel = Panel(
                    "Ana menüye dönmek için ENTER tuşuna basın",
                    border_style=theme["secondary"],
                    box=box.ROUNDED
                )
                console.print(back_panel)
                input()
            
            except FileNotFoundError:
                error_panel = Panel(
                    f"Dosya bulunamadı: {file_path}\nLütfen doğru dosya yolunu girdiğinizden emin olun.",
                    title=f"[{theme['error']}]Hata[/]",
                    border_style=theme["error"],
                    box=box.ROUNDED
                )
                console.print(error_panel)
                sleep(1)  # Daha kısa bekleme süresi
                continue
            except ValueError:
                error_panel = Panel(
                    "Geçersiz sayısal değer girdiniz.\nLütfen pozitif tam sayılar girin.",
                    title=f"[{theme['error']}]Hata[/]",
                    border_style=theme["error"],
                    box=box.ROUNDED
                )
                console.print(error_panel)
                sleep(1)  # Daha kısa bekleme süresi
                continue
        
        # Servisleri göster
        elif menu_choice == 3:
            show_services()
        
        # Çıkış yap
        elif menu_choice == 0:
            show_exit_animation()
            break

if __name__ == "__main__":
    # Programı başlat
    main()
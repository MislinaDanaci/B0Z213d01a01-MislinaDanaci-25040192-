simdi=float(input("simdi saat kac"))
uyanis=float(input("kacta uyanman gerek"))
sure=float(input("kac saat gerek"))
ihtiyac=float(input("kac saat uyuman gerek"))

geceye_kalan=24-simdi
toplam_vakit=geceye_kalan+uyanis
kalan_uyku= toplam_vakit-sure

if kalan_uyku >= ihtiyac:
    print ("süre sorunun yok uyumak için {kalan_uyku}saatin var")
else:
    print ("uyuman gerek") 
    

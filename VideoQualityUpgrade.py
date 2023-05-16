import cv2
import shutil

def video_kalite_yukseltme(giris_dosyasi, cikis_dosyasi, cikis_cozunurluk):
    giris_video = cv2.VideoCapture(giris_dosyasi)
    fps = giris_video.get(cv2.CAP_PROP_FPS)
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    frame_sayisi = int(giris_video.get(cv2.CAP_PROP_FRAME_COUNT))
    cikis_video = cv2.VideoWriter(cikis_dosyasi, codec, fps / 2, cikis_cozunurluk)

    while True:
        ret, frame = giris_video.read()
        if not ret:
            break
        frame = cv2.resize(frame, cikis_cozunurluk)
        cikis_video.write(frame)

    giris_video.release()
    cikis_video.release()
    print("Video kalite yükseltme işlemi tamamlandı.")

def video_indir(dosya_yolu, hedef_dosya):
    shutil.move(dosya_yolu, hedef_dosya)
    print("Video başarıyla indirildi.")

giris_dosyasi = r'C:\Users\MONSTER\Desktop\zao\zaopat.mp4'
cikis_dosyasi = r'C:\Users\MONSTER\Desktop\zao\yeni.mp4'
cikis_cozunurluk = (3840, 2160)

video_kalite_yukseltme(giris_dosyasi, cikis_dosyasi, cikis_cozunurluk)
hedef_dosya = "yeni_video.mp4"
video_indir(cikis_dosyasi, hedef_dosya)
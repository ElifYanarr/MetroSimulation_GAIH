from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

# Istasyon sınıfı, her bir istasyonun özelliklerini ve komşularını tutar.
class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx  # İstasyonun benzersiz kimliği (örneğin, "K1")
        self.ad = ad    # İstasyonun adı (örneğin, "Kızılay")
        self.hat = hat  # İstasyonun bağlı olduğu hat (örneğin, "Kırmızı Hat")
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    # İstasyona bir komşu ekler ve iki istasyon arasındaki süreyi belirtir.
    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

# MetroAgi sınıfı, metro ağını ve istasyonları yönetir.
class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}  # İstasyonları idx'e göre tutar
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)  # Hatları ve istasyonları tutar

    # Yeni bir istasyon ekler.
    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)  # Yeni bir Istasyon nesnesi oluştur
            self.istasyonlar[idx] = istasyon  # İstasyonu sözlüğe ekle
            self.hatlar[hat].append(istasyon)  # İstasyonu ilgili hatta ekle

    # İki istasyon arasında bağlantı ekler.
    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]  # İlk istasyonu al
        istasyon2 = self.istasyonlar[istasyon2_id]  # İkinci istasyonu al
        istasyon1.komsu_ekle(istasyon2, sure)  # İkinci istasyonu birinciye komşu olarak ekle
        istasyon2.komsu_ekle(istasyon1, sure)  # Birinci istasyonu ikinciye komşu olarak ekle
    
    # BFS algoritması ile en az aktarmalı rotayı bulur.
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None  # Başlangıç veya hedef istasyon yoksa None döndür

        baslangic = self.istasyonlar[baslangic_id]  # Başlangıç istasyonunu al
        hedef = self.istasyonlar[hedef_id]  # Hedef istasyonunu al

        kuyruk = deque([(baslangic, [baslangic])])  # BFS için kuyruk oluştur
        ziyaret_edildi = set()  # Ziyaret edilen istasyonları tut

        while kuyruk:
            mevcut_istasyon, rota = kuyruk.popleft()  # Kuyruktan bir istasyon al

            if mevcut_istasyon == hedef:
                return rota  # Hedefe ulaşıldıysa rotayı döndür

            ziyaret_edildi.add(mevcut_istasyon)  # Mevcut istasyonu ziyaret edildi olarak işaretle

            for komsu, _ in mevcut_istasyon.komsular:
                if komsu not in ziyaret_edildi:
                    kuyruk.append((komsu, rota + [komsu]))  # Komşuyu kuyruğa ekle

        return None  # Rota bulunamazsa None döndür

    # A* algoritması ile en hızlı rotayı bulur.
    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None  # Başlangıç veya hedef istasyon yoksa None döndür

        baslangic = self.istasyonlar[baslangic_id]  # Başlangıç istasyonunu al
        hedef = self.istasyonlar[hedef_id]  # Hedef istasyonunu al

        pq = [(0, id(baslangic), baslangic, [baslangic])]  # A* için öncelik kuyruğu oluştur
        ziyaret_edildi = set()  # Ziyaret edilen istasyonları tut

        while pq:
            toplam_sure, _, mevcut_istasyon, rota = heapq.heappop(pq)  # Kuyruktan bir istasyon al

            if mevcut_istasyon == hedef:
                return rota, toplam_sure  # Hedefe ulaşıldıysa rotayı ve süreyi döndür

            if mevcut_istasyon in ziyaret_edildi:
                continue  # Ziyaret edildiyse atla

            ziyaret_edildi.add(mevcut_istasyon)  # Mevcut istasyonu ziyaret edildi olarak işaretle

            for komsu, sure in mevcut_istasyon.komsular:
                if komsu not in ziyaret_edildi:
                    yeni_toplam_sure = toplam_sure + sure  # Yeni toplam süreyi hesapla
                    heapq.heappush(pq, (yeni_toplam_sure, id(komsu), komsu, rota + [komsu]))  # Komşuyu kuyruğa ekle

        return None  # Rota bulunamazsa None döndür

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

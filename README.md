# MetroSimulation_GAIH
Belirli bir metro ağındaki en hızlı ve en az aktarmalı rotaları bulduran simülasyon projesi

## Kullanılan Teknolojiler ve Kütüphaneler
-Python (VSCode)

-Collections Modülü:
  Python'ın standart kütüphanelerinden biridir. Veri yapılarını verimli bir şekilde kullanmak için özel veri tipleri sağlar. Projede collections.deque kullanılmıştır.

  Deque: Baştan ve sondan ekleme ve çıkarma işlemleri yapabilen bir kuyruk (queue) yapısıdır. BFS (Breadth-First Search) algoritmasında, keşfedilecek istasyonları tutmak için deque kullanıldı. BFS, kuyruk yapısı kullandığı için deque tercih edilmiştir.

  Defaultdict: Eğer bir anahtar sözlükte yoksa, otomatik olarak varsayılan bir değer atar.Her yeni hat için otomatik olarak boş bir liste oluşturduğu için, hatlar ve istasyonlar arasındaki ilişkiyi kolayca yönetmeyi sağlar.

-Heapq Modülü: Heap veri yapısını kullanarak (priority queue) uygulamasını sağlar.  En küçük elemana hızlı erişim sağlar ve eleman ekleme, çıkarma işlemlerini hızlı bir şekilde gerçekleştirir. A* algoritmasında, en düşük maliyetli rotayı bulmak için (priority queue) kullanıldı.

-Typing Modülü: Tür belirlenmesini, kodun daha okunabilir olmasını ve hataların önceden tespit edilmesini sağlar.(List, Dict, Set, Tuple) 
   
   Optional: Bir tür ipucudur. Bir değişkenin belirli bir türde olabileceğini veya None olabileceğini belirtir.

## Algoritmaların Çalışma Mantığı

  BFS Algoritması:
- En az aktarmalı rotayı bulmak için kullanılır.
- Kuyruk (queue) yapısı kullanır.
- Başlangıç düğümünden başlayarak tüm komşu düğümleri keşfeder ve bu işlemi hedef düğüme ulaşana kadar tekrarlar.

  A* Algoritması:
- En hızlı rotayı bulmak için kullanılır.
- Öncelik kuyruğu (priority queue) ve tahmini maliyet hesaplaması kullanır. Bu kuyruk, en düşük maliyetli düğümü her zaman öncelikli olarak işler.
 
## Örnek Kullanım ve Test Sonuçları

=== Test Senaryoları ===

1. AŞTİ'den OSB'ye:
En az aktarmalı rota: AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB
En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB

2. Batıkent'ten Keçiören'e:
En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Keçiören
En hızlı rota (21 dakika): Batıkent -> Demetevler -> Gar -> Keçiören

3. Keçiören'den AŞTİ'ye:
En az aktarmalı rota: Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
En hızlı rota (19 dakika): Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ

## Projeyi Geliştirme Fikirleri

- Daha büyük bir metro ağı üzerinde test edilebilir.
- Yalnızca metro hatları değil, diğer toplu taşıma hatlarının da dahil edildiği yeni bir simülasyon yazılabilir.(Yürüme mesafesinin taksi,uber gibi ücrete tabi tutan araçlar da eklenebilir.)
- Günlük saat dilimlerine göre gece modu uygulaması hayata geçirilebilir. Bu mod, gece saatlerinde metro seferlerinin sıklığını azaltarak hem enerji tasarrufu sağlayacak hem de maliyetleri düşürecektir. Ayrıca, gece saatlerinde daha az yoğunluk olan hatlarda seferlerin optimize edilmesi, kullanıcıların bekleme sürelerini de azaltacaktır.
- Görselleştirilebilir, animasyonlar eklenebilir.
.
.
.

   

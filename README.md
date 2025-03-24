## 1. Route Optimization (Metro Simulation)

![1000168785](https://github.com/user-attachments/assets/cbb5a56c-e267-4446-b798-97e2bafb0846)

Bu proje, bir metro ağı üzerinde iki istasyon arasındaki en hızlı ve en az aktarmalı rotayı belirleyerek, rota optimizasyonunu hedefleyen bir simülasyon geliştirmeyi amaçlamaktadır. Bu sayede kullanıcılar için en verimli güzergahların bulunması sağlanır.

---

## 2. Kullanılan Kütüphaneler ve Teknolojiler 📚

● heapq  :  Öncelikli kuyruk (priority queue) işlemleri için kullanılır. A* algoritması sırasında en kısa süreli yolun önceliklendirilmesini sağlar.  
● collections  :  Genişletilebilir çift yönlü kuyruk yapısıdır. BFS algoritması için performans avantajı sağlayan bir yapı sunar.  
● networkx  :  Grafik (graph) verilerini işlemek ve görselleştirmek için kullanılır. Düğümler (istasyonlar) ve kenarlar (bağlantılar) bu yapı üzerinde modellenmiştir.     
● typing  : Veri türlerini açıkça tanımlamak için kullanılır.  
● matplotlib  : Grafiksel görselleştirme için kullanılır.  

---

## 3. Kullanılan Algoritmaların Çalışma Mantığı 

### BFS (Breadth First Search)

Breadth-First Search, yani genişlik öncelikli arama algoritması, bir graf yapısında başlangıç düğümünden (node) başlayarak hedef düğüme ulaşana kadar katman katman ilerleyen bir arama algoritmasıdır.

En kısa yolun uzunluğu kenar sayısı bakımından bulunmak istendiğinde kullanılır ve her kenarın ağırlığı eşitse en kısa yolu garanti eder.

#### Nasıl Çalışır?

-> Başlangıç düğümünü sıraya (queue) ekle ve ziyaret edildi olarak işaretle.  

Sıra boşalana kadar:

-> Sıradan bir düğüm al (dequeue).

-> Tüm komşularını kontrol et.

-> Ziyaret edilmemiş olanları sıraya ekle ve işaretle.

Bu şekilde her katman sırayla dolaşılmış olur.

---

Bir örnek üzerinden çalışma mantığını anlayalım:   

![image](https://github.com/user-attachments/assets/d891f72b-7fdf-4321-83f8-5824da90de2d)

Adımlar:

Başla: 0 → sıraya ekle → ziyaret edildi

Komşuları (1, 2, 3) sıraya eklenir

1 çıkartılır → komşuları (4, 5) eklenir

2 çıkartılır → yeni komşu (6, 7) eklenir

3 çıkartılır → zaten ziyaret edilenler atlanır

Bu işlem tüm düğümler gezilene kadar devam eder.

---

### A* (A Star) Algoritması

A* algoritması, bir noktadan başka bir noktaya giderken en kısa ve en mantıklı yolu bulmak için kullanılır. Akıllı bir algoritmadır çünkü sadece komşulara bakmakla kalmaz, aynı zamanda hedefe en çabuk ulaşacak yolu tahmin ederek hareket eder.

Bu yüzden A*, rastgele değil, hedef odaklı arama yapar.   


#### Nasıl Çalışır?

A* algoritması, her düğüm (nokta) için bir puan hesaplar:

f(n) = g(n) + h(n)

Bu formüldeki her terim şunu ifade eder:

● g(n): Başlangıçtan şu anki düğüme kadar olan gerçek yol maliyeti (örneğin geçen süre, mesafe, vs.)

● h(n): Bu düğümden hedefe olan tahmini maliyet (heuristic = sezgisel)

● f(n): Toplam tahmini maliyet. A* her zaman f(n) en küçük olan yolu seçer.

---

#### Heuristic (h(n)) Fonksiyonu Nedir?   

Bu algoritmanın zekice kısmı burasıdır. h(n), bir düğümden hedefe olan tahmini uzaklığı ifade eder. Örneğin, bir haritada düğümler ızgara üzerinde ise, h(n) genellikle Manhattan mesafesi ya da Euclidean mesafesi ile hesaplanır. Bu tahminler, algoritmanın daha doğru tahminlerle daha az düğüm denemesini sağlar.   

---

Bir örnek üzerinden anlayalım: 

![image](https://github.com/user-attachments/assets/5042473a-f7ef-4fb3-9338-ff5f0d196632)

Başlangıç düğümümüz: a
Hedef düğümümüz: z

1. Adım: Başlangıç
Başlangıç: a,  
g(a) = 0  
h(a) = 21 (turuncu sayı)  
f(a) = g + h = 0 + 21 = 21  
Açık liste: {a}  
Kapalı liste: {}  

2. Adım: a'nın komşularını değerlendir
a → b (9), c (4), d (7)  
b:  
g(b) = g(a) + 9 = 9  
h(b) = 14  
f(b) = 9 + 14 = 23  
c:  
g(c) = 0 + 4 = 4  
h(c) = 18  
f(c) = 4 + 18 = 22  
d:  
g(d) = 0 + 7 = 7  
h(d) = 18  
f(d) = 7 + 18 = 25  
Açık liste: {b (23), c (22), d (25)}  
Kapalı liste: {a}  

3. Adım: En düşük f'ye sahip olanı seç: c (22)
Şimdi c’nin komşularını değerlendir: e (17), f (12)  
e:  
g(e) = g(c) + 17 = 4 + 17 = 21  
h(e) = 5  
f(e) = 21 + 5 = 26  
f:  
g(f) = 4 + 12 = 16  
h(f) = 8  
f(f) = 16 + 8 = 24  
Açık liste: {b (23), d (25), e (26), f (24)}  
Kapalı liste: {a, c}  

4. Adım: En düşük f: b (23)  
b → e (11) komşusu var  
g(e) = min(önceki 21, yeni 9+11=20) → daha iyi  
g(e) = 20  
h(e) = 5  
f(e) = 25  
e güncellendi.  
Açık liste: {d (25), f (24), e (25)}  
Kapalı liste: {a, c, b}  

5. Adım: En düşük f: f (24)  
f → z (9) komşusu var  
z:  
g(z) = g(f) + 9 = 16 + 9 = 25  
h(z) = 0  
f(z) = 25  
Açık liste: {d (25), e (25), z (25)}  
Kapalı liste: {a, c, b, f}  

6. Adım: z bulundu!  
Zaten hedef düğümümüz. Şimdi geriye doğru yolu çıkaralım:
z geldi f’ten (z ← f)  
f geldi c’den (f ← c)  
c geldi a’dan (c ← a)  
Yol: a → c → f → z  
Toplam maliyet:  
a → c: 4  
c → f: 12  
f → z: 9  
-> Toplam: 25  

### Sonuç:  
#### A algoritmasıyla bulunan en kısa yol:* a → c → f → z  
#### Toplam maliyet: 25  

---

### Neden Bu Algoritmalar Seçildi?
BFS: Basit ve garanti çözüm sunar. Özellikle "aktarma" sayısının optimizasyonunda oldukça verimlidir.  

A*: Süre optimizasyonu için uygundur ve heuristik eklenerek daha hızlı çözümler üretebilir. Gelecekte harita üzerinde fiziksel uzaklıkla çalışan bir heuristic fonksiyonu tanımlanarak performansı artırılabilir.  

---

# 4. Örnek Kullanım ve Test Sonuçları  

Tanımlı Hatlar:

Kırmızı Hat: Kızılay - Ulus - Demetevler - OSB

Mavi Hat: AŞTİ - Kızılay - Sıhhiye - Gar

Turuncu Hat: Batıkent - Demetevler - Gar - Keçiören

---

## Sonuçlar

![image](https://github.com/user-attachments/assets/b74f14a4-1a59-4e86-b582-8110844101ba)

---

## Görselleştirme

1. AŞTİ'den OSB'ye:  
En az aktarmalı rota: AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB  
En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB  

![1Figure_1_akbank](https://github.com/user-attachments/assets/453d87d7-11eb-4e0a-b853-7029317fca27)

---

2. Batıkent'ten Keçiören'e:  
En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Keçiören  
En hızlı rota (21 dakika): Batıkent -> Demetevler -> Gar -> Keçiören  

![2Figure_1_akbank](https://github.com/user-attachments/assets/99b129aa-af08-4078-8a74-3ad161442934)

---

3. Keçiören'den AŞTİ'ye:  
En az aktarmalı rota: Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ  
En hızlı rota (19 dakika): Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ  

![3Figure_1_akbank](https://github.com/user-attachments/assets/5241195f-1882-48c8-a773-ddcb807291f1)

---

# 5. Projeyi Geliştirme Fikirleri 

- Google Maps veya OpenStreetMap entegrasyonu düşünülebilir.  
- Tren gecikmeleri, bakım çalışmaları gibi gerçek zamanlı bilgilerle rota önerileri güncellenebilir.  
- Basit bir web arayüzü geliştirilebilir.

---

# 6. Kaynaklar
1. https://www.101computing.net/a-star-search-algorithm/
2. https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/

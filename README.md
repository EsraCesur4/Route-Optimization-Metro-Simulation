# Route Optimization (Metro Simulation)

![1000168785](https://github.com/user-attachments/assets/cbb5a56c-e267-4446-b798-97e2bafb0846)

Bu proje, bir metro ağı üzerinde iki istasyon arasındaki en hızlı ve en az aktarmalı rotayı belirleyerek, rota optimizasyonunu hedefleyen bir simülasyon geliştirmeyi amaçlamaktadır. Bu sayede kullanıcılar için en verimli güzergahların bulunması sağlanır.

### Kullanılan Kütüphaneler
● heapq
● collections
● networkx
● matplotlib


## Hangi algoritmaları kullandım?

### BFS (Breadth First Search)

Breadth-First Search, yani genişlik öncelikli arama algoritması, bir graf yapısında başlangıç düğümünden (node) başlayarak hedef düğüme ulaşana kadar katman katman ilerleyen bir arama algoritmasıdır.

En kısa yolun uzunluğu kenar sayısı bakımından bulunmak istendiğinde kullanılır ve her kenarın ağırlığı eşitse en kısa yolu garanti eder.

### A* (A Star) Algoritması

A* algoritması, bir noktadan başka bir noktaya giderken en kısa ve en mantıklı yolu bulmak için kullanılır. Akıllı bir algoritmadır çünkü sadece komşulara bakmakla kalmaz, aynı zamanda hedefe en çabuk ulaşacak yolu tahmin ederek hareket eder.

Bu yüzden A*, rastgele değil, hedef odaklı arama yapar.

A* algoritması, her düğüm (nokta) için bir puan hesaplar:

f(n) = g(n) + h(n)

Bu formüldeki her terim şunu ifade eder:

g(n): Başlangıçtan şu anki düğüme kadar olan gerçek yol maliyeti (örneğin geçen süre, mesafe, vs.)

h(n): Bu düğümden hedefe olan tahmini maliyet (heuristic = sezgisel)

f(n): Toplam tahmini maliyet. A* her zaman f(n) en küçük olan yolu seçer.



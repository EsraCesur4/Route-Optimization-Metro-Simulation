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
A* algoritması, bir başlangıç noktasından hedefe giden en kısa ve en hızlı yolu bulmak için kullanılan bir arama algoritmasıdır. BFS gibi çalışır, fakat her adımda sadece yakın olanları değil, aynı zamanda hedefe en yaklaştıran yolları da tercih eder.

Bu yüzden A* algoritması hem verimli hem de doğru sonuç verir.

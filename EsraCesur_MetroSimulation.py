from collections import defaultdict, deque
import heapq
from typing import Dict, List, Tuple, Optional
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Patch

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları
        # Pozisyonlar eklenmiştir
        self.pos = None  

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)
        # Hat renkleri eklenmiştir
        self.hat_colors = {
            "Kırmızı Hat": "#FF3B30",
            "Mavi Hat": "#007AFF",
            "Turuncu Hat": "#FF9500"
        }

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur
        
        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. BFS algoritmasını kullanarak en az aktarmalı rotayı bulun
        3. Rota bulunamazsa None, bulunursa istasyon listesi döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - collections.deque kullanarak bir kuyruk oluşturun, HINT: kuyruk = deque([(baslangic, [baslangic])])
        - Ziyaret edilen istasyonları takip edin
        - Her adımda komşu istasyonları keşfedin
        """
        
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = {baslangic}

        kuyruk = deque([(baslangic, [baslangic])])  # (istasyon, rota) şeklinde kuyruk oluştur
        
        # Kuyruk boşalana kadar döngü devam eder. Yani tüm yollar denenmeden algoritma durmaz.
        while kuyruk: 
            mevcut_istasyon, mevcut_rota = kuyruk.popleft()
            
            # Hedefe ulaşıldığında rotayı döndür
            if mevcut_istasyon == hedef:
                return mevcut_rota 
                
            # Komşuları kontrol et
            for komsu, sure in mevcut_istasyon.komsular:
                if komsu not in ziyaret_edildi:
                    ziyaret_edildi.add(komsu)
                    yeni_rota = mevcut_rota + [komsu]
                    kuyruk.append((komsu, yeni_rota)) # Bu yeni istasyon ve rota, kuyruğa eklenir ki daha sonra bu yol üzerinden arama devam etsin.
                    
        return None  # Rota bulunamadı: arama sırasında kuyruk boşalırsa yani tüm olası yollar tarandıktan 
                     # sonra hedefe ulaşılmadığında çalışır. Bu, geçerli girişlerle bir rota bulunamadığını belirtir.   

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur
        
        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. A* algoritmasını kullanarak en hızlı rotayı bulun
        3. Rota bulunamazsa None, bulunursa (istasyon_listesi, toplam_sure) tuple'ı döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - heapq modülünü kullanarak bir öncelik kuyruğu oluşturun, HINT: pq = [(0, id(baslangic), baslangic, [baslangic])]
        - Ziyaret edilen istasyonları takip edin
        - Her adımda toplam süreyi hesaplayın
        - En düşük süreye sahip rotayı seçin
        """

        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = set()
        
        # Öncelik kuyruğu: (toplam_tahmini_sure, istasyon_id, istasyon, rota, toplam_sure)
        # id(istasyon) ekleme sebebi, aynı tahmini süreye sahip istasyonlar olduğunda heapq'nun karşılaştırma yapabilmesi içindir
        pq = [(0, id(baslangic), baslangic, [baslangic], 0)]
        
        while pq:
            _, _, guncel_istasyon, guncel_rota, toplam_sure = heapq.heappop(pq)
            
            # Eğer hedefe ulaştıysak rotayı ve toplam süreyi döndür
            if guncel_istasyon.idx == hedef_id:
                return (guncel_rota, toplam_sure)
                
            # Eğer bu istasyon zaten işlendiyse atla
            if guncel_istasyon.idx in ziyaret_edildi:
                continue
                
            ziyaret_edildi.add(guncel_istasyon.idx)
            
            # Tüm komşuları kontrol et
            for komsu, sure in guncel_istasyon.komsular:
                if komsu.idx not in ziyaret_edildi:
                    yeni_sure = toplam_sure + sure
                    
                    # Hat değişimi varsa ek süre ekle (aktarma süresi)
                    # Heuristic: direct distance to goal (in this case, all are 0)
                    h_score = 0  # Basit bir heuristik, gerçek uygulamada daha karmaşık olabilir
                    f_score = yeni_sure + h_score
                    
                    yeni_rota = guncel_rota + [komsu]
                    heapq.heappush(pq, (f_score, id(komsu), komsu, yeni_rota, yeni_sure))
                    
        return None  # Rota bulunamadı: arama sırasında kuyruk boşalırsa yani tüm olası yollar tarandıktan 
                     # sonra hedefe ulaşılmadığında çalışır. Bu, geçerli girişlerle bir rota bulunamadığını belirtir. 


    def metro_agini_gorselleştir(self, title="Metro Ağı Haritası", ax=None):
      """Metro ağının görsel haritasını oluşturur"""
      if ax is None:
          fig, ax = plt.subplots(figsize=(14, 10))
      
      G = nx.Graph()  # Boş bir ağ grafiği oluştur
      
      # Her hat için başlangıç konumu ve yön bilgisi tanımlanır
      hat_positions = {
          "Kırmızı Hat": {"base": (0, 0), "direction": (1, 0)},
          "Mavi Hat": {"base": (0, -2), "direction": (1, 0)},
          "Turuncu Hat": {"base": (1, -4), "direction": (1, 0)}
      }
      
      # Her hat için istasyonları sırayla yerleştir
      for hat_adi, istasyonlar in self.hatlar.items():
          base = hat_positions[hat_adi]["base"]
          direction = hat_positions[hat_adi]["direction"]
          
          sorted_stations = sorted(istasyonlar, key=lambda x: x.idx)
          
          for i, istasyon in enumerate(sorted_stations):
              if istasyon.ad == "Kızılay":
                  pos = (base[0] + direction[0], base[1] + direction[1])
              elif istasyon.ad == "Demetevler":
                  if istasyon.idx == "K3":
                      pos = (base[0] + 3 * direction[0], base[1] + direction[1])
                  else:
                      pos = (base[0] + 2 * direction[0], base[1] + direction[1])
              elif istasyon.ad == "Gar":
                  pos = (base[0] + 3 * direction[0], base[1] + direction[1])
              else:
                  pos = (base[0] + (i+1) * direction[0], base[1] + direction[1])
              
              G.add_node(istasyon.idx, name=istasyon.ad, line=istasyon.hat)
              istasyon.pos = pos

      # Belirli istasyonlara manuel konum atamaları
      custom_positions = {
          "K1": (1, 0), "K2": (2, 0), "K3": (3, 0), "K4": (4, 0),
          "M1": (0, -2), "M2": (1, -2), "M3": (2, -2), "M4": (3, -2),
          "T1": (1, -4), "T2": (2, -4), "T3": (3, -4), "T4": (4, -4),
      }
      
      for idx, pos in custom_positions.items():
          if idx in self.istasyonlar:
              self.istasyonlar[idx].pos = pos
      
      # Kenar (bağlantı) bilgileri ekleniyor
      for istasyon_id, istasyon in self.istasyonlar.items():
          for komsu, sure in istasyon.komsular:
              if not G.has_edge(istasyon.idx, komsu.idx):
                  hat_tipi = "aktarma" if istasyon.hat != komsu.hat else istasyon.hat
                  G.add_edge(istasyon.idx, komsu.idx, weight=sure, type=hat_tipi)

      pos = {idx: istasyon.pos for idx, istasyon in self.istasyonlar.items()}
      
      # Kenar renklerini ayarla
      edge_colors = []
      for u, v, data in G.edges(data=True):
          if data['type'] == "aktarma":
              edge_colors.append("#8E8E93")  # Gri renk
          else:
              edge_colors.append(self.hat_colors[data['type']])
      
      # Kenarları çiz
      nx.draw_networkx_edges(G, pos, width=3, edge_color=edge_colors, ax=ax)
      
      # İstasyon adlarını yerleştir
      labels = {node: G.nodes[node]['name'] for node in G.nodes()}
      nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_weight='bold', ax=ax)
      
      # Her hat için düğümleri çiz
      for hat, color in self.hat_colors.items():
          hat_nodes = [node for node in G.nodes() if G.nodes[node]['line'] == hat]
          nx.draw_networkx_nodes(G, pos, nodelist=hat_nodes, node_color=color, 
                                node_size=700, alpha=0.8, ax=ax)

      # Aktarma istasyonlarını beyaz renkle vurgula
      transfer_stations = []
      for node in G.nodes():
          neighbors = list(G.neighbors(node))
          neighbor_lines = [G.nodes[n]['line'] for n in neighbors]
          if G.nodes[node]['line'] in neighbor_lines or len(set(neighbor_lines)) > 1:
              transfer_stations.append(node)
              
      if transfer_stations:
          nx.draw_networkx_nodes(G, pos, nodelist=transfer_stations, 
                                node_color='white', node_size=400, alpha=0.6, ax=ax)

      # Kenar etiketlerini yaz
      edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
      nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, ax=ax)

      ax.set_title(title, fontsize=16, fontweight='bold')
      ax.set_axis_off()
      ax.figure.tight_layout()

      return G, pos


    def rotayi_gorselleştir(self, rota: List[Istasyon], baslik: str, toplam_sure: Optional[int] = None, ax=None):
      """Bulunan rotayı görsel olarak gösterir ve açıklamaları grafiğin altında yerleştirir"""
      if not rota:
          print("Görselleştirilecek rota bulunamadı.")
          return
      
      if ax is None:
          fig, ax = plt.subplots(figsize=(14, 10))
      
      # Metro ağını arka planda çiz
      G, pos = self.metro_agini_gorselleştir(title=baslik, ax=ax)
      
      # Rota üzerindeki kenarları oluştur ve çiz (kalın açık mavi)
      rota_kenarlari = [(rota[i].idx, rota[i+1].idx) for i in range(len(rota) - 1)]
      nx.draw_networkx_edges(G, pos, edgelist=rota_kenarlari, width=8, 
                            edge_color="cyan", alpha=0.7, ax=ax)
      
      # Başlangıç ve bitiş istasyonlarını yeşil ile göster
      baslangic_bitis = [rota[0].idx, rota[-1].idx]
      nx.draw_networkx_nodes(G, pos, nodelist=baslangic_bitis, 
                            node_color='green', node_size=900, alpha=0.7, ax=ax)
      
      # Aktarma yapılan istasyonları sarı ile vurgula
      aktarma_istasyonlari = []
      for i in range(1, len(rota)-1):
          if rota[i-1].hat != rota[i].hat or rota[i].hat != rota[i+1].hat:
              aktarma_istasyonlari.append(rota[i].idx)
      if aktarma_istasyonlari:
          nx.draw_networkx_nodes(G, pos, nodelist=aktarma_istasyonlari, 
                                node_color='yellow', node_size=700, alpha=0.7, ax=ax)

      # Alt açıklama metni oluştur
      aktarma_sayisi = len(set(ist.hat for ist in rota)) - 1
      info_text = f"Başlangıç: {rota[0].ad}\nBitiş: {rota[-1].ad}\nAktarma Sayısı: {aktarma_sayisi}"
      if toplam_sure is not None:
          info_text += f"\nToplam Süre: {toplam_sure} dakika"
      
      ax.text(0.5, -0.1, info_text, transform=ax.transAxes, fontsize=12, 
              ha='center', va='top', bbox=dict(facecolor='white', alpha=0.7))
      
      # Renk açıklama tablosu (legend) ekle
      legend_elements = [
          Patch(facecolor=self.hat_colors["Kırmızı Hat"], edgecolor='k', label='Kırmızı Hat'),
          Patch(facecolor=self.hat_colors["Mavi Hat"], edgecolor='k', label='Mavi Hat'),
          Patch(facecolor=self.hat_colors["Turuncu Hat"], edgecolor='k', label='Turuncu Hat'),
          Patch(facecolor="#8E8E93", edgecolor='k', label='Aktarma Bağlantısı'),
          Patch(facecolor="cyan", edgecolor='k', label='Seçilen Rota')
      ]
      ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.8, 0), ncol=1)
      
      ax.figure.tight_layout()
      return


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
    
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota1 = metro.en_az_aktarma_bul("M1", "K4")
    sonuc1 = metro.en_hizli_rota_bul("M1", "K4")
    if rota1:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota1))
    if sonuc1:
        rota1_hiz, sure1 = sonuc1
        print(f"En hızlı rota ({sure1} dakika):", " -> ".join(i.ad for i in rota1_hiz))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota2 = metro.en_az_aktarma_bul("T1", "T4")
    sonuc2 = metro.en_hizli_rota_bul("T1", "T4")
    if rota2:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota2))
    if sonuc2:
        rota2_hiz, sure2 = sonuc2
        print(f"En hızlı rota ({sure2} dakika):", " -> ".join(i.ad for i in rota2_hiz))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota3 = metro.en_az_aktarma_bul("T4", "M1")
    sonuc3 = metro.en_hizli_rota_bul("T4", "M1")
    if rota3:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota3))
    if sonuc3:
        rota3_hiz, sure3 = sonuc3
        print(f"En hızlı rota ({sure3} dakika):", " -> ".join(i.ad for i in rota3_hiz))
    
    # After printing all results, create a single figure with all plots below
    fig, axs = plt.subplots(3, 2, figsize=(14, 15))
    
    # Senaryo 1 plots:
    if rota1:
        metro.rotayi_gorselleştir(rota1, "AŞTİ'den OSB'ye: En Az Aktarmalı Rota", ax=axs[0, 0])
    if sonuc1:
        metro.rotayi_gorselleştir(rota1_hiz, "AŞTİ'den OSB'ye: En Hızlı Rota", sure1, ax=axs[0, 1])
    
    # Senaryo 2 plots:
    if rota2:
        metro.rotayi_gorselleştir(rota2, "Batıkent'ten Keçiören'e: En Az Aktarmalı Rota", ax=axs[1, 0])
    if sonuc2:
        metro.rotayi_gorselleştir(rota2_hiz, "Batıkent'ten Keçiören'e: En Hızlı Rota", sure2, ax=axs[1, 1])
    
    # Senaryo 3 plots:
    if rota3:
        metro.rotayi_gorselleştir(rota3, "Keçiören'den AŞTİ'ye: En Az Aktarmalı Rota", ax=axs[2, 0])
    if sonuc3:
        metro.rotayi_gorselleştir(rota3_hiz, "Keçiören'den AŞTİ'ye: En Hızlı Rota", sure3, ax=axs[2, 1])
    
    # Adjust layout to ensure the below-axis texts are visible
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.show()

# Architektura Systemów Komputerowych

## Wykład 10: Wirtualizacja.

### 1. **Wirtualizacja** 
Jest to technika tworzenia **abstrakcyjnych, wirtualnych zasobów** (np. systemów operacyjnych, serwerów, sieci) na podstawie fizycznych zasobów sprzętowych. <br>Polega na **izolowaniu środowisk wykonawczych** w obrębie jednej maszyny fizycznej, co pozwala na równoczesne uruchamianie wielu niezależnych systemów lub aplikacji.

### 2. Główne cele wirtualizacji to:  
- **Optymalizacja wykorzystania zasobów** (np. udostępnienie jednego serwera wielu użytkownikom).  
- **Izolacja** (awaria jednego środowiska nie wpływa na inne).  
- **Elastyczność** (łatwe migracje, skalowanie, testowanie).  

---

### **3. Wirtualizacja na poziomie OS (konteneryzacja)**:  

| **Cecha**                    | **Opis**                                                                                |
|------------------------------|-----------------------------------------------------------------------------------------|
| **Hypervisor**               | Działa w przestrzeni użytkownika hosta, wykorzystując wspólne jądro OS.                 |
| **Przykłady**                | Docker, LXC, Kubernetes.                                                                |
| **Zalety**                   | Lekkość, szybkość, niskie zużycie zasobów, szybkie uruchamianie i skalowanie aplikacji. |
| **Ograniczenia**             | Wszystkie kontenery współdzielą to samo jądro OS, brak wsparcia dla różnych systemów.   |
| **Zastosowanie**             | Mikroserwisy, DevOps, chmury obliczeniowe, CI/CD.                                       | 

---

### **4. Hypervisor (monitor maszyn wirtualnych)**:  

| **Cecha**        | **Typ 1 (bare-metal)**                                 | **Typ 2 (hostowany)**                             |
|------------------|--------------------------------------------------------|---------------------------------------------------|
| **Opis**         | Działa bezpośrednio na sprzęcie, bez warstwy OS.       | Działa jako aplikacja na istniejącym OS.          |
| **Zalety**       | Wysoka wydajność, bezpośredni dostęp do sprzętu.       | Łatwość instalacji i użytkowania, dostępny na PC. |
| **Wady**         | Trudniejsza konfiguracja, wymaga dedykowanego sprzętu. | Niższa wydajność przez warstwę OS hosta.          |
| **Przykłady**    | VMware ESXi, Xen, Hyper-V                              | VirtualBox, VMware Workstation                    |
| **Zastosowanie** | Chmury obliczeniowe, centra danych.                    | Testowanie, komputery osobiste.                   |

---

### **5. Rodzaje wirtualizacji procesora** 

| **Rodzaj wirtualizacji**    | **Opis**                                                             | **Zalety**                                | **Wady**                                  | **Przykłady**              |
|-----------------------------|----------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|----------------------------|
| **Pełna wirtualizacja**     | Emuluje cały sprzęt, pozwala uruchomić niemodyfikowany OS gościa.    | Obsługuje każdy OS, pełna izolacja.       | Większy narzut wydajnościowy.             | VMware ESXi, QEMU          |
| **Parawirtualizacja**       | OS gościa współpracuje z hypervisorem przez API, wymaga modyfikacji. | Wyższa wydajność niż pełna wirtualizacja. | Konieczna modyfikacja OS gościa.          | Xen, VMware ESXi (PV mode) |
| **Wirtualizacja sprzętowa** | Wykorzystuje rozszerzenia procesora (Intel VT-x, AMD-V).             | Lepsza wydajność, brak potrzeby emulacji czy modyfikacji.| Wymaga obsługi sprzętowej. | KVM, Microsoft Hyper-V     |

---

### **6. Różnica między wirtualizacją a konteneryzacją**  

| **Kryterium**         | **Wirtualizacja**                          | **Konteneryzacja**                          |  
|-----------------------|--------------------------------------------|---------------------------------------------|  
| **Poziom abstrakcji** | Emuluje cały sprzęt (maszyna wirtualna).   | Współdzieli jądro OS hosta (kontener).      |  
| **Wydajność**         | Wyższe zużycie zasobów (OS dla każdej VM). | Lekka, minimalne narzuty.                   |  
| **Izolacja**          | Silna (każda VM ma własne jądro i zasoby). | Słabsza (wspólne jądro, izolacja procesów). |  
| **Przykłady**         | VMware, Hyper-V, VirtualBox.               | Docker, Kubernetes, LXC.                    |  
| **Zastosowanie**      | Środowiska wymagające pełnej izolacji.     | Mikrousługi, skalowalne aplikacje.          |  

**Podsumowanie**:  
- Wirtualizacja jest **uniwersalna** (obsługuje różne OS), ale **cięższa**.  
- Konteneryzacja jest **szybsza i tańsza**, ale ograniczona do jednego jądra OS.

---

# Bibliografia

## Wykład 10:
Materiał bazowy, https://fulmanski.pl/zajecia/comp_sys_arch/zajecia_20242025/lecture_10_virtualization.pdf
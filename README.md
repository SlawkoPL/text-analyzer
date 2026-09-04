# 📊 Analizator Tekstu (Text Analyzer)

Prosty i wydajny program konsolowy służący do **statystycznej analizy tekstu**. Projekt został stworzony w celu automatycznego zliczania oraz kategoryzacji poszczególnych komponentów ciągów znaków (alfanumerycznych, specjalnych oraz białych znaków).

## 🚀 Funkcje programu
Program analizuje przekazany tekst i generuje szczegółowy raport zawierający:
* **Łączną liczbę znaków** (wliczając spacje).
* **Podział na litery** z rozbiciem na małe i duże znaki (pełna obsługa standardowego alfabetu).
* **Zliczanie cyfr** (wartości numerycznych).
* **Wykrywanie znaków specjalnych** (interpunkcja, symbole).
* **Zliczanie spacji**.

## 📊 Przykład działania (Testy walidacyjne)
Algorytm zliczania oraz logika klasyfikacji znaków zostały przetestowane i zweryfikowane na tekstach próbnych. Poniżej znajdują się oficjalne wyniki działania programu dla czystego tekstu testowego (bez znaków diakrytycznych):

| Metryka | Wynik programu | Status |
| :--- | :---: | :---: |
| **Łącznie znaków** | 495 | ✅ Poprawny |
| **Litery (łącznie)** | 377 | ✅ Poprawny |
| `-- Małe litery` | 363 | ✅ Poprawny |
| `-- Duże litery` | 14 | ✅ Poprawny |
| **Liczby (cyfry)** | 12 | ✅ Poprawny |
| **Znaki specjalne** | 24 | ✅ Poprawny |
| **Spacje** | 82 | ✅ Poprawny |

## 🛠️ Technologie
* **Python** Język programowania wykorzystany do budowy algorytmu.
* **Git / GitHub** – system kontroli wersji.

## 📈 Planowany rozwój projektu
W przyszłości planowane jest rozbudowanie analizatora o następujące moduły:
1. Pełna obsługa kodowania UTF-8 (polskie znaki diakrytyczne).
2. Algorytm zliczania unikalnych słów oraz wyszukiwania najczęściej powtarzających się fraz.
3. Integracja z graficznym interfejsem użytkownika (GUI).

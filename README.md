
## Завдання 1: Порівняльний аналіз алгоритмів за часом виконання

### Опис
В рамках цього завдання було проведено порівняльний аналіз різних алгоритмів шляхом тестування їх на різних наборах даних (S=100, M=1000, L=10000), кожен з наборів виконувався 10 разів. Для кожного алгоритму було виміряно час виконання, що дозволило емпірично оцінити їх ефективність у різних умовах.

### Алгоритми сортування:
- Сортування злиттям
- Сортування вставками
- Timsort

### Результати
Тестування показало, що Timsort значно перевершує інші алгоритми сортування завдяки поєднанню двох підходів: сортування злиттям для великих наборів даних та сортування вставками для малих наборів даних. Результати наведені в таблиці:

| Algorithm               | Dataset Size | Fastest Time      | Slowest Time      | Average Time      |
|-------------------------|--------------|-------------------|-------------------|-------------------|
| Merge Sort              | Small        | 0.000108 seconds  | 0.000155 seconds  | 0.000118 seconds  |
| Insertion Sort          | Small        | 0.000135 seconds  | 0.000237 seconds  | 0.000149 seconds  |
| Quick Sort              | Small        | 0.000103 seconds  | 0.000121 seconds  | 0.000107 seconds  |
| Timsort (Python built-in)| Small       | 0.000003 seconds  | 0.000007 seconds  | 0.000004 seconds  |
| Merge Sort              | Medium       | 0.001451 seconds  | 0.004123 seconds  | 0.001839 seconds  |
| Insertion Sort          | Medium       | 0.017831 seconds  | 0.021977 seconds  | 0.018458 seconds  |
| Quick Sort              | Medium       | 0.001387 seconds  | 0.001514 seconds  | 0.001419 seconds  |
| Timsort (Python built-in)| Medium      | 0.000053 seconds  | 0.000079 seconds  | 0.000064 seconds  |
| Merge Sort              | Large        | 0.020031 seconds  | 0.022284 seconds  | 0.020947 seconds  |
| Insertion Sort          | Large        | 1.977249 seconds  | 2.011343 seconds  | 1.993875 seconds  |
| Quick Sort              | Large        | 0.018045 seconds  | 0.022831 seconds  | 0.018797 seconds  |
| Timsort (Python built-in)| Large       | 0.001019 seconds  | 0.001131 seconds  | 0.001056 seconds  |

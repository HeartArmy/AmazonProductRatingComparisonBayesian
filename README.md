# 📊 Bayesian Product Rating Comparator

Compare products more intelligently by adjusting average ratings based on the number of reviews.

Raw star ratings can be misleading:
- A 5.0 rating with 3 reviews is not equal to
- A 4.6 rating with 10,000 reviews

This tool applies a **Bayesian weighted rating formula** to account for statistical confidence.

---

## 🚀 What This Solves

Most marketplaces show:
- Average rating
- Number of ratings

But they don't combine them properly for fair ranking.

This script calculates:

1. ✅ Bayesian Weighted Rating  
2. ✅ Log-adjusted confidence score  
3. ✅ Ranked comparison output  

---

## 🧠 The Formula Used

Bayesian Weighted Rating:

WR = (v / (v + m)) * R + (m / (v + m)) * C

Where:

- R = product's average rating
- v = number of reviews
- C = global marketplace average rating
- m = minimum review threshold for full trust

Low-review products are pulled toward the global average.  
High-review products stay closer to their true rating.

---

## ⚙️ How To Use

1. Open the script.
2. Manually edit the `products` list:

```python
products = [
    ("Product A", 4.9, 20),
    ("Product B", 4.6, 10000),
]
```

3. Adjust these parameters if needed:

```python
C = 4.2   # Estimated marketplace average
m = 500   # Review threshold
```

4. Run:

```bash
python your_script_name.py
```

---

## 📈 Example Output

```
1. Product B
   Weighted Rating: 4.58

2. Product A
   Weighted Rating: 4.32
```

---

## 🛠 Use Cases

- Amazon product comparison
- Niche e-commerce research
- Competitive product analysis
- Data science learning exercise
- Statistical ranking experiments

---

## 🔍 Why Bayesian Instead of Raw Average?

Because rating without volume is noise.

More reviews = higher confidence.  
This approach penalizes small sample sizes and rewards consistency.

---

## 📌 Future Improvements

- Wilson lower-bound ranking
- CSV import/export
- Web scraping integration
- Visualization charts
- Auto-calculation of global average

---

## 📜 License

MIT

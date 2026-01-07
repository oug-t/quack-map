# Cloud-Native Spatial Query: DuckDB + Overture Maps

A **lightweight, serverless GIS pipeline** that queries massive global datasets **directly in Amazon S3** without downloading them.

This project demonstrates **Zero-Copy Data Engineering** by using DuckDB’s **HTTP range requests** to extract specific geospatial features (e.g., *pizza places in Washington, D.C.*) from the **Overture Maps Foundation** open dataset.

---

## 🚀 Key Features

- **Serverless Compute**  
  Runs locally (or in AWS Lambda) while data remains in the cloud.

- **Zero-Copy ETL**  
  Uses Parquet range requests to fetch only the required bytes—filtering **100GB+ datasets down to KBs in seconds**.

- **Modern Stack**  
  DuckDB (SQL Engine) · Leafmap (Visualization) · GeoParquet (Data Format)

- **Cost Efficient**  
  No database servers, no data ingestion, no massive local storage.

---

## 🛠️ Requirements

- Python **3.8+**
- Internet connection (access to AWS `us-west-2`)

---

## 📦 Installation

```bash
pip install duckdb leafmap pandas pyarrow
🏃‍♂️ Usage
Clone the repository (or copy the script).

Run the script:

bash
Copy code
python main.py
View the results:

The console prints the top 5 matching features

An interactive map file dc_map.html is generated
Open it in any web browser to explore the data

## ⚙️ How It Works

### 1. Connect
DuckDB loads the `spatial` and `httpfs` extensions, enabling geospatial
operations and HTTP/S3 access.

### 2. Query
SQL is executed **directly against the public Overture Maps S3 bucket**:

s3://overturemaps-us-west-2/

No data is downloaded up front—DuckDB reads only what it needs.

### 3. Filter
A **bounding box predicate** (e.g. `WHERE lon > ...`) allows DuckDB to
**prune Parquet files using metadata**, drastically minimizing data transfer.

### 4. Visualize
Query results are converted into a **Pandas DataFrame** and rendered on an
interactive map using **Leafmap**.

---

## ⚠️ Note on Data Persistence

The **Overture Maps public S3 bucket is ephemeral**, and dataset releases rotate
frequently.

- **Current target release:** `2025-12-17.0`
- Verify active releases at **Overture Maps Downloads**

If you encounter a **“No files found”** error, update the release date in the
script to the latest available version.

---

## ✨ Why This Matters

This project demonstrates that **cloud-scale geospatial analytics no longer
requires**:

- Long ETL pipelines  
- Persistent databases  
- Large local disks  

By combining **DuckDB + GeoParquet**, S3 effectively becomes a **queryable
spatial data lake**—and frankly, this is where modern GIS pipelines are heading.


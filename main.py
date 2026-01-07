import duckdb
import leafmap

con = duckdb.connect()

con.install_extension("spatial")
con.load_extension("spatial")

con.install_extension("httpfs")
con.load_extension("httpfs")

con.sql("SET s3_region='us-west-2';")

print("🦆... quacking places in DC...")

release_date = "2025-12-17.0"

query = f"""
SELECT
    names.primary AS name,
    ST_X(ST_Centroid(geometry)) AS lon,
    ST_Y(ST_Centroid(geometry)) AS lat
FROM read_parquet(
    's3://overturemaps-us-west-2/release/{release_date}/theme=places/type=place/*.parquet'
)
WHERE
    lon > -77.12 AND lon < -76.90
    AND lat > 38.79 AND lat < 39.00
    AND names.primary ILIKE '%Pizza%'
LIMIT 50;
"""

df = con.sql(query).df()

if df.empty:
    print("⚠️ Query succeeded, but no pizza places found.")
    exit()

print(f"✅ Found {len(df)} pizza places in DC!")
print(df[['name']].head())

m = leafmap.Map(center=[38.8977, -77.0365], zoom=13)

m.add_points_from_xy(
    df,
    x="lon",
    y="lat",
    layer_name="DC Pizza"
)

m.save("dc_map.html")
print("🍕 Map saved to dc_map.html")

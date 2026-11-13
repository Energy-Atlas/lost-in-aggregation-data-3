"""Split the release's per-type hourly files into one Parquet file per context, as the explorer reads them.

Usage: python split.py <download folder> <output folder>
Each output file holds one context's runs (run_id, hour, heating_w, cooling_w), in a single row group,
in the order of the release file.
"""
import sys
from pathlib import Path

import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

src, out = Path(sys.argv[1]), Path(sys.argv[2])
total = 0
for f in sorted(src.glob("hourly-*.parquet")):
    btype = f.stem.removeprefix("hourly-")
    t = pq.read_table(f)
    ctx_col = t.column("context_id").cast(pa.string())
    t = t.drop_columns(["context_id"])
    contexts = pc.unique(ctx_col).to_pylist()
    for ctx in contexts:
        part = t.filter(pc.equal(ctx_col, ctx))
        dest = out / "hourly" / btype / f"{ctx}.parquet"
        dest.parent.mkdir(parents=True, exist_ok=True)
        pq.write_table(part, dest, compression="zstd", compression_level=9, row_group_size=1 << 20, use_dictionary=["run_id"])
        total += 1
    print(f"{btype}: {len(contexts)} contexts", flush=True)
print(f"{total} context files")

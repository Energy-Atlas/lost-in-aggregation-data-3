# lost-in-aggregation-data-3

Hourly heating and cooling series for the explorer of [Lost in Aggregation?](https://energy-atlas.github.io/lost-in-aggregation/) (ASIM 2026 poster, C. Li, Z. J. Wang, T. Dogan, Environmental Systems Lab, Cornell University).

This repository holds no data in git. On every push, its workflow:
1. downloads the hourly files of its building types (LP, LargeOffice, PP, GB, HighriseApartment) from the GitHub Release [data-v1.0.0](https://github.com/Energy-Atlas/lost-in-aggregation/releases/tag/data-v1.0.0);
2. checks them against the release checksums;
3. splits them into one Parquet file per context;
4. publishes them with GitHub Pages at <https://energy-atlas.github.io/lost-in-aggregation-data-3/>, under `hourly/<building_type>/<context_id>.parquet`.

The study's hourly data are split across several such sites because a single GitHub Pages site holds at most 1 GB.

Licence: CC BY 4.0 (see `LICENSE`). The data dictionary is in the [release](https://github.com/Energy-Atlas/lost-in-aggregation/releases/tag/data-v1.0.0) and on the [data page](https://energy-atlas.github.io/lost-in-aggregation/data/).

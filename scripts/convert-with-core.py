from pathlib import Path

import polars as pl

resource_dir = Path(__file__).resolve().parent.parent
folder_path = resource_dir / "data-raw"

df_abundance = pl.read_csv(
    folder_path / "Expe3Abundance.csv", infer_schema_length=100_000
)
df_richness = pl.read_csv(
    folder_path / "Expe3Richness.csv", infer_schema_length=100_000
)

# Create a concatenated csv with the values from 3a and 3b
df_experiment_3_all = pl.concat([df_abundance, df_richness], how="align")


# Rename the first column to time_measurement_weeks, second to site_id, third to plot_id
# keep the last two headers
df_experiment_3_all = df_experiment_3_all.rename(
    {"time_measurement": "time_measurement_weeks", "site": "site_id", "plot": "plot_id"}
)

df_experiment_3_all.write_csv(folder_path / "data-experiment-3-ready.csv")

df_experiment_3_all.glimpse()
